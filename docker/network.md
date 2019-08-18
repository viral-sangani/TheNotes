---------------------------------------------------

# Docker Network

### `docker network ls`
	* Show all network.
	* --network bridge -> 
		* Default Docker Virtual Network, which is NATed behind the Host IP.
	* --network host ->
		* It gains performance by skipping virtual network and directly connecting to Host network
		* Sacrifices security of that network
	* --networm none ->
		* Remove eth0 and only leaves you with localhost interface in container

### `docker network inspect <name>`
	* Shows Meta data about that network
	* Shows all containers attached to that network
	
### `docker network create <name>`
	* Spawns  a new virtual network for you to attach containers to
	
### Note
	* Can Define Network while creating Container
	* " --network <name> "
	
### `docker network connect <network name> <container name>`
	* Dynamically create a NIC in a container on an existing virtual netwrk
	
### `docker networm disconnect <network name> <container name>
	* Remove Virtual Network / NIC from container

---------------------------------------------------

## Docker Network DNS
	* Docker daemon has a build-in DNS server that containers use by dafault
	* Docker defaults the hostname to the container's name, but you can also set alias
	* " --net-alias " gives  a specific DNS name to container, used to Achive DNS Round Robin

