from music21.note import Note, Rest
from music21.stream import Stream
from music21.chord import Chord
from math import sqrt

def calculate_pitch(pitch):
    if pitch == 0:
        return pitch
    if pitch % 12 == 0:
        return pitch / int(sqrt(pitch**2)) * 12
    return (- 12 if pitch < 0 else 0) + pitch % 12

def calculate_duration(duration):
    return min(int(float(duration) * 4) / 4, 4.0)

class Melody():
    def __init__(self, part: Stream):
        self.notes = []
        self.previous_pitch = None
        if part is not None: 
            for element in part.recurse():
                if isinstance(element, Note):
                    self.add_note(element)
                elif isinstance(element, Chord):
                    self.add_chord(element)
                elif isinstance(element, Rest):
                    self.add_rest(element)
    
    def add_note(self, note: Note):
        duration = calculate_duration(note.quarterLength)
        if self.previous_pitch is None:
            self.notes.append((0, duration))
        else:
            self.notes.append((calculate_pitch(note.pitch.midi - self.previous_pitch), duration))
        self.previous_pitch = note.pitch.midi

    def add_chord(self, chord: Chord):
        duration = calculate_duration(chord.quarterLength)
        for pitch in chord.pitches[:-1]:
            if self.previous_pitch is None:
                self.notes.append((0, duration))
            else:
                self.notes.append((calculate_pitch(pitch.midi - self.previous_pitch), duration))
            self.previous_pitch = pitch.midi
        last_pitch = chord.pitches[-1]
        self.notes.append((calculate_pitch(last_pitch.midi - self.previous_pitch), duration))

    def add_rest(self, rest: Rest):
        duration = calculate_duration(rest.quarterLength)
        if len(self.notes) != 0:
            self.notes[-1] = (self.notes[-1][0], self.notes[-1][1] + duration)
            
    def to_notes(self) -> [(int, float)]:
        return self.notes