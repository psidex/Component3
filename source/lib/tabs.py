from PyQt5.QtWidgets import QWidget

"""
Handles everything to do with tabs in the main editor
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

    def load_file(self, file_name, file_text):
        self.tab_widget.addTab(QWidget(), file_name)
        self.tab_texts.append(file_text)
        self.tab_texts[self.tab_widget.currentIndex()] = self.text_edit_widget.toPlainText()
        self.tab_widget.setCurrentIndex(len(self.tab_texts)-1)
        self.text_edit_widget.setPlainText(self.tab_texts[-1])
