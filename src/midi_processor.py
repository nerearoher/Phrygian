
# Relevant:
# https://mido.readthedocs.io/en/latest/midi_files.html
# https://github.com/Skuldur/Classical-Piano-Composer

from sys import argv
from glob import glob
from multiprocessing import Pool
import json
from music21 import converter
from music21.note import Note, Rest
from music21.chord import Chord

from melody import Melody

def read_melodies_from_file(file: str):
    print(f"Processing file: {file}")
    try:
        score = converter.parse(file)
    except:
        print(f"An error ocurred, skipping file: {file}")
        return []
    return list(map(lambda part: Melody(part), score))

def print_usage():
    print("Usage: " + argv[0] + " <midi files folder> <output file>")

if len(argv) > 1 and (argv[1] == "-h" or argv[1] == "--help"):
    print_usage()
    exit()

if len(argv) != 3:
    print("Wrong number of arguments")
    print_usage()
    exit()

midi_files = glob(argv[1] + "/**/*.mid") + glob(argv[1] + "/**/*.MID")

pool = Pool()
unflattened_melodies = pool.imap_unordered(read_melodies_from_file, midi_files)
melodies = [m for melodies in unflattened_melodies for m in melodies]
with open(argv[2], "w") as output:
    raw_melodies = list(map(lambda melody: melody.to_notes(), melodies))
    output.write(json.dumps(raw_melodies))
