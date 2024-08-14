from flask import Flask
from app.controllers.user_controller import UserController


def create_app():
    app = Flask(__name__)

    user_controller = UserController()

    @app.route('/users', methods=['POST'])
    def create_user():
        return user_controller.create_user()
    
    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        return user_controller.get_user(user_id)
    
    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        return user_controller.update_user(user_id)
    
    @app.route("/users/<int:user_id>", methods=['DELETE'])
    def delete_user(user_id):
        return user_controller.delete_user(user_id)
    
    return app