import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, QLabel,
    QHBoxLayout, QPushButton
    )



class MyView(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Counter")

        row = QHBoxLayout(self)
        row.addWidget(QLabel(self,text="Count: "))
        
        self.countLabel = QLabel(self)
        row.addWidget(self.countLabel)

        self.resetCount()

        incrementButton = QPushButton(self)
        incrementButton.setText("Increment")
        incrementButton.clicked.connect(self.incrementCount)


    def resetCount(self):
        self.count = 0
        self.countLabel.setText(f"{self.count}")

    def incrementCount(self):
        self.count += 1
        self.countLabel.setText(f"{self.count}")


app = QApplication([])

v = MyView()
v.show()

sys.exit(app.exec())
