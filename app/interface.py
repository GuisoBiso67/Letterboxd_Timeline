import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class TimelineWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.decades = {}
    for decade in range(1870, 2030, 10):
      label = QLabel(f"{decade}s", self)
      self.decades[decade] = label

    self.initUI()

  def initUI(self):
    self.setWindowTitle("Your Letterboxd Timeline")
    self.setWindowIcon(QIcon("media/letterboxd-icon.png"))
    self.setGeometry(300,300,1400,500)
    self.setStyleSheet("background-color: #202830;"
                       "color: #ffffff;"
                       "font-size: 20px;"
                       "font-family: Consolas;")
    
    hbox = QHBoxLayout()
    hbox.setSpacing(30)
    

    for decade in range(1870, 2030, 10):
      container = QWidget()
      vbox = QVBoxLayout()
      dot = QLabel("●")
      line = QLabel("---|---")
      label = self.decades[decade]

      label.setAlignment(Qt.AlignCenter)
      line.setAlignment(Qt.AlignCenter)
      dot.setAlignment(Qt.AlignCenter)

      vbox.addWidget(dot)
      vbox.addWidget(line)
      vbox.addWidget(label)

      container.setLayout(vbox)

      hbox.addWidget(container, 1)

    central = QWidget()
    central.setLayout(hbox)
    self.setCentralWidget(central)

    """ for decade in range(1870, 2030, 10):
      label = self.decades[decade]
      label.setAlignment(Qt.AlignCenter)
      hbox.addWidget(label, 1)

    hbox.setSpacing(30)
    central = QWidget()
    central.setLayout(hbox)
    self.setCentralWidget(central) """


