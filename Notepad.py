"""



"""


import sys
import os
from PyQt5.QtWidgets import \
    QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog,QAction,qApp,QMainWindow

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





class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.window = Notepad()
        self.setCentralWidget(self.window)

        self.createMenu()

    def createMenu(self):

        menuBar = self.menuBar()

        file = menuBar.addMenu("File")

        openFile = QAction("Open File",self)
        saveFile = QAction("Save File",self)
        clearText = QAction("Clear Text",self)
        exitFile = QAction("Exit", self)

        openFile.setShortcut("Ctrl+O")
        saveFile.setShortcut("Ctrl+S")
        exitFile.setShortcut("Ctrl+Q")

        file.addAction(openFile)
        file.addAction(saveFile)
        file.addAction(clearText)
        file.addAction(exitFile)


        file.triggered.connect(self.response)
        self.setWindowTitle("Notepad(--)")
        self.show()

    def response(self, action):

        if action.text() == "Open File":
            self.window.open_file()

        elif action.text() == "Save File":
            self.window.save_file()

        elif action.text() == "Clear Text":
            self.window.clear_text()

        elif action.text() == "Exit":
            qApp.quit()

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec())
