# -*- encoding: utf-8 -*-
"""
@File    :   client_test.py
@Time    :   2023/10/04 00:16:02
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""


from client import rpcclient


if __name__ == "__main__":
    c = rpcclient.RPCClient()
    c.connect("127.0.0.1", 5000)
    res = c.test("testcase", kw="1")
    print(f"The result is: {res}")
