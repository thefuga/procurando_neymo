import sys
from socket import *
import consts

class Client(object):

    def __init__(self):
        self.__server_name = consts.DEFAULT_NAME
        self.__server_port = consts.DEFAULT_PORT
        self.__client_socket = socket(AF_INET, SOCK_STREAM)


    def init_client(self):

        self.__client_socket.connect((self.__server_name, self.__server_port))

        while True:
            query = input("Digita qualquer merda: ") #será a requisição de partida
            self.__client_socket.send(str.encode(query))
            response = self.__client_socket.recv(1024) #resposta do server, com mensagem contendo oponente ou erro
            print(response.decode("utf-8"))

            self.__client_socket.close()
            break



if __name__ == "__main__":

    client = Client()
    client.init_client()
