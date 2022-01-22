import json
from sys import argv
import numpy as np
from common import prepare_sequences, create_network
from music21.note import Note
from music21.stream import Stream

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file> <neural networks weights> <initial note> <output midi file>")

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

def generate_midi(initial_note, notes):
    stream = [] 
    pitch = initial_note.pitch.midi
    new_note = Note(pitch)
    new_note.quarterLength = notes[np.random.randint(0, len(notes))][1]
    stream.append(new_note)

    for note in notes:
        pitch = normalize_pitch(pitch + note[0])
        new_note = Note(pitch)
        new_note.quarterLength = note[1]
        stream.append(new_note)

    return Stream(stream)

if len(argv) > 1 and (argv[1] == "-h" or argv[1] == "--help"):
    print_usage()
    exit()

if len(argv) != 5:
    print("Wrong number of arguments")
    print_usage()
    exit()

with open(argv[1], "r") as input:
    content = input.read()
    weights_file = argv[2]
    initial_note = Note(argv[3])
    output_file = argv[4]
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
    midi = generate_midi(initial_note, notes)
    midi.write('midi', fp=output_file)
    print("Train network")