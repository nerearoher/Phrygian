import json
import tensorflow as tf
import np as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation, \
                         BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from sys import argv

def print_usage():
    print("Usage: " + argv[0] + " <processed midis file>")

def to_categorical(sequence):
    # TODO

def prepare_sequences(melodies, unique_pitches, unique_durations, output_size):
    sequence_length = 50

    pitch_to_index = dict((pitch, number) for number, pitch in enumerate(unique_pitches))
    duration_to_index = dict((duration, number) for number, duration in enumerate(unique_durations))

    to_index = lambda(note: [pitch_to_index[note[0]], duration_to_index[note[1]]])

    melodies = [[to_index(note) for note in melody] for melody in melodies]
    network_input = []
    network_output = []

    for melody in melodies:
        for i in range(0, len(melody) - sequence_length):
            sequence_in = [x for note in melody[i:i + sequence_length] for x in note]
            sequence_out = melody[i + sequence_length]
            network_input.append(sequence_in)
            network_output.append(to_categorical(sequence_out))

    # reshape the input into a format compatible with LSTM layers
    network_input = np.array(network_input)

    return (network_input, network_output)

def create_network(melodies, output_size):
    """ create the structure of the neural network """
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(melodies.shape[1], melodies.shape[2]),
        recurrent_dropout=0.3,
        return_sequences=True
    ))
    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(output_size))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    return model

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

    create_network(melodies, output_size)

    print("Train network")