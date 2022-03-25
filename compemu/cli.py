from argparse import ArgumentParser, FileType


def start():
    arg_parser = ArgumentParser(description="Computer emulator CLI")
    arg_parser.add_argument("program", type=FileType("r"))
    args = arg_parser.parse_args()

    for instruction in args.program:
        print(instruction)
