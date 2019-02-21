from marshmallow import Schema, fields, post_load, ValidationError
from my_app.models.User import User

def validate_name(info):
    if  len(info) < 3 :
        raise ValidationError('Invalid length of info')


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True, validate=validate_name)
    surname = fields.Str(required=True, validate=validate_name)
    firstname = fields.Str(required=True, validate=validate_name)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate_name)
    profile_picture = fields.Str()
    user_type = fields.Str(required=True)

    @post_load
    def make_user(self, data):
        return User(**data)