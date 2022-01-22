import json
from keras.callbacks import ModelCheckpoint
from sys import argv
from common import prepare_sequences, create_network


def print_usage():
    print("Usage: " + argv[0] + " <processed midis file>")

def train_network(network, sequences, outputs):
    filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        mode='min'
    )
    network.fit(sequences, outputs, epochs=8, callbacks=[checkpoint])

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
    train_network(network, sequences, outputs)

    print("Train network")