class TemplateModelResponse:
    
    def newFormat(self, item):
        return {
            'string': item['string'],
            'object_id': item['object_id']
        }

    def modelAdapter(self, item):
        return list(map(self.newFormat, item))