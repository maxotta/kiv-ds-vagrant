#
# Simple backend demo server image
#

#FROM ghcr.io/maxotta/kiv-ds-docker:v0.9.0
FROM max/ds1:0.99.2
RUN yum -q -y install python3
RUN pip3 install flask

COPY python /opt/backend

CMD /usr/bin/python3 /opt/backend/simple-backend.py

# EOF
