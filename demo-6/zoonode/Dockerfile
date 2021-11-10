#
# Zookeeper server node demo container image
#

FROM ghcr.io/maxotta/kiv-ds-docker:latest

RUN yum -q -y install java-1.8.0-openjdk
RUN yum -q -y install nc

RUN groupadd zookeeper && \
    useradd -g zookeeper -d /opt/zookeeper -s /sbin/nologin zookeeper

ADD https://dlcdn.apache.org/zookeeper/zookeeper-3.7.0/apache-zookeeper-3.7.0-bin.tar.gz /opt

RUN tar zxvf /opt/apache-zookeeper-3.7.0-bin.tar.gz -C /opt && \
    ln -s /opt/apache-zookeeper-3.7.0-bin /opt/zk && \
    mkdir /opt/zk/data && \
    chown -R zookeeper:zookeeper /opt/zk/* && \
    rm /opt/apache-zookeeper-3.7.0-bin.tar.gz

COPY docker-entrypoint.sh /opt/zk/bin/docker-entrypoint.sh
RUN  chmod a+x /opt/zk/bin/docker-entrypoint.sh

EXPOSE 2181 2888 3888 8080

ENV ZOOCFGDIR=/opt/zk/conf ZOO_CONF_DIR=/opt/zk/conf ZOO_DATA_DIR=/opt/zk/data ZOO_LOG_DIR=/opt/zk/logs ZOO_TICK_TIME=2000 ZOO_INIT_LIMIT=5 ZOO_SYNC_LIMIT=2 ZOO_AUTOPURGE_PURGEINTERVAL=0 ZOO_AUTOPURGE_SNAPRETAINCOUNT=3 ZOO_MAX_CLIENT_CNXNS=60 ZOO_STANDALONE_ENABLED=false ZOO_ADMINSERVER_ENABLED=true

HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=3 CMD nc -z localhost 2181 && nc -z localhost 22

CMD /opt/zk/bin/docker-entrypoint.sh /opt/zk/bin/zkServer.sh start-foreground

# EOF
