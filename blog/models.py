from django.db import models
from django.utils.timezone import now


# class BaseModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_time = models.DateTimeField('创建时间', default=now)
#     last_mod_time = models.DateTimeField('修改时间', default=now)
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None):
#         return

class User(models.Model):
    nick_name = models.CharField('姓名', max_length=16)
    email = models.EmailField('邮箱')
    password = models.CharField('密码', max_length=200)


class Author(models.Model):
    # article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, default=1)
    name = models.CharField('姓名', max_length=16)
    sex = models.CharField('性别', max_length=8, choices=[('male', '男'), ('female', '女')])
    tel = models.CharField('电话', max_length=16, default='')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=40, default='')
    # 正文
    context = models.TextField('正文', null=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='作者', null=True, blank=True)
    pub_date = models.DateTimeField('发布时间', blank=True, null=True, default=now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, verbose_name='文章')
    comment = models.TextField('评论', null=True)
    comment_date = models.DateTimeField('评论时间', blank=True, null=True)
