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
            response = self.__client_socket.recv(16) #resposta do server, com mensagem contendo MSG_OK ou MSG_NOPE
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            port = int(tokens[1])
            self.__client_socket.close()
            return(ip, port)
        elif(message[0:1].decode() == consts.ASK_ESP_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(16)
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            port = int(tokens[1])
            self.__client_socket.close()
            return(ip, port)
        elif(message[0:1].decode() == consts.ASK_ANY_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(16)
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            port = int(tokens[1])
            self.__client_socket.close()
            return(ip, port)

        self.__client_socket.close()
        

if __name__ == "__main__":
    message = bytes(consts.ASK_HOST.encode()) + r"teste$$$$$$$$$$$".encode()
    client = Client()
    print(client.init_client(message))