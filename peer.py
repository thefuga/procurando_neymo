import socket as skt
import threading
import time
import select
import consts 

class ServerPeer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__running = True
        #self.__my_port = my_port
        #self.__my_ip = my_ip
        self.__connection_socket = None
        self.__address = None
        
       

    def run(self):
        host = ''
        port = 1776
        socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        socket.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
        socket.bind((host, port))
        socket.listen(1)

        self.__connection_socket, self.__address = socket.accept()
            
        while self.__running == 1:
            input_ready, output_ready, except_ready = select.select ([self.__connection_socket], [self.__connection_socket], [])
            for input_item in input_ready:
                # Handle sockets
                data = self.__connection_socket.recv(1024)
                if data:
                    print("Them: " + data)
                else:
                    break
            time.sleep(0)
        

    def kill(self):
        self.__running = 0


class ClientPeer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__running = 1
        self.__peer_ip = None
        self.__client_socket = None
        #self.__peer_port = None
        

    def run(self):

        port = 1776
        self.__client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.__client_socket.connect((self.__peer_ip, port))

        # Select loop for listen
        while self.__running == True:
            input_ready, output_ready, except_ready = select.select ([self.__client_socket], [self.__client_socket], [])
            for input_item in input_ready:
                # Handle sockets
                data = self.__client_socket.recv(1024)
                if data:
                    print("Them: " + data)
                else:
                    break
            time.sleep(0)


    def kill(self):
        self.__running = 0


class PlayInput(threading.Thread):

    def __init__(self, client_peer, server_peer):
        threading.Thread.__init__(self)
        self.client_peer = client_peer
        self.server_peer = server_peer
        self.__running = 1
        

    def run(self):

        while self.__running == True:

            text = input('')

            try:
                self.client_peer.__client_socket.sendall(text)
            except:
                Exception

            try:
                self.server_peer.__connection_socket.sendall(text)
            except:
                Exception

            time.sleep(0)
        
        
    def kill(self):
        self.running = 0


if __name__ == "__main__":

    ip_addr = input('What IP (or type listen)?:')

    if ip_addr == 'listen':
        server_peer = ServerPeer()
        client_peer = ClientPeer()
        server_peer.start()
        play_input = PlayInput(client_peer, server_peer)
        play_input.start()
    elif ip_addr == 'Listen':
        server_peer = ServerPeer()
        client_peer = ClientPeer()
        server_peer.start()
        play_input = PlayInput(client_peer, server_peer)
        play_input.start()
    else:
        server_peer = ServerPeer()
        client_peer = ClientPeer()
        client_peer.__peer_ip = ip_addr
        play_input = PlayInput(client_peer, server_peer)
        client_peer.start()
        play_input.start()

