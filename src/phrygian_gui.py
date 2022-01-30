from PyQt5.QtWidgets import (
  QApplication, QWidget, 
  QPushButton, QVBoxLayout, 
  QHBoxLayout, QDialog, 
  QLabel, QFileDialog, 
  QTextEdit, QComboBox, 
  QFormLayout, QLineEdit, 
  QGridLayout, QLineEdit,
  QLayout, QSpinBox, QDialogButtonBox
)
from PyQt5.QtCore import Qt
from css import PHRYGIAN_GUI

# from process_midis import process
# from train_network import train
# from generate_music import generate
from music21 import instrument

PROCESS_STRING = 'Process MIDIs melodies'
TRAIN_STRING = 'Train neuronal network'
GENERATE_STRING = 'Generate music'

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

def on_process_button_clicked():
  dialog = QDialog()
  dialog.setStyleSheet(PHRYGIAN_GUI)
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(PROCESS_STRING)

  def set_midi_folder():
    directory_list = QFileDialog.getExistingDirectory(None, "Select MIDI input Directory")
    if directory_list:
      line_edit_midi_folder.setText(directory_list[0])

  def set_output_file():
    line_edit_output_file.setText(QFileDialog.getSaveFileName(None, 'Create a processed midi file', '', '')[0])

  label_midi_folder = QLabel('Select a midi folder')
  label_output_midi = QLabel('File to save the generated melodies')
  label_midi_folder.setObjectName('QLabelRow')
  label_output_midi.setObjectName('QLabelRow')

  browser_button_midi = QPushButton('Browser...')
  browser_button_midi.setStyleSheet(PHRYGIAN_GUI)
  browser_button_output = QPushButton('Browser...')
  browser_button_output.setStyleSheet(PHRYGIAN_GUI)

  line_edit_midi_folder = QLineEdit()
  line_edit_midi_folder.setObjectName('QLineEdit')
  line_edit_midi_folder.setReadOnly(True)
  browser_button_midi.pressed.connect(set_midi_folder)
  layout.addWidget(line_edit_midi_folder)
  layout.addRow(label_midi_folder, line_edit_midi_folder)
  layout.addWidget(browser_button_midi)

  line_edit_output_file = QLineEdit()
  line_edit_output_file.setObjectName('QLineEdit')
  line_edit_output_file.setReadOnly(True)
  browser_button_output.pressed.connect(set_output_file)
  layout.addWidget(line_edit_output_file)
  layout.addRow(label_output_midi, line_edit_output_file)
  layout.addWidget(browser_button_output)

  qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
  buttonBox = QDialogButtonBox(qbtn)
  buttonBox.accepted.connect(dialog.accept)
  buttonBox.rejected.connect(dialog.reject)
  layout.addWidget(buttonBox)

  dialog.setLayout(layout)
  dialog.exec()

def on_train_button_clicked():
  dialog = QDialog()
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(TRAIN_STRING)

  def set_processed_midi():
    line_edit_processed_midi.setText(QFileDialog.getOpenFileName (None, 'Select processed midi file')[0])

  def set_weights_folder():
    directory_list = QFileDialog.getExistingDirectory(None, "Select weights Directory")
    if directory_list:
      line_edit_midi_folder.setText(directory_list[0])

  label_processed_midi = QLabel('Select processed midi')
  label_wights_folder = QLabel('Select neural network weights folder')

  browser_button_midi = QPushButton('Browser...')
  browser_button_wights = QPushButton('Browser...')

  line_edit_processed_midi = QLineEdit()
  line_edit_processed_midi.setReadOnly(True)
  browser_button_midi.pressed.connect(set_processed_midi)
  layout.addWidget(line_edit_processed_midi)
  layout.addRow(label_processed_midi, line_edit_processed_midi)
  layout.addWidget(browser_button_midi)

  line_edit_weights_folder = QLineEdit()
  line_edit_weights_folder.setReadOnly(True)
  browser_button_wights.pressed.connect(set_weights_folder)
  layout.addWidget(line_edit_weights_folder)
  layout.addRow(label_wights_folder, line_edit_weights_folder)
  layout.addWidget(browser_button_wights)

  qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
  buttonBox = QDialogButtonBox(qbtn)
  buttonBox.accepted.connect(dialog.accept)
  buttonBox.rejected.connect(dialog.reject)
  layout.addWidget(buttonBox)

  dialog.setLayout(layout)
  dialog.exec()
  
