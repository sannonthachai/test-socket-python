from repositories.template import TemplateRepository
from bson import ObjectId
from json import loads
from setting import MONGODB_GRID_FS_BOT_IMG

class TemplateService: 
    
    def __init__(self, template_repository: TemplateRepository):
        self.template_repository = TemplateRepository

    def read_all(self):
        all_template = self.template_repository.find_all()
        return all_template

    def read_by_id(self, id):
        template = self.template_repository.find_by_id(id)
        return template

    def create(self, body):
        new_domain = self.template_repository.new_domain()
        new_domain.object_id = ObjectId(body['object_id'])
        new_domain.string = body['string']
        new_domain.save()

        return {
            "_id": str(new_domain.id),
            "object_id": ObjectId(body['object_id']),
            "string": body['string']
        }