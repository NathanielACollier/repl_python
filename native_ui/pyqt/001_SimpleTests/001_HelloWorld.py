import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, QLabel)



class HelloWorldView(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Empty")

        label = QLabel(self)
        label.setText("Hello World!")


app = QApplication([])

v = HelloWorldView()
v.show()

sys.exit(app.exec())
