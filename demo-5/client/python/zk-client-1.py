#
# Zookeeper client demo 1
#

import os
import logging
import pprint as pp
from kazoo.client import KazooClient

def main():
  ensemble = os.environ['ZOO_HOSTS']
  print(f"Client will use these servers: { ensemble }.")
  zk = KazooClient(hosts=ensemble)
  zk.start()

  children = zk.get_children("/ds")
  pp.pprint(children)

main()

#
# EOF
#
