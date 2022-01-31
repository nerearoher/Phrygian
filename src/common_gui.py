from PyQt5.QtWidgets import QMessageBox

def accept_and_finish(args, function, parent):
  question = QMessageBox(parent)
  question.setText("The process is about to take place. Are you ready?")
  question.setIcon(QMessageBox.Question)
  question.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
  question.setDefaultButton(QMessageBox.Yes)
  if question.exec() == QMessageBox.Yes:
    function(*args)

    done = QMessageBox(parent)
    done.setText("Done!")
    done.setIcon(QMessageBox.Information)
    done.setStandardButtons(QMessageBox.Ok)
    done.exec()
