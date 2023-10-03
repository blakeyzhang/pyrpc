# -*- encoding: utf-8 -*-
"""
@File    :   rpcclient.py
@Time    :   2023/10/04 00:14:00
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""
import json
from client import tcpclient


class RPCStub:
    def __getattr__(self, function):
        def func(*args, **kwargs):
            data = {
                "method_name": function,
                "method_args": args,
                "method_kwargs": kwargs,
            }
            self.send(json.dumps(data))
            return self.recv(1024)

        setattr(self, function, func)
        return func


class RPCClient(tcpclient.TCPClient, RPCStub):
    pass
