#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket

"""
查询本机ip地址
:return: ip
2020年04月27日16:26:45
"""
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip



if __name__ == '__main__':
    print("本机ip地址是:%s"%get_host_ip())
