
from flask import Flask, request, jsonify, session, make_response
from flask_restful import Resource, Api,HTTPException
from my_app.models import User
from my_app.schemas import UserSchema
from marshmallow import EXCLUDE
from my_app import db, app
api = Api(app)


class AddUserResource(Resource):
    """API to add user"""
    def post(self):
        json_data =  request.get_json(force=True)
        user_schema = UserSchema.UserSchema()
        if not  json_data:
            return {' Message': 'No input data provided'}, 400
        data = user_schema.load(json_data)
        
api.add_resource(AddUserResource, '/signup', methods=['POST'])