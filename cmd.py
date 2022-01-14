import argparse
import actions as ac

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help='Pyqt5 tools')

p_build = subparsers.add_parser("build")
# somar.add_argument("-a", type=int, help="Valor a")
# somar.add_argument("-b", type=int, help="Valor b")

p_new = subparsers.add_parser("new")
p_new.add_argument("item")

p_designer = subparsers.add_parser("designer")
p_designer.add_argument("item",nargs='?')

args = parser.parse_args()
if args.command == "build": 
    ac.build()
elif args.command == "new":
    print("Not implemented")
elif args.command == "designer":
    ac.designer(args.item)
