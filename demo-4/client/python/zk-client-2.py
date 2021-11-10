#
# Zookeeper client demo 2
#
# Zookeper ephemeral node demo.

import os
from kazoo.client import KazooClient
import socket
from time import sleep

def main():
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  # Create the client instance
  zk = KazooClient(hosts=ensemble)
  # Start a Zookeeper session
  zk.start()

  # Create an ephemeral node with the same name as the hostname.
  # If the '/ds/clients' context doesn't exist yet, it will be also created
  zk.create(f"/ds/clients/{ socket.gethostname() }", ephemeral=True, makepath=True)
  sleep(15)

  # Close the session
  zk.stop()

main()

#
# EOF
#
