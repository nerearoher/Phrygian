from os import path
import json
from tensorflow.keras.callbacks import ModelCheckpoint
from common import prepare_sequences, create_network

def train_network(network, sequences, outputs, weights_folder):
    filepath = path.join(weights_folder, "weights-{epoch:02d}-{loss:.4f}.hdf5")

    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        mode='min'
    )
    network.fit(sequences, outputs, epochs=8, callbacks=[checkpoint])

def train(sequences_file, weights_folder):
    with open(sequences_file, "r") as input:
        content = input.read()
        melodies = json.loads(content)

        pitches = [note[0] for melody in melodies for note in melody]
        durations = [note[1] for melody in melodies for note in melody]
        unique_pitches = list(set(pitches))
        unique_durations = list(set(durations))
        output_size = len(unique_pitches) + len(unique_durations)
        (sequences, outputs) = prepare_sequences(melodies, unique_pitches, unique_durations)

        network = create_network(sequences, output_size)
        train_network(network, sequences, outputs, weights_folder)
