
# Relevant:
# https://mido.readthedocs.io/en/latest/midi_files.html
# https://github.com/Skuldur/Classical-Piano-Composer

import sys
from glob import glob
from music21 import converter, instrument, note, chord

if len(sys.argv) != 2:
    print("Wrong number of arguments")
    print("Usage: " + sys.argv[0] + " <midi files folder>")
    exit()

midi_files = glob(sys.argv[1] + "/**/*.mid")
melodies = []
for file in midi_files:
    print(f"Processing file: {file}")
    score = converter.parse(file)
    for part in score:
        for element in part.recurse():
            print(element)
        break
    break

