import sys
from socket import *
import consts

class Server(object):

    def __init__(self):
        self.__port = consts.DEFAULT_PORT
        self.__name = consts.DEFAULT_NAME
        self.__socket = socket(AF_INET, SOCK_STREAM)


    def init_server(self):

        self.__socket.bind((self.__name, self.__port))
        self.__socket.listen(5)

        connection_socket, address = self.__socket.accept()

        while True:
            query = connection_socket.recv(1024)#vai depender do protocolo. Pode tanto ser um nome de usuário ou uma palavra reservada para pegar um usuário qualquer.

            if(query):
                print(query.decode("utf-8"))

                connection_socket.send(query) #retorna o endereço do usuário encontrado ou erro. No momento, retornando a própria solicitação só pra testar.
                connection_socket.close()
                connection_socket, address = self.__socket.accept()


if __name__ == "__main__":
    server = Server()
    server.init_server()
