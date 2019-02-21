import peewee

db = peewee.SqliteDatabase('./apidocs/api_doc.db')


class ApiDoc(peewee.Model):
    title = peewee.CharField(default='')
    url = peewee.CharField()
    method = peewee.CharField()
    description = peewee.CharField(default='')

    class Meta:
        database = db
