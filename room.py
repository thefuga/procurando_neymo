# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sala.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, controller):
        self.controller = controller
        self.room_window = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        Dialog.setWindowTitle("Sala")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 381, 29))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 80, 101, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 80, 101, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.button_1)
        self.pushButton_2.clicked.connect(self.button_2)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def button_1(self):
        self.controller.room_rendezvous("host", self.lineEdit.text())

    def button_2(self):
        self.controller.room_rendezvous("player", self.lineEdit.text())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Nome da sala:"))
        self.pushButton.setText(_translate("Dialog", "Criar"))
        self.pushButton_2.setText(_translate("Dialog", "Buscar"))

