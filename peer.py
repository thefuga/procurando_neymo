import socket as skt
import threading
import time
import select
import consts 


class ServerPeer(threading.Thread):

    def __init__(self, my_ip, my_port):
        threading.Thread.__init__(self)
        self.running = True
        self.my_port = my_port
        self.my_ip = my_ip
        self.connection_socket = None
        self.address = None
        self.message = None
        self.active = False
        

    def run(self):
        socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        socket.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
        socket.bind((self.my_ip, self.my_port))
        socket.listen(1)

        self.connection_socket, self.address = socket.accept()
            
        while self.running == True:
            input_ready, output_ready, except_ready = select.select ([self.connection_socket], [self.connection_socket], [])
            for input_item in input_ready:
                # Handle sockets
                data = self.connection_socket.recv(7)
                if data:
                    self.message = (data[0:1].decode(), data[1:3].decode(), data[3:5].decode(), data[5:7].decode())
                    if self.message[0] == consts.MSG_YOUR_TURN:
                        self.active = True
                    elif self.message[0] == consts.MSG_MY_TURN:
                        self.active == False              
                else:
                    self.message = None
                    break
            time.sleep(0)


    def kill(self):
        self.running = False


class ClientPeer(threading.Thread):

    def __init__(self, peer_ip, peer_port):
        threading.Thread.__init__(self)
        self.running = True
        self.client_socket = None
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.host = None
        self.message = None
        self.active = False
        

    def run(self):
        self.client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.client_socket.connect((self.peer_ip, self.peer_port))


        while self.running == True:
            input_ready, output_ready, except_ready = select.select ([self.client_socket], [self.client_socket], [])

            for input_item in input_ready:
                data = self.client_socket.recv(7)
                if data:
                    self.message = (data[0:1].decode(), data[1:3].decode(), data[3:5].decode(), data[5:7].decode())
                    if self.message[0] == consts.MSG_YOUR_TURN:
                        self.active = True
                    elif self.message[0] == consts.MSG_MY_TURN:
                        self.active == False                                       
                else:
                    self.message = None
                    break

            time.sleep(0)


    def kill(self):
        self.running = False


class PlayInput(threading.Thread):

    def __init__(self, client_peer, server_peer):
        threading.Thread.__init__(self)
        self.client_peer = client_peer
        self.server_peer = server_peer        
        self.running = True
        self.message = None
        

    def run(self):

        while self.running == True:
            while(not self.message):
               pass

            try:
                self.client_peer.client_socket.sendall(self.message)
            except Exception:
                pass

            try:
                self.server_peer.connection_socket.sendall(self.message)
            except Exception:
                pass

            self.message = None

            time.sleep(0)
        

    def kill(self):
        self.running = False


    def play(self, message_type=None, first_card="__", second_card="__", score="__"):
        self.message = bytes(message_type.encode() + first_card.encode() + second_card.encode() + score.encode())
        if message_type == consts.MSG_YOUR_TURN:
            self.client_peer.active = False
            self.server_peer.active = False
        elif message_type == consts.MSG_MY_TURN:
            self.client_peer.active = True
            self.server_peer.active = True


class Peer():

    def __init__(self, server_ip="", server_port=3216, my_ip=None, my_port=3216, listening=True):
        if listening:
            self.server_peer = ServerPeer(server_ip, server_port)
            self.client_peer = ClientPeer(my_ip, my_port)
            self.server_peer.start()
            self.play_input = PlayInput(self.client_peer, self.server_peer)
            self.play_input.start()
        else:
            self.server_peer = ServerPeer(server_ip, server_port)
            self.client_peer = ClientPeer(my_ip, my_port)
            self.play_input = PlayInput(self.client_peer, self.server_peer)
            self.client_peer.start()
            self.play_input.start()


