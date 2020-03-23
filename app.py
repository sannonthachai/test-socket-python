from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from database.mongoengine import MongoEngine
from flask_socketio import SocketIO
from exceptions.http_exception import errors
import setting

##################### Domains #################
from domains.template import TemplateDomain

##################### Repositories #################
from repositories.template import TemplateRepository

##################### Services #####################
from services.template import TemplateService

##################### Controller #####################
from controllers.template import TemplateReadAllController, TemplateReadByIDController, TemplateCreateController

app = Flask(__name__)
CORS(app)
api = Api(app, errors=errors)

mongoengine = MongoEngine(setting.MONGODB_NAME , setting.MONGODB_URI)
pmongoengine_conn = mongoengine.connector()

###################### Test ########################
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

##################### Repositories #################
template_repo = TemplateRepository(TemplateDomain)


##################### Services #####################
template_service = TemplateService(template_repo)


##################### End Point ####################
api.add_resource(HelloWorld, '/')
api.add_resource(TemplateReadAllController, '/get_all', resource_class_kwargs={'template_service': template_service})
api.add_resource(TemplateReadByIDController, '/get_by', resource_class_kwargs={'template_service': template_service})
api.add_resource(TemplateCreateController, '/save', resource_class_kwargs={'template_service': template_service})


if __name__ == '__main__':
    app.run(port=5000,  host='0.0.0.0')