import os
import json
import hashlib
from datetime import datetime
from getpass import getpass
from dottar_cli.utils import file_ops, hash_utils

def run(message):
    if not os.path.exists(".dottar/index"):
        print("❌ No repository found. Run 'dottar init' first.")
        return

    with open(".dottar/config.json") as f:
        config = json.load(f)

    secure_mode = config.get("secure_mode", False)
    if secure_mode:
        password_input = getpass("🔐 Enter master password: ")
        if not hash_utils.verify_password(password_input, config["password"]):
            print("❌ Incorrect password. Commit aborted.")
            return

    with open(".dottar/index", "r") as f:
        files = [line.strip() for line in f if line.strip()]

    if not files:
        print("⚠️  No files staged for commit.")
        return

    commit_data = {
        "timestamp": datetime.now().isoformat(),
        "message": message,
        "files": {}
    }

    for file in files:
        if os.path.exists(file):
            content = open(file, "rb").read()
            if secure_mode:
                content = file_ops.encrypt_blob(content, password_input)
            file_hash = hashlib.sha256(content).hexdigest()
            blob_path = f".dottar/blobs/{file_hash}"
            with open(blob_path, "wb") as blob:
                blob.write(content)
            commit_data["files"][file] = file_hash

    commit_hash = hashlib.sha1((commit_data["timestamp"] + message).encode()).hexdigest()
    with open(f".dottar/commits/{commit_hash}.json", "w") as f:
        json.dump(commit_data, f, indent=2)

    with open(".dottar/HEAD", "w") as f:
        f.write(commit_hash)

    open(".dottar/index", "w").close()
    print(f"✅ Commit saved as {commit_hash}")