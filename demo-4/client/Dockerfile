#
# Zookeeper client node demo container image
#

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

RUN yum -q -y install python3
RUN yum -q -y install python3-pip
RUN pip3 install kazoo

COPY python /opt/zk/client

# EOF
