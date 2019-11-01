from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.client import EventType
import socket
import time
import pprint as pp

GROUP_PATH = '/kiv/ds/group-1'

zk = None

def notification_handler(event) :
    global zk
    print('Notification event recieved:')
    pp.pprint(event)
    children = zk.get_children(GROUP_PATH, watch=notification_handler)
    print('Group members: ')
    pp.pprint(children)

def main() :
    global zk
    zk = KazooClient(hosts='10.0.1.11:2181,10.0.1.12:2181,10.0.1.13:2181')
    zk.start()
    children = zk.get_children(GROUP_PATH, watch=notification_handler)
    while True :
        time.sleep(5)
    zk.stop()

main()
