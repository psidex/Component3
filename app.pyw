from PyQt5 import QtCore, QtGui, QtWidgets
from maingui import Ui_MainWindow
import syntax_pars
import sys

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.setupeditor()
        self.actionLoad_py_or_hex.triggered.connect(self.loadfile)

    def loadfile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open file", "/home")
        if name[0]:
            with open(name[0], "r") as f:
                self.editor.setText(f.read())

    def setupeditor(self):
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.editor.setFont(font)
        self.highlighter = syntax_pars.PythonHighlighter(self.editor.document())

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())

""""
Recourses used

http://zetcode.com/gui/pyqt5
http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/

Syntax highlighter from here: https://github.com/art1415926535/PyQt5-syntax-highlighting
"""
