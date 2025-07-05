# dottar_cli/status.py
import os

def run():
    if not os.path.exists(".dottar/index"):
        print("❌ Not a Dottar repository.")
        return

    print("📦 Staged files:")
    with open(".dottar/index", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        if not lines:
            print("   (No files staged)")
        for line in lines:
            print("   •", line)
