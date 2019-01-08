from django.contrib import admin

from .models import Board
from .models import Article


# Register your models here.
admin.site.register(Board)
admin.site.register(Article)
