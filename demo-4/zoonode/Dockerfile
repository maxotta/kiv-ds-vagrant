#
# Zookeeper server node demo container image
#

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

ARG ZK_VERSION=3.7.2

RUN yum -q -y install java-1.8.0-openjdk

RUN groupadd zookeeper && \
    useradd -g zookeeper -d /opt/zookeeper -s /sbin/nologin zookeeper

ADD https://dlcdn.apache.org/zookeeper/zookeeper-${ZK_VERSION}/apache-zookeeper-${ZK_VERSION}-bin.tar.gz /opt

RUN tar zxvf /opt/apache-zookeeper-${ZK_VERSION}-bin.tar.gz -C /opt && \
    ln -s /opt/apache-zookeeper-${ZK_VERSION}-bin /opt/zk && \
    mkdir /opt/zk/data && \
    chown -R zookeeper:zookeeper /opt/zk/* && \
    rm /opt/apache-zookeeper-${ZK_VERSION}-bin.tar.gz

COPY zoo.cfg /opt/zk/conf
COPY myid /opt/zk/data

EXPOSE 2181 2888 3888 8080

CMD /opt/zk/bin/zkServer.sh start-foreground

# EOF
