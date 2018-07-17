import card
import deck
import consts
import deck
import gameOver
import mainWindow
import room
import server
import random
from PyQt5 import QtWidgets
import sys
import roomController

class Controller(object):

    def __init__(self, ui):
        self.myScore = 0
        self.opScore = 0
        self.seed = random.random()
        self.deck = deck.Deck(self.seed)
        self.ui = ui
        #ui.show_room_window(self)

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    room_window = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()
    room_ui = room.Ui_Dialog()
    ui = mainWindow.Ui_MainWindow()
    controller = Controller(ui)
    room_ui.setupUi(room_window ,controller)
    ui.setupUi(main_window,controller)
    main_window.show()
    room_window.show() 

    sys.exit(app.exec_())
    


