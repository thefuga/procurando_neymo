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

class RoomController(object):

    def __init__(self, ui):
        self.myScore = 0
        self.opScore = 0
        self.seed = random.random()
        self.deck = deck.Deck(self.seed)
        self.ui = ui

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = room.Ui_Dialog()
    controller = RoomController(ui)
    ui.setupUi(main_window,controller)
    main_window.show()
    
    sys.exit(app.exec_())
    



