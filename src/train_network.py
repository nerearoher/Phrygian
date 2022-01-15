import json
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation, \
                         BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from sys import argv

SEQUENCE_LENGTH = 50

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file>")

def prepare_sequences(melodies, unique_pitches, unique_durations):
    pitches_number = len(unique_pitches)
    pitches_durations = len(unique_durations)
    def to_categorical(note):
        result = [0 for i in range(pitches_number + pitches_durations)]
        result[note[0]] = 1
        result[note[1] + pitches_number] = 1
        return result

    pitch_to_index = dict((pitch, number) for number, pitch in enumerate(unique_pitches))
    duration_to_index = dict((duration, number) for number, duration in enumerate(unique_durations))
    to_index = lambda note: [pitch_to_index[note[0]], duration_to_index[note[1]]]
    melodies = [[to_index(note) for note in melody] for melody in melodies]

    sequences = []
    outputs = []
    for melody in melodies:
        for i in range(0, len(melody) - SEQUENCE_LENGTH):
            sequence_in = [x for note in melody[i:i + SEQUENCE_LENGTH] for x in note]
            sequence_out = melody[i + SEQUENCE_LENGTH]
            sequences.append(sequence_in)
            outputs.append(to_categorical(sequence_out))

    # reshape the input into a format compatible with LSTM layers
    sequences = np.array(sequences)
    outputs = np.array(outputs)

    return (sequences, outputs)

def create_network(sequences, output_size):
    """ create the structure of the neural network """
    network = Sequential()
    network.add(LSTM(512, 
        input_shape=(SEQUENCE_LENGTH * 2, 1),
        return_sequences=True, 
        recurrent_dropout=0.3
    ))
    network.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
    network.add(LSTM(512))
    network.add(BatchNorm())
    network.add(Dropout(0.3))
    network.add(Dense(256))
    network.add(Activation('relu'))
    network.add(BatchNorm())
    network.add(Dropout(0.3))
    network.add(Dense(output_size))
    network.add(Activation('softmax'))
    network.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    return network

def train_network(network, sequences, outputs):
    filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    network.fit(sequences, outputs, epochs=200, callbacks=[checkpoint])

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