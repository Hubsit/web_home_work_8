import json

from models import Author, Quote
import connect


with open('json/authors.json') as file:
    authors = json.load(file)
    for author in authors:
        Author(**author).save()

with open('json/quotes.json') as file:
    quotes = json.load(file)
    for quote in quotes:
        author = Author.objects(fullname=quote.pop('author')).first()
        Quote(author=author, **quote).save()