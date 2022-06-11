import datetime
from flask_restful import Resource
from flask import request
import spacy
from services.requests import handleRequest
from ext.database.db_client import set_database

mongo,db,Users = set_database()

def handle_detect_request(pwd_exists,usr, tex1, tex2):
  if pwd_exists:
      #faz update
      tokens = Users.find_one({'Username': usr})["Tokens"]
      #se o user tiver tokens, deixa passar
      if tokens <= 0:
        retJson = {
          "message":"Error! Not enough tokens.",
          "status": 401
        }
      else:
        # usa natural language processing pra comparar os textos
        nlp = spacy.load("en_core_web_sm")
        text1 = nlp(text1)
        text2 = nlp(text2)
        ratio = text1.similarity(text2)
        tokens = tokens -1
        Users.update_one({'Username': usr}, {"$set": {
          "Similiarity": ratio,
          "Tokens": tokens,
          "UpdatedAt": datetime.now(),
        }})
        retJson = {
          "message":"Sentence successfully saved.",
          "Tokens": tokens,
          "status": 202,
        }
  else:
    retJson = {
    "message":"Error! User or password incorrect.",
    "status": 400
    }

  return retJson

class Detect(Resource):
  def patch(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'detect')
    return res
