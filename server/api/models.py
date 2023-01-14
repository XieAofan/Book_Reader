from django.db import models

class User(models.Model):
    usrename = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    bookshelf = models.JSONField()

class Site(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    site_strategy = models.JSONField()

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_id = models.AutoField(primary_key=True)
    source =  models.JSONField()
    current_source = models.JSONField()

class Source():
    def __init__(self) -> None:
        self.name = ''
        self.url = ''
        self.id = None
