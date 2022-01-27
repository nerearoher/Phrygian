
# Relevant:
# https://github.com/Skuldur/Classical-Piano-Composer

from multiprocessing import Pool
import json
from music21 import converter
from music21.note import Note, Rest
from music21.chord import Chord
from glob import glob

from melody import Melody

def read_melodies_from_file(file: str):
    print(f"Processing file: {file}")
    try:
        score = converter.parse(file)
    except:
        print(f"An error ocurred, skipping file: {file}")
        return []
    return list(map(lambda part: Melody(part), score))

def process(midi_folder, output_file):
    midi_files = glob(midi_folder + "/**/*.mid") + glob(midi_folder + "/**/*.MID")

    pool = Pool()
    unflattened_melodies = pool.imap_unordered(read_melodies_from_file, midi_files)
    melodies = [m for melodies in unflattened_melodies for m in melodies]
    with open(output_file, "w") as output:
        raw_melodies = list(map(lambda melody: melody.to_notes(), melodies))
        output.write(json.dumps(raw_melodies))
