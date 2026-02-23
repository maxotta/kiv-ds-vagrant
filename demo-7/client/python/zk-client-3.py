#
# Zookeeper client demo 3
#
# Watch handler demo.

import os
import pprint as pp
from kazoo.client import KazooClient
from time import sleep

zk = None

# This is the watch handler routine. The event information is passed in the 'event' parameter
def watch_handler(event):
  global zk
  print("Received watch event.")
  pp.pprint(event)
  # Get the current list of node children and set the watch again, because their are one-time triggers
  children = zk.get_children("/ds/clients", watch=watch_handler)
  pp.pprint(children)

def main():
  global zk
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  # Create the client instance
  zk = KazooClient(hosts=ensemble)
  # Start a Zookeeper session
  zk.start()

  # Ensure the clients context path exists
  zk.create("/ds/clients", makepath=True)
  # Get the list of child nodes and set the one-time watch handler
  children = zk.get_children("/ds/clients", watch=watch_handler)
  pp.pprint(children)

  # Sleep for 5 min.
  sleep(300)

  # Close the session
  zk.stop()

main()

#
# EOF
#
