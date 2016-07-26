# -*- coding: utf-8 -*-

from django.db import models

class Picture(models.Model): 
    user = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    image = models.CharField(null=True,max_length=500)
        
class Article(models.Model): 
    user = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)
    content = models.TextField(blank=True, null=True)
    
class Article_images(models.Model): 
    articleid = models.IntegerField(db_column='articleId', blank=True, null=True)  # Field name made lowercase.
    pictureid = models.IntegerField(db_column='pictureId', blank=True, null=True)
        
class Comments(models.Model):
    user = models.IntegerField(db_column='userId', blank=True, null=True)
    article = models.IntegerField(db_column='articleId', blank=True, null=True)
    comments = models.IntegerField(db_column='commentsId', blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)
    content = models.TextField(blank=True, null=True)
        
class Complaints(models.Model):
    user = models.IntegerField(db_column='userId', blank=True, null=True)
    article = models.IntegerField(db_column='articleId', blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)
    content = models.TextField(blank=True, null=True, verbose_name='举报内容')
    isread = models.CharField(default='0',max_length=10, verbose_name='是否已处理')
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)
 