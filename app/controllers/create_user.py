from json import dumps

from flask import request, Response
from marshmallow import ValidationError

from app.responses import ResponseCodes
from app.schemas.request_schema import RequestSchema
from app.services.user_service import UserService


class CreateUser:

    def create():
        try:
            mimetype = 'application/json'

            request_body = request.get_json()
            
            request_data_serialized = RequestSchema().load(request_body)

            UserService().register_user(request_data_serialized)

            return Response(
                response=dumps({"message": "User created with success."}),
                mimetype=mimetype,
                status=ResponseCodes.CREATED
            )
        
        except ValidationError as err:
            return Response(
                response=dumps(err.messages),
                mimetype=mimetype,
                status=ResponseCodes.BAD_REQUEST
            )
