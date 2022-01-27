
from sys import argv
from glob import glob


def print_process_usage():
    print("This subcommand processes a folder with midi files and produces a file with the results")
    print("Usage: " + argv[0] + " process [-h|--help] <midi files folder> <output file>")

def process_cli(args):
    if len(args) != 2 or args[0] in ["-h", "--help"]:
        print_process_usage()
        exit()


commands = {
    "process": process_cli,
    "train": "",
    "generate": "",
}

def print_usage():
    print("Phrygian is a tool for music composition using AI")
    print("Usage: " + argv[0] + " [-h|--help] " + "|".join(commands.keys()))
    print("You can also call help on each subcommand")

if len(argv) < 2 or argv[1] in ["-h", "--help"] or argv[1] not in commands.keys():
    print_usage()
    exit()
    
commands[argv[1]](argv[2:])

