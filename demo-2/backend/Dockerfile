#
# Simple backend demo server image
#

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

RUN yum -q -y install python3
RUN yum -q -y install python3-pip
RUN pip3 install flask

COPY python /opt/backend

HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=3 CMD curl -s http://localhost:5000/ping | grep pong

CMD /usr/bin/python3 /opt/backend/simple-backend.py

# EOF
