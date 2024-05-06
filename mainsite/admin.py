from django.contrib import admin
from .models import Lesson, Category, Comment, UserAvatar, Course

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(UserAvatar)
admin.site.register(Course)