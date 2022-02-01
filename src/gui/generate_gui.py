from PyQt5.QtWidgets import (
  QWidget, QPushButton, QVBoxLayout, 
  QHBoxLayout, QDialog, QLabel,
  QFileDialog, QComboBox, QFormLayout, QLineEdit, 
  QSpinBox, QDialogButtonBox 
)
from logic.common import instruments, scales
from logic.generate_music import generate
from .common_gui import accept_and_finish

symbol_to_accidental = {
  ' ' : '',
  '♯': '#',
  '♭': '-'
}

class NoteInput(QHBoxLayout):
  def __init__(self):
    super().__init__()
    self.pitch = QComboBox()
    self.pitch.addItems([chr(i) for i in range(ord('A'), ord('G') + 1)])
    self.addWidget(self.pitch)

    self.symbol = QComboBox()
    self.symbol.addItems(symbol_to_accidental.keys())
    self.addWidget(self.symbol)

    self.scale = QSpinBox()
    self.scale.setRange(1, 8)
    self.scale.setValue(3)
    self.addWidget(self.scale)

  def get_note(self):
    return str(self.pitch.currentText()) + \
      str(symbol_to_accidental[self.symbol.currentText()]) + \
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
    browser_button_midi.setObjectName('BrowserButton')
    browser_button_midi.pressed.connect(lambda: self.processed_midi_input.setText(
      QFileDialog.getOpenFileName(None, 'Select processed midi file (melodies)')[0]
    ))
    form_layout.addWidget(browser_button_midi)

    label_weights = QLabel('Select the weights to use')
    self.weights_input = QLineEdit()
    self.weights_input.setReadOnly(True)
    form_layout.addRow(label_weights, self.weights_input)
    browser_button_weights = QPushButton('Browser...')
    browser_button_weights.setObjectName('BrowserButton')
    browser_button_weights.pressed.connect(lambda: self.weights_input.setText(
      QFileDialog.getOpenFileName(None, "Select neural networks weights")[0]
    ))
    form_layout.addWidget(browser_button_weights)

    label_output_midi = QLabel('Write output midi file')
    self.output_file_input = QLineEdit()
    self.output_file_input.setReadOnly(True)
    form_layout.addRow(label_output_midi, self.output_file_input)
    browser_button_output = QPushButton('Browser...')
    browser_button_output.setObjectName('BrowserButton')
    browser_button_output.pressed.connect(lambda: self.output_file_input.setText(
      QFileDialog.getSaveFileName(None, 'Save output midi File', '', '*.mid;;*.MID')[0]
    ))
    form_layout.addWidget(browser_button_output)

    label_note = QLabel('Select the initial note')
    self.note_input = NoteInput()
    form_layout.addRow(label_note, self.note_input)

    label_instruments = QLabel('Select the instrument')
    self.instrument_input = QComboBox()
    self.instrument_input.addItems(instruments.keys())
    self.instrument_input.setCurrentIndex(list(instruments.keys()).index('Piano'))
    form_layout.addRow(label_instruments, self.instrument_input)

    label_scale = QLabel('Select the scale')
    self.scale_input = QComboBox()
    self.scale_input.addItems(scales.keys())
    self.scale_input.setCurrentIndex(list(scales.keys()).index('Phrygian'))
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

  def end_dialog(self):
    accept_and_finish([
      self.processed_midi_input.text(),
      self.weights_input.text(),
      self.output_file_input.text(),
      self.note_input.get_note(),
      self.instrument_input.currentText(),
      self.scale_input.currentText(),
      self.number_of_notes_input.value()
    ], generate, self)

