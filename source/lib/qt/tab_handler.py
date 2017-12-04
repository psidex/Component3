"""
class - tab_handler
___________________
A basic handler for PyQt5's QTabWidget to be paired with a QPlainTextEdit

When a tab is clicked on the QTabWidget, the QPlainTextEdit will be
automatically switched to that tabs saved text. There is no maximum number of
tabs, and the widget can never have less than 1 tab

Arg num + name     : Type           : Default  : Description
--------------------------------------------------------------
1 tab_widget       : QTabWidget     : -        : The QTabWidget to use
2 text_edit_widget : QPlainTextEdit : -        : The QPlainTextEdit to use
3 default_name     : String         : "new.py" : The default name for any new tabs

Example usage:
my_tab_handler = tab_handler(my_tab_widget, my_plain_text_edit)


function - tab_handler.new_tab
______________________________
Creates a new tab on the tab widget and moves to that tab

Arg num + name : Type   : Default           : Description
--------------------------------------------------------------
1 editor_text  : String : ""                : The text to be inserted into the text edit
2 tab_name     : String : self.default_name : The name of the new tab

Example usage:
new_file_button.clicked.connect(my_tab_handler.new_tab)
"""

from PyQt5.QtWidgets import QWidget

class tab_handler(object):
    def __init__(self, tab_widget, text_edit_widget, default_name="new.py"):
        self.tab_widget = tab_widget
        self.text_edit_widget = text_edit_widget
        self.tab_texts = []
        self.default_tab_name = default_name
        # Auto bind stuff
        self.tab_widget.tabCloseRequested.connect(self.tab_closed)
        self.tab_widget.tabBarClicked.connect(self.change_tab)
        self.new_tab()

    def tab_closed(self, index):
        if self.tab_widget.count() == 1:
            # Can't close last tab
            return
        elif self.tab_widget.currentIndex() == index:
            # Deleting currently veiwed tab, so move to different tab before deleting
            if index == 0:
                self.change_tab(index+1)
                self.tab_widget.setCurrentIndex(index+1)
            else:
                self.change_tab(index-1)
                self.tab_widget.setCurrentIndex(index-1)

        # Not currently looking at closing tab so just remove it from memory
        del self.tab_texts[index]
        self.tab_widget.removeTab(index)

    def change_tab(self, index):
        # Save the current tabs text to tab_texts then set the text edits text to the new
        # index in tab_texts
        self.tab_texts[self.tab_widget.currentIndex()] = self.text_edit_widget.toPlainText()
        self.text_edit_widget.setPlainText(self.tab_texts[index])

    def new_tab(self, tab_name=None, editor_text=""):
        if not tab_name:
            tab_name = self.default_tab_name
        self.tab_widget.addTab(QWidget(), tab_name)
        self.tab_texts.append(editor_text)
        self.tab_texts[self.tab_widget.currentIndex()] = self.text_edit_widget.toPlainText()  # Save the current tabs text
        self.tab_widget.setCurrentIndex(len(self.tab_texts)-1)  # Switch to last tab in tab list (the new tab)
        self.text_edit_widget.setPlainText(self.tab_texts[-1])  # Switch to last text in tab_texts (the new text)
