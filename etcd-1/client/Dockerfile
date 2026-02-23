#
# etcd golang client node demo container image
# go install go.etcd.io/etcd/client/v3@latest
#FROM golang:1.24 AS go

FROM ghcr.io/maxotta/kiv-dsa-vagrant-base-docker:latest

RUN dnf update -y
RUN dnf install golang -y

RUN go get go.etcd.io/etcd/client/v3
# go mod download go.etcd.io/etcd/client/v3

# EOF
