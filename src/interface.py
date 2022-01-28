
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLabel, QFileDialog, QTextEdit, QComboBox
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
# from common_gui import set_midi_folder
# from process_midis import process
# from train_network import train
# from generate_music import generate

PROCESS_STRING = 'Process MIDIs melodies'
TRAIN_STRING = 'Train neuronal network'
GENERATE_STRING = 'Generate music'

def on_process_button_clicked():
  dialog = QDialog()
  layout = QVBoxLayout()
  dialog.setWindowTitle(PROCESS_STRING)

  def set_midi_folder():
    midi_folder.setText(str(QFileDialog.getExistingDirectory(None, "Select Directory")))

  def set_output_file():
    # TODO save function
    # ESTA MAL
    # saveName, Filter = QFileDialog.getSaveFileName(None, "Save a Material property file", TargetDir, "*.FCMat")
    output_file.setText(str(QFileDialog.getSaveFileName(None, 'Save File', '', '*.mid;;*.MID')))

  midi_label = QLabel('Select a folder with midi files to extract melodies')
  midi_layout = QHBoxLayout()
  midi_folder = QTextEdit()
  midi_button = QPushButton("Browser...")
  midi_layout.addWidget(midi_folder)
  midi_layout.addWidget(midi_button)
  midi_button.clicked.connect(set_midi_folder)
  layout.addWidget(midi_label)
  layout.addLayout(midi_layout)

  output_label = QLabel('Select a folder to save the generated melodies')
  output_layout = QHBoxLayout()
  output_file = QTextEdit()
  output_button = QPushButton("Browser...")
  output_layout.addWidget(output_file)
  output_layout.addWidget(output_button)
  output_button.clicked.connect(set_output_file)
  layout.addWidget(output_label)
  layout.addLayout(output_layout)

  dialog.setLayout(layout)
  dialog.exec()

def on_train_button_clicked():
  dialog = QDialog()
  layout = QVBoxLayout()
  dialog.setWindowTitle(TRAIN_STRING)

  def set_processed_midi():
    processed_midi_file.setText(str(QFileDialog.getOpenFileName (None, 'Select processed midi file')))

  def set_weights_folder():
    weights_folder.setText(str(QFileDialog.getExistingDirectory(None, "Select Directory")))

  processed_midi_label = QLabel('Select a processed midi file')
  processed_midi_layout = QHBoxLayout()
  processed_midi_file = QTextEdit()
  processed_midi_button = QPushButton("Browser...")
  processed_midi_layout.addWidget(processed_midi_file)
  processed_midi_layout.addWidget(processed_midi_button)
  processed_midi_button.clicked.connect(set_processed_midi)
  layout.addWidget(processed_midi_label)
  layout.addLayout(processed_midi_layout)

  weights_label = QLabel('Select a folder to save the generated melodies')
  weights_layout = QHBoxLayout()
  weights_folder = QTextEdit()
  weights_button = QPushButton("Browser...")
  weights_layout.addWidget(weights_folder )
  weights_layout.addWidget(weights_button)
  weights_button.clicked.connect(set_weights_folder)
  layout.addWidget(weights_label)
  layout.addLayout(weights_layout)
  
  label = QLabel('You clicked the train button!')
  layout.addWidget(label)

  dialog.setLayout(layout)
  dialog.exec()

def on_generate_button_clicked():
  dialog = QDialog()
  layout = QVBoxLayout()
  dialog.setWindowTitle(GENERATE_STRING)

  label = QLabel('You clicked the generate button!')
  layout.addWidget(label)

  dialog.setLayout(layout)
  dialog.exec()

app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.blue)
app.setPalette(palette)

window = QWidget()
window.setWindowTitle("Phrygian")
layout = QVBoxLayout()

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
