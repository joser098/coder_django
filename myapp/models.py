from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Autores(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    posts = models.CharField(max_length=5)

    def __str__(self):
        return self.name    
