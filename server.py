import sys
import socket as skt
import consts

class Server(object):

    def __init__(self):
        self.__port = consts.DEFAULT_PORT
        self.__name = consts.DEFAULT_NAME
        self.__socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.__hosts = []


    def init_server(self):

        self.__socket.bind((self.__name, self.__port))
        self.__socket.listen(5)

        connection_socket, address = self.__socket.accept()

        while True:
            query = connection_socket.recv(40)#

            if(query):
                if(query[0:1].decode() == consts.ASK_HOST):
                    print("ASK_HOST")
                    self.__hosts.append((query[1:17].decode(), address, query[17:].decode()))
                    print(query[1:17].decode())
                    print(query[17:].decode())
                    connection_socket.send(bytes(consts.SRVR_ANSR.encode() + str(address[0]).encode() + ":".encode() + str(address[1]).encode()) + query[17:])
                    #connection_socket.send(consts.MSG_OK.encode())                    
                elif(query[0:1].decode() == consts.ASK_ESP_OPP):
                    print("ASK_ESP_OPP")
                    found = False
                    for host in self.__hosts:
                        if host[0] == query[1:17].decode():
                            print(str(host[1][0]) + ":" + str(host[1][1]))
                            print(len(bytes(consts.SRVR_ANSR.encode() + str(host[1][0]).encode() + ":".encode() + str(host[1][1]).encode())))
                            connection_socket.send(bytes(consts.SRVR_ANSR.encode() + str(host[1][0]).encode() + ":".encode() + str(host[1][1]).encode()) + query[17:])
                            self.__hosts.remove(host)
                            found = True
                            break
                    if not found:
                        connection_socket.send(consts.MSG_NOPE.encode())                    
                elif(query[0:1].decode() == consts.ASK_ANY_OPP):
                    print("ASK_ANY_OPP")
                    if len(self.__hosts) > 0:
                        connection_socket.send(bytes(consts.SRVR_ANSR.encode() + str(self.__hosts[0][1][0]).encode() + ":".encode() + str(self.__hosts[0][1][1]).encode()) + query[17:])
                        self.__hosts.remove(self.__hosts[0])
                    else:
                        connection_socket.send(consts.MSG_NOPE.encode())

                connection_socket.close()
                connection_socket, address = self.__socket.accept()


if __name__ == "__main__":
    server = Server()
    server.init_server()
