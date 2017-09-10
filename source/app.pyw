from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontMetrics
from maingui import Ui_MainWindow
from pathlib import Path
import sys

import syntax
from py_and_hex import decompiler, compiler

class IDE_main_app(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.tab_texts = [""]  # Tabs
        self.setupeditor()

    def loadfile(self, types):
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

        self.editor_tabs.addTab(QtWidgets.QWidget(), p.name)
        self.tab_texts.append(file_text)
        if self.editor_tabs.count() > 1:
            self.editor_tabs.show()
        self.tab_texts[self.editor_tabs.currentIndex()] = self.main_editor.toPlainText()
        self.editor_tabs.setCurrentIndex(len(self.tab_texts)-1)
        self.main_editor.setPlainText(self.tab_texts[-1])

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
        self.main_editor.setStyleSheet("background-color: rgb(38,50,56); color: white;")
        self.highlighter = syntax.PythonSyntaxHighlighter(self.main_editor.document())

        self.load_py_btn.clicked.connect(lambda: self.loadfile("*.py *.pyw"))
        self.load_hex_btn.clicked.connect(lambda: self.loadfile("*.hex"))
        self.main_editor.textChanged.connect(self.update_line_numbers)

        self.editor_tabs.tabCloseRequested.connect(self.tab_closed)
        self.editor_tabs.tabBarClicked.connect(self.change_tab)
        self.editor_tabs.addTab(QtWidgets.QWidget(), "new.py")
        self.editor_tabs.hide()

    def tab_closed(self, index):
        if self.editor_tabs.count() == 1:
            # Shouldn't be able to close the last tab but there is a guard just inscase
            return
        elif self.editor_tabs.currentIndex() != index:
            # Not currently looking at closing tab so just remove it from memory
            del self.tab_texts[index]
            self.editor_tabs.removeTab(index)
        else:
            # Deleting currently veiwed tab, so move to different tab before deleting
            if index == 0:
                self.change_tab(index+1)
                self.editor_tabs.setCurrentIndex(index+1)
            else:
                self.change_tab(index-1)
                self.editor_tabs.setCurrentIndex(index-1)
                
            del self.tab_texts[index]
            self.editor_tabs.removeTab(index)

        if self.editor_tabs.count() <= 1:
            self.editor_tabs.hide()

    def change_tab(self, index):
        self.tab_texts[self.editor_tabs.currentIndex()] = self.main_editor.toPlainText()
        self.main_editor.setPlainText(self.tab_texts[index])

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
http://www.december.com/html/spec/colorsvg.html
"""
