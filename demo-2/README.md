# ![DS Logo](../images/icon-32-ds.png) Demo 2

The aim of this demo is to show how to:
* spin up 2 nodes using Vagrant
* how to build your own Docker images by extending the prepared Docker base image [kiv-ds-docker](https://github.com/maxotta/kiv-ds-docker/pkgs/container/kiv-ds-docker) and use them in you own projects
* how to map container ports
* how to access applications/services running inside containers

## Deployment diagram

![Demo 2 deployment diagram](images/demo-2-deployment.png)

*Picture 1: Deployment diagram of Demo 2*

## Running the demo

Just enter `vagrant up` in the `demo-2` directory and wait until all nodes start up:

![Demo 2 startup](images/demo-2-startup.png)

*Picture 2: Demo-2 starting up*

If you want to see which containers are currently running with some additional information, type the command `docker ps`.

## Accessing the deployed service

In order to access the deployed services through the frontend web-server, you need to know how the container ports are mapped to the host. The `docker ps` command's output shows, that the **frontend** container port **80/tcp** is mapped to port **8080/tcp**,
so we access the service via **http://localhost:8080**:

![Demo 2 access services](images/demo-2-services.png)

*Picture 3: Accessing Demo-2 service from the host machine*

## Accessing the deployed services on Windows outside from WSL2
<a name="access-wsl2"></a>
The previous instructions work on Linux and inside the WSL2 environment on Windows. If you want to access the service from a web browser running on the Windows host machine, you need to know through which interface to access the WSL2 VM. You can figure this out by looking at the routing table inside WSL2:

![Demo 2 access WSL2 VM from outside](images/demo-2-host-access-ip.png)

*Picture 4: Figuring out the IP address of the WSL2 VM on Windows*

Now, when you know the IP address, you can access the service also from outside WSL2 - just replace **localhost** with the IP address in the URLs shown in the above examples:

![Demo 2 acces WSL2 VM with browser from outside WSL2](images/demo-2-browser.png)

*Picture 5: Accessing the service with a browser from outside the WSL2 VM*
 
 ## Cleanup

 If you think you've played enough with this demo, just run the `vagrant destroy -f` command.

---



