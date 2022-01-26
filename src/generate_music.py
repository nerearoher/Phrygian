import json
from sys import argv
import numpy as np
import random
from common import prepare_sequences, create_network, instruments, scales
from music21.note import Note
from music21.stream import Stream
from music21 import instrument

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file> <neural networks weights> <initial note> <output midi file> <instrument>")
    print("Available instruments: " + ", ".join(instruments.keys()))

def generate_notes(model, network_input, unique_pitches, unique_durations):
    base = sequences[np.random.randint(0, len(sequences) - 1)]
    base = base.tolist()
    print(base)

    prediction_output = []
    longest_duration = -1

    while len(prediction_output) < 100 or prediction_output[-1][1] < longest_duration * 0.75 and len(prediction_output) < 300:
        input = np.reshape(base, (1, len(base), 1))
        prediction = model.predict(input, verbose=0)

        pitch = np.argmax(prediction[0][:len(unique_pitches)])
        duration = np.argmax(prediction[0][len(unique_durations):])
        longest_duration = duration if duration > longest_duration else longest_duration
        prediction_output.append([unique_pitches[pitch], unique_durations[duration]])

        base.insert(0, pitch)
        base.insert(0, duration)
        base = base[:-2]
        if len(prediction_output) > 3:
            if prediction_output[-3][0] == prediction_output[-2][0] == prediction_output[-1][0]:
                base = sequences[np.random.randint(0, len(sequences) - 1)]
                base = base.tolist()
                prediction_output = prediction_output[:-2]

    return prediction_output

def normalize_pitch(pitch):
    if pitch < 24:
        return pitch + 12
    if pitch > 84:
        return pitch - 12
    return pitch

def get_instrument(name_instrument):
    if not name_instrument in instruments:
        print("Invalid instrument " + name_instrument + ", check the list of available instruments:")
        print("Available instruments: " + ", ".join(instruments.keys()))
        exit(-1)
    return instruments[name_instrument]

def get_scale(name_scale):
    if not name_scale in scales:
        print("Invalid scale " + name_scale + ", check the list of available scales:")
        print("Available scales: " + ", ".join(scales.keys()))
        exit(-1)
    return scales[name_scale]

def pitch_into_scale(pitch, scale):
    pivot_index = len(scale) // 2
    pivot = scale[pivot_index]
    if len(scale) <= 2:
        if pitch == pivot or pitch == scale[pivot_index - 1]:
            return pitch
        else:
            if len(scale) == 1:
                return scale[0]
            else:
                if abs(scale[0] - pitch) < abs(scale[1] - pitch):
                    return scale[0]
                elif abs(scale[1] - pitch) < abs(scale[0] - pitch):
                    return scale[1]
                else:
                    return scale[0] if bool(random.getrandbits(1)) else scale[1]
    else:
        if pitch <= pivot:
            return normalize_pitch(pitch, scale[:pivot_index + 1])
        else:
            return normalize_pitch(pitch, scale[pivot_index:])

def generate_midi(initial_note, notes, name_instrument, name_scale):
    stream = [get_instrument(name_instrument)]
    scale = get_scale(name_scale)
    initial_pitch = initial_note.pitch.midi
    pitch = initial_pitch
    new_note = Note(pitch)
    new_note.quarterLength = notes[np.random.randint(0, len(notes))][1]
    stream.append(new_note)

    for note in notes:
        pitch = normalize_pitch(pitch + note[0], scale)
        pitch = pitch_into_scale(pitch, scale)
        new_note = Note(pitch)
        new_note.quarterLength = note[1]
        stream.append(new_note)

    stream = Stream(stream)
    stream.show()
    return stream

if len(argv) > 1 and (argv[1] == "-h" or argv[1] == "--help"):
    print_usage()
    exit()

if len(argv) != 6:
    print("Wrong number of arguments")
    print_usage()
    exit()

with open(argv[1], "r") as input:
    content = input.read()
    weights_file = argv[2]
    initial_note = Note(argv[3])
    output_file = argv[4]
    name_instrument = argv[5]
    melodies = json.loads(content)

    pitches = [note[0] for melody in melodies for note in melody]
    durations = [note[1] for melody in melodies for note in melody]
    unique_pitches = list(set(pitches))
    unique_durations = list(set(durations))
    output_size = len(unique_pitches) + len(unique_durations)
    (sequences, outputs) = prepare_sequences(melodies, unique_pitches, unique_durations)

    network = create_network(sequences, output_size)
    network.load_weights(weights_file)
    notes = generate_notes(network, sequences, unique_pitches, unique_durations)
    midi = generate_midi(initial_note, notes, name_instrument)
    midi.write('midi', fp=output_file)
    print("Train network")