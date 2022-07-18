# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnVerifyCPF = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerifyCPF.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnVerifyCPF.setFont(font)
        self.btnVerifyCPF.setObjectName("btnVerifyCPF")
        self.gridLayout.addWidget(self.btnVerifyCPF, 0, 1, 1, 1)
        self.btnGenerateCPF = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerateCPF.setFont(font)
        self.btnGenerateCPF.setObjectName("btnGenerateCPF")
        self.gridLayout.addWidget(self.btnGenerateCPF, 1, 1, 1, 1)
        self.inputVerifyCPF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inputVerifyCPF.setFont(font)
        self.inputVerifyCPF.setObjectName("inputVerifyCPF")
        self.gridLayout.addWidget(self.inputVerifyCPF, 0, 0, 1, 1)
        self.labelReturn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelReturn.setFont(font)
        self.labelReturn.setStyleSheet("")
        self.labelReturn.setText("")
        self.labelReturn.setAlignment(QtCore.Qt.AlignCenter)
        self.labelReturn.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.labelReturn.setObjectName("labelReturn")
        self.gridLayout.addWidget(self.labelReturn, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validador/Gerador de CPF"))
        self.btnVerifyCPF.setText(_translate("MainWindow", "VALIDAR CPF"))
        self.btnGenerateCPF.setText(_translate("MainWindow", "GERAR CPF"))