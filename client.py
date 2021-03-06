import sys
import socket as skt
import consts

class Client(object):

    def __init__(self):
        self.__server_name = consts.DEFAULT_NAME
        self.__server_port = consts.DEFAULT_PORT
        self.__client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        

    def init_client(self, message_type, seed=None, room_name=None):

        if(len(room_name) > 16):
            room_name = room_name[:16]
        elif(len(room_name) < 16):
            while len(room_name) < 16:
                room_name += r"$"

        message = bytes(message_type.encode() + room_name.encode() + str(seed).encode())

        self.__client_socket.connect((self.__server_name, self.__server_port))

        if(message[0:1].decode() == consts.ASK_HOST):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(40)
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            tokens = tokens[1].split("§")
            port = int(tokens[0])
            new_seed = int(tokens[1])
            self.__client_socket.close()
            print(ip, port, new_seed)
            return(ip, port, new_seed)
        elif(message[0:1].decode() == consts.ASK_ESP_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(40)
            if(response.decode() == consts.MSG_NOPE):
                self.__client_socket.close()
                return None
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            tokens = tokens[1].split("§")
            port = int(tokens[0])
            new_seed = int(tokens[1])
            self.__client_socket.close()
            return(ip, port, new_seed)
        elif(message[0:1].decode() == consts.ASK_ANY_OPP):
            self.__client_socket.send(message)
            response = self.__client_socket.recv(40)
            if(response.decode() == consts.MSG_NOPE):
                self.__client_socket.close()
                return None
            tokens = response[1:].decode().split(":")
            ip = tokens[0]
            tokens = tokens[1].split("§")
            port = int(tokens[0])
            new_seed = int(tokens[1])
            self.__client_socket.close()
            return(ip, port, new_seed)

        self.__client_socket.close()