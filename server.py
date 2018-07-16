import sys
from socket import *
import consts

class Server(object):

    def __init__(self):
        self.__port = consts.DEFAULT_PORT
        self.__name = consts.DEFAULT_NAME
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__hosts = []

    def init_server(self):

        self.__socket.bind((self.__name, self.__port))
        self.__socket.listen(5)

        connection_socket, address = self.__socket.accept()

        while True:
            query = connection_socket.recv(32)#

            if(query):
                if(query[0:1].decode() == consts.ASK_HOST):
                    #message = bytearray()
                    print("ASK_HOST")
                    self.__hosts.append((query[1:17].decode(), address))
                    print(query[1:17].decode())
                    connection_socket.send(consts.MSG_OK.encode())                    
                elif(query[0:1].decode() == consts.ASK_ESP_OPP):
                    print("ASK_ESP_OPP")
                    connection_socket.send(query)                    
                elif(query[0:1].decode() == consts.ASK_ANY_OPP):
                    print("ASK_ANY_OPP")
                    connection_socket.send(query)                    

                connection_socket.close()
                connection_socket, address = self.__socket.accept()


if __name__ == "__main__":
    server = Server()
    server.init_server()
