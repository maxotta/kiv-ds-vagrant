#!/usr/bin/python3

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:{0}".format(port))

while True:
    socket.send_string("Server message to client3")
    msg = socket.recv()
    print(msg)
    time.sleep(1)
