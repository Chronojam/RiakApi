from flask import request
from flask.ext import restful
from dbaccess import client
from util import balancer_address

# Call me to register all the api/buckets/ routes.
def RegisterRoutes(api):
  api.add_resource(Buckets, '/api/buckets')
  api.add_resource(BucketsItem, '/api/buckets/<string:bucketid>')
  api.add_resource(BucketsItemProperties, '/api/buckets/<string:bucketid>/properties')
  api.add_resource(BucketsItemKeys, '/api/buckets/<string:bucketid>/keys')
  api.add_resource(BucketItemKeysValue, '/api/buckets/<string:bucketid>/keys/<keyid>')

class Buckets(restful.Resource):
  # GET /api/buckets 
  # get a list of buckets in this cluster
  def get(self):
    ret_array = []
    for bucket in client.get_buckets():
      ret_array.append(bucket.name)
    return { 'buckets' : ret_array }

class BucketsItem(restful.Resource):
  # GET /api/buckets/<string:bucketid>
  # list information about this bucket.
  def get(self, bucketid):
    bucket = client.bucket(bucketid)
    return { 'keys' : '{0}api/buckets/{1}/keys'.format(balancer_address, bucketid),
             'properties' : '{0}api/buckets/{1}/properties'.format(balancer_address, bucketid),
             'name' : bucketid }

class BucketsItemProperties(restful.Resource):
  # GET /api/buckets/<string:bucketid>/properties
  # get a list of properties associated with this bucket.
  def get(self, bucketid):
    bucket = client.bucket(bucketid)
    return bucket.get_properties()

class BucketsItemKeys(restful.Resource):
  # GET /api/buckets/<string:bucketid>/keys
  # get a list of keys associated with this bucket.
  def get(self, bucketid):
    bucket = client.bucket(bucketid)
    ret_dict = {}
    for key in bucket.get_keys():
      ret_dict[key] = '{0}api/buckets/{1}/keys/{2}'.format(balancer_address, bucketid, key)
    return ret_dict

  # POST /api/buckets/<string:bucketid>/keys
  # add a bunch of keys and values to the bucket.
  def post(self, bucketid):
    bucket = client.bucket(bucketid)
    if not 'items' in request.json:
      return { 'Error' : 'Missing items property from body' }, 401
    for item in request.json['items']:
      if not 'key' in item or not 'value' in item:
        return { 'Error' : 'Bad Request' }, 400
    
      if bucket.get(item['key']).exists:
        pass
      else:
        obj = bucket.new(item['key'], item['value'])
        obj.store()
    return 'success'

class BucketItemKeysValue(restful.Resource):
  # GET /api/buckets/<string:bucketid>/keys/<keyid>
  # returns the value of the key with the given id.
  def get(self, bucketid, keyid):
    bucket = client.bucket(bucketid)
    obj = bucket.get(keyid)
    if not obj.exists:
      return { 'Error' : 'No such key' }
    else:
      return { keyid : obj.encoded_data }

  # POST /api/buckets/<string:bucketid>/keys/<keyid>
  # create or update a key inside a bucket { 'value' : NEW_VALUE }
  def post(self, bucketid, keyid):
    bucket = client.bucket(bucketid)
    obj = bucket.get(keyid)
    if not 'value' in request.json:
      return { 'Error' : 'Bad Request' }, 400
    
    obj = bucket.new(keyid, request.json['value'])
    obj.store()
    return "success"
