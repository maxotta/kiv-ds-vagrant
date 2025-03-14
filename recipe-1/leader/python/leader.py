#
# A simple example of a leader node that broadcasts a "heartbeat" message every 5 seconds.
#

from time import sleep
from scapy.all import *

def main():
    n = 0
    while True:
        print("Hello from leader")
        packet = IP(dst="10.0.1.255") / UDP(sport=5000,dport=5000) / f'Hello from leader: {n}'
        send(packet)
        sleep(5)
        n += 1

main()

# EOF
