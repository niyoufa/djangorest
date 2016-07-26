# -*- coding: utf-8 -*-
from rest_framework import serializers
from others.models import News
from rr_user.models import User

class NewsSerializer(serializers.ModelSerializer):
    user1name = serializers.SerializerMethodField()
    user1sex = serializers.SerializerMethodField()
    user1mobile = serializers.SerializerMethodField()
    user1icon = serializers.SerializerMethodField()
    user2name = serializers.SerializerMethodField()
    user2sex = serializers.SerializerMethodField()
    user2mobile = serializers.SerializerMethodField()
    user2icon = serializers.SerializerMethodField()
    noreadnum = serializers.SerializerMethodField()
    def get_user1name(self,instance):
        try:
            return User.objects.get(id=instance.user1).get_short_name()
        except User.DoesNotExist:
            return None
    def get_user1sex(self,instance):
        try:
            return User.objects.get(id=instance.user1).sex
        except User.DoesNotExist:
            return None
    def get_user1mobile(self,instance):
        try:
            return User.objects.get(id=instance.user1).phone
        except User.DoesNotExist:
            return None
    def get_user1icon(self,instance):
        try:
            return User.objects.get(id=instance.user1).get_icon()
        except User.DoesNotExist:
            return 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/man.png'
    def get_user2name(self,instance):
        try:
            return User.objects.get(id=instance.user2).get_short_name()
        except User.DoesNotExist:
            return None
    def get_user2sex(self,instance):
        try:
            return User.objects.get(id=instance.user2).sex
        except User.DoesNotExist:
            return None
    def get_user2mobile(self,instance):
        try:
            return User.objects.get(id=instance.user2).phone
        except User.DoesNotExist:
            return None
    def get_user2icon(self,instance):
        try:
            return User.objects.get(id=instance.user2).get_icon()
        except User.DoesNotExist:
            return 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/man.png'
    def get_noreadnum(self,instance):
        try:
            user2 = self.context.get('request').GET.get('pk')
            if instance.user2==user2:
                user1=instance.user1
            else:
                user1=instance.user2
            return News.objects.filter(user2=user2,user1=user1).exclude(isread='1').count()
        except:
            return None
    
    class Meta:
        model = News
        exclude = ()
        