# Generated by Django 4.2 on 2024-05-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=90, verbose_name='Заголовок'),
        ),
    ]
