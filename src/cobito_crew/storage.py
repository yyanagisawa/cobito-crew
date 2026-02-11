from __future__ import annotations

import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_db_path(cwd: Path | None = None) -> Path:
    base = cwd or Path.cwd()
    return base / ".cobito_crew" / "state.db"


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS workspaces (
  name TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS missions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  workspace_name TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'open',
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(workspace_name) REFERENCES workspaces(name)
);

CREATE TABLE IF NOT EXISTS advances (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  workspace_name TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  status TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(workspace_name) REFERENCES workspaces(name),
  FOREIGN KEY(mission_id) REFERENCES missions(id)
);

CREATE TABLE IF NOT EXISTS decisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  workspace_name TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  advance_id INTEGER NOT NULL,
  kind TEXT NOT NULL,
  reason TEXT NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY(workspace_name) REFERENCES workspaces(name),
  FOREIGN KEY(mission_id) REFERENCES missions(id),
  FOREIGN KEY(advance_id) REFERENCES advances(id)
);

CREATE TABLE IF NOT EXISTS workspace_locks (
  workspace_name TEXT PRIMARY KEY,
  advance_id INTEGER NOT NULL,
  acquired_at TEXT NOT NULL,
  FOREIGN KEY(workspace_name) REFERENCES workspaces(name),
  FOREIGN KEY(advance_id) REFERENCES advances(id)
);
"""


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    conn.commit()


def ensure_workspace(conn: sqlite3.Connection, name: str) -> None:
    conn.execute("INSERT OR IGNORE INTO workspaces(name) VALUES (?)", (name,))


def _touch(conn: sqlite3.Connection, table: str, row_id: int) -> None:
    conn.execute(
        f"UPDATE {table} SET updated_at = ? WHERE id = ?",
        (utc_now_iso(), row_id),
    )


@dataclass(frozen=True)
class Mission:
    id: int
    workspace_name: str
    title: str
    body: str
    status: str
    created_at: str
    updated_at: str


@dataclass(frozen=True)
class Advance:
    id: int
    workspace_name: str
    mission_id: int
    title: str
    body: str
    status: str
    created_at: str
    updated_at: str


VALID_ADVANCE_STATUSES = {
    "draft",
    "ready",
    "in_review",
    "approved",
    "rejected",
    "expired",
}


def create_mission(conn: sqlite3.Connection, workspace_name: str, title: str, body: str) -> Mission:
    ensure_workspace(conn, workspace_name)
    now = utc_now_iso()
    cur = conn.execute(
        """
        INSERT INTO missions(workspace_name, title, body, status, created_at, updated_at)
        VALUES (?, ?, ?, 'open', ?, ?)
        """,
        (workspace_name, title, body, now, now),
    )
    conn.commit()
    return get_mission(conn, int(cur.lastrowid))


def get_mission(conn: sqlite3.Connection, mission_id: int) -> Mission:
    row = conn.execute("SELECT * FROM missions WHERE id = ?", (mission_id,)).fetchone()
    if row is None:
        raise ValueError(f"mission not found: {mission_id}")
    return Mission(**dict(row))


def list_missions(conn: sqlite3.Connection, workspace_name: str) -> list[Mission]:
    rows = conn.execute(
        "SELECT * FROM missions WHERE workspace_name = ? ORDER BY id DESC",
        (workspace_name,),
    ).fetchall()
    return [Mission(**dict(r)) for r in rows]


def create_advance(
    conn: sqlite3.Connection,
    workspace_name: str,
    mission_id: int,
    title: str,
    body: str,
    status: str = "draft",
) -> Advance:
    if status not in VALID_ADVANCE_STATUSES:
        raise ValueError(f"invalid advance status: {status}")
    mission = get_mission(conn, mission_id)
    if mission.workspace_name != workspace_name:
        raise ValueError("workspace_name must match mission.workspace_name")

    now = utc_now_iso()
    cur = conn.execute(
        """
        INSERT INTO advances(workspace_name, mission_id, title, body, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (workspace_name, mission_id, title, body, status, now, now),
    )
    conn.commit()
    return get_advance(conn, int(cur.lastrowid))


