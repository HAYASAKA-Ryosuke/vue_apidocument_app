from wsgiref import simple_server
from .kettle.application import Application
import peewee
from .models import ApiDoc
from .views import  list, create_webapi, edit_webapi, delete_webapi

db = peewee.SqliteDatabase('./apidocs/api_doc.db')

db.connect()
db.create_tables([ApiDoc])
application = Application()
application.router.register('GET', '/apidocs/', list)
application.router.register('POST', '/apidocs/', create_webapi)
application.router.register('PUT', '/apidocs/:api_id/', edit_webapi)
application.router.register('DELETE', '/apidocs/:api_id/', delete_webapi)


def run():
    httpd = simple_server.make_server('', 8000, application)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
