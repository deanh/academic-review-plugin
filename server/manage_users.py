#!/usr/bin/env python3
"""
Manage quiz server users.

Usage:
    python manage_users.py add <username>
    python manage_users.py remove <username>
    python manage_users.py list
"""

import json
import sys
from getpass import getpass
from pathlib import Path

from werkzeug.security import generate_password_hash

USERS_FILE = Path(__file__).parent / "users.json"


def load_users() -> dict:
    if USERS_FILE.exists():
        with open(USERS_FILE) as f:
            return json.load(f)
    return {}


def save_users(users: dict):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def add_user(username: str):
    users = load_users()
    if username in users:
        print(f"User '{username}' already exists. Updating password.")

    password = getpass("Password: ")
    confirm = getpass("Confirm:  ")
    if password != confirm:
        print("Passwords don't match.")
        sys.exit(1)
    if len(password) < 4:
        print("Password must be at least 4 characters.")
        sys.exit(1)

    users[username] = generate_password_hash(password)
    save_users(users)
    print(f"User '{username}' {'updated' if username in users else 'added'}.")


def remove_user(username: str):
    users = load_users()
    if username not in users:
        print(f"User '{username}' not found.")
        sys.exit(1)

    del users[username]
    save_users(users)
    print(f"User '{username}' removed.")


def list_users():
    users = load_users()
    if not users:
        print("No users configured.")
        return
    print(f"{len(users)} user(s):")
    for username in sorted(users):
        print(f"  - {username}")


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 3:
            print("Usage: manage_users.py add <username>")
            sys.exit(1)
        add_user(sys.argv[2])
    elif command == "remove":
        if len(sys.argv) != 3:
            print("Usage: manage_users.py remove <username>")
            sys.exit(1)
        remove_user(sys.argv[2])
    elif command == "list":
        list_users()
    else:
        print(f"Unknown command: {command}")
        print(__doc__.strip())
        sys.exit(1)


if __name__ == "__main__":
    main()
