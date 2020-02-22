from repositories.template import TemplateRepository
from models.response.template import TemplateModelResponse
from models.request.template import TemplateModelRequest
import json
# from setting import MONGODB_GRID_FS_BOT_IMG

class TemplateService: 
    
    def __init__(self, template_repository: TemplateRepository):
        self.template_repository = template_repository

    def read_all(self):
        model_adapter = TemplateModelResponse()
        
        all_template = self.template_repository.find_all()
        list_all_template = json.loads(all_template)
        
        all_template_adapter = model_adapter.modelAdapter(list_all_template)

        return all_template_adapter

    def read_by_id(self, id):
        model_adapter = TemplateModelResponse()

        template_by_id = self.template_repository.find_by_id(id)
        list_template_by_id = json.loads(template_by_id)

        template_by_id_adapter = model_adapter.modelAdapter(list_template_by_id)

        return template_by_id_adapter

    def create(self, body):
        model_adapter = TemplateModelRequest(body)

        new_domain = self.template_repository.new_domain()
        new_domain.object_id = model_adapter.object_id
        new_domain.string = model_adapter.string
        new_domain.save()

        return "OK"