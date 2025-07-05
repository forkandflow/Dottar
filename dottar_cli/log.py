# dottar_cli/log.py
import os
import json

def run():
    if not os.path.exists(".dottar/commits"):
        print("❌ No commits found.")
        return

    files = os.listdir(".dottar/commits")
    if not files:
        print("ℹ️  No commits yet.")
        return

    for fname in sorted(files):
        with open(f".dottar/commits/{fname}") as f:
            data = json.load(f)
            print("\n🔸 Commit:", fname.replace(".json", ""))
            print("📅 Date:", data["timestamp"])
            print("📝 Message:", data["message"])
            print("📁 Files:")
            for file in data["files"]:
                print("   •", file)
