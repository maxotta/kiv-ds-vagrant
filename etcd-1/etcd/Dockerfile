#
# etcd
#

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

ENV ETCD_VERSION="v3.5.19"
ENV DOWNLOAD_URL="https://github.com/etcd-io/etcd/releases/download"
ENV INSTALL_DIR="/opt/etcd"

RUN mkdir -p ${INSTALL_DIR} ; \
    curl -L ${DOWNLOAD_URL}/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -o /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz ; \
    tar xzvf /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -C ${INSTALL_DIR} --strip-components=1 ; \
    rm -f /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz

COPY docker-entrypoint.sh ${INSTALL_DIR}/docker-entrypoint.sh
RUN  chmod a+x ${INSTALL_DIR}/docker-entrypoint.sh

EXPOSE 2379 2380

CMD ${INSTALL_DIR}/docker-entrypoint.sh ${INSTALL_DIR}/etcd --config-file /etc/etcd.conf.yml

# EOF
