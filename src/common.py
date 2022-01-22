import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation, \
                         BatchNormalization as BatchNorm

SEQUENCE_LENGTH = 30

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
    network = Sequential()
    network.add(LSTM(512, 
        input_shape=(SEQUENCE_LENGTH * 2, 1),
        return_sequences=True, 
        recurrent_dropout=0.3
    ))
    network.add(LSTM(512))
    network.add(BatchNorm())
    network.add(Dropout(0.3))
    network.add(Dense(output_size))
    network.add(Activation('softmax'))
    network.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    return network