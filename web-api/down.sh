docker kill $(docker ps | grep "webapi/webapi:latest" | cut -c1-12)
docker kill $(docker ps | grep "webapi/webapibalancer:latest" | cut -c1-12)

# I know how horrible this is, but it works for me.
docker rm $(docker ps -a | grep Exited | awk '{print $1}')
