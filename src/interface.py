
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QLabel, QFileDialog, QTextEdit
from PyQt5 import QtCore

from process_midis import process
from train_network import train
from generate_music import generate

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
    output_file.setText(QFileDialog.getOpenFileName(None, 'Single File', '', '*.mid;;*.MID'))

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

  file_name, _ = QFileDialog.getOpenFileName(None, 'Single File', '', '*.mid;;*.MID')
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
