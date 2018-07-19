import socket
import threading
import time
import select
import consts 

class ServerPeer(threading.Thread):

    def __init__(self, my_port, my_ip):
        threading.Thread.__init__(self)
        self.__running = True
        self.__my_port = my_port
        self.__my_ip = my_ip
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       

    def run(self):
            
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((self.__my_ip, self.__my_port))
        self.__socket.listen(1)

        self.__connection_socket, address = self.__socket.accept()
            
        while self.__running:
            input_ready, output_ready, except_ready = select.select ([self.self.__socket], [self.self.__socket], [])
            for input_item in input_ready:
                # Handle sockets
                data = self.__connection_socket.recv(1024)
                if data:
                    print("Them: " + data)
                else:
                    break
            time.sleep(0)
        

    def kill(self):
        self.__running = False


class ClientPeer(threading.Thread):

    def __init__(self, peer_port, peer_ip):
        threading.Thread.__init__(self)
        self.__running = True
        self.__peer_ip = peer_ip
        self.__peer_port = peer_port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):

        self.__client_socket.connect((self.__peer_ip, self.__peer_port))

        # Select loop for listen
        while self.__running:
            input_ready,output_ready,except_ready = select.select ([self.__client_socket], [self.__client_socket], [])
            for input_item in input_ready:
                # Handle sockets
                data = self.__client_socket.recv(1024)
                if data:
                    print("Them: " + data)
                else:
                    break
            time.sleep(0)


    def kill(self):
        self.__running = False


class PlayInput(threading.Thread):

    def __init__(self, client_peer, server_peer):
        threading.Thread.__init__(self)
        self.client_peer = client_peer
        self.server_peer = server_peer
        self.__running = True
        

    def run(self):

        while self.__running == True:

            text = input('')

            try:
                client_peer.__client_socket.sendall(text)
            except:
                Exception

            try:
                server_peer.__connection_socket.sendall(text)
            except:
                Exception

            time.sleep(0)
        
        
    def kill(self):
        self.running = False


if __name__ == "__main__":

    ip_addr = input('What IP (or type listen)?:')

    if ip_addr == 'listen':
        server_peer = ServerPeer(1776, "")
        client_peer = ClientPeer(1776, None)
        server_peer.start()
        play_input = PlayInput(client_peer, server_peer)
        play_input.start()
    elif ip_addr == 'Listen':
        server_peer = ServerPeer(1776, "")
        client_peer = ClientPeer(1776, None)
        server_peer.start()
        play_input = PlayInput(client_peer, server_peer)
        play_input.start()
    else:
        server_peer = ServerPeer(1776, "")
        client_peer = ClientPeer(1776, None)
        client_peer.peer_ip = ip_addr
        play_input = PlayInput(client_peer, server_peer)
        client_peer.start()
        play_input.start()

