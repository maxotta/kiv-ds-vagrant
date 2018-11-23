#!/usr/bin/python3

import zmq
import random
import sys
import time

host = "node-1.local"
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://{0}:{1}".format(host, port))

while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("client message to server1")
    socket.send_string("client message to server2")
    time.sleep(1)
