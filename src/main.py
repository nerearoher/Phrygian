
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
        melody = []
        previous_pitch = None
        for element in part.recurse():
            print(element)
            if element.quarterLength:
                duration = element.quarterLength

            if isinstance(element, note.Note):
                if previous_pitch is None:
                    melody.append((0, duration))
                else:
                    melody.append((element.pitch.midi - previous_pitch, duration))
                previous_pitch = element.pitch.midi
            elif isinstance(element, chord.Chord):
                for pitch in element.pitches[:-1]:
                    if previous_pitch is None:
                        melody.append((0, duration))
                    else:
                        melody.append((pitch.midi - previous_pitch, 0))
                    previous_pitch = pitch.midi
                last_pitch = element.pitches[-1]
                melody.append((last_pitch.midi - previous_pitch, duration))
                previous_pitch = last_pitch.midi
            elif isinstance(element, note.Rest) and len(melody) != 0:
                melody[-1] = (melody[-1][0], melody[-1][1] + duration)
        print(str(melody))
        melodies.append(melody)
