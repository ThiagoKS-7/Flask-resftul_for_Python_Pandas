import datetime
from flask_restful import Resource
from flask import request
from services.requests import handleRequest
from ext.database.db_client import set_database

mongo,db,Users = set_database()

def handle_user_request(have_same_data, usr,hash_pwd):
    if not have_same_data:
      Users.insert_one({
        "Username":usr,
        "Password":hash_pwd,
        "Text1":"",
        "Text2":"",
        "Similiarity":"", 
        "Tokens": 10,
        "CreatedAt": datetime.now(),
        "UpdatedAt":""
      })
      retJson = {
      "message":"You successfully signed up!",
      "status": 201
      }
    else:
      retJson = {
       "message":"Error! User already exists.",
       "status": 409
      }

    return retJson
    
def handle_list_users_request(pwd_exists,usr):
    if pwd_exists:
      #faz update
      tokens = Users.find_one({'Username': usr})["Tokens"]
      # se o user tiver tokens, deixa passar
      if tokens <= 0:
        retJson = {
          "message":"Error! Not enough tokens.",
          "status": 401
        }
      else:
        tokens = tokens -1
        result = []
        for col in Users.find({},{"Username":1, "Text1":1, "Text2":1, "Tokens":1}):
          result.append({
            "username":col["Username"],
            "text1":col["Text1"],
            "text2":col["Text2"],
            "tokens":col["Tokens"],
          })
        
        retJson = {
          "message":"Data successfully retrieved.",
          "data": result,
          "Tokens": tokens,
          "status": 200,
        }
    else:
      retJson = {
      "message":"Error! User or password incorrect.",
      "status": 400
      }

    return retJson


class Register(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'register')
    return res

class GetUsers(Resource):
  def get(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'get-users')
    return res