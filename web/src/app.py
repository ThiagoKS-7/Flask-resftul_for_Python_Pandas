'''
Registrar user 0 tokens
Cada user recebe 10 tokens
post de similarity - 1 token
'''

from flask_restful import Api
from flask import Flask
from ext.ui import get_urls
from ext.api import get_resources




data = {
  "title": "Flask tutorial",
  "subtitle": "Running on port 5000"
}

def create_app():
  app = Flask(__name__)
  get_urls(app, data)
  api = create_api(app)
  get_resources(api)
  return app

def create_api(app):
  api =  Api(app)
  return api
 




if __name__ == '__main__':
  app = create_app()
  app.run(host='0.0.0.0')