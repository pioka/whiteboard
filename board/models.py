from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'owner'))


class BoardShare(models.Model):
    source = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='source')
    destination = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='destination')


class Tag(models.Model):
    COLORS = (
        ('primary', 'Primary'),
        ('success', 'Success'),
        ('danger', 'Danger'),
        ('warning', 'Warning'),
        ('info', 'Info'),
        ('secondary', 'Secondary'))

    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16, choices=COLORS)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_archived = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.subject
