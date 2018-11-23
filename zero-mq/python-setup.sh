#!/bin/sh
yum -q -y install python36
yum -q -y install python36-devel
yum -q -y install python34-pip
yum -q -y install python34-devel
pip3.4 install --upgrade pip
