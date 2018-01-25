# System / 3rd party lib imports
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFontMetrics, QFont
from pathlib import Path
import webbrowser
import sys

# Custom / Local imports
from lib import fs
from lib.qt import qt_utils
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
		self.highlighter = python_syntax_highlighter(self.main_editor.document())
		self.tab_handler = tab_handler(self.editor_tabs, self.main_editor)

		# Connect buttons to actions
		self.new_file_btn.clicked.connect(self.tab_handler.new_tab)
		self.load_py_btn.clicked.connect(lambda: self.open_new_file("*.py *.pyw"))
		self.load_hex_btn.clicked.connect(lambda: self.open_new_file("*.hex"))
		self.save_py_btn.clicked.connect(lambda: self.save_to_file("py"))
		self.save_hex_btn.clicked.connect(self.save_to_file)
		self.help_btn.clicked.connect(self.open_help)
	
	def open_new_file(self, f_type):
		filename = fs.open_file_dialouge(f_type)
		if not filename:
			return  # Do nothing
		if "py" in f_type:
			file_text = fs.open_from_py(filename)
		elif "hex" in f_type:
			file_text = fs.open_from_hex(filename)
		else:
			return
		self.tab_handler.new_tab(Path(filename).name, file_text)
	
	def save_to_file(self, f_type):
		filename, filetext = self.tab_handler.get_current_tab()
		filename, path = fs.save_file_dialouge(filename)
		if f_type == "py":
			fs.save_to_py(filename, filetext)
		else:
			fs.save_to_hex(filename, filetext)
	
	def open_help(self):
		webbrowser.open("https://microbit-micropython.readthedocs.io/en/latest/")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	prog = IDE_main_app(dialog)
	dialog.show()
	sys.exit(app.exec_())  # Quit process when GUI closed
