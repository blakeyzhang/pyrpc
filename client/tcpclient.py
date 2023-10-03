# -*- encoding: utf-8 -*-
"""
@File    :   tcpclient.py
@Time    :   2023/10/04 00:13:49
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""

import socket


class TCPClient:
    def __init__(self) -> None:
        self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host="127.0.0.1", port=5000):
        self.clientsock.connect((host, port))

    def send(self, data):
        self.clientsock.sendall(data.encode("utf-8"))

    def recv(self, length):
        res = self.clientsock.recv(length)
        res = res.decode("utf-8")
        return res
