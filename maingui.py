# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.editor = QtWidgets.QTextEdit(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.editor.setObjectName("editor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_py_or_hex = QtWidgets.QAction(MainWindow)
        self.actionLoad_py_or_hex.setObjectName("actionLoad_py_or_hex")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCompile_To_hex = QtWidgets.QAction(MainWindow)
        self.actionCompile_To_hex.setObjectName("actionCompile_To_hex")
        self.actionReadme = QtWidgets.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")
        self.menuFile.addAction(self.actionLoad_py_or_hex)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionCompile_To_hex)
        self.menuHelp.addAction(self.actionReadme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro:bit Python3 IDE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_py_or_hex.setText(_translate("MainWindow", "Load (.py or .hex)"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionCompile_To_hex.setText(_translate("MainWindow", "Compile To .hex"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

