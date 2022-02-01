from PyQt5.QtWidgets import (
  QPushButton, QDialog, QLabel,
  QFileDialog, QLineEdit, QDialogButtonBox,
  QFormLayout, QVBoxLayout, QWidget, QSpinBox
)
from .common_gui import accept_and_finish
from logic.train_network import train

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
    form = QWidget(self)
    form_layout = QFormLayout()
    label_processed_midi = QLabel('Select processed midi')
    self.processed_midi_input = QLineEdit()
    self.processed_midi_input.setReadOnly(True)
    form_layout.addRow(label_processed_midi, self.processed_midi_input)

    browser_button_midi = QPushButton('Browser...')
    browser_button_midi.setObjectName('BrowserButton')
    browser_button_midi.pressed.connect(self.set_processed_midi)
    form_layout.addWidget(browser_button_midi)

    label_weights_folder = QLabel('Select neural network weights folder')
    self.weights_folder_input = QLineEdit()
    self.weights_folder_input.setReadOnly(True)
    form_layout.addRow(label_weights_folder, self.weights_folder_input)

    browser_button_wights = QPushButton('Browser...')
    browser_button_wights.setObjectName('BrowserButton')
    browser_button_wights.pressed.connect(self.set_weights_folder)
    form_layout.addWidget(browser_button_wights)

    label_output_midi = QLabel('Number of epochs')
    label_output_midi.setObjectName('QLabelRow')
    self.epochs = QSpinBox()
    self.epochs.setObjectName('QSpinBox')
    self.epochs.setRange(1, 999999)
    self.epochs.setValue(8)
    form_layout.addRow(label_output_midi, self.epochs)

    form.setLayout(form_layout)
    self.layout.addWidget(form)

  def setup_end_buttons(self):
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.end_dialog)
    buttonBox.rejected.connect(self.reject)
    self.layout.addWidget(buttonBox)

  def end_dialog(self):
    accept_and_finish([
      self.processed_midi_input.text(),
      self.weights_folder_input.text(),
      self.epochs.value()
    ], train, self)

  def set_processed_midi(self):
    self.processed_midi_input.setText(
      QFileDialog.getOpenFileName (None, 'Select processed midi file')[0]
    )

  def set_weights_folder(self):
    directory_list = QFileDialog.getExistingDirectory(None, "Select weights Directory")
    print(directory_list)
    if directory_list:
      self.weights_folder_input.setText(directory_list)