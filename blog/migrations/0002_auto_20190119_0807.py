# Generated by Django 2.1.5 on 2019-01-19 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=2, verbose_name='性别')),
                ('tel', models.CharField(default='', max_length=16, verbose_name='电话')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='context',
            field=models.TextField(null=True, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=40, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='author',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Article'),
        ),
    ]
