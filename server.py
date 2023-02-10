#!/bin/python3
from socket import *
from fib import fib
import re
from threading import Thread

def onlynum(byte_array):
    string = byte_array.decode('ascii')
    numbers = re.findall(r'\d+', string)
    if not numbers:
        return 0
    return int(''.join(numbers))

def fib_server(address):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client,addr = sock.accept()
        print("Connection", addr)
        Thread(target=fib_handler,args=(client,),daemon=True).start()
        

def fib_handler(client):
    while True:
        client.send(b"Input >> ")
        req = client.recv(100)
        if not req:
            break
        n = onlynum(req)
        result = fib(n)
        resp = str(result).encode('ascii') +b'\n'
        client.send(b"Output >> "+resp)
    print("Closed")

fib_server(('',25000))



