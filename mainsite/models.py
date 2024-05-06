from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     is_teacher = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.username



class UserAvatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="blog_user_info")
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='photos'
    )

    def __str__(self):
        return f'{self.user} avatar'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Course(models.Model):
    title = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", null=True)
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=None)
    name = models.CharField(max_length=30, verbose_name="Комментарій")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата", default=None)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коментарій"
        verbose_name_plural = "Коментарі"
