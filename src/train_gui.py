from PyQt5.QtWidgets import (
  QPushButton, QDialog, QLabel,
  QFileDialog, QLineEdit, QDialogButtonBox,
  QFormLayout
)
from common_gui import accept_and_finish

def train(*args):
  pass
# from train_network import train

class TrainWindow(QDialog):
  def __init__(self, parent):
    super().__init__(parent)
    self.setWindowTitle("Train neural network")
    self.layout = QFormLayout()
    self.setup_form()
    self.setup_end_buttons()
    self.setLayout(self.layout)
    self.exec()

  def setup_form(self):
    label_processed_midi = QLabel('Select processed midi')
    self.processed_midi_input = QLineEdit()
    self.processed_midi_input.setReadOnly(True)
    self.layout.addRow(label_processed_midi, self.processed_midi_input)

    browser_button_midi = QPushButton('Browser...')
    browser_button_midi.pressed.connect(self.set_processed_midi)
    self.layout.addWidget(browser_button_midi)

    label_weights_folder = QLabel('Select neural network weights folder')
    self.weight_folder_input = QLineEdit()
    self.weight_folder_input.setReadOnly(True)
    self.layout.addRow(label_weights_folder, self.weight_folder_input)

    browser_button_wights = QPushButton('Browser...')
    browser_button_wights.pressed.connect(self.set_weights_folder)
    self.layout.addWidget(browser_button_wights)

  def setup_end_buttons(self):
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.end_dialog)
    buttonBox.rejected.connect(self.reject)
    self.layout.addWidget(buttonBox)

  def end_dialog(self):
    accept_and_finish([
      self.processed_midi_input.text(),
      self.weights_folder_input.text()
    ], train, self)

  def set_processed_midi(self):
    self.processed_midi_input.setText(
      QFileDialog.getOpenFileName (None, 'Select processed midi file')[0]
    )

  def set_weights_folder(self):
    directory_list = QFileDialog.getExistingDirectory(None, "Select weights Directory")
    if directory_list:
      self.weights_folder_input.setText(directory_list[0])