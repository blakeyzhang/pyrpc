# -*- encoding: utf-8 -*-
"""
@File    :   rpcserver.py
@Time    :   2023/10/04 00:14:26
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""
import json
from server import tcpserver


class RPCStub:
    def __init__(self) -> None:
        self._functions = {}

    def register_function(self, func, name=None):
        if name is None:
            name = func.__name__
        self._functions[name] = func


class JSONRPC:
    def __init__(self) -> None:
        self.data = None

    def from_data(self, data):
        self.data = json.loads(data.decode("utf-8"))

    def call_method(self):
        method_name = self.data.get("method_name", "")
        method_args = self.data.get("method_args", None)
        method_kwargs = self.data.get("method_kwargs", None)

        if method_name in self._functions:
            res = self._functions[method_name](*method_args, **method_kwargs)
        else:
            res = "Please use the correct function"

        data = {"res": res}
        return json.dumps(data)


class RPCServer(tcpserver.TCPServer, JSONRPC, RPCStub):
    def __init__(self) -> None:
        tcpserver.TCPServer.__init__(self)
        JSONRPC.__init__(self)
        RPCStub.__init__(self)

    def loop(self, host="0.0.0.0", port=5000):
        self.bind_listen(host, port)
        print(f"Server start at: {host}:{port}")
        while True:
            self.accept_receive_close()

    def process_request(self, data):
        self.from_data(data)
        return self.call_method()
