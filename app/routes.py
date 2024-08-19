from flask import Flask, g
from app.controllers.user_controller import UserController
from app.repositories.db_connection import DbConnection


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
    
    @app.before_request
    def open_db_connection():
        g.db = DbConnection().connect()

    @app.teardown_appcontext
    def close_db_connection(response):
        if g.db is not None:
            DbConnection().disconnect()
    
    return app