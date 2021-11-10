#
# Zookeeper client demo 1
#
# Basic client listing children of a node.

import os
import pprint as pp
from kazoo.client import KazooClient

def main():
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  # Create the client instance
  zk = KazooClient(hosts=ensemble)
  # Start a Zookeeper session
  zk.start()

  # List node children
  children = zk.get_children("/ds")
  pp.pprint(children)

  # Close the session
  zk.stop()

main()

#
# EOF
#
