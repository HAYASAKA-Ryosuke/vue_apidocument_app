from .controller import get_list, create_apidoc
import json

def list(request, response):
    result = get_list(request)
    return response.json(json.dumps(dict(apidocs=result)))


def create_webapi(request, response):
    result = create_apidoc(request)
    return response.json(json.dumps(dict(apidoc=result)))

def edit_webapi(request, response):
    print(request.actions)
    return response.text('ham egg spam')


def delete_webapi(request, response):
    print(request.actions)
    return response.text('ham egg spam')
