from django.contrib import admin
from .models import Article, Category, Comment, Message, Like

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)

# Register your models here.
