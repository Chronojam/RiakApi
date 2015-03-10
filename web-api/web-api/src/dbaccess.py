import os
from riak import RiakClient

# riak01,riak02,riak03,192.168.2.14 etc..
riak_instances = os.environ.get('RIAK_INSTANCES')

if not riak_instances:
  import sys
  print "RIAK_INSTANCES environment variable not set."
  sys.exit(2)

riak_instances.split(',')
riak_nodes=[]

for address in riak_instances.split(','):
  riak_nodes.append(
    {
      'host': address,
      'http_port': 8098,
      'pbc_port': 8087
    })

client = RiakClient(nodes=riak_nodes)