def on_generate_button_clicked():
  dialog = QDialog()
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(GENERATE_STRING)

  def set_processed_midi():
    line_edit_processed_midi.setText(QFileDialog.getOpenFileName (None, 'Select processed midi file')[0])

  def set_weights_file():
    line_edit_weights.setText(QFileDialog.getOpenFileName(None, "Select neural networks weights")[0])
  
  def set_line_edit_output_midi_file():
    line_edit_output_midi_file.setText(QFileDialog.getSaveFileName(None, 'Save output midi File', '', '*.mid;;*.MID')[0])

  label_processed_midi = QLabel('Select a processed midi file')
  line_edit_processed_midi = QLineEdit()
  line_edit_processed_midi.setReadOnly(True)
  browser_button_midi = QPushButton('Browser...')
  browser_button_midi.pressed.connect(set_processed_midi)
  layout.addWidget(line_edit_processed_midi)
  layout.addRow(label_processed_midi, line_edit_processed_midi)
  layout.addWidget(browser_button_midi)

  label_weights = QLabel('Select a folder to save the generated melodies')
  line_edit_weights = QLineEdit()
  line_edit_weights.setReadOnly(True)
  browser_button_nw = QPushButton('Browser...')
  browser_button_nw.pressed.connect(set_weights_file)
  layout.addWidget(line_edit_weights)
  layout.addRow(label_weights, line_edit_weights)
  layout.addWidget(browser_button_nw)

  label_output_midi = QLabel('Write output midi file')
  line_edit_output_midi_file = QLineEdit()
  line_edit_output_midi_file.setReadOnly(True)
  browser_button_output = QPushButton('Browser...')
  browser_button_output.pressed.connect(set_line_edit_output_midi_file)
  layout.addWidget(line_edit_output_midi_file)
  layout.addRow(label_output_midi, line_edit_output_midi_file)
  layout.addWidget(browser_button_output)

  label_note = QLabel('Select the initial note')
  combo_box_pitch = QComboBox()
  combo_box_pitch.addItems([chr(i) for i in range(ord('A'), ord('G') + 1)])

  combo_box_accidental = QComboBox()
  combo_box_accidental.addItems(['', '♯', '♭'])

  spin_box_scale = QSpinBox()
  spin_box_scale.setRange(1, 8)
  spin_box_scale.setValue(3)
  layout.addWidget(spin_box_scale)

  note_layout = QHBoxLayout()
  note_layout.addWidget(combo_box_pitch)
  note_layout.addWidget(combo_box_accidental)
  note_layout.addWidget(spin_box_scale)
  layout.addRow(label_note, note_layout)

  label_instruments = QLabel('Select the instrument')
  combo_box_instruments = QComboBox()
  combo_box_instruments.addItems(INSTRUMENTS.keys())
  combo_box_instruments.setCurrentIndex(list(INSTRUMENTS.keys()).index('Piano'))
  layout.addWidget(combo_box_instruments)
  layout.addRow(label_instruments, combo_box_instruments)

  label_scale = QLabel('Select the scale')
  combo_box_scale = QComboBox()
  combo_box_scale.addItems(SCALES.keys())
  layout.addWidget(combo_box_scale)
  layout.addRow(label_scale, combo_box_scale)

  label_number = QLabel('Select the number of notes')
  spin_box_notes = QSpinBox()
  spin_box_notes.setRange(2, 999999)
  spin_box_notes.setValue(100)
  layout.addWidget(spin_box_notes)
  layout.addRow(label_number, spin_box_notes)
  
  qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
  buttonBox = QDialogButtonBox(qbtn)
  buttonBox.accepted.connect(dialog.accept)
  buttonBox.rejected.connect(dialog.reject)
  layout.addWidget(buttonBox)

  dialog.setLayout(layout)
  dialog.exec()

app = QApplication([])

window = QWidget()
window.setWindowTitle("Phrygian")
window.setStyleSheet(PHRYGIAN_GUI)
layout = QVBoxLayout()
layout.setSizeConstraint(QLayout.SetFixedSize)

label_welcome = QLabel('WELCOME TO PHRYGIAN')
layout.addWidget(label_welcome)
label_welcome.setObjectName('label_welcome')

process_button = QPushButton(PROCESS_STRING)
train_button = QPushButton(TRAIN_STRING)
generate_button = QPushButton(GENERATE_STRING)

layout.addWidget(process_button)
layout.addWidget(train_button)
layout.addWidget(generate_button)

process_button.clicked.connect(on_process_button_clicked)
train_button.clicked.connect(on_train_button_clicked)
generate_button.clicked.connect(on_generate_button_clicked)

window.setLayout(layout)
window.show()
app.exec()
