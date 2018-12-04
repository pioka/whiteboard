from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User , through='Membership', related_name='members')

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Tag(models.Model):
    COLORS = (
        ('PR', 'Primary'),
        ('SU', 'Success'),
        ('DA', 'Danger'),
        ('WA', 'Warning'),
        ('IN', 'Info'),
        ('SE', 'Secondary'))

    name = models.CharField(max_length=16)
    color = models.CharField(max_length=2, choices=COLORS)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_archived = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.subject
