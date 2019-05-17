"""



"""


import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog

class Notepad(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.writing_area = QTextEdit()

        self.delete = QPushButton("Clear")
        self.open = QPushButton("Open File")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()

        h_box.addWidget(self.delete)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()

        v_box.addWidget(self.writing_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad(-)")

        self.delete.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)

        self.show()

    def clear_text(self):

        self.writing_area.clear()

    def open_file(self):

        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))

        with open(file_name[0], "r") as file:

            self.writing_area.setText(file.read())

    def save_file(self):

        file_name = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))

        with open(file_name[0], "w") as file:

            file.write(self.writing_area.toPlainText())
















app = QApplication(sys.argv)
window = Notepad()
sys.exit(app.exec())

