from django.contrib import admin

from .models import Janr, Book, Comment

admin.site.register([Janr, Book, Comment])