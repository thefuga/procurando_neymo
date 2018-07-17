import sys
from socket import *
import consts

class Client(object):

    def __init__(self):
        self.__server_name = consts.DEFAULT_NAME
        self.__server_port = consts.DEFAULT_PORT
        self.__client_socket = socket(AF_INET, SOCK_STREAM)


    def init_client(self, message):

        self.__client_socket.connect((self.__server_name, self.__server_port))

        if(message[0:1].decode() == consts.ASK_HOST):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(4) #resposta do server, com mensagem contendo MSG_OK ou MSG_NOPE
            print(response.decode("utf-8"))
        elif(message[0:1].decode() == consts.ASK_ESP_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(16)
            print(response[0:1].decode())
            print(response[1:].decode())
        elif(message[0:1].decode() == consts.ASK_ANY_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(16)
            print(response[0:1].decode())
            print(response[1:].decode())

        self.__client_socket.close()
        

if __name__ == "__main__":
    message = bytes(consts.ASK_ANY_OPP.encode()) + r"teste$$$$$$$$$$$".encode()
    client = Client()
    client.init_client(message)