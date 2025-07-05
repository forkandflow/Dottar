import os
import shutil

def run(source_path, target_path):
    if not os.path.exists(os.path.join(source_path, ".dottar")):
        print("❌ No Dottar repository found in source path.")
        return

    if os.path.exists(target_path):
        print("❌ Target path already exists. Aborting to prevent overwrite.")
        return

    shutil.copytree(source_path, target_path)
    print(f"✅ Dottar repository cloned to: {target_path}")