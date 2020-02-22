from domains.template import TemplateDomain
from bson import ObjectId

class TemplateRepository:

    def __init__(self, template_domain: TemplateDomain):
        self.template_domain = template_domain
        
    def new_domain(self) -> TemplateDomain:
        return self.template_domain()

    def find_by_id(self, ID):
        return self.template_domain.objects( object_id=ID ).to_json()

    def find_all(self):
        return self.template_domain.objects().to_json()
    
    
    