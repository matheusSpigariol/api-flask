from json import dumps

from flask import Response

from app.exception.custom_erros import UserNotFound
from app.responses import ResponseCodes
from app.services.user_service import UserService


class GetUser:

    def get(user_id):
        try:
            mimetype = 'application/json'

            response = UserService().get_user_infos(user_id)

            return Response(
                response=dumps(response),
                mimetype=mimetype,
                status=ResponseCodes.SUCCESS
            )
        
        except UserNotFound as exc:
            return Response(
                response=dumps(exc._message),
                mimetype=mimetype,
                status=exc._status
            )
