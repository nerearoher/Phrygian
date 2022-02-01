from sys import argv
from logic.process_midis import process
from logic.train_network import train
from logic.common import instruments, scales
from logic.generate_music import generate
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
    print("Usage: " + argv[0] + " train <processed midis file> <neural network weights folder> <number of epochs>")

def train_cli(args):
    if len(args) != 3 or args[0] in ["-h", "--help"]:
        print_train_usage()
        exit()
    train(*args)

def print_generate_usage():
    print("This subcommand takes several arguments which uses to generate a midi file")
    print("Usage: " + argv[0] + " generate <processed midis file> <neural networks weights> <output midi file>")
    print("Optional arguments should be added at the end")
    print("Initial pitch (Default A3): [(-p|--pitch) <pitch>] ")
    print("Instrument (Default Piano): [(-i|--instrument) <instrument>]")
    print("Scale (Default Chromatic): [(-s|--scale) <scale>] ")
    print("Number of notes (Default 100): [(-n|--notes) <number of notes>] ")
    print("\nAvailable instruments: " + ", ".join(instruments.keys()))
    print("\nAvailable scales: " + ", ".join(scales.keys()))

def check_initial_note(note):
    if not match("^[a-gA-G][#b-]?[1-7]$", note):
        print("Invalid initial note " + note + ", see the examples:")
        print("Si        1st octave  ->   B1 or b1")
        print("Re Sharp  4th octave  ->   D#4 or d#4")
        print("Do Flat   7th octave  ->   C-7, c-7, Cb7 or cb7")
        exit(-1)

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

def generate_cli(args):
    if len(args) not in [3, 5, 7, 9, 11] or args[0] in ["-h", "--help"]:
        print_generate_usage()
        exit()
    note = "A3"
    instrument = "Piano"
    scale = "Chromatic"
    number_of_notes = "100"
    optionals = args[3:]
    for (option, value) in list(zip(optionals[::2], optionals[1::2])):
        if option in ["-p", "--pitch"]:
            check_initial_note(value)
            note = value
        elif option in ["-i", "--instrument"]:
            check_instrument(value)
            instrument = value
        elif option in ["-s", "--scale"]:
            check_scale(value)
            scale = value
        elif option in ["-n", "--notes"]:
            number_of_notes = value
        else:
            print_generate_usage()
            exit(-1)
    generate(*args[:3], note, instrument, scale, int(number_of_notes))

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

