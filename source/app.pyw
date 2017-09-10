from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics
from maingui import Ui_MainWindow
from pathlib import Path
import sys

from utils.syntax import PythonSyntaxHighlighter
from py_and_hex import decompiler, compiler
from utils.tabs import tab_handler

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.setupeditor()

    def load_file(self, types):
        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open file", "/home", types)
        name = name[0]
        if not name:
            return  # Return nothing
        p = Path(name)
        if p.suffix == ".hex":
            d_c = decompiler.decompile(name)
            if d_c != -1:
                file_text = d_c
            else:
                return  # ToDo: Add error popup here
        else:
            with open(name, "r") as f:
                file_text = f.read()

        self.tab_handler.load_file(p.name, file_text)

    def update_line_numbers(self):
        """ WIP """
        line_count = 0
        text = self.main_editor.toPlainText()
        for line in text.split("\n"):
            line_count += 1

    def setupeditor(self):
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.main_editor.setFont(font)
        fontWidth = QFontMetrics(self.main_editor.currentCharFormat().font()).averageCharWidth()
        self.main_editor.setTabStopWidth(4 * fontWidth)
        self.highlighter = PythonSyntaxHighlighter(self.main_editor.document())

        self.tab_handler = tab_handler(self.editor_tabs, self.main_editor)
        self.editor_tabs.tabCloseRequested.connect(self.tab_handler.tab_closed)
        self.editor_tabs.tabBarClicked.connect(self.tab_handler.change_tab)
        self.editor_tabs.addTab(QtWidgets.QWidget(), "new.py")

        self.load_py_btn.clicked.connect(lambda: self.load_file("*.py *.pyw"))
        self.load_hex_btn.clicked.connect(lambda: self.load_file("*.hex"))
        self.new_file_btn.clicked.connect(lambda: self.tab_handler.load_file("new.py", ""))
        self.main_editor.textChanged.connect(self.update_line_numbers)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())
