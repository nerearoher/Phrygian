import json
import numpy as np
import random
from common import prepare_sequences, create_network, instruments, scales
from melody import calculate_pitch
from music21.note import Note
from music21.stream import Stream
from math import sqrt

def generate_notes(model, network_input, unique_pitches, unique_durations):
    base = sequences[np.random.randint(0, len(sequences) - 1)]
    base = base.tolist()

    prediction_output = []
    while len(prediction_output) < 100:
        input = np.reshape(base, (1, len(base), 1))
        prediction = model.predict(input, verbose=0)

        pitch = np.argmax(prediction[0][:len(unique_pitches)])
        duration = np.argmax(prediction[0][len(unique_durations):])
        prediction_output.append([unique_pitches[pitch], unique_durations[duration]])

        base.insert(0, unique_pitches[pitch])
        base.insert(0, unique_durations[duration])
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
            return pitch_into_scale(pitch, scale[:pivot_index + 1])
        else:
            return pitch_into_scale(pitch, scale[pivot_index:])

def calculate_positive_pitch(pitch):
    if pitch == 0:
        return pitch
    if pitch % 12 == 0:
        return int(pitch / sqrt(pitch**2) * 12)
    return pitch % 12

def generate_midi(initial_note, notes, instrument, scale):
    stream = [instruments[instrument]]
    scale = scales[scale]
    initial_pitch = initial_note.pitch.midi
    pitch = initial_pitch
    new_note = Note(pitch)
    new_note.quarterLength = notes[np.random.randint(0, len(notes))][1]
    stream.append(new_note)

    for note in notes:
        pitch = normalize_pitch(pitch + note[0])
        dif = pitch - initial_pitch
        relative_pitch = calculate_pitch(dif)
        relative_positive_pitch = calculate_positive_pitch(relative_pitch)
        pitch += pitch_into_scale(relative_positive_pitch, scale) - relative_pitch
        new_note = Note(pitch)
        new_note.quarterLength = note[1]
        stream.append(new_note)
    
    dif = (pitch - initial_pitch) % 12
    pitch -= dif + (0 if dif > 6 else - 12)
    new_note = Note(pitch)
    new_note.quarterLength = 4
    stream.append(new_note)

    stream = Stream(stream)
    stream.show()
    return stream

def generate(melodies, weights_file, output_file, initial_note, instrument, scale):
    with open(melodies, "r") as input:
        melodies = json.loads(input.read())
        initial_note = Note(initial_note)

        pitches = [note[0] for melody in melodies for note in melody]
        durations = [note[1] for melody in melodies for note in melody]
        unique_pitches = list(set(pitches))
        unique_durations = list(set(durations))
        output_size = len(unique_pitches) + len(unique_durations)
        (sequences, outputs) = prepare_sequences(melodies, unique_pitches, unique_durations)

        network = create_network(sequences, output_size)
        network.load_weights(weights_file)
        notes = generate_notes(network, sequences, unique_pitches, unique_durations)
        midi = generate_midi(initial_note, notes, instrument, scale)
        midi.write('midi', fp=output_file)
        print("Music generated!")
