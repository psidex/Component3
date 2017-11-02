from PyQt5.QtWidgets import QWidget

"""
tab_handler
Controls a Qt tab widget. Does not allow closing of last tab.

Example usage:
my_tab_handler = tab_handler(editor_tab_widget, editor_text_edit)
editor_tab_widget.tabCloseRequested.connect(my_tab_handler.tab_closed)
editor_tab_widget.tabBarClicked.connect(my_tab_handler.change_tab)
editor_tab_widget.addTab(QtWidgets.QWidget(), "new.py")
create_new_file_btn.clicked.connect(lambda: my_tab_handler.load_file("new.py", ""))
"""
class tab_handler(object):
    def __init__(self, tab_widget, text_edit_widget):
        self.tab_widget = tab_widget
        self.text_edit_widget = text_edit_widget
        self.tab_texts = [""]

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
        self.tab_texts[self.tab_widget.currentIndex()] = self.text_edit_widget.toPlainText()
        self.text_edit_widget.setPlainText(self.tab_texts[index])

    def new_tab(self, tab_name, editor_text):
        self.tab_widget.addTab(QWidget(), tab_name)
        self.tab_texts.append(editor_text)
        self.tab_texts[self.tab_widget.currentIndex()] = self.text_edit_widget.toPlainText()
        self.tab_widget.setCurrentIndex(len(self.tab_texts)-1)
        self.text_edit_widget.setPlainText(self.tab_texts[-1])
