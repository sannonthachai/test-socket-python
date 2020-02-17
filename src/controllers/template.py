from src.services.template import TemplateService
from flask import request
from flask_restful import Resource, reqparse

class TemplateReadAllController(Resource):

    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def get(self):
        response = self.template_service.read_all()
        return response

class TemplateReadByIDController(Resource):
    
    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def get(self):
        id = request.args.get('id')
        response = self.template_service.read_all(id)
        return response

class TemplateCreateController(Resource):
    
    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('string', type=str, help='string template')
        parser.add_argument('object_id', type=int, help='object_id template')

        response = self.template_service.create(parser.parse_args())

        return response