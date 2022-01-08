import json
from sys import argv

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file>")

if len(argv) > 1 and (argv[1] == "-h" or argv[1] == "--help"):
    print_usage()
    exit()

if len(argv) != 2:
    print("Wrong number of arguments")
    print_usage()
    exit()

with open(argv[1], "r") as input:
    content = input.read()
    melodies = json.loads(content)
    print("Train network")