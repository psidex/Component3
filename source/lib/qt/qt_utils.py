from PyQt5.QtWidgets import QMessageBox

"""
Creates a Qt popup window with these properties:
window_title
title
message
icon=QMessageBox.Information
action=None - Should be a function if passed
exit=False - Program will exit when message is closed
"""
def popup(window_title, title, message, icon=QMessageBox.Information, action=None, exit=False):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setWindowTitle(window_title)
    msg.setText(title)
    msg.setInformativeText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    if action:
        msg.buttonClicked.connect(action)
    if exit:
        # For fatal errors
        sys.exit(msg.exec_())
    else:
        msg.exec_()
