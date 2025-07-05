# dottar_cli/add.py
import os

def run(filename):
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' does not exist.")
        return

    with open(".dottar/index", "a") as f:
        f.write(filename + "\n")
    print(f"✅ Added '{filename}' to staging area.")
