# -=- coding: utf-8 -=-
from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'
        ordering = ['-article_date']
    article_title = models.CharField(max_length=250)
    article_description = models.TextField()
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
         return self.article_title



class Comments(models.Model):
    class Meta:
        db_table = 'comments'
    comments_text = models.TextField(verbose_name='Текст комментария:')
    comments_article = models.ForeignKey(Article)

