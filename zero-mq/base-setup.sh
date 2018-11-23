#!/bin/sh
yum -q -y install epel-release
yum -q -y group install 'Development Tools'
yum -q -y install mc
yum -q -y install screen
