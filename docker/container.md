# Docker

-----------------------

### `docker container run -p 80:80 nginx`
	* Download/Use nginx image and open port 80 of both machine
	* Start a new container from Image every time
	* " --detach/-d " to run in background and give Unique ID

### `docker container ls`
	* List all container (running) with Unique IDs.
	* " -a " to list all the container

### `docker container port <Name>`
	* Show all exposed ports

### `docker container stop <unique ID/ Name>`
	* Stop Container

### Example `docker container run -p 80:80 -d --name <name> nginx`

### `docker container logs <unique ID/ Name>`
	* To see logs of running container

### `docker container top <name>`
	* To see process running inside a container

### `docker container rm <ID> <ID> ...`
	* To remove container (not running container)
	* " -f " to remove Forcefully

### `docker ps`
	* To see all running containers

### Note :: 
	> `--env` 
	  * to pass environmental variable when we run docker

### `docker container inspect <name>`
	* Show meta data about the container (startup config, volumes, networking, etc...)

### `docker container stats`
	* Show live performance data for all containers

## `docker container run -it`
	* Starts a new container interactively

## `docker container exec -it`
	* Run additional command in existing container

## `docker container start -ai`
	* Start docker interactively

### `docker container inspect --format '{{ .NetworkSettings.IPAddress  }}' nginx`
	* Shows the Virtual IP of container
