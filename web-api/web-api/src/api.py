from flask import Flask
from flask.ext import restful
import bucket

# Basic initialization
app = Flask(__name__)
api = restful.Api(app)

# Register bucket routes:
bucket.RegisterRoutes(api)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
