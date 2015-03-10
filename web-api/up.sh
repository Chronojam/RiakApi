docker build -t webapi/webapi web-api/
docker run \
--link riak_riaknode01:riak_riaknode01 \
--link riak_riaknode02:riak_riaknode02 \
--link riak_riaknode03:riak_riaknode03 \
--env BALANCER_ADDRESS=http://localhost:8079/ \
--env RIAK_INSTANCES=riak_riaknode01,riak_riaknode02,riak_riaknode03 \
--name webapi_webapi01 -d webapi/webapi python api.py

docker run \
--link riak_riaknode01:riak_riaknode01 \
--link riak_riaknode02:riak_riaknode02 \
--link riak_riaknode03:riak_riaknode03 \
--env BALANCER_ADDRESS=http://localhost:8079/ \
--env RIAK_INSTANCES=riak_riaknode01,riak_riaknode02,riak_riaknode03 \
--name webapi_webapi02 -d webapi/webapi python api.py

docker run \
--link riak_riaknode01:riak_riaknode01 \
--link riak_riaknode02:riak_riaknode02 \
--link riak_riaknode03:riak_riaknode03 \
--env BALANCER_ADDRESS=http://localhost:8079/ \
--env RIAK_INSTANCES=riak_riaknode01,riak_riaknode02,riak_riaknode03 \
--name webapi_webapi03 -d webapi/webapi python api.py

docker build -t webapi/webapibalancer web-api-balancer/
docker run \
--link webapi_webapi01:webapi_webapi01 \
--link webapi_webapi02:webapi_webapi02 \
--link webapi_webapi03:webapi_webapi03 \
--publish "8079:80" \
--name webapi_webapibalancer -d webapi/webapibalancer nginx -g "daemon off;"
