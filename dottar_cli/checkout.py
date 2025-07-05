import os
import json
from getpass import getpass
from dottar_cli.utils import file_ops, hash_utils

def run(commit_id):
    commit_path = f".dottar/commits/{commit_id}.json"
    if not os.path.exists(commit_path):
        print("❌ Commit not found.")
        return

    with open(".dottar/config.json") as f:
        config = json.load(f)

    secure_mode = config.get("secure_mode", False)
    password_input = None
    if secure_mode:
        password_input = getpass("🔐 Enter master password: ")
        if not hash_utils.verify_password(password_input, config["password"]):
            print("❌ Incorrect password. Checkout aborted.")
            return

    with open(commit_path, "r") as f:
        commit = json.load(f)

    print(f"🔁 Restoring files from commit: {commit_id}")
    for file, blob_hash in commit["files"].items():
        blob_path = f".dottar/blobs/{blob_hash}"
        if os.path.exists(blob_path):
            content = open(blob_path, "rb").read()
            if secure_mode:
                content = file_ops.decrypt_blob(content, password_input)
            with open(file, "wb") as out:
                out.write(content)
            print(f"✅ Restored: {file} (overwritten with version from commit)")

    print("🟢 All files restored to this commit.")