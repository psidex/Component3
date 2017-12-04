# System / 3rd party lib imports
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontMetrics, QFont
import sys

# Custom / Local imports
from lib.qt import utils
from lib.qt.tab_handler import tab_handler
from lib.qt.py_syntax_highlighter import python_syntax_highlighter
sys.path.append("res/qt")  # Add res/qt to module path
from app_ui import Ui_MainWindow

class IDE_main_app(Ui_MainWindow):
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)
		self.setup_editor()
	
	def setup_editor(self):
		# Setup nice font (move to .ui file)
		font = QFont()
		font.setFamily("Courier")
		font.setFixedPitch(True)
		font.setPointSize(10)
		self.main_editor.setFont(font)

		# Setup font width and setup width of tab character
		fontWidth = QFontMetrics(font).averageCharWidth()
		self.main_editor.setTabStopWidth(4 * fontWidth)

		self.highlighter = python_syntax_highlighter(self.main_editor.document())

		self.tab_handler = tab_handler(self.editor_tabs, self.main_editor)

		# Connect buttons to actions
		self.new_file_btn.clicked.connect(self.tab_handler.new_tab)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())  # Quit process when GUI closed
