from PyQt5.QtWidgets import (
  QApplication, QWidget, 
  QPushButton, QVBoxLayout, 
  QHBoxLayout, QDialog, 
  QLabel, QFileDialog, 
  QTextEdit, QComboBox, 
  QFormLayout, QLineEdit, 
  QGridLayout, QLineEdit,
  QLayout, QSpinBox,
  QDialogButtonBox, QMessageBox
)
from PyQt5.QtCore import Qt
from css import PHRYGIAN_GUI
from generate_gui import GenerationWindow

# from process_midis import process
# from train_network import train
# from generate_music import generate

# TODO: Eliminar esto cuando acabe el desarrollo de la gui
def process(*args):
  pass
def train(*args):
  pass

PROCESS_STRING = 'Process MIDIs melodies'
TRAIN_STRING = 'Train neuronal network'
GENERATE_STRING = 'Generate music'


def accept_and_finish(args, function, dialog):
  question = QMessageBox()
  question.setText("The process is about to take place. Are you ready?")
  question.setIcon(QMessageBox.Question)
  question.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
  question.setDefaultButton(QMessageBox.Yes)
  question.exec()

  function(*args)

  done = QMessageBox()
  done.setText("Done!")
  done.setIcon(QMessageBox.Information)
  done.setStandardButtons(QMessageBox.Ok)
  done.exec()
  dialog.accept()

def on_process_button_clicked():
  dialog = QDialog()
  dialog.setStyleSheet(PHRYGIAN_GUI)
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(PROCESS_STRING)

  def set_midi_folder():
    directory_list = QFileDialog.getExistingDirectory(None, "Select MIDI input Directory")
    if directory_list:
      line_edit_midi_folder.setText(directory_list)

  def set_output_file():
    line_edit_output_file.setText(QFileDialog.getSaveFileName(None, 'Create a processed midi file (melodies)', '', '')[0])

  label_midi_folder = QLabel('Select a midi folder')
  label_midi_folder.setObjectName('QLabelRow')
  line_edit_midi_folder = QLineEdit()
  line_edit_midi_folder.setObjectName('QLineEdit')
  line_edit_midi_folder.setReadOnly(True)
  browser_button_midi = QPushButton('Browser...')
  browser_button_midi.setStyleSheet(PHRYGIAN_GUI)
  browser_button_midi.pressed.connect(set_midi_folder)
  layout.addRow(label_midi_folder, line_edit_midi_folder)
  layout.addWidget(browser_button_midi)

  label_output_midi = QLabel('File to save the generated melodies')
  label_output_midi.setObjectName('QLabelRow')
  line_edit_output_file = QLineEdit()
  line_edit_output_file.setObjectName('QLineEdit')
  line_edit_output_file.setReadOnly(True)
  browser_button_output = QPushButton('Browser...')
  browser_button_output.setStyleSheet(PHRYGIAN_GUI)
  browser_button_output.pressed.connect(set_output_file)
  layout.addRow(label_output_midi, line_edit_output_file)
  layout.addWidget(browser_button_output)

  qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
  buttonBox = QDialogButtonBox(qbtn)
  buttonBox.accepted.connect(lambda: accept_and_finish([
    line_edit_midi_folder.text(),
    line_edit_output_file.text()
  ], process, dialog))
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
  layout.addRow(label_processed_midi, line_edit_processed_midi)
  layout.addWidget(browser_button_midi)

  line_edit_weights_folder = QLineEdit()
  line_edit_weights_folder.setReadOnly(True)
  browser_button_wights.pressed.connect(set_weights_folder)
  layout.addRow(label_wights_folder, line_edit_weights_folder)
  layout.addWidget(browser_button_wights)

  qbtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
  buttonBox = QDialogButtonBox(qbtn)
  buttonBox.accepted.connect(lambda: accept_and_finish([
    line_edit_processed_midi.text(),
    line_edit_weights_folder.text()
  ], train, dialog))
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
generate_button.clicked.connect(lambda: GenerationWindow(window))

window.setLayout(layout)
window.show()
app.exec()
