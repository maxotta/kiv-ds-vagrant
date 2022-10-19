#
# Zookeeper server node demo container image
#

FROM ghcr.io/maxotta/kiv-ds-docker:latest

RUN yum -q -y install java-1.8.0-openjdk

RUN groupadd zookeeper && \
    useradd -g zookeeper -d /opt/zookeeper -s /sbin/nologin zookeeper

ADD https://dlcdn.apache.org/zookeeper/zookeeper-3.7.1/apache-zookeeper-3.7.1-bin.tar.gz /opt

RUN tar zxvf /opt/apache-zookeeper-3.7.1-bin.tar.gz -C /opt && \
    ln -s /opt/apache-zookeeper-3.7.1-bin /opt/zk && \
    mkdir /opt/zk/data && \
    chown -R zookeeper:zookeeper /opt/zk/* && \
    rm /opt/apache-zookeeper-3.7.1-bin.tar.gz

COPY zoo.cfg /opt/zk/conf
COPY myid /opt/zk/data

EXPOSE 2181 2888 3888 8080

CMD /opt/zk/bin/zkServer.sh start-foreground

# EOF
