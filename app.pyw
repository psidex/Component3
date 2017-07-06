from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics
from maingui import Ui_MainWindow
import syntax
import sys

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.setupeditor()
        self.actionLoad_py_or_hex.triggered.connect(self.loadfile)

    def loadfile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open file", "/home", "*.py *.pyw *.hex")
        if name[0]:
            with open(name[0], "r") as f:
                self.editor.setPlainText(f.read())

    def setupeditor(self):
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.editor.setFont(font)
        fontWidth = QFontMetrics(self.editor.currentCharFormat().font()).averageCharWidth()
        self.editor.setTabStopWidth(4 * fontWidth)
        self.editor.setStyleSheet("background-color: rgb(38,50,56); color: white;")
        self.highlighter = syntax.PythonSyntaxHighlighter(self.editor.document())

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())

"""
Resources used:

Qt5 Stuff:
https://stackoverflow.com/
http://zetcode.com/gui/pyqt5
http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
http://pyqt.sourceforge.net/Docs/PyQt4/qfiledialog.html

Syntax highlighter help:
https://github.com/art1415926535/PyQt5-syntax-highlighting
http://carsonfarmer.com/2009/07/syntax-highlighting-with-pyqt/
https://regex101.com/
http://www.rexegg.com/regex-quickstart.html
"""
