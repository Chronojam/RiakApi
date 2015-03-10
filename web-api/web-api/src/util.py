import os

balancer_address = os.environ.get('BALANCER_ADDRESS')
if not balancer_address:
  import sys
  print "BALANCER_ADDRESS not set."
  sys.exit(2)
