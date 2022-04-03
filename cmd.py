import argparse
import actions as ac
import config

parser = argparse.ArgumentParser()
parser.add_argument("--depth", type=int, default=10, help="Depth of the search for ui files.")
subparsers = parser.add_subparsers(dest="command", required=True, help='Pyqt5 tools')

p_build = subparsers.add_parser("build")


p_new = subparsers.add_parser("new")
p_new.add_argument("item", choices=("QMainWindow", "QDialog", "QWidget", "app"))
p_new.add_argument("name")

p_designer = subparsers.add_parser("designer")
p_designer.add_argument("item",nargs='?')

p_watch = subparsers.add_parser('watch')

args = parser.parse_args()
config.max_depth = args.depth
if args.command == "build": 

    ac.build()
elif args.command == "new":
    ac.new_item(args.item, args.name)
elif args.command == "designer":
    ac.designer(args.item)
elif args.command == "watch":
    ac.start_watching(".", recursive=True)
