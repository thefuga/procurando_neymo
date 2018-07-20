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
import time
import numpy
import client as clt
import peer

class Controller(object):

    def __init__(self, ui, room_ui, game_over_ui):
        self.myScore = 0
        self.opScore = 0
        self.lock_1 = -1
        self.lock_2 = -1
        self.myTurn = True
        self.seed = random.random()
        #self.deck = deck.Deck(self.seed)
        self.ui = ui
        self.game_over_ui = game_over_ui
        self. room_ui = room_ui
        self.peer = None
        #ui.show_room_window(self)


    def click_action(self,id):
        if self.lock_1 != id:
            if self.lock_2 == -1:
                self.lock_2 = self.deck.cards[id].image_path
                self.lock_1 = id
            else:
                if(self.lock_2 == self.deck.cards[id].image_path):
                    self.myScore+=1
                    self.ui.lock_buttons(id)
                    self.ui.lcdNumber.display(self.myScore)
                    if((self.myScore >= 9) or (self.opScore >=9)):
                        if(self.myScore > self.opScore):
                            self.game_over_ui.label.setText("O HEXA VEM!")
                        else:
                            self.game_over_ui.label.setText( "O HEXA NÃO VEM!")
                        self.peer.play_input.play(message_type=consts.MSG_YOUR_TURN, 
                        first_card=str(self.lock_1) if self.lock_1 >= 10 else "0" +  str(self.lock_1), 
                        second_card=str(id) if id >= 10 else "0" + str(id), score="0" + str(self.myScore)) #enviar as cartas que foram jogadas. Atualmente, o outro jogador está recebendo e printando "TESTE"
                        self.ui.main_window.hide()
                        self.game_over_ui.game_over_window.show()
                        
                else:
                    time.sleep(1)
                    self.myTurn = False
                    self.ui.reset_buttons(id)
                    self.peer.play_input.play(message_type=consts.MSG_YOUR_TURN, 
                    first_card=str(self.lock_1) if self.lock_1 >= 10 else "0" +  str(self.lock_1), 
                    second_card=str(id) if id >= 10 else "0" + str(id), score="0" + str(self.myScore)) #enviar as cartas que foram jogadas. Atualmente, o outro jogador está recebendo e printando "TESTE"
                    self.play_control()
                    message = self.peer.server_peer.message or self.peer.client_peer.message
                    self.opScore = int(message[3])
                    self.ui.lcdNumber_2.display(self.opScore)
                    if(self.opScore >= 9):
                        self.game_over_ui.label.setText( "O HEXA NÃO VEM!")
                        self.ui.main_window.hide()
                        self.game_over_ui.game_over_window.show()
                        

                self.lock_2 = -1
                self.lock_1 = -1
        
        
    def room_rendezvous(self, message_type, room_name_1):
        client = clt.Client()
        if(message_type == "host"):
            self.ip_port_seed=client.init_client(consts.ASK_HOST, room_name=room_name_1, seed = numpy.random.randint(9))
            self.myTurn = True
            self.peer = peer.Peer(server_port=self.ip_port_seed[1], my_port=self.ip_port_seed[1])
            self.peer.client_peer.active = True
            self.peer.server_peer.active = True
        elif(room_name_1 == ""):
            self.ip_port_seed=client.init_client(consts.ASK_ANY_OPP, room_name="")
            self.myTurn = False
            self.peer = peer.Peer(my_ip=self.ip_port_seed[0], server_port=self.ip_port_seed[1], my_port=self.ip_port_seed[1], listening=False)
        else:
            self.ip_port_seed=client.init_client(consts.ASK_ESP_OPP, room_name=room_name_1)
            self.myTurn = False
            self.peer = peer.Peer(my_ip=self.ip_port_seed[0], server_port=self.ip_port_seed[1], my_port=self.ip_port_seed[1], listening=False)

        self.deck = deck.Deck(self.ip_port_seed[2])
        
        self.room_ui.room_window.hide()
        self.ui.main_window.show()
        self.ui.set_all_buttons(self.myTurn)
        self.play_control()
    

    def play_control(self):
        self.ui.set_all_buttons(False)
        while(not(self.peer.client_peer.active or self.peer.server_peer.active)):
            pass
        self.myTurn = True
        self.ui.set_all_buttons(True)
        self.peer.play_input.play(message_type=consts.MSG_MY_TURN)

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    room_window = QtWidgets.QMainWindow()
    main_window = QtWidgets.QMainWindow()
    game_over_window = QtWidgets.QMainWindow()
    room_ui = room.Ui_Dialog()
    ui = mainWindow.Ui_MainWindow()
    game_over_ui = gameOver.Ui_Dialog()
    controller = Controller(ui, room_ui, game_over_ui)
    room_ui.setupUi(room_window ,controller)
    ui.setupUi(main_window,controller)
    game_over_ui.setupUi(game_over_window,controller)
    
    room_window.show() 
    #sgame_over_window.show()
      #  if (controller.lock_1 != -1 and controller.lock_2 != -1):
      #      if controller.deck.cards[controller.lock_1].id == controller.deck.cards[controller.lock_2].id:
     #           controller.myScore = controller.myScore + 1
                #trava os botoes e da +1 na propria myScore
            #else:
                #reseta os 2 botoes clicados
     #   controller.lock_1 = controller.lock_2 = -1

    sys.exit(app.exec_())
    
    


