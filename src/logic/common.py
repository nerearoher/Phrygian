import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation, \
                         BatchNormalization as BatchNorm
from music21 import instrument

SEQUENCE_LENGTH = 50

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
    network.add(LSTM(128, 
        input_shape=(SEQUENCE_LENGTH * 2, 1)
    ))
    network.add(BatchNorm())
    network.add(Dropout(0.3))
    network.add(Dense(output_size))
    network.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    return network

instruments = {
    "Accordion": instrument.Accordion(),
    "AcousticBass": instrument.AcousticBass(),
    "AcousticGuitar": instrument.AcousticGuitar(),
    "Agogo": instrument.Agogo(),
    "Alto": instrument.Alto(),
    "AltoSaxophone": instrument.AltoSaxophone(),
    "Bagpipes": instrument.Bagpipes(),
    "Banjo": instrument.Banjo(),
    "Baritone": instrument.Baritone(),
    "BaritoneSaxophone": instrument.BaritoneSaxophone(),
    "Bass": instrument.Bass(),
    "BassClarinet": instrument.BassClarinet(),
    "BassDrum": instrument.BassDrum(),
    "BassTrombone": instrument.BassTrombone(),
    "Bassoon": instrument.Bassoon(),
    "BongoDrums": instrument.BongoDrums(),
    "BrassInstrument": instrument.BrassInstrument(),
    "Castanets": instrument.Castanets(),
    "Celesta": instrument.Celesta(),
    "Choir": instrument.Choir(),
    "ChurchBells": instrument.ChurchBells(),
    "Clarinet": instrument.Clarinet(),
    "Clavichord": instrument.Clavichord(),
    "Conductor": instrument.Conductor(),
    "CongaDrum": instrument.CongaDrum(),
    "Contrabass": instrument.Contrabass(),
    "Contrabassoon": instrument.Contrabassoon(),
    "Cowbell": instrument.Cowbell(),
    "CrashCymbals": instrument.CrashCymbals(),
    "Cymbals": instrument.Cymbals(),
    "Dulcimer": instrument.Dulcimer(),
    "ElectricBass": instrument.ElectricBass(),
    "ElectricGuitar": instrument.ElectricGuitar(),
    "ElectricOrgan": instrument.ElectricOrgan(),
    "ElectricPiano": instrument.ElectricPiano(),
    "EnglishHorn": instrument.EnglishHorn(),
    "FingerCymbals": instrument.FingerCymbals(),
    "Flute": instrument.Flute(),
    "FretlessBass": instrument.FretlessBass(),
    "Glockenspiel": instrument.Glockenspiel(),
    "Gong": instrument.Gong(),
    "Guitar": instrument.Guitar(),
    "Handbells": instrument.Handbells(),
    "Harmonica": instrument.Harmonica(),
    "Harp": instrument.Harp(),
    "Harpsichord": instrument.Harpsichord(),
    "HiHatCymbal": instrument.HiHatCymbal(),
    "Horn": instrument.Horn(),
    "Kalimba": instrument.Kalimba(),
    "KeyboardInstrument": instrument.KeyboardInstrument(),
    "Koto": instrument.Koto(),
    "Lute": instrument.Lute(),
    "Mandolin": instrument.Mandolin(),
    "Maracas": instrument.Maracas(),
    "Marimba": instrument.Marimba(),
    "MezzoSoprano": instrument.MezzoSoprano(),
    "Oboe": instrument.Oboe(),
    "Ocarina": instrument.Ocarina(),
    "Organ": instrument.Organ(),
    "PanFlute": instrument.PanFlute(),
    "Percussion": instrument.Percussion(),
    "Piano": instrument.Piano(),
    "Piccolo": instrument.Piccolo(),
    "PipeOrgan": instrument.PipeOrgan(),
    "PitchedPercussion": instrument.PitchedPercussion(),
    "Ratchet": instrument.Ratchet(),
    "Recorder": instrument.Recorder(),
    "ReedOrgan": instrument.ReedOrgan(),
    "RideCymbals": instrument.RideCymbals(),
    "Sampler": instrument.Sampler(),
    "SandpaperBlocks": instrument.SandpaperBlocks(),
    "Saxophone": instrument.Saxophone(),
    "Shakuhachi": instrument.Shakuhachi(),
    "Shamisen": instrument.Shamisen(),
    "Shehnai": instrument.Shehnai(),
    "Siren": instrument.Siren(),
    "Sitar": instrument.Sitar(),
    "SizzleCymbal": instrument.SizzleCymbal(),
    "SleighBells": instrument.SleighBells(),
    "SnareDrum": instrument.SnareDrum(),
    "Soprano": instrument.Soprano(),
    "SopranoSaxophone": instrument.SopranoSaxophone(),
    "SplashCymbals": instrument.SplashCymbals(),
    "SteelDrum": instrument.SteelDrum(),
    "StringInstrument": instrument.StringInstrument(),
    "SuspendedCymbal": instrument.SuspendedCymbal(),
    "Taiko": instrument.Taiko(),
    "TamTam": instrument.TamTam(),
    "Tambourine": instrument.Tambourine(),
    "TempleBlock": instrument.TempleBlock(),
    "Tenor": instrument.Tenor(),
    "TenorDrum": instrument.TenorDrum(),
    "TenorSaxophone": instrument.TenorSaxophone(),
    "Timbales": instrument.Timbales(),
    "Timpani": instrument.Timpani(),
    "TomTom": instrument.TomTom(),
    "Triangle": instrument.Triangle(),
    "Trombone": instrument.Trombone(),
    "Trumpet": instrument.Trumpet(),
    "Tuba": instrument.Tuba(),
    "TubularBells": instrument.TubularBells(),
    "Ukulele": instrument.Ukulele(),
    "UnpitchedPercussion": instrument.UnpitchedPercussion(),
    "Vibraphone": instrument.Vibraphone(),
    "Vibraslap": instrument.Vibraslap(),
    "Viola": instrument.Viola(),
    "Violin": instrument.Violin(),
    "Violoncello": instrument.Violoncello(),
    "Vocalist": instrument.Vocalist(),
    "Whip": instrument.Whip(),
    "Whistle": instrument.Whistle(),
    "WindMachine": instrument.WindMachine(),
    "Woodblock": instrument.Woodblock(),
    "WoodwindInstrument": instrument.WoodwindInstrument(),
    "Xylophone": instrument.Xylophone()
}

