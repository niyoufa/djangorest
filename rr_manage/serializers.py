# -*- coding: utf-8 -*-
from rest_framework import serializers
from rr_user.models import User
from rr_manage.models import (
                            Area, Version, Legalservice, Certificate, Ordertype, Reporttype, 
                            Skilledfield, Comments, Park, Bank, Indexpic, Tags
                            )

 
class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        exclude = ()
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        exclude = ('type',)
    
    
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name')
    
        
        
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skilledfield
        fields = ('id', 'business')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','userid', 'createtime', 'description')        
############################################################################################################
class ParkmapSerializer(serializers.ModelSerializer):
    title=serializers.ReadOnlyField(source='park_name')
    type=serializers.SerializerMethodField()
    def get_type(self,obj):
        obj=u'园区'
        return obj 
    class Meta:
        model = Park
        fields = ('type', 'id', 'longitude','latitude','title','icon','content')

class UsermapSerializer(serializers.ModelSerializer):
    title=serializers.ReadOnlyField(source='name')
    id=serializers.ReadOnlyField(source='user.id')
    position=serializers.ReadOnlyField(source='certificate.name')
    type=serializers.SerializerMethodField()
    def get_type(self,obj):
        obj=u'财税师'
        return obj
    class Meta:
        model = User
        fields = ('type', 'id', 'longitude','latitude','title','icon','content','position','user_star','workage')
############################################################################################################
class VersionSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    def get_url(self,obj):
        obj='https://www.baidu.com'
        return obj
    class Meta:
        model = Version
        exclude = ()

############################################################################################################
class OrdertypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordertype
        fields = ('id', 'name','description')
############################################################################################################
############################################################################################################
class IndexpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexpic
        exclude = ()
############################################################################################################
############################################################################################################
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id','bank','branch')