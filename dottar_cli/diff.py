import os
import json
import difflib

def run(commit1, commit2):
    path1 = f".dottar/commits/{commit1}.json"
    path2 = f".dottar/commits/{commit2}.json"

    if not os.path.exists(path1) or not os.path.exists(path2):
        print("❌ One or both commit IDs are invalid.")
        return

    with open(path1) as f1, open(path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    files1 = data1.get("files", {})
    files2 = data2.get("files", {})

    common_files = set(files1.keys()) & set(files2.keys())

    for file in common_files:
        with open(f".dottar/blobs/{files1[file]}", "rb") as f:
            content1 = f.read().decode(errors="ignore").splitlines()
        with open(f".dottar/blobs/{files2[file]}", "rb") as f:
            content2 = f.read().decode(errors="ignore").splitlines()

        print(f"\n📄 Diff for: {file}")
        for line in difflib.unified_diff(content1, content2, fromfile=commit1, tofile=commit2, lineterm=""):
            print(line)
