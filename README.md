## Flask Docker Sandbox

A very basic playground for learning Docker and Flask using the built-in server in Flask.

### System Requirements

This sandbox has been tested on Mac OS X 10.12.6 with Docker v17.12

### Running
```bash
docker build -t <IMAGE-NAME>:<TAG> <PATH/TO/DOCKERFILE>
docker run -d -p <PUBLISHED-PORT>:80 <IMAGE-NAME>:<TAG>
```
Test to see that the service works:
```bash
curl http://localhost:<PUBLISHED-PORT>
```

### Debugging
See if the container is running:
```bash
docker ps -a
```
This should output something similar to:
```bash
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                              NAMES
<CONTAINER-ID>      <IMAGE-NAME>:<TAG>     "python3 -m flask ru…"   3 minutes ago       Up 3 minutes        0.0.0.0:<PUBLISHED-PORT>->80/tcp   trusting_easley
```
and status could indicate if the container has been correctly instantiated. To view and follow the logs:
```bash
docker logs -f <CONTAINER-ID>
```
which, if everything worked fine when curling the service, should output something similar to:
```bash
* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
<IP-NUMBER> - - [01/Jan/2018 13:37:00] "GET / HTTP/1.1" 200 -
```
