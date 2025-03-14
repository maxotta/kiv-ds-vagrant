#
# Follower
#

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

RUN yum -q -y install tcpdump
RUN yum -q -y install libpcap
RUN yum -q -y install python3
RUN yum -q -y install python3-pip
RUN pip3 install scapy

COPY python /opt/python

CMD /usr/bin/python3 /opt/python/follower.py

# EOF
