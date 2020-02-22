from mongoengine import StringField, Document, DateTimeField, ObjectIdField, FileField
from datetime import datetime

class TemplateDomain(Document):
    
    object_id = StringField(max_length=200, required=True)
    string = StringField(max_length=200, required=True, unique=True)
    date = DateTimeField(default=datetime.utcnow)