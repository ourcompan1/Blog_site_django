from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def new_comment(self, data):
        comment = Comment()
        comment.author = data['name']
        comment.email = data['email']
        comment.message = data['message']
        comment.article = self
        comment.date = datetime.now().date()
        comment.save()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField()
