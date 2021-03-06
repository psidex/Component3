# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 593)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.load_py_btn = QtWidgets.QToolButton(self.centralwidget)
        self.load_py_btn.setMinimumSize(QtCore.QSize(80, 45))
        self.load_py_btn.setStyleSheet("")
        self.load_py_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_py_btn.setIcon(icon1)
        self.load_py_btn.setObjectName("load_py_btn")
        self.gridLayout.addWidget(self.load_py_btn, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 8, 1, 1)
        self.load_hex_btn = QtWidgets.QToolButton(self.centralwidget)
        self.load_hex_btn.setMinimumSize(QtCore.QSize(80, 45))
        self.load_hex_btn.setText("")
        self.load_hex_btn.setIcon(icon1)
        self.load_hex_btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.load_hex_btn.setObjectName("load_hex_btn")
        self.gridLayout.addWidget(self.load_hex_btn, 2, 2, 1, 1)
        self.load_py_label = QtWidgets.QLabel(self.centralwidget)
        self.load_py_label.setAlignment(QtCore.Qt.AlignCenter)
        self.load_py_label.setObjectName("load_py_label")
        self.gridLayout.addWidget(self.load_py_label, 0, 1, 1, 1)
        self.save_py_btn = QtWidgets.QToolButton(self.centralwidget)
        self.save_py_btn.setMinimumSize(QtCore.QSize(80, 45))
        self.save_py_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_py_btn.setIcon(icon2)
        self.save_py_btn.setObjectName("save_py_btn")
        self.gridLayout.addWidget(self.save_py_btn, 2, 5, 1, 1)
        self.load_hex_label = QtWidgets.QLabel(self.centralwidget)
        self.load_hex_label.setAlignment(QtCore.Qt.AlignCenter)
        self.load_hex_label.setObjectName("load_hex_label")
        self.gridLayout.addWidget(self.load_hex_label, 0, 2, 1, 1)
        self.save_hex_btn = QtWidgets.QToolButton(self.centralwidget)
        self.save_hex_btn.setMinimumSize(QtCore.QSize(80, 45))
        self.save_hex_btn.setText("")
        self.save_hex_btn.setIcon(icon2)
        self.save_hex_btn.setObjectName("save_hex_btn")
        self.gridLayout.addWidget(self.save_hex_btn, 2, 6, 1, 1)
        self.new_file_btn = QtWidgets.QToolButton(self.centralwidget)
        self.new_file_btn.setMinimumSize(QtCore.QSize(80, 45))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/icons/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_file_btn.setIcon(icon3)
        self.new_file_btn.setObjectName("new_file_btn")
        self.gridLayout.addWidget(self.new_file_btn, 2, 0, 1, 1)
        self.save_hex_label = QtWidgets.QLabel(self.centralwidget)
        self.save_hex_label.setAlignment(QtCore.Qt.AlignCenter)
        self.save_hex_label.setObjectName("save_hex_label")
        self.gridLayout.addWidget(self.save_hex_label, 0, 6, 1, 1)
        self.save_py_label = QtWidgets.QLabel(self.centralwidget)
        self.save_py_label.setAlignment(QtCore.Qt.AlignCenter)
        self.save_py_label.setObjectName("save_py_label")
        self.gridLayout.addWidget(self.save_py_label, 0, 5, 1, 1)
        self.new_file_label = QtWidgets.QLabel(self.centralwidget)
        self.new_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_file_label.setObjectName("new_file_label")
        self.gridLayout.addWidget(self.new_file_label, 0, 0, 1, 1)
        self.help_label = QtWidgets.QLabel(self.centralwidget)
        self.help_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_label.setObjectName("help_label")
        self.gridLayout.addWidget(self.help_label, 0, 7, 1, 1)
        self.help_btn = QtWidgets.QToolButton(self.centralwidget)
        self.help_btn.setMinimumSize(QtCore.QSize(80, 45))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_btn.setIcon(icon4)
        self.help_btn.setObjectName("help_btn")
        self.gridLayout.addWidget(self.help_btn, 2, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.editor_tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.editor_tabs.setMaximumSize(QtCore.QSize(16777215, 21))
        self.editor_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.editor_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.editor_tabs.setElideMode(QtCore.Qt.ElideRight)
        self.editor_tabs.setTabsClosable(True)
        self.editor_tabs.setMovable(False)
        self.editor_tabs.setTabBarAutoHide(False)
        self.editor_tabs.setObjectName("editor_tabs")
        self.verticalLayout.addWidget(self.editor_tabs)
        self.main_editor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.main_editor.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.main_editor.setFont(font)
        self.main_editor.setStyleSheet("background-color: rgb(38,50,56); color: white;")
        self.main_editor.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.main_editor.setTabStopWidth(32)
        self.main_editor.setObjectName("main_editor")
        self.verticalLayout.addWidget(self.main_editor)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.editor_tabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro:bit Python3 IDE"))
        self.load_py_label.setText(_translate("MainWindow", "Load from .py"))
        self.load_hex_label.setText(_translate("MainWindow", "Load from .hex"))
        self.new_file_btn.setText(_translate("MainWindow", "..."))
        self.save_hex_label.setText(_translate("MainWindow", "Save to .hex"))
        self.save_py_label.setText(_translate("MainWindow", "Save to .py"))
        self.new_file_label.setText(_translate("MainWindow", "New file"))
        self.help_label.setText(_translate("MainWindow", "Help"))
        self.help_btn.setText(_translate("MainWindow", "..."))
        self.action.setText(_translate("MainWindow", "Load (.py or .hex)"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionCompile_To_hex.setText(_translate("MainWindow", "Compile To .hex"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))

import app_ui_res_rc
