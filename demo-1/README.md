# Demo 1

First demo showing how to spin up 2 nodes with given names and IP addresses. In order to start the demo, enter the following command in this directory:
```
vagrant up
```
After that, you can access the nodes via ssh, like:
```
vagrant ssh node1
```
To see what's actually running, use the docker command:
```
docker ps
```
The output should be something like:
```
CONTAINER ID   IMAGE                                  COMMAND                  CREATED          STATUS          PORTS                    NAMES
cd2f2fcb87bd   ghcr.io/maxotta/kiv-ds-docker:v0.9.0   "/etc/kiv-ds-startup…"   21 minutes ago   Up 21 minutes   127.0.0.1:2200->22/tcp   node2
919f2f5906b4   ghcr.io/maxotta/kiv-ds-docker:v0.9.0   "/etc/kiv-ds-startup…"   22 minutes ago   Up 22 minutes   127.0.0.1:2222->22/tcp   node1
```

Finally, you can stop the whole thing with:
```
vagrant halt
```
or cleanup with:
```
vagrant destroy -f
```


