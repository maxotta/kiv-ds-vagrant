#
# Zookeeper client demo 3
#
# Watch handler demo.

import os
import pprint as pp
from kazoo.client import KazooClient
from time import sleep

zk = None
my_node = None
# This is the watch handler routine. The event information is passed in the 'event' parameter
def watch_handler(event):
  global zk
  print("Received watch event.")
  pp.pprint(event)
  # Get the current list of node children and set the watch again, because their are one-time triggers
  children = zk.get_children("/ds/cluster-1", watch=watch_handler)
  print("Current cluster members:")
  pp.pprint(children)


def my_handler(event):
  print("Received watch event.")
  pp.pprint(event)
  my_data = zk.get(my_node, watch=my_handler)
  print(f"My data is: { my_data }.")

def main():
  global zk
  global my_node
  ensemble = os.environ['ZOO_SERVERS']
  print(f"Client will use these servers: { ensemble }.")
  # Create the client instance
  zk = KazooClient(hosts=ensemble)
  # Start a Zookeeper session
  zk.start()
  cluster_info = zk.get("/ds/cluster-1")
  pp.pprint(cluster_info)
  my_node = zk.create("/ds/cluster-1/node-", ephemeral=True, sequence=True)
  print(f"My node is: { my_node }.")

  cluster_members = zk.get_children("/ds/cluster-1", watch=watch_handler)

  print(f"My path is: {my_node}")
  my_data = zk.get(my_node, watch=my_handler)
  print(f"My data is: { my_data }.")

  # Sleep for 5 min
  sleep(300)
  # Close the session
  zk.stop()

main()

#
# EOF
#