def get_advance(conn: sqlite3.Connection, advance_id: int) -> Advance:
    row = conn.execute("SELECT * FROM advances WHERE id = ?", (advance_id,)).fetchone()
    if row is None:
        raise ValueError(f"advance not found: {advance_id}")
    return Advance(**dict(row))


def list_advances(conn: sqlite3.Connection, workspace_name: str, mission_id: int | None = None) -> list[Advance]:
    if mission_id is None:
        rows = conn.execute(
            "SELECT * FROM advances WHERE workspace_name = ? ORDER BY id DESC",
            (workspace_name,),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT * FROM advances
            WHERE workspace_name = ? AND mission_id = ?
            ORDER BY id DESC
            """,
            (workspace_name, mission_id),
        ).fetchall()
    return [Advance(**dict(r)) for r in rows]


def get_latest_advance_for_mission(conn: sqlite3.Connection, mission_id: int) -> Advance | None:
    row = conn.execute(
        "SELECT * FROM advances WHERE mission_id = ? ORDER BY id DESC LIMIT 1",
        (mission_id,),
    ).fetchone()
    return None if row is None else Advance(**dict(row))


def set_advance_status(conn: sqlite3.Connection, advance_id: int, status: str) -> Advance:
    if status not in VALID_ADVANCE_STATUSES:
        raise ValueError(f"invalid advance status: {status}")
    conn.execute("UPDATE advances SET status = ?, updated_at = ? WHERE id = ?", (status, utc_now_iso(), advance_id))
    conn.commit()
    return get_advance(conn, advance_id)


def acquire_workspace_lock(conn: sqlite3.Connection, workspace_name: str, advance_id: int) -> None:
    ensure_workspace(conn, workspace_name)
    conn.execute(
        "INSERT INTO workspace_locks(workspace_name, advance_id, acquired_at) VALUES (?, ?, ?)",
        (workspace_name, advance_id, utc_now_iso()),
    )


def release_workspace_lock(conn: sqlite3.Connection, workspace_name: str, advance_id: int) -> None:
    conn.execute(
        "DELETE FROM workspace_locks WHERE workspace_name = ? AND advance_id = ?",
        (workspace_name, advance_id),
    )


def get_workspace_lock(conn: sqlite3.Connection, workspace_name: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM workspace_locks WHERE workspace_name = ?",
        (workspace_name,),
    ).fetchone()


def start_review(conn: sqlite3.Connection, advance_id: int) -> Advance:
    adv = get_advance(conn, advance_id)
    if adv.status != "ready":
        raise ValueError(f"advance must be ready to start review (current: {adv.status})")

    existing = get_workspace_lock(conn, adv.workspace_name)
    if existing is not None:
        raise RuntimeError(
            f"workspace is locked: {adv.workspace_name} (advance_id={existing['advance_id']})"
        )

    try:
        acquire_workspace_lock(conn, adv.workspace_name, adv.id)
        conn.execute(
            "UPDATE advances SET status = 'in_review', updated_at = ? WHERE id = ?",
            (utc_now_iso(), adv.id),
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise RuntimeError(f"failed to acquire workspace lock for {adv.workspace_name}") from e

    return get_advance(conn, adv.id)


def decide(conn: sqlite3.Connection, advance_id: int, kind: str, reason: str) -> Advance:
    adv = get_advance(conn, advance_id)
    if adv.status != "in_review":
        raise ValueError(f"advance must be in_review to decide (current: {adv.status})")

    lock = get_workspace_lock(conn, adv.workspace_name)
    if lock is None or int(lock["advance_id"]) != adv.id:
        raise RuntimeError(f"workspace lock not held for advance: {adv.id}")

    if kind not in {"approved", "rejected"}:
        raise ValueError("kind must be 'approved' or 'rejected'")

    new_status = "approved" if kind == "approved" else "rejected"

    conn.execute(
        """
        INSERT INTO decisions(workspace_name, mission_id, advance_id, kind, reason, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (adv.workspace_name, adv.mission_id, adv.id, kind, reason, utc_now_iso()),
    )
    conn.execute(
        "UPDATE advances SET status = ?, updated_at = ? WHERE id = ?",
        (new_status, utc_now_iso(), adv.id),
    )
    release_workspace_lock(conn, adv.workspace_name, adv.id)
    conn.commit()
    return get_advance(conn, adv.id)
