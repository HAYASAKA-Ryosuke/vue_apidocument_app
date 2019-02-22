import peewee
from .models import ApiDoc
from playhouse.shortcuts import model_to_dict
import json

def get_list(request):
    api_doc = [model_to_dict(api_doc) for api_doc in ApiDoc.select()]
    return api_doc


def create_apidoc(request):
    data = json.loads(request.data)
    api_doc = ApiDoc.create(title=data.get('title'), url=data.get('url'), method=data.get('method'), description=data.get('description', ''))
    return model_to_dict(api_doc)
