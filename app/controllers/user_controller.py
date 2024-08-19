from json import dumps

from flask import request, jsonify, Response
from app.services.user_service import UserService


class UserController:
    def __init__(self) -> None:
        self._user_service = UserService()

    def create_user(self) -> Response:
        data = request.get_json()
        user = self._user_service.create_user(
            name=data['name'],
            email=data['email']
        )

        return self.make_response(user.to_dict(), 201)
    
    def get_user(self, user_id) -> Response:
        user = self._user_service.get_user(user_id)
        if user:
            return self.make_response(user.to_dict(), 200)
        
        return self.make_response({"message": "User not found"}, 404)
    
    def update_user(self, user_id: int) -> Response:
        data = request.get_json()
        user = self._user_service.update_user(user_id, data['name'], data['email'])
        if user:
            return self.make_response(user.to_dict(), 200)
        
        return self.make_response({"message": "User not found"}, 404)
    
    def delete_user(self, user_id: int) -> Response:
        success = self._user_service.delete_user(user_id)
        if success:
            return self.make_response({"message": "User deleted"}, 200)
        
        return self.make_response({"message": "User not found"}, 404)
    

    def make_response(self, data, status_code) -> Response:
        return Response(dumps(data), status_code)
