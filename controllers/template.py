from services.template import TemplateService
from flask import request
from flask_restful import Resource

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
        response = self.template_service.read_by_id(id)

        return response

class TemplateCreateController(Resource):
    
    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def post(self):
        response = self.template_service.create(request.json)

        return response
        