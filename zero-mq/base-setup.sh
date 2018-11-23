#!/bin/sh
yum -q -y install epel-release
yum -q -y install avahi
yum -q -y install avahi-tools
yum -q -y install nss-mdns
if [ ! -f /etc/avahi/avahi-daemon.conf.bak ] ; then
    systemctl stop avahi-daemon
    mv /etc/avahi/avahi-daemon.conf /etc/avahi/avahi-daemon.conf.bak
    NAT_IF=`route | awk '/default/{ print $8 }'`
    sed "/^\[server\]$/a allow-interfaces=$NAT_IF\ndeny-interfaces=lo" /etc/avahi/avahi-daemon.conf.bak > /etc/avahi/avahi-daemon.conf
    systemctl start avahi-daemon
fi

