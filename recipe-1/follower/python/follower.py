#
# A simple client that listens for messages broadcasted by the leader node
#

from scapy.all import *

def main():
    while True:
        sniff(iface = "eth1",
              count=1,
              lfilter = lambda f: f[IP].dst == "10.0.1.255", 
              prn = lambda x: x.show())

main()

# EOF
