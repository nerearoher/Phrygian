import pathlib
from os import path
from PyQt5.QtWidgets import (
  QApplication, QWidget, QPushButton,
  QVBoxLayout, QLabel, QLayout, QSpinBox,
)
from PyQt5.QtGui import QPixmap
from css import PHRYGIAN_GUI
from generate_gui import GenerationWindow
from train_gui import TrainWindow
from process_gui import ProcessWindow

PROCESS_STRING = 'Process MIDIs'
TRAIN_STRING = 'Train neural network'
GENERATE_STRING = 'Generate music'

app = QApplication([])

window = QWidget()
window.setWindowTitle("Phrygian")
window.setStyleSheet(PHRYGIAN_GUI)
layout = QVBoxLayout()
layout.setSizeConstraint(QLayout.SetFixedSize)

path_abs = pathlib.Path(__file__).absolute().parent
label_welcome = QLabel()
path_image = path.join(path_abs, "logo.png")
image = QPixmap(path_image)
label_welcome.setPixmap(image)
layout.addWidget(label_welcome)

process_button = QPushButton(PROCESS_STRING)
train_button = QPushButton(TRAIN_STRING)
generate_button = QPushButton(GENERATE_STRING)

layout.addWidget(process_button)
layout.addWidget(train_button)
layout.addWidget(generate_button)

process_button.clicked.connect(lambda: ProcessWindow(window))
train_button.clicked.connect(lambda: TrainWindow(window))
generate_button.clicked.connect(lambda: GenerationWindow(window))

window.setLayout(layout)
window.show()
app.exec()
