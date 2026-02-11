from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cobito_crew.advance_template import load_phase0_template
from cobito_crew.storage import (
    VALID_ADVANCE_STATUSES,
    connect,
    create_advance,
    create_mission,
    decide,
    default_db_path,
    get_advance,
    get_latest_advance_for_mission,
    get_mission,
    init_db,
    list_advances,
    list_missions,
    set_advance_status,
    start_review,
)


def _repo_root() -> Path:
    return Path.cwd()


def _db_path(args: argparse.Namespace) -> Path:
    return Path(args.db).expanduser() if args.db else default_db_path(_repo_root())


def cmd_init(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
    print("ok")
    return 0


def cmd_mission_create(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        mission = create_mission(conn, args.workspace, args.title, args.body)
    print(f"mission {mission.id} created")
    return 0


def cmd_mission_list(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        missions = list_missions(conn, args.workspace)
    for m in missions:
        print(f"{m.id}\t{m.status}\t{m.title}")
    return 0


def cmd_mission_show(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        m = get_mission(conn, args.id)
    print(f"Mission {m.id} ({m.workspace_name})\nTitle: {m.title}\n\n{m.body}")
    return 0


def cmd_advance_template(args: argparse.Namespace) -> int:
    template = load_phase0_template(_repo_root())
    print(template)
    return 0


def cmd_advance_create(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        adv = create_advance(
            conn,
            workspace_name=args.workspace,
            mission_id=args.mission,
            title=args.title,
            body=args.body,
            status=args.status,
        )
    print(f"advance {adv.id} created ({adv.status})")
    return 0


def cmd_advance_list(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        advances = list_advances(conn, workspace_name=args.workspace, mission_id=args.mission)
    for a in advances:
        print(f"{a.id}\t{a.status}\tmission={a.mission_id}\t{a.title}")
    return 0


def cmd_advance_show(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = get_advance(conn, args.id)
    print(f"Advance {a.id} ({a.workspace_name})\nStatus: {a.status}\nMission: {a.mission_id}\nTitle: {a.title}\n\n{a.body}")
    return 0


def cmd_advance_latest(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = get_latest_advance_for_mission(conn, args.mission_id)
    if a is None:
        print(f"error: no advances for mission {args.mission_id}", file=sys.stderr)
        return 2
    if args.id_only:
        print(a.id)
    else:
        print(f"{a.id}\t{a.status}\tmission={a.mission_id}\t{a.title}")
    return 0


def cmd_advance_set_status(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = set_advance_status(conn, args.id, args.status)
    print(f"advance {a.id} -> {a.status}")
    return 0


def cmd_advance_review(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = start_review(conn, args.id)
    print(f"advance {a.id} -> {a.status}")
    return 0


def cmd_advance_approve(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = decide(conn, args.id, kind="approved", reason=args.reason)
    print(f"advance {a.id} -> {a.status}")
    return 0


def cmd_advance_reject(args: argparse.Namespace) -> int:
    with connect(_db_path(args)) as conn:
        init_db(conn)
        a = decide(conn, args.id, kind="rejected", reason=args.reason)
    print(f"advance {a.id} -> {a.status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cobito-crew")
    p.add_argument("--db", help="SQLite DB path (default: .cobito_crew/state.db)")

    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("init", help="initialize local state DB")
    sp.set_defaults(func=cmd_init)

    sp = sub.add_parser("mission-create", help="create a mission")
    sp.add_argument("--workspace", required=True)
    sp.add_argument("--title", required=True)
    sp.add_argument("--body", required=True)
    sp.set_defaults(func=cmd_mission_create)

    sp = sub.add_parser("mission-list", help="list missions")
    sp.add_argument("--workspace", required=True)
    sp.set_defaults(func=cmd_mission_list)

    sp = sub.add_parser("mission-show", help="show mission")
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_mission_show)

    sp = sub.add_parser("advance-template", help="print phase0 advance template")
    sp.set_defaults(func=cmd_advance_template)

    sp = sub.add_parser("advance-create", help="create an advance")
    sp.add_argument("--workspace", required=True)
    sp.add_argument("--mission", required=True, type=int)
    sp.add_argument("--title", required=True)
    sp.add_argument("--body", required=True)
    sp.add_argument("--status", default="draft", choices=sorted(VALID_ADVANCE_STATUSES))
    sp.set_defaults(func=cmd_advance_create)

    sp = sub.add_parser("advance-list", help="list advances")
    sp.add_argument("--workspace", required=True)
    sp.add_argument("--mission", type=int)
    sp.set_defaults(func=cmd_advance_list)

    sp = sub.add_parser("advance-show", help="show advance")
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_advance_show)

    sp = sub.add_parser("advance-latest", help="print latest advance for mission")
    sp.add_argument("mission_id", type=int)
    sp.add_argument("--id-only", action="store_true", help="print only advance id")
    sp.set_defaults(func=cmd_advance_latest)

    sp = sub.add_parser("advance-set-status", help="set advance status")
    sp.add_argument("id", type=int)
    sp.add_argument("status", choices=sorted(VALID_ADVANCE_STATUSES))
    sp.set_defaults(func=cmd_advance_set_status)

    sp = sub.add_parser("advance-review", help="start review (acquire workspace lock)")
    sp.add_argument("id", type=int)
    sp.set_defaults(func=cmd_advance_review)

    sp = sub.add_parser("advance-approve", help="approve advance (release lock)")
    sp.add_argument("id", type=int)
    sp.add_argument("--reason", required=True)
    sp.set_defaults(func=cmd_advance_approve)

    sp = sub.add_parser("advance-reject", help="reject advance (release lock)")
    sp.add_argument("id", type=int)
    sp.add_argument("--reason", required=True)
    sp.set_defaults(func=cmd_advance_reject)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (ValueError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