# https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes
scales = {
    "Chromatic": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Octatonic": [0, 1, 3, 4, 6, 7, 9, 10, 12],
    "Hexatonic-Whole-Tone": [0, 2, 4, 6, 8, 10, 12],
    "Hexatonic-Blues": [0, 3, 5, 6, 7, 10, 12],
    "Pentatonic": [0, 2, 4, 7, 9, 12],
    "Pentatonic-Blues": [0, 2, 3, 4, 7, 9, 12],
    "Neapolitan-Major": [0, 1, 3, 5, 7, 9, 11, 12],
    "Neapolitan-Minor": [0, 1, 3, 5, 7, 8, 11, 12],
    "Flamenco": [0, 1, 4, 5, 7, 8, 11, 12], 
    "Minor": [0, 2, 3, 5, 7, 8, 11, 12],
    "Ionian": [0, 2, 4, 5, 7, 9, 11, 12],
    "Dorian": [0, 2, 4, 5, 7, 9, 10, 12],
    "Phrygian": [0, 1, 3, 6, 7, 8, 10, 12],
    "Lydian": [0, 2, 4, 6, 7, 9, 11, 12],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10, 12],
    "Aeolian": [0, 2, 3, 5, 7, 8, 10, 12],
    "Locrian": [0, 1, 3, 5, 6, 8, 10, 12],
    "Enigma": [0, 1, 4, 6, 8, 10, 11, 12]
}
