from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pub_date = models.DateField()
    uuid = models.CharField(max_length=30)
    pub_name = models.CharField(max_length=30)
    file_name = models.CharField(max_length=30)
    file_url = models.CharField(max_length=200)
    def __str__(self):
        return self.title
