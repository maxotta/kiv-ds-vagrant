#!/bin/sh
MDNS_SUBNET=$1
yum -q -y install avahi
yum -q -y install avahi-tools
yum -q -y install nss-mdns
if [ ! -f /etc/avahi/avahi-daemon.conf.bak ] ; then
    systemctl stop avahi-daemon
    mv /etc/avahi/avahi-daemon.conf /etc/avahi/avahi-daemon.conf.bak
    MDNS_IFACE=`route | awk "/$MDNS_SUBNET/{ print $8 }"`
    sed "/^\[server\]$/a allow-interfaces=$MDNS_IFACE\ndeny-interfaces=lo" /etc/avahi/avahi-daemon.conf.bak > /etc/avahi/avahi-daemon.conf
    systemctl start avahi-daemon
fi

