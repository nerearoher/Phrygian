
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
        return []
    melodies = []
    for part in score:
        melody = Melody(part)
        melodies.append(melody)
    return melodies

if len(sys.argv) != 2:
    print("Wrong number of arguments")
    print("Usage: " + sys.argv[0] + " <midi files folder>")
    exit()

midi_files = glob(sys.argv[1] + "/**/*.mid")

pool = Pool()
unflattened_melodies = pool.imap_unordered(read_melodies_from_file, midi_files)
melodies = [m for melodies in unflattened_melodies for m in melodies]
with open('melodies', 'w') as output:
    json_melodies = json.dumps(list(map(lambda melody: melody.notes, melodies)))
    output.write(json_melodies) 
