from kazoo.client import KazooClient
import socket
import time
import pprint as pp

GROUP_PATH = '/kiv/ds/group-1'

def main() :

    zk = KazooClient(hosts='10.0.1.11:2181,10.0.1.12:2181,10.0.1.13:2181')
    zk.start()

    children = zk.get_children('/')
    pp.pprint(children)

    node_name = socket.gethostname()
    print('My name is: ' + node_name)

    zk.ensure_path(GROUP_PATH)
    zk.create(GROUP_PATH + '/' + node_name + '_', ephemeral=True, sequence=True)

    time.sleep(20)

    zk.stop()


main()
print('DONE')
