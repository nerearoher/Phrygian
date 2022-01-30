from PyQt5.QtWidgets import (
  QWidget, QPushButton, QVBoxLayout, 
  QHBoxLayout, QDialog, QLabel,
  QFileDialog, QComboBox, QFormLayout, QLineEdit, 
  QSpinBox, QDialogButtonBox 
)
from music21 import instrument
from common_gui import accept_and_finish

INSTRUMENTS = {
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

SCALES = {
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

def generate(*args):
  pass

class NoteInput(QHBoxLayout):
  def __init__(self):
    super().__init__()
    self.pitch = QComboBox()
    self.pitch.addItems([chr(i) for i in range(ord('A'), ord('G') + 1)])
    self.addWidget(self.pitch)

    self.symbol = QComboBox()
    self.symbol.addItems(['', '♯', '♭'])
    self.addWidget(self.symbol)

    self.scale = QSpinBox()
    self.scale.setRange(1, 8)
    self.scale.setValue(3)
    self.addWidget(self.scale)

  def get_note(self):
    return str(self.pitch.currentData()) + \
      str(self.symbol.currentData()) + \
      str(self.scale.value())

class GenerationWindow(QDialog):
  def __init__(self, parent):
    super().__init__(parent)
    self.setWindowTitle("GenerateMusic")
    self.layout = QVBoxLayout()
    self.setup_form()
    self.setup_end_buttons()
    self.setLayout(self.layout)
    self.exec()

  def setup_form(self):
    form = QWidget(self)
    form_layout = QFormLayout()
    label_processed_midi = QLabel('Select a processed midi file')
    self.processed_midi_input = QLineEdit()
    self.processed_midi_input.setReadOnly(True)
    form_layout.addRow(label_processed_midi, self.processed_midi_input)
    browser_button_midi = QPushButton('Browser...')
    browser_button_midi.pressed.connect(lambda: self.processed_midi_input.setText(
      QFileDialog.getOpenFileName(None, 'Select processed midi file (melodies)')[0]
    ))
    form_layout.addWidget(browser_button_midi)

    label_weights = QLabel('Select a folder to save the generated melodies')
    self.weights_input = QLineEdit()
    self.weights_input.setReadOnly(True)
    form_layout.addRow(label_weights, self.weights_input)
    browser_button_weights = QPushButton('Browser...')
    browser_button_weights.pressed.connect(lambda: self.weights_input.setText(
      QFileDialog.getOpenFileName(None, "Select neural networks weights")[0]
    ))
    form_layout.addWidget(browser_button_weights)

    label_output_midi = QLabel('Write output midi file')
    self.output_file_input = QLineEdit()
    self.output_file_input.setReadOnly(True)
    form_layout.addRow(label_output_midi, self.output_file_input)
    browser_button_output = QPushButton('Browser...')
    browser_button_output.pressed.connect(lambda: self.output_file_input.setText(
      QFileDialog.getSaveFileName(None, 'Save output midi File', '', '*.mid;;*.MID')[0]
    ))
    form_layout.addWidget(browser_button_output)

    label_note = QLabel('Select the initial note')
    self.note_input = NoteInput()
    form_layout.addRow(label_note, self.note_input)

    label_instruments = QLabel('Select the instrument')
    self.instrument_input = QComboBox()
    self.instrument_input.addItems(INSTRUMENTS.keys())
    self.instrument_input.setCurrentIndex(list(INSTRUMENTS.keys()).index('Piano'))
    form_layout.addRow(label_instruments, self.instrument_input)

    label_scale = QLabel('Select the scale')
    self.scale_input = QComboBox()
    self.scale_input.addItems(SCALES.keys())
    form_layout.addRow(label_scale, self.scale_input)

    label_number = QLabel('Select the number of notes')
    self.number_of_notes_input = QSpinBox()
    self.number_of_notes_input.setRange(2, 999999)
    self.number_of_notes_input.setValue(100)
    form_layout.addRow(label_number, self.number_of_notes_input)
    form.setLayout(form_layout)
    self.layout.addWidget(form)

  def setup_end_buttons(self):
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.end_dialog)
    buttonBox.rejected.connect(self.reject)
    self.layout.addWidget(buttonBox)

  def end_dialog():
    accept_and_finish([
      self.processed_midi_input.text(),
      self.weigths_input.text(),
      self.output_file_input.text(),
      self.note_input.get_note(),
      self.instruments_input.currentData(),
      self.scale_input.currentData(),
      self.number_of_notes_input.value()
    ], generate, self)

