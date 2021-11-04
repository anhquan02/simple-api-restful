from .user import UserApi,UsersApi

def initialize_routes(api):
    api.add_resource(UsersApi,'/api/user')
    api.add_resource(UserApi,'/api/user/<id>')