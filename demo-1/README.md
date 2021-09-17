# ![DS Logo](../images/icon-32-ds.png) Demo 1

The aim of this demo is to introduce you to the Vagrant tool and how you can use it for setting up and running *"virtual machines"* on your computer. In order to be able to run it, you must follow the instructions given in the main [README.md](../README.md#installation) file.

## Running the demo

To run the demo, open the terminal (on Windows the WSL2 terminal), go to the `demo-1` directory and enter: `vagrant up`.

## Deployment diagram

![Demo 1 deployment diagram](images/demo-1-deployment.png)

*Picture 1: Deployment diagram of Demo 1*


## Accessing the running node (container)

* vagrant ssh node1

## Managing the nodes

* vagrant up
* vagrant halt
* vagrant destroy
* vagrant provision

## The Vagrantfile

### Vagrant.configure

### config.vm.define

### Synced folders

### Link to Vagrant doc

### The kiv-ds-docker image

### Basic Docker commands

### Link to Docker doc

## Cleanup

 If you think you've played enough with this demo, just run the `vagrant destroy -f` command.

---

