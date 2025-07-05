import os
import json
from getpass import getpass

def run():
    if os.path.exists(".dottar"):
        print("⚠️  Repository already initialized.")
        return

    os.makedirs(".dottar/commits")
    os.makedirs(".dottar/blobs")
    with open(".dottar/index", "w") as f:
        pass
    with open(".dottar/HEAD", "w") as f:
        f.write("")

    # Set master password (optional)
    print("🔐 Setup secure mode (optional)")
    password = getpass("Set master password (press enter to skip): ")
    secure_mode = False
    password_hash = ""
    if password:
        from dottar_cli.utils.hash_utils import hash_password
        password_hash = hash_password(password)
        secure_mode = True

    with open(".dottar/config.json", "w") as f:
        json.dump({"version": "0.2.0", "secure_mode": secure_mode, "password": password_hash}, f, indent=2)

    print("✅ Dottar repository initialized.")
