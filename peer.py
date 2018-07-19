import socket as skt
import threading
import time
import select
import consts 


class ServerPeer(threading.Thread):

    def __init__(self, my_ip, my_port):
        threading.Thread.__init__(self)
        self.running = 1
        self.my_port = my_port
        self.my_ip = my_ip
        self.connection_socket = None
        self.address = None
        

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
                data = self.connection_socket.recv(4)
                if data:
                    print("Them: " + data[0:2].decode() + data[2:4].decode())
                else:
                    break
            time.sleep(0)
        

    def kill(self):
        self.running = 0


class ClientPeer(threading.Thread):

    def __init__(self, peer_ip, peer_port):
        threading.Thread.__init__(self)
        self.running = 1
        self.client_socket = None
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.host = None
        

    def run(self):
        self.client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.client_socket.connect((self.peer_ip, self.peer_port))

        # Select loop for listen
        while self.running == True:

            input_ready, output_ready, except_ready = select.select ([self.client_socket], [self.client_socket], [])

            for input_item in input_ready:
                # Handle sockets
                data = self.client_socket.recv(4)
                if data:
                    print("Them: " + data[0:2].decode() + data[2:4].decode())
                else:
                    break

            time.sleep(0)


    def kill(self):
        self.running = 0


class PlayInput(threading.Thread):

    def __init__(self, client_peer, server_peer):
        threading.Thread.__init__(self)
        self.client_peer = client_peer
        self.server_peer = server_peer        
        self.running = 1
        self.message = None
        

    def run(self):

        while self.running == True:

            #self.message = bytes(input("").encode())

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
        self.running = 0


    def play(self, first_card, second_card):
        self.message = bytes(first_card.encode() + second_card.encode())
        #self.message = first_card#, second_card



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


if __name__ == "__main__":
    ip_addr = input('What IP (or type listen)?:')

    if ip_addr == 'listen':
        peer = Peer()
    else:
        peer = Peer(my_ip = ip_addr, listening=False)

    #time.sleep(5)
    #peer.play_input.play("a", "b")

