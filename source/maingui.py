# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.load_py_btn = QtWidgets.QToolButton(self.centralwidget)
        self.load_py_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.load_py_btn.setObjectName("load_py_btn")
        self.gridLayout.addWidget(self.load_py_btn, 0, 0, 1, 1)
        self.save_py_btn = QtWidgets.QToolButton(self.centralwidget)
        self.save_py_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.save_py_btn.setObjectName("save_py_btn")
        self.gridLayout.addWidget(self.save_py_btn, 0, 4, 1, 1)
        self.save_hex_btn = QtWidgets.QToolButton(self.centralwidget)
        self.save_hex_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.save_hex_btn.setObjectName("save_hex_btn")
        self.gridLayout.addWidget(self.save_hex_btn, 0, 5, 1, 1)
        self.load_hex_btn = QtWidgets.QToolButton(self.centralwidget)
        self.load_hex_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.load_hex_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.load_hex_btn.setObjectName("load_hex_btn")
        self.gridLayout.addWidget(self.load_hex_btn, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.main_editor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.main_editor.setMinimumSize(QtCore.QSize(0, 0))
        self.main_editor.setTabStopWidth(40)
        self.main_editor.setObjectName("main_editor")
        self.verticalLayout.addWidget(self.main_editor)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCompile_To_hex = QtWidgets.QAction(MainWindow)
        self.actionCompile_To_hex.setObjectName("actionCompile_To_hex")
        self.actionReadme = QtWidgets.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro:bit Python3 IDE"))
        self.load_py_btn.setText(_translate("MainWindow", "Load from .py"))
        self.save_py_btn.setText(_translate("MainWindow", "Save to .py"))
        self.save_hex_btn.setText(_translate("MainWindow", "Save to .hex"))
        self.load_hex_btn.setText(_translate("MainWindow", "Load from .hex"))
        self.action.setText(_translate("MainWindow", "Load (.py or .hex)"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionCompile_To_hex.setText(_translate("MainWindow", "Compile To .hex"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))

