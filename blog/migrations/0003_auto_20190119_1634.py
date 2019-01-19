# Generated by Django 2.1.5 on 2019-01-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190119_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='article',
        ),
        migrations.AddField(
            model_name='author',
            name='article',
            field=models.ManyToManyField(to='blog.Article'),
        ),
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], max_length=4, verbose_name='性别'),
        ),
    ]
