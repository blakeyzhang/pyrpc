# -*- encoding: utf-8 -*-
"""
@File    :   server_test.py
@Time    :   2023/10/04 00:38:30
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""

from server import rpcserver


def test(*args, **kwargs):
    print(f"The method registered on the server is called.")
    print(f"test: args = {args}, kwargs = {kwargs}")
    return "done"


if __name__ == "__main__":
    s = rpcserver.RPCServer()
    s.register_function(test)
    s.loop("127.0.0.1", 5000)
