
# Relevant:
# https://mido.readthedocs.io/en/latest/midi_files.html
# https://github.com/Skuldur/Classical-Piano-Composer

import sys
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
    return list(map(lambda part: melodies.append(Melody(part)), score))

def print_usage():
    print("Usage: " + sys.argv[0] + " <midi files folder> <output file>")

if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
    print_usage()
    exit()

if len(sys.argv) != 3:
    print("Wrong number of arguments")
    print_usage()
    exit()

midi_files = glob(sys.argv[1] + "/**/*.mid") + glob(sys.argv[1] + "/**/*.MID")

pool = Pool()
unflattened_melodies = pool.imap_unordered(read_melodies_from_file, midi_files)
melodies = [m for melodies in unflattened_melodies for m in melodies]
with open(sys.argv[2], "w") as output:
    output.write(json.dumps(list(map(lambda melody: melody.notes, melodies))))
