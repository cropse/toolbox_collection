import os
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from send2trash import send2trash

# useage: python3 purge_old_file
parser = argparse.ArgumentParser()
parser.add_argument("folder_path", type=str, help="folder you want to scan")
parser.add_argument("-d", "--days", type=int, default=30, help="days you want to delete")

args = parser.parse_args()

f_path = Path(args.folder_path)
now_time = datetime.now()
for _file in f_path.iterdir():
    try:
        file_time = max(datetime.fromtimestamp(os.path.getatime(_file)), 
            datetime.fromtimestamp(os.path.getctime(_file)))
    except OSError:
        file_time = datetime.fromtimestamp(os.path.getctime(_file))
    if now_time - file_time > timedelta(days=args.days):
        send2trash(_file.as_posix())
        print(f"delete file {_file}")
