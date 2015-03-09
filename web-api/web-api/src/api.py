from flask import Flask
from flask.ext import restful
app = Flask(__name__)
api = restful.Api(app)

from riak import RiakClient, RiakNode, RiakObject

r = RiakClient(nodes=[
  {
    'host':'riak_riaknode01',
    'http_port': 8098,
    'pbc_port': 8087
  },
  {
    'host':'riak_riaknode02',
    'http_port': 8098,
    'pbc_port': 8087
  },
  {
    'host':'riak_riaknode03',
    'http_port': 8098,
    'pbc_port': 8087
  }
])

class BucketItem(restful.Resource):
  def get(self, bucketid, itemid):
    bucket = r.bucket(bucketid)
    obj = bucket.get(itemid)
    return { itemid : str(obj.data) }

class Bucket(restful.Resource):
  def get(self, bucketid):
    bucket = r.bucket(bucketid)
    return { bucketid : bucket.get_keys() }

class Buckets(restful.Resource):
  def get(self):
    ret_array = []
    for bucket in r.get_buckets():
      ret_array.append(bucket.name)
    return { 'Buckets' : ret_array }

# get the value of some item in a bucket.
api.add_resource(BucketItem, '/bucket/<string:bucketid>/<itemid>')

# get a list of all keys in a bucket.
api.add_resource(Bucket, '/bucket/<string:bucketid>')

# get a list of all buckets
api.add_resource(Buckets, '/bucket')

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
