import subprocess
from typing import Union
import helpers as hp
from pathlib import Path
from InquirerPy import inquirer


def build():
    folder = Path(".")
    items = hp.find_ui_files(folder)
    for item in items:
        print(f"Compilando {item}")
        hp.compile(item)


def get_ui_file(path: Path) -> Union[Path, None]:
    if path.is_dir():
        for entry in path.iterdir():
            if entry.suffix == ".ui":
                return entry
    elif path.suffix == ".ui":
        return path
    return None


def designer(term):
    
    if not term:
        subprocess.Popen(["pyqt5-tools", "designer"])
        return
    path = Path(term)
    file = get_ui_file(path)
    if file:
        subprocess.Popen(["pyqt5-tools", "designer", str(file)])
    else:
        folder = Path(".")
        items = hp.find_ui_files(folder, term_search=term)
        if not items:
            print("Item not found")
            return
        file_ = inquirer.select(
            message="Model:",
            choices=items,
        ).execute()
        subprocess.Popen(["pyqt5-tools", "designer", file_])


def new_item(item, name):
    if item == "QMainWindow":
        hp.new_main_window(name)
    elif item == "QDialog":
        hp.new_dialog_window(name)
    elif item == "QWidget":
        hp.new_widget(name)
    elif item == "app":
        hp.new_app(name)
