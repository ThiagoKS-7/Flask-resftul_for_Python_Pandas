from models.Similiarity import Detect
from models.Tokens import Refill
from models.User import GetUsers, Register

def get_resources(api):
    api.add_resource(Register, '/register')
    api.add_resource(Detect, '/detect')
    api.add_resource(GetUsers, '/get-users')
    api.add_resource(Refill, '/refill')



