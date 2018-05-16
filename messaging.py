#!/usr/bin/python2
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("aaj khush to bhut hoge tum",("192.168.43.86",9999))
s.sendto("aaj kht hoge tum",("192.168.43.86",9999))
