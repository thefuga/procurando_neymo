# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import room
import sys
import deck
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller):
        self.main_window = MainWindow
        self.controller = controller
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 881, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 320, 881, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_2.addWidget(self.pushButton_12)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 540, 881, 211))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_3.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_3.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 40, 141, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(self.controller.myScore)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(750, 40, 141, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.display(self.controller.opScore)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 10, 141, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_1.setIconSize(QtCore.QSize(129,199))
        self.pushButton_1.clicked.connect(self.on_click_1)
        self.pushButton_2.setIconSize(QtCore.QSize(129,199))
        self.pushButton_2.clicked.connect(self.on_click_2)
        self.pushButton_3.setIconSize(QtCore.QSize(129,199))
        self.pushButton_3.clicked.connect(self.on_click_3)
        self.pushButton_4.setIconSize(QtCore.QSize(129,199))
        self.pushButton_4.clicked.connect(self.on_click_4)
        self.pushButton_5.setIconSize(QtCore.QSize(129,199))
        self.pushButton_5.clicked.connect(self.on_click_5)
        self.pushButton_6.setIconSize(QtCore.QSize(129,199))
        self.pushButton_6.clicked.connect(self.on_click_6)
        self.pushButton_7.setIconSize(QtCore.QSize(129,199))
        self.pushButton_7.clicked.connect(self.on_click_7)
        self.pushButton_8.setIconSize(QtCore.QSize(129,199))
        self.pushButton_8.clicked.connect(self.on_click_8)
        self.pushButton_9.setIconSize(QtCore.QSize(129,199))
        self.pushButton_9.clicked.connect(self.on_click_9)
        self.pushButton_10.setIconSize(QtCore.QSize(129,199))
        self.pushButton_10.clicked.connect(self.on_click_10)
        self.pushButton_11.setIconSize(QtCore.QSize(129,199))
        self.pushButton_11.clicked.connect(self.on_click_11)
        self.pushButton_12.setIconSize(QtCore.QSize(129,199))
        self.pushButton_12.clicked.connect(self.on_click_12)
        self.pushButton_13.setIconSize(QtCore.QSize(129,199))
        self.pushButton_13.clicked.connect(self.on_click_13)
        self.pushButton_14.setIconSize(QtCore.QSize(129,199))
        self.pushButton_14.clicked.connect(self.on_click_14)
        self.pushButton_15.setIconSize(QtCore.QSize(129,199))
        self.pushButton_15.clicked.connect(self.on_click_15)
        self.pushButton_16.setIconSize(QtCore.QSize(129,199))
        self.pushButton_16.clicked.connect(self.on_click_16)
        self.pushButton_17.setIconSize(QtCore.QSize(129,199))
        self.pushButton_17.clicked.connect(self.on_click_17)
        self.pushButton_18.setIconSize(QtCore.QSize(129,199))
        self.pushButton_18.clicked.connect(self.on_click_18)

        self.pushButton_1.pressed.connect(self.on_press_1)
        self.pushButton_2.pressed.connect(self.on_press_2)
        self.pushButton_3.pressed.connect(self.on_press_3)
        self.pushButton_4.pressed.connect(self.on_press_4)
        self.pushButton_5.pressed.connect(self.on_press_5)
        self.pushButton_6.pressed.connect(self.on_press_6)
        self.pushButton_7.pressed.connect(self.on_press_7)
        self.pushButton_8.pressed.connect(self.on_press_8)
        self.pushButton_9.pressed.connect(self.on_press_9)
        self.pushButton_10.pressed.connect(self.on_press_10)
        self.pushButton_11.pressed.connect(self.on_press_11)
        self.pushButton_12.pressed.connect(self.on_press_12)
        self.pushButton_13.pressed.connect(self.on_press_13)
        self.pushButton_14.pressed.connect(self.on_press_14)
        self.pushButton_15.pressed.connect(self.on_press_15)
        self.pushButton_16.pressed.connect(self.on_press_16)
        self.pushButton_17.pressed.connect(self.on_press_17)
        self.pushButton_18.pressed.connect(self.on_press_18)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procurando Neymo"))
        self.pushButton_1.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", ""))
        self.pushButton_7.setText(_translate("MainWindow", ""))
        self.pushButton_8.setText(_translate("MainWindow", ""))
        self.pushButton_9.setText(_translate("MainWindow", ""))
        self.pushButton_10.setText(_translate("MainWindow", ""))
        self.pushButton_11.setText(_translate("MainWindow", ""))
        self.pushButton_12.setText(_translate("MainWindow", ""))
        self.pushButton_13.setText(_translate("MainWindow", ""))
        self.pushButton_14.setText(_translate("MainWindow", ""))
        self.pushButton_15.setText(_translate("MainWindow", ""))
        self.pushButton_16.setText(_translate("MainWindow", ""))
        self.pushButton_17.setText(_translate("MainWindow", ""))
        self.pushButton_18.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Você:"))
        self.label_2.setText(_translate("MainWindow", "Adversário:"))

    def on_click_1(self):
        self.controller.click_action(0)
    
    def on_click_2(self):
        self.controller.click_action(1)

    def on_click_3(self):
        self.controller.click_action(2)

    def on_click_4(self):
        self.controller.click_action(3)

    def on_click_5(self):
        self.controller.click_action(4)

    def on_click_6(self):
        self.controller.click_action(5)

    def on_click_7(self):
        self.controller.click_action(6)

    def on_click_8(self):
        self.controller.click_action(7)

    def on_click_9(self):
        self.controller.click_action(8)

    def on_click_10(self):
        self.controller.click_action(9)

    def on_click_11(self):
        self.controller.click_action(10)

    def on_click_12(self):
        self.controller.click_action(11)

    def on_click_13(self):
        self.controller.click_action(12)

    def on_click_14(self):
        self.controller.click_action(13)

    def on_click_15(self):
        self.controller.click_action(14)

    def on_click_16(self):
        self.controller.click_action(15)

    def on_click_17(self):
        self.controller.click_action(16)

    def on_click_18(self):
        self.controller.click_action(17)

    def on_press_1(self):
        self.pushButton_1.setIcon(QtGui.QIcon(self.controller.deck.cards[0].image_path))

    def on_press_2(self):
        self.pushButton_2.setIcon(QtGui.QIcon(self.controller.deck.cards[1].image_path))
   
    def on_press_3(self):
        self.pushButton_3.setIcon(QtGui.QIcon(self.controller.deck.cards[2].image_path))

    def on_press_4(self):
        self.pushButton_4.setIcon(QtGui.QIcon(self.controller.deck.cards[3].image_path))

    def on_press_5(self):
        self.pushButton_5.setIcon(QtGui.QIcon(self.controller.deck.cards[4].image_path))

    def on_press_6(self):
        self.pushButton_6.setIcon(QtGui.QIcon(self.controller.deck.cards[5].image_path))

    def on_press_7(self):
        self.pushButton_7.setIcon(QtGui.QIcon(self.controller.deck.cards[6].image_path))

    def on_press_8(self):
        self.pushButton_8.setIcon(QtGui.QIcon(self.controller.deck.cards[7].image_path))

    def on_press_9(self):
        self.pushButton_9.setIcon(QtGui.QIcon(self.controller.deck.cards[8].image_path))

    def on_press_10(self):
        self.pushButton_10.setIcon(QtGui.QIcon(self.controller.deck.cards[9].image_path))

    def on_press_11(self):
        self.pushButton_11.setIcon(QtGui.QIcon(self.controller.deck.cards[10].image_path))
 
    def on_press_12(self):
        self.pushButton_12.setIcon(QtGui.QIcon(self.controller.deck.cards[11].image_path))
      
    def on_press_13(self):
        self.pushButton_13.setIcon(QtGui.QIcon(self.controller.deck.cards[12].image_path))
    
    def on_press_14(self):
        self.pushButton_14.setIcon(QtGui.QIcon(self.controller.deck.cards[13].image_path))

    def on_press_15(self):
        self.pushButton_15.setIcon(QtGui.QIcon(self.controller.deck.cards[14].image_path))

    def on_press_16(self):
        self.pushButton_16.setIcon(QtGui.QIcon(self.controller.deck.cards[15].image_path))

    def on_press_17(self):
        self.pushButton_17.setIcon(QtGui.QIcon(self.controller.deck.cards[16].image_path))
 
    def on_press_18(self):
        self.pushButton_18.setIcon(QtGui.QIcon(self.controller.deck.cards[17].image_path))
    
    def reset_1(self):        
        self.pushButton_1.setIcon(QtGui.QIcon())
    
    def reset_2(self):        
        self.pushButton_2.setIcon(QtGui.QIcon())
    
    def reset_3(self):        
        self.pushButton_3.setIcon(QtGui.QIcon())
    
    def reset_4(self):        
        self.pushButton_4.setIcon(QtGui.QIcon())
    
    def reset_5(self):        
        self.pushButton_5.setIcon(QtGui.QIcon())
    
    def reset_6(self):        
        self.pushButton_6.setIcon(QtGui.QIcon())
    
    def reset_7(self):        
        self.pushButton_7.setIcon(QtGui.QIcon())
    
    def reset_8(self):        
        self.pushButton_8.setIcon(QtGui.QIcon())
    
    def reset_9(self):        
        self.pushButton_9.setIcon(QtGui.QIcon())
    
    def reset_10(self):        
        self.pushButton_10.setIcon(QtGui.QIcon())
    
    def reset_11(self):        
        self.pushButton_11.setIcon(QtGui.QIcon())
    
    def reset_12(self):        
        self.pushButton_12.setIcon(QtGui.QIcon())
    
    def reset_13(self):        
        self.pushButton_13.setIcon(QtGui.QIcon())
    
    def reset_14(self):        
        self.pushButton_14.setIcon(QtGui.QIcon())
    
    def reset_15(self):        
        self.pushButton_15.setIcon(QtGui.QIcon())
    
    def reset_16(self):        
        self.pushButton_16.setIcon(QtGui.QIcon())
    
    def reset_17(self):        
        self.pushButton_17.setIcon(QtGui.QIcon())
    
    def reset_18(self):        
        self.pushButton_18.setIcon(QtGui.QIcon())
    
    def reset_buttons(self, id):
        if self.controller.lock_1 == 0:
            self.reset_1()
        elif self.controller.lock_1 == 1:
            self.reset_2()
        elif self.controller.lock_1 == 2:
            self.reset_3()
        elif self.controller.lock_1 == 3:
            self.reset_4()
        elif self.controller.lock_1 == 4:
            self.reset_5()
        elif self.controller.lock_1 == 5:
            self.reset_6()
        elif self.controller.lock_1 == 6:
            self.reset_7()
        elif self.controller.lock_1 == 7:
            self.reset_8()
        elif self.controller.lock_1 == 8:
            self.reset_9()
        elif self.controller.lock_1 == 9:
            self.reset_10()
        elif self.controller.lock_1 == 10:
            self.reset_11()
        elif self.controller.lock_1 == 11:
            self.reset_12()
        elif self.controller.lock_1 == 12:
            self.reset_13()
        elif self.controller.lock_1 == 13:
            self.reset_14()
        elif self.controller.lock_1 == 14:
            self.reset_15()
        elif self.controller.lock_1 == 15:
            self.reset_16()
        elif self.controller.lock_1 == 16:
            self.reset_17()
        elif self.controller.lock_1 == 17:
            self.reset_18()

        if id == 0:
            self.reset_1()
        elif id == 1:
            self.reset_2()
        elif id == 2:
            self.reset_3()
        elif id == 3:
            self.reset_4()
        elif id == 4:
            self.reset_5()
        elif id == 5:
            self.reset_6()
        elif id == 6:
            self.reset_7()
        elif id == 7:
            self.reset_8()
        elif id == 8:
            self.reset_9()
        elif id == 9:
            self.reset_10()
        elif id == 10:
            self.reset_11()
        elif id == 11:
            self.reset_12()
        elif id == 12:
            self.reset_13()
        elif id == 13:
            self.reset_14()
        elif id == 14:
            self.reset_15()
        elif id == 15:
            self.reset_16()
        elif id == 16:
            self.reset_17()
        elif id == 17:
            self.reset_18()

    def lock_buttons(self, id):
        if self.controller.lock_1 == 0:
            self.pushButton_1.setEnabled(False)
        elif self.controller.lock_1 == 1:
            self.pushButton_2.setEnabled(False)
        elif self.controller.lock_1 == 2:
            self.pushButton_3.setEnabled(False)
        elif self.controller.lock_1 == 3:
            self.pushButton_4.setEnabled(False)
        elif self.controller.lock_1 == 4:
            self.pushButton_5.setEnabled(False)
        elif self.controller.lock_1 == 5:
            self.pushButton_6.setEnabled(False)
        elif self.controller.lock_1 == 6:
            self.pushButton_7.setEnabled(False)
        elif self.controller.lock_1 == 7:
            self.pushButton_8.setEnabled(False)
        elif self.controller.lock_1 == 8:
            self.pushButton_9.setEnabled(False)
        elif self.controller.lock_1 == 9:
            self.pushButton_10.setEnabled(False)
        elif self.controller.lock_1 == 10:
            self.pushButton_11.setEnabled(False)
        elif self.controller.lock_1 == 11:
            self.pushButton_12.setEnabled(False)
        elif self.controller.lock_1 == 12:
            self.pushButton_13.setEnabled(False)
        elif self.controller.lock_1 == 13:
            self.pushButton_14.setEnabled(False)
        elif self.controller.lock_1 == 14:
            self.pushButton_15.setEnabled(False)
        elif self.controller.lock_1 == 15:
            self.pushButton_16.setEnabled(False)
        elif self.controller.lock_1 == 16:
            self.pushButton_17.setEnabled(False)
        elif self.controller.lock_1 == 17:
            self.pushButton_18.setEnabled(False)

        if id == 0:
            self.pushButton_1.setEnabled(False)
        elif id == 1:
            self.pushButton_2.setEnabled(False)
        elif id == 2:
            self.pushButton_3.setEnabled(False)
        elif id == 3:
            self.pushButton_4.setEnabled(False)
        elif id == 4:
            self.pushButton_5.setEnabled(False)
        elif id == 5:
            self.pushButton_6.setEnabled(False)
        elif id == 6:
            self.pushButton_7.setEnabled(False)
        elif id == 7:
            self.pushButton_8.setEnabled(False)
        elif id == 8:
            self.pushButton_9.setEnabled(False)
        elif id == 9:
            self.pushButton_10.setEnabled(False)
        elif id == 10:
            self.pushButton_11.setEnabled(False)
        elif id == 11:
            self.pushButton_12.setEnabled(False)
        elif id == 12:
            self.pushButton_13.setEnabled(False)
        elif id == 13:
            self.pushButton_14.setEnabled(False)
        elif id == 14:
            self.pushButton_15.setEnabled(False)
        elif id == 15:
            self.pushButton_16.setEnabled(False)
        elif id == 16:
            self.pushButton_17.setEnabled(False)
        elif id == 17:
            self.pushButton_18.setEnabled(False)

    def set_all_buttons(self, setter):
        pass
        #self.pushButton_1.setEnabled(setter)
        #self.pushButton_2.setEnabled(setter)
        #self.pushButton_3.setEnabled(setter)
        #self.pushButton_4.setEnabled(setter)
        #self.pushButton_5.setEnabled(setter)
        #self.pushButton_6.setEnabled(setter)
        #self.pushButton_7.setEnabled(setter)
        #self.pushButton_8.setEnabled(setter)
        #self.pushButton_9.setEnabled(setter)
        #self.pushButton_10.setEnabled(setter)
        #self.pushButton_11.setEnabled(setter)
        #self.pushButton_12.setEnabled(setter)
        #self.pushButton_13.setEnabled(setter)
        #self.pushButton_14.setEnabled(setter)
        #self.pushButton_15.setEnabled(setter)
        #self.pushButton_16.setEnabled(setter)
        #self.pushButton_17.setEnabled(setter)
        #self.pushButton_18.setEnabled(setter)

    def reset_all_buttons(self):
        self.reset_1()
        self.reset_2()
        self.reset_3()
        self.reset_4()
        self.reset_5()
        self.reset_6()
        self.reset_7()
        self.reset_8()
        self.reset_9()
        self.reset_10()
        self.reset_11()
        self.reset_12()
        self.reset_13()
        self.reset_14()
        self.reset_15()
        self.reset_16()
        self.reset_17()
        self.reset_18()