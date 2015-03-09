docker build -t riak/riaknode riak-node/
docker run \
--tty=True \
--name riak_riaknode01 -d riak/riaknode /etc/riak/run.sh

docker run \
--tty=True \
--name riak_riaknode02 -d riak/riaknode /etc/riak/run.sh

docker run \
--tty=True \
--name riak_riaknode03 -d riak/riaknode /etc/riak/run.sh
