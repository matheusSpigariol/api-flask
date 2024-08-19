from marshmallow import fields, post_load, validate
from marshmallow.validate import Email

from app.schemas.base_schema import BaseSchema
from app.schemas.make_request_dto import make_request_dto

class RequestSchema(BaseSchema):
    name = fields.Str(required=True, validate=validate.Length(min = 1))
    email = fields.Email(required=True, validate=Email())

    @post_load
    def make_request_dto(self, data, **kwargs):
        return make_request_dto(data, **kwargs)
