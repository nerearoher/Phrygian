from music21.note import Note, Rest
from music21.stream import Stream
from music21.chord import Chord

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
        duration = float(note.quarterLength)
        if self.previous_pitch is None:
            self.notes.append((0, duration))
        else:
            self.notes.append((note.pitch.midi - self.previous_pitch, duration))
        self.previous_pitch = note.pitch.midi

    def add_chord(self, chord: Chord):
        duration = float(chord.quarterLength)
        for pitch in chord.pitches[:-1]:
            if self.previous_pitch is None:
                self.notes.append((0, duration))
            else:
                self.notes.append((pitch.midi - self.previous_pitch, 0))
            self.previous_pitch = pitch.midi
        last_pitch = chord.pitches[-1]
        self.notes.append((last_pitch.midi - self.previous_pitch, duration))

    def add_rest(self, rest: Rest):
        duration = float(rest.quarterLength)
        if len(self.notes) != 0:
            self.notes[-1] = (self.notes[-1][0], self.notes[-1][1] + duration)