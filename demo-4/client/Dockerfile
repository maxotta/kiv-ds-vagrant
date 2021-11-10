#
# Zookeeper client node demo container image
#

FROM ghcr.io/maxotta/kiv-ds-docker:latest

RUN yum -q -y install python3
RUN pip3 install kazoo

COPY python /opt/zk/client

# EOF
