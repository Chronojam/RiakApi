#!/bin/bash

IPADDR=$(ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1 }')

sed -i "s/.*-name riak@127.0.0.1.*/-name riak@$IPADDR/" /etc/riak/vm.args
sed -i "s/127.0.0.1/$IPADDR/" /etc/riak/app.config

cat /etc/riak/app.config

#sudo /usr/local/bin/mungehosts -a "127.0.0.1 $RIAK_NODE_NAME"
#riak start
riak console
