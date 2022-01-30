from PyQt5.QtWidgets import (
  QPushButton, QDialog, QLabel,
  QFileDialog, QLineEdit, QDialogButtonBox,
  QFormLayout, QVBoxLayout, QWidget
)
from common_gui import accept_and_finish
from process_midis import process

class ProcessWindow(QDialog):
  def __init__(self, parent):
    super().__init__(parent)
    self.setWindowTitle("Process MIDIs")
    self.layout = QVBoxLayout()
    self.setup_form()
    self.setup_end_buttons()
    self.setLayout(self.layout)
    self.exec()

  def setup_form(self):
    form = QWidget(self)
    form_layout = QFormLayout()
    label_midi_folder = QLabel('Select a midi folder')
    label_midi_folder.setObjectName('QLabelRow')
    self.midi_folder_input = QLineEdit()
    self.midi_folder_input.setObjectName('QLineEdit')
    self.midi_folder_input.setReadOnly(True)
    form_layout.addRow(label_midi_folder, self.midi_folder_input)

    browser_button_midi = QPushButton('Browser...')
    browser_button_midi.setObjectName('BrowserButton')
    browser_button_midi.pressed.connect(self.set_midi_folder)
    form_layout.addWidget(browser_button_midi)

    label_output_midi = QLabel('File to save the generated melodies')
    label_output_midi.setObjectName('QLabelRow')
    self.output_file_input = QLineEdit()
    self.output_file_input.setObjectName('QLineEdit')
    self.output_file_input.setReadOnly(True)
    form_layout.addRow(label_output_midi, self.output_file_input)

    browser_button_output = QPushButton('Browser...')
    browser_button_output.setObjectName('BrowserButton')
    browser_button_output.pressed.connect(self.set_output_file)
    form_layout.addWidget(browser_button_output)

    form.setLayout(form_layout)
    self.layout.addWidget(form)

  def setup_end_buttons(self):
    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.end_dialog)
    buttonBox.rejected.connect(self.reject)
    self.layout.addWidget(buttonBox)

  def end_dialog(self):
    accept_and_finish([
      self.midi_folder_input.text(),
      self.output_file_input.text()
    ], process, self)

  def set_midi_folder(self):
    directory_list = QFileDialog.getExistingDirectory(None, "Select MIDI input Directory")
    if directory_list:
      self.midi_folder_input.setText(directory_list)

  def set_output_file(self):
    self.output_file_input.setText(QFileDialog.getSaveFileName(None, 'Create a processed midi file (melodies)', '', '')[0])