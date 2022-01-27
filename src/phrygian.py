from sys import argv
from process_midis import process
from train_network import train
from common import instruments, scales
from generate_music import generate
from re import match

def print_process_usage():
    print("This subcommand processes a folder with midi files and produces a file with the results")
    print("Usage: " + argv[0] + " process [-h|--help] <midi files folder> <output file>")

def process_cli(args):
    if len(args) != 2 or args[0] in ["-h", "--help"]:
        print_process_usage()
        exit()
    process(*args)

def print_train_usage():
    print("This subcommand takes a preprocessed file and trains a neural network")
    print("Usage: " + argv[0] + " train <processed midis file> <neural network weights folder>")

def train_cli(args):
    if len(args) != 2 or args[0] in ["-h", "--help"]:
        print_train_usage()
        exit()
    train(*args)

def print_generate_usage():
    print("This subcommand takes several arguments which uses to generate a midi file")
    print("Usage: " + argv[0] + " generate <processed midis file> <neural networks weights> <output midi file> <initial note> <instrument> <scale>")
    print("\nAvailable instruments: " + ", ".join(instruments.keys()))
    print("\nAvailable scales: " + ", ".join(scales.keys()))

def check_instrument(instrument):
    if not instrument in instruments:
        print("Invalid instrument " + instrument + ", check the list of available instruments:")
        print("Available instruments: " + ", ".join(instruments.keys()))
        exit(-1)

def check_scale(scale):
    if not scale in scales:
        print("Invalid scale " + scale + ", check the list of available scales:")
        print("Available scales: " + ", ".join(scales.keys()))
        exit(-1)

def check_initial_note(note):
    if not match("^[a-gA-G][#b-]?[1-7]$", note):
        print("Invalid initial note " + scale + ", see the examples:")
        print("Si        1st octave  ->   B1 or b1")
        print("Re Sharp  4th octave  ->   D#4 or d#4")
        print("Do Flat   7th octave  ->   C-7, c-7, Cb7 or cb7")

def generate_cli(args):
    if len(args) < 3 or len(args) > 6 or args[0] in ["-h", "--help"]:
        print_generate_usage()
        print(len(args) )
        exit()
    if len(args) > 3:
        check_initial_note(args[3])
        if len(args) > 4:
            check_instrument(args[4])
            if len(args) > 5:
                check_scale(args[5])
    generate(*args)

commands = {
    "process": process_cli,
    "train": train_cli,
    "generate": generate_cli,
}

def print_usage():
    print("Phrygian is a tool for music composition using AI")
    print("Usage: " + argv[0] + " [-h|--help] " + "|".join(commands.keys()))
    print("You can also call help on each subcommand")

if len(argv) < 2 or argv[1] in ["-h", "--help"] or argv[1] not in commands.keys():
    print_usage()
    exit()
    
commands[argv[1]](argv[2:])

