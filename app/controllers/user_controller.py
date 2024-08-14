from flask import request, jsonify
from app.services.user_service import UserService


class UserController:
    def __init__(self):
        self._user_service = UserService()

    def create_user(self):
        data = request.get_json()
        user = self._user_service.create_user(
            name=data['name'],
            email=data['email']
        )

        return jsonify(user.to_dict()), 201
    
    def get_user(self, user_id):
        user = self._user_service.get_user(user_id)
        if user:
            return jsonify(user.to_dict()), 200
        
        return jsonify({"message": "User not found"}), 404
    
    def update_user(self, user_id: int):
        data = request.get_json()
        user = self._user_service.update_user(user_id, data['name'], data['email'])
        if user:
            return jsonify(user.to_dict()), 200
        
        return jsonify({"message": "User not found"}), 404
    
    def delete_user(self, user_id: int):
        success = self._user_service.delete_user(user_id)
        if success:
            return jsonify({"message": "User deleted"}), 200
        
        return jsonify({"message": "User not found"}), 404
