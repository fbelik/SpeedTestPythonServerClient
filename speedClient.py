#! /usr/bin/env python3

import socket
import sys
import time

# Cmd arguments: HOST_ADDR, HOST_PORT, CHUNK_LEN

if len(sys.argv) != 4:
    print('Missing arguments')
    print('./speedClient [HOST_ADDR] [HOST_PORT] [CHUNKS]')
    sys.exit(0)

HOST = sys.argv[1] 
try:
    PORT = int(sys.argv[2])
except ValueError:
    print('Could not read port number')
    sys.exit(0)
try:
    CHUNKS = int(sys.argv[3])
except ValueError:
    print('Could not read number of chunks')
    sys.exit(0)
ADDR = (HOST,PORT)

MSG = b''
filename = 'randomText.short'
try:
    with open(filename, 'rb') as f:
        MSG = f.read()
        SIZE_CHUNK = len(MSG)
        print('The server message size is %d' % SIZE_CHUNK)
    SIZE = SIZE_CHUNK * CHUNKS
except:
    print('Cannot find file %s' % filename)
    sys.exit(0)

print('About to request %d chunks of %d bytes' % (CHUNKS, SIZE_CHUNK))
print("There will be a '.' printed for every 1 chunks (%d kbytes) recieved" % (SIZE_CHUNK/1000))
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
except Exception as e:
    print('Unsuccessful connection to address %s' % str(ADDR))
    print('Error:', e)
    sys.exit(0)

CHUNKS_SEND = CHUNKS.to_bytes(4, byteorder='big')
client.send(CHUNKS_SEND)
START = time.time()
print('Start time: %d seconds, %d microseconds' % (START, START * 1000000 % 1000000))
for i in range(CHUNKS):
    recieved = len(client.recv(SIZE_CHUNK))
    while (recieved < SIZE_CHUNK):
        recieved += len(client.recv(SIZE_CHUNK - recieved))
        #print(recieved)
    print('.', flush=True, end='')
END = time.time()
print()
DIFF = END-START
print('End time: %d seconds, %d microseconds' % (END, END * 1000000 % 1000000))
print('It took %f seconds to read %d bytes for a speed of %f bytes/second, %f kBps, %f MBps, %f GBps' % (DIFF, SIZE, SIZE/DIFF, SIZE/(1000*DIFF), SIZE/(1000000*DIFF), SIZE/(1000000000*DIFF)))
print('Or, in bits/second, %f bits/second, %f kbps, %f Mbps, %f Gbps' % (SIZE*8/DIFF, SIZE*8/(1000*DIFF), SIZE*8/(1000000*DIFF), SIZE*8/(1000000000*DIFF)))

