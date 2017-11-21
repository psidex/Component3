# System imports
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontMetrics, QFont
from maingui import Ui_MainWindow
from pathlib import Path
import webbrowser
import sys

# Custom imports
from lib.syntax.highlighter import python_syntax_highlighter
from lib.py_and_hex import decompiler, compiler
from lib.tabs import tab_handler
from lib.utils import popup

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.setup_editor()

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
                popup("Error", "Cannot load {}".format(p.name), "It is not a MicroPython file, baka")
                return
        else:
            with open(name, "r") as f:
                file_text = f.read()

        self.tab_handler.load_file(p.name, file_text)

    def open_help(self):
        webbrowser.open("https://microbit-micropython.readthedocs.io/en/latest/")

    def setup_editor(self):
        font = QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.main_editor.setFont(font)
        fontWidth = QFontMetrics(self.main_editor.currentCharFormat().font()).averageCharWidth()
        self.main_editor.setTabStopWidth(4 * fontWidth)
        self.highlighter = python_syntax_highlighter(self.main_editor.document())

        self.tab_handler = tab_handler(self.editor_tabs, self.main_editor)
        self.editor_tabs.tabCloseRequested.connect(self.tab_handler.tab_closed)
        self.editor_tabs.tabBarClicked.connect(self.tab_handler.change_tab)
        self.editor_tabs.addTab(QtWidgets.QWidget(), "new.py")

        self.load_py_btn.clicked.connect(lambda: self.load_file("*.py *.pyw"))
        self.load_hex_btn.clicked.connect(lambda: self.load_file("*.hex"))
        self.help_btn.clicked.connect(self.open_help)
        self.new_file_btn.clicked.connect(lambda: self.tab_handler.load_file("new.py", ""))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())
