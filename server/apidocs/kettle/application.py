from .router import Router
from .request import Request
from .response import Response


class Application:
    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        view, actions = self.router.search(environ.get('REQUEST_METHOD'), environ.get('PATH_INFO', '/'))

        if view is None:
            response = Response().text('404 not found', 404)
        else:
            response = view(Request(environ, actions), Response())

        if not ('Access-Control-Allow-Origin', '*') in response.headers:
            response.headers.append(('Access-Control-Allow-Origin', '*'),)
            response.headers.append(('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept'),)
            response.headers.append(("Access-Control-Allow-Methods", "*"),)
            response.headers.append(("Access-Control-Allow-Credentials", "true"),)
        if environ.get('REQUEST_METHOD') == 'OPTIONS':
            start_response("204 No Content", response.headers)
            return []
        start_response(response.status, response.headers)
        return [response.body]
