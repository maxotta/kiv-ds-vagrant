#
# Setup image with NGINX as frontend (proxy) server
#

#FROM ghcr.io/maxotta/kiv-ds-docker:v0.9.0
FROM max/ds1:0.99.2
RUN yum -q -y install epel-release && \
    yum -q -y install nginx && \
    rm -rf /usr/share/nginx/html

COPY html /usr/share/nginx/html
COPY config/backend-upstream.conf /etc/nginx/conf.d/backend-upstream.conf
COPY config/backend-proxy.conf /etc/nginx/default.d/backend-proxy.conf

CMD /usr/bin/sleep 60 && /usr/sbin/nginx && tail -F /var/log/nginx/access.log /var/log/nginx/error.log
