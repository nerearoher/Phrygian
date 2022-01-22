import json
from sys import argv
import numpy as np
from common import prepare_sequences, create_network

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file> <neural networks weights>")

def generate_notes(model, network_input, unique_pitches, unique_durations):
    base = sequences[np.random.randint(0, len(sequences) - 1)]

    prediction_output = []

    # generate 500 notes
    for note_index in range(500):
        input = numpy.reshape(base, (1, len(base), 1))
        prediction = model.predict(input, verbose=0)

        pitch = np.argmax(prediction[:len(unique_pitches)])
        duration = np.argmax(prediction[len(unique_durations):])
        prediction_output.append([unique_pitches[pitch], unique_durations[duration]])

        base.append(index)
        base = base[1:len(base)]

    return prediction_output

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

    pitches = [note[0] for melody in melodies for note in melody]
    durations = [note[1] for melody in melodies for note in melody]
    unique_pitches = list(set(pitches))
    unique_durations = list(set(durations))
    output_size = len(unique_pitches) + len(unique_durations)
    (sequences, outputs) = prepare_sequences(melodies, unique_pitches, unique_durations)

    network = create_network(sequences, output_size)
    network.load_weight(argv[2])
    print(generate_notes(network, sequences, outputs))

    print("Train network")