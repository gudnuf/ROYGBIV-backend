## ROYGBIV
This repo is a python plugin for core lightning to implement prisms with BOLT 12

### Docker with Polar
You'll need to have a running instance of `bitcoin` and a couple of `cln` nodes in polar. 
Do a `docker network ls` to get the polar created network name. It will look like `1_default` or `n_default` depending on how many testnets of polar you've setup.
The contained `example.docker-compose.yml` can be copied and renamed to `docker-compose.yml` and then run `docker compose run` against. Replace that listed polar network in your file. 

### Running `lightning-cli` in your node 

You need to alias the following in order to successfully run `lightning-cli` inside your container.
```
docker exec -it 0004e61198f06ff793fd1988d330dc52ed1b87fce31cba114ec9bb50370739a8 bash 

root@alice:/# alias lightning-cli="lightning-cli --network regtest"
root@alice:/# lightning-cli listpeers
{
   "peers": []
}
root@alice:/# 

```