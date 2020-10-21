from translator import controller, view, model
from translator.args_parser import parse_args
from sys import argv

args = argv[1:]
controller.run(view, model, args=parse_args(args, model.LANGUAGES) if args else None)
