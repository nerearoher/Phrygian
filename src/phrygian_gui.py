import pathlib
from os import path
from PyQt5.QtWidgets import (
  QApplication, QWidget, QPushButton,
  QVBoxLayout, QLabel, QLayout, QSpinBox,
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from gui.css import PHRYGIAN_GUI
from gui.generate_gui import GenerationWindow
from gui.train_gui import TrainWindow
from gui.process_gui import ProcessWindow

PROCESS_STRING = 'Process MIDIs'
TRAIN_STRING = 'Train neural network'
GENERATE_STRING = 'Generate music'

app = QApplication([])

path_abs = pathlib.Path(__file__).absolute().parent.parent
path_image = path.join(path_abs, "images", "logo.png")
path_image_sphere = path.join(path_abs, "images", "logo_sphere.png")

window = QWidget()
window.setWindowTitle("Phrygian")
window.setWindowIcon(QIcon(str(path_image_sphere)))
window.setStyleSheet(PHRYGIAN_GUI)
layout = QVBoxLayout()
layout.setSizeConstraint(QLayout.SetFixedSize)

label_welcome = QLabel()
image = QPixmap(path_image)
label_welcome.setPixmap(image)
layout.addWidget(label_welcome, alignment = Qt.AlignCenter)

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
