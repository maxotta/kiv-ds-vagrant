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
  zk = KazooClient(hosts=ensemble)
  zk.start()

  children = zk.get_children("/ds")
  pp.pprint(children)

  zk.stop()

main()

#
# EOF
#
