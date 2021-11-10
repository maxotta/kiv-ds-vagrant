# ![DS Logo](images/icon-64-ds.png) Distributed Systems Lab Demo Projects

## Introduction

This repository serves as a collection of small demo projects for students enrolled to the [Distributed Systems course](https://portal.zcu.cz/StagPortletsJSR168/CleanUrl?urlid=prohlizeni-predmet-sylabus&predmetZkrPrac=KIV&predmetZkrPred=DS&predmetRok=2021&predmetSemestr=ZS&plang=en) taught at [DCSE](http://www.kiv.zcu.cz/en/education/index.html) / [UWB](https://www.zcu.cz/en/index.html)

## Distributed systems demos

The provided demos serve as a template and knowledge base for projects, that students work out in the Lab. The demos are:

* [***Demo-1***](demo-1) - the simplest demo showing the basic use of Vagrant and Docker. Starts one Linux node running a SSH server.
* [***Demo-2***](demo-2) - shows how to setup and start two connected nodes/containers. It's a simple frontend web server (proxy) connected to a backend server.
* [***Demo-3***](demo-3) - extends demo-2 in making the backend scalable (N backend servers) and configures the proxy server to act as a load balancer.
* [***Demo-4***](demo-4) - a basic demo of a single Apache ZooKeeper running in standalone mode and serving several clients.
* [***Demo-5***](demo-5) - shows how to setup a cluster of ZooKeeper servers (ensemble).
* [***Demo-6***](demo-6) - shows how to use Docker volumes in extending the previous demo with persistent data storage, so the ZooKeeper container can be removed, upgraded, etc. without any loss of data. Also, it shows how to setup and use container service health check provided by Docker.

## Required Software

### Operating Systems
If you want to play with the provided examples you will need one of the following operating systems:

![Linux](images/icon-32-linux.png) [Linux](https://linux.org/pages/download/) (Debian/Ubuntu based distributions preferred)

![macOS](images/icon-32-macos.png) [macOS](https://en.wikipedia.org/wiki/MacOS) from [Apple](https://www.apple.com/)

![Win](images/icon-32-win.png) [Windows Subsystem for Linux - WSL2](https://docs.microsoft.com/en-us/windows/wsl/about) from [Microsoft](https://www.microsoft.com/)

* See also: [WSL2 Installation instructions for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

If you encounter difficulties with setting up the following software, please don't waste your time and install a Debian or Ubuntu based Linux distro inside a VM on the [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads) and use it as your development environment.

### ![Git](images/icon-32-git.png) Git

You will need [Git](https://git-scm.com/downloads) the be able to clone this repo to your machine or even to actively contribute to the continuous improvement of this project. [Pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) are welcome!

### ![Docker](images/icon-32-docker.png) Docker

All nodes/services of the provided distributed systems examples are running inside [Containers](https://www.docker.com/resources/what-container). Containers are simple and lightweight and do not consume much of your computer's resources unlike virtual machines.

* [Installing Docker on Ubuntu Linux](https://docs.docker.com/engine/install/ubuntu/) or [other Linux distributions](https://docs.docker.com/engine/install/#server)
* [Installing Docker on macOS](https://docs.docker.com/desktop/mac/install/)
* [Installing Docker on Windows (WSL2)](https://docs.docker.com/desktop/windows/install/)

### ![Vagrant](images/icon-32-vagrant.png) Vagrant

The [Vagrant tool](https://www.vagrantup.com/intro) will help us to easily set-up and dispose distributed systems consisting of multiple nodes. With Vagrant, you will start to [think about the infrastructure like of code (IaC)](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac). A good intro to IaC (in czech language) can be found at [Zdrojak.CZ](https://zdrojak.cz/clanky/infrastructure-as-code-lehky-uvod/)

However, the official intro to Vagrant aptly states that *Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "works on my machine" excuse a relic of the past.* :-)

For installation, follow the instructions for the OS of your choice at the [Vagrant Downloads page](https://www.vagrantup.com/downloads)

Verify your installation by trying out the [Demo-1](demo-1)

---
