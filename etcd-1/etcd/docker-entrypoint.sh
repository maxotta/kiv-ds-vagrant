#!/bin/bash

# CLUSTER=# ${NAME_1}=http://${HOST_1}:2380,${NAME_2}=http://${HOST_2}:2380,${NAME_3}=http://${HOST_3}:2380

# This script takes etcd configuration from environment variables and builds an etcd configuration file.
set -e

# Generate the config only if it doesn't exist
if [[ ! -f "/etc/etcd.conf.yml" ]]; then
    {
        echo "name: '${NODE_NAME}'"
        echo "data-dir: '/var/lib/etcd'"
        echo "initial-advertise-peer-urls: 'http://${NODE_IP}:2380'"
        echo "listen-peer-urls: 'http://0.0.0.0:2380'"
        echo "advertise-client-urls: 'http://${NODE_IP}:2379'"
        echo "listen-client-urls: 'http://0.0.0.0:2379'"
        echo "initial-cluster: '${CLUSTER}'"
        echo "initial-cluster-state: 'new'"
        echo "initial-cluster-token: 'etcd-cluster'"
    } >> "/etc/etcd.conf.yml"
fi

exec "$@"
