from socket import *
import consts 
import threading
import time
import select

class Peer(object):

    class ServerPeer(threading.Thread):

        def __init__(self, my_port, my_ip):
            threading.Thread.__init__(self)
            self.__running = True
            self.__my_port = my_port
            self.__my_ip = my_ip
            self.__socket = socket(AF_INET, SOCK_STREAM)

       
        def run(self):
            
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__socket.bind((self.__my_ip, self.__my_port))
            self.__socket.listen(1)

            self.__connection_socket, address = self.__socket.accept()
            
            while self.__running:
                input_ready, output_ready, except_ready = select.select ([self.__client_socket], [self.__client_socket], [])
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
            self.__client_socket = socket(AF_INET, SOCK_STREAM)


        def run(self):

            self.__socket.connect((self.__peer_ip, self.__peer_port))

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

        def __init__(self):
            threading.Thread.__init__(self)
            self.__running = True
        

        def run(self):

            while self.__running == True:

                text = input('')

                try:
                    client_peer.__socket.sendall(text)
                except:
                    Exception

                try:
                    server_peer.__connection_socket.sendall(text)
                except:
                    Exception

                time.sleep(0)
        
        
        def kill(self):
            self.running = False


    client_peer = None
    server_peer = None
    play_input = None


    def __init__(self, my_ip, my_port, peer_ip, peer_port):

        ip_addr = input('What IP (or type listen)?:')

        if ip_addr == 'listen':
            server_peer = self.ServerPeer(my_port, my_ip)
            client_peer = self.ClientPeer(peer_port, peer_ip)
            server_peer.start()
            play_input = self.PlayInput
            play_input.start()
        elif ip_addr == 'Listen':
            server_peer = self.ServerPeer(my_port, my_ip)
            client_peer = self.ClientPeer(peer_port, peer_ip)
            server_peer.start()
            play_input = self.PlayInput
            play_input.start()
        else:
            server_peer = self.ServerPeer(my_port, my_ip)
            client_peer = self.ClientPeer(peer_port, peer_ip)
            client_peer.peer_ip = ip_addr
            play_input = self.PlayInput()
            client_peer.start()
            play_input.start()


if __name__ == "__main__":
    peer = Peer('', 1776, '', 1776)
