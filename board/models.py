from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    archived = models.BooleanField()

    def __str__(self):
        return self.title
