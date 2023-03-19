from mongoengine import Document
from mongoengine.fields import StringField, ListField, ReferenceField


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, reverse_delete_rule='CASCADE')
    quote = StringField()

