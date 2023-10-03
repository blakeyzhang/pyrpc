# -*- encoding: utf-8 -*-
"""
@File    :   tcpserver.py
@Time    :   2023/10/04 00:14:11
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""

import socket

import client


class TCPServer:
    def __init__(self) -> None:
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, host, port):
        self.serversocket.bind((host, port))
        self.serversocket.listen(5)

    def accept_receive_close(self):
        clientsocket, address = self.serversocket.accept()
        res = clientsocket.recv(1024)
        data = self.process_request(res)
        clientsocket.sendall(data.encode("utf-8"))
        clientsocket.close()
