from django.contrib import admin
from .models import Category, Ebook, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Comment)