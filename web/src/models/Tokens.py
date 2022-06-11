import datetime
from flask_restful import Resource
from flask import request
from services.requests import handleRequest
from ext.database.db_client import set_database

mongo,db,Users = set_database()

def handle_refill_request(pwd_exists, usr, target, tokens):
  #se existe um password pra aquele user, é pq ele existe
  if pwd_exists and usr == 'admin':
    #faz update
    Users.update_one({'Username': target}, {"$set": {
      "Tokens": tokens,
      "UpdatedAt": datetime.now(),
    }})
    retJson = {
      "message":"Tokens sucessfully refilled.",
      "Tokens": tokens,
      "status": 202,
    }
  else:
    retJson = {
    "message":"Error! Only admin can refill tokens.",
    "status": 400
    }

  return retJson

class Refill(Resource):
  def patch(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'refill')
    return res