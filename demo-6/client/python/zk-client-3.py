#
# Zookeeper client demo 3
#
# Watch handler demo.

import os
import pprint as pp
from kazoo.client import KazooClient
from time import sleep

zk = None

def watch_handler(event):
  global zk
  print("Received watch event.")
  pp.pprint(event)
  children = zk.get_children("/ds/clients", watch=watch_handler)
  pp.pprint(children)

def main():
  global zk
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  zk = KazooClient(hosts=ensemble)
  zk.start()

  zk.create("/ds/clients", makepath=True)
  children = zk.get_children("/ds/clients", watch=watch_handler)
  pp.pprint(children)

  sleep(300)

  zk.stop()

main()

#
# EOF
#
