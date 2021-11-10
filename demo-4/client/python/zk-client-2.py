#
# Zookeeper client demo 2
#
# Zookeper ephemeral node demo.

import os
import pprint as pp
from kazoo.client import KazooClient
import socket
from time import sleep

def main():
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  zk = KazooClient(hosts=ensemble)
  zk.start()

  zk.create(f"/ds/clients/{ socket.gethostname() }", ephemeral=True, makepath=True)
  sleep(15)

  zk.stop()

main()

#
# EOF
#
