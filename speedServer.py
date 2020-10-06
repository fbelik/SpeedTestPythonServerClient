#!/usr/bin/env python3

import socket
import threading
import sys

if (len(sys.argv) != 3):
    print("Missing command line arguments")
    print("./speedServer [HOST-ADDR] [PORT]")
    sys.exit()

try:
    PORT = int(sys.argv[2])
except ValueError:
    print('Could not read port number')
    sys.exit(0)
HOST = sys.argv[1]
ADDR = (HOST,PORT)

TO_SEND = b''
with open('randomText.short', 'rb') as f:
    TO_SEND = f.read()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print('[LISTENING] server is listening on %s' % str(ADDR))
print('[MESSAGE SIZE] %d bytes' % len(TO_SEND))

def handleClient(conn, addr, numChunks): 
    print('[CONNECTION FORMED] address %s - %d CHUNKS TO SEND' % (addr, numChunks))
    connected = True
    try:
        while connected and numChunks > 0:
            conn.send(TO_SEND)
            numChunks-=1
        print('[CLOSING CONNECTION] address %s' % (addr,))
        conn.close()
    except BrokenPipeError:
        print('[CONNECTION BROKEN] closing socket %s' % (addr,))
        conn.close()

while True:
    try:
        conn, addr = server.accept()
        chunksToSend = b''
        left = 4
        while (left > 0):
            chunksToSend += conn.recv(left)
            left = 4 - len(chunksToSend)
        chunksToSend = int.from_bytes(chunksToSend, 'big')
        threading.Thread(target=handleClient, args=(conn, addr, chunksToSend)).start()
    except KeyboardInterrupt:
        print('\n[SHUTTING DOWN] socket closing')
        break
server.close()
