import shutil
import glob
import os

source_dir = os.path.join("2025素材", "2025素材")
dest_dir = "images"

# ディレクトリが存在するか確認
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# JPGファイルをコピー
jpg_files = glob.glob(os.path.join(source_dir, "*.jpg"))
for jpg_file in jpg_files:
    shutil.copy2(jpg_file, dest_dir)
    print(f"Copied: {os.path.basename(jpg_file)}")

# MP4ファイルをコピー
mp4_files = glob.glob(os.path.join(source_dir, "*.mp4"))
for mp4_file in mp4_files:
    shutil.copy2(mp4_file, dest_dir)
    print(f"Copied: {os.path.basename(mp4_file)}")

print(f"\nTotal: {len(jpg_files)} JPG files, {len(mp4_files)} MP4 files copied.")

