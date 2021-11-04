from flask import request, Response
from database.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, UpdatingUserError, InternalServerError, DeletingUserError,UserNotExistsError,EmailAlreadyExistsError
class UsersApi(Resource):

    def get(self):
        query = User.objects()
        users = User.objects().to_json()        
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            print(body)
            user = User(**body)
            user.save()
            id = user.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError    
    


class UserApi(Resource):    
    def put(self,id):
        try:
            body = request.get_json()
            User.objects.get(id=id).update(**body)
            return '',200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserError
        except Exception:
            raise InternalServerError 
    def delete(self,id):
        try:
            user = User.objects.get(id=id).delete()            
            return '',200
        except DoesNotExist:
            raise DeletingUserError
        except Exception:
            raise InternalServerError 

    def get(self, id):
        try:
            user = User.objects.get(id=id).to_json()
            return Response(user, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError    
