import argparse
from dottar_cli import init, add, commit, status, log, checkout, diff, clone

def main():
    parser = argparse.ArgumentParser(prog="dottar", description="Dottar: A Secure Version Control System")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Initialize a new Dottar repository")

    add_parser = subparsers.add_parser("add", help="Add file to staging area")
    add_parser.add_argument("filename", help="File to add")

    commit_parser = subparsers.add_parser("commit", help="Commit staged files")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")

    subparsers.add_parser("status", help="Show current status")
    subparsers.add_parser("log", help="Show commit history")

    checkout_parser = subparsers.add_parser("checkout", help="Restore files from a commit")
    checkout_parser.add_argument("commit_id", help="Commit hash to checkout")

    diff_parser = subparsers.add_parser("diff", help="Show file differences between two commits")
    diff_parser.add_argument("commit1", help="First commit ID")
    diff_parser.add_argument("commit2", help="Second commit ID")

    clone_parser = subparsers.add_parser("clone", help="Clone a local Dottar repository")
    clone_parser.add_argument("source_path", help="Path to existing Dottar repo")
    clone_parser.add_argument("target_path", help="Target path to clone into")

    args = parser.parse_args()

    if args.command == "init":
        init.run()
    elif args.command == "add":
        add.run(args.filename)
    elif args.command == "commit":
        commit.run(args.message)
    elif args.command == "status":
        status.run()
    elif args.command == "log":
        log.run()
    elif args.command == "checkout":
        checkout.run(args.commit_id)
    elif args.command == "diff":
        diff.run(args.commit1, args.commit2)
    elif args.command == "clone":
        clone.run(args.source_path, args.target_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()