import bcrypt
from flask import Response
from datetime import datetime
from models.User import handle_user_request, handle_list_users_request
from models.Similiarity import handle_detect_request
from models.Tokens import handle_refill_request

def checkPostedData(collection,body, functionName):
  if 'username' not in body or 'password' not in body:
    error = {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 401
    }
    return error
  if functionName == 'register':
    usr = body["username"]
    pwd = body["password"].encode('utf-8')
    hash_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt())
    have_same_data = collection.find_one({'Username': usr})
    return handle_user_request(have_same_data,usr,hash_pwd)
  # checa se é a função de detectar o plágio
  elif functionName == 'detect':
    usr = body["username"]
    pwd = body["password"]
    text1 = body["text1"]
    text2 = body["text2"]
    pwd_exists = collection.find_one({'Username': usr})["Password"]
    return handle_detect_request(pwd_exists,usr,text1,text2)
  elif functionName == 'get-users':
    usr = body["username"]
    pwd_exists = collection.find_one({'Username': usr})["Password"]
    # se existe um password pra aquele user, é pq ele existe
    return handle_list_users_request(pwd_exists,usr)
  elif functionName == 'refill':
    usr = body["username"]
    target=body["target"]
    pwd = body["password"]
    tokens = body["tokens"]
    pwd_exists = collection.find_one({'Username': usr})["Password"]
    return handle_refill_request(pwd_exists, usr, target, tokens)


'''
# Tenta checar se a request tá certa
# se não der, retorna bad request
'''
def handleRequest(collection,body, routeName):
    print(collection,body,routeName)
    try:  
      res = checkPostedData(collection,body, routeName)
      return res
    except Exception as e:
      error = Response("Error!  " + str(e),status=400)
      return error