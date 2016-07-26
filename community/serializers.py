# -*- coding: utf-8 -*-
from rest_framework import serializers
from community.models import Article, Comments, Complaints, Article_images, Picture
from rr_user.models import User
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image',)
    
class CommentsSerializer(serializers.ModelSerializer):
    commentsuser = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    def get_commentsuser(self,instance):
        try:
            commentsuser=Comments.objects.get(id=instance.comments).user
            return User.objects.get(id=commentsuser).name
        except :
            return None
    def get_username(self,instance):
        try:
            return User.objects.get(id=instance.user).get_short_name()
        except User.DoesNotExist:
            return None
    class Meta:
        model = Comments
        exclude = ()       
         
class ArticleSerializer(serializers.ModelSerializer):
    commentsarticle = serializers.SerializerMethodField()
    imageURLs = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    usericon = serializers.SerializerMethodField()
    def get_commentsarticle(self,instance):
        commentsuser=Comments.objects.filter(article=instance.id)
        return CommentsSerializer(commentsuser,many=True,read_only=True).data
    def get_imageURLs(self,instance):
        images=Article_images.objects.filter(articleid=instance.id).values_list('pictureid', flat=True)
        return PictureSerializer(Picture.objects.filter(id__in=images),many=True,read_only=True).data
    def get_username(self,instance):
        try:
            return User.objects.get(id=instance.user).get_short_name()
        except User.DoesNotExist:
            return None
    def get_usericon(self,instance):
        try:
            return User.objects.get(id=instance.user).get_icon()
        except User.DoesNotExist:
            return 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/man.png'
    class Meta:
        model = Article
        exclude = ()
    
class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        exclude = ('modifyby','isread')  