from pathlib import Path
import subprocess
from typing import List
import config

def compile(path):
    path = Path(path)
    output = path.parent / f"{path.stem}_ui.py"
    # args = ["python", "-m", "PyQt5.uic.pyuic", str(path), "-o", str(output)]
    args = ["pyuic5", str(path), "-o", str(output)]
    subprocess.run(args)

def find_ui_files(folder: Path, depth=0) -> List[Path]:
    if depth >= config.max_depth:
        return []
    items = []
    for entry in folder.iterdir():
        if entry.is_dir():
            items += find_ui_files(entry, depth + 1)
        elif entry.suffix == ".ui":
            items.append(entry)
    return items

