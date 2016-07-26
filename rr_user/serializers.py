# -*- coding: utf-8 -*-
from rest_framework import serializers
from rr_user.models import User, UserCompany, Financeuser, Expressadd, Workexperience, Price
from business.models import Order, Withdrawal, Review
from rr_manage.models import Certificate
from others.models import CompanyUser
from django.db.models import Sum, Min
from django.db.models import Q
from django.utils import timezone
from map.getdistance import *

class UserSerializer(serializers.ModelSerializer):
    icon = serializers.ReadOnlyField(source='get_icon')
    class Meta:
        model = User
        exclude = ('password','last_login','username','type','createTime','createBy','modifyBy','iconPath')
        

class CompanySerializer(serializers.ModelSerializer):
    candelete = serializers.SerializerMethodField()
    revenueArea = serializers.SerializerMethodField()
    cp_name = serializers.ReadOnlyField(source="companyname")
    def get_candelete(self,instance):
        a=Order.objects.filter(companyid=instance.id).count()
        if a==0:
            return True
        return False
    def get_revenueArea(self,instance):
        try:
            return CompanyUser.objects.get(id=instance.id).revenueArea
        except:
            return None
    class Meta:
        model = UserCompany
        exclude = ()

class FinanceuserSerializer(serializers.ModelSerializer):
    servicenum = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    sex = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    certificatename = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    idcardimg = serializers.SerializerMethodField()
    idcardimg_opp = serializers.SerializerMethodField()
    accountantimg = serializers.SerializerMethodField()
    accountantimg_opp = serializers.SerializerMethodField()
    certificateimg = serializers.SerializerMethodField()
    certificateimg_opp = serializers.SerializerMethodField()
    workexperience = serializers.SerializerMethodField()
    def get_workexperience(self,instance):
        try:
            workexperience=Workexperience.objects.filter(userid=instance.id)
            serializers=WorkexperienceSerializer(workexperience, many=True, read_only=True)
            return serializers.data
        except Workexperience.DoesNotExist:
            return None
    def get_distance(self,instance):
        request = self.context.get('request')
        if request.GET.get('lat') and request.GET.get('lng'):
            p1 = Point()
            p1.lat = float(request.GET.get('lat').encode("utf-8"))
            p1.lng = float(request.GET.get('lng').encode("utf-8"))
            p2 = Point()
            try:
                p2.lat = float(User.objects.get(id=instance.id).latitude)
                p2.lng = float(User.objects.get(id=instance.id).longitude)
            except:
                p2.lat = p1.lat
                p2.lng = p1.lng
            return getDistance(p1, p2)
        return None
    def get_servicenum(self,instance):
        serviceno = Order.objects.filter(servicesproviderid=instance.id,order_status__in=['2','3']).count()
        return serviceno
    def get_certificatename(self,instance):
        if instance.certificateid:
            return Certificate.objects.get(id=instance.certificateid).name
        return None
    def get_icon(self,instance):
        return User.objects.get(id=instance.id).get_icon()
    def get_name(self,instance):
        return User.objects.get(id=instance.id).name
    def get_sex(self,instance):
        return User.objects.get(id=instance.id).sex
    def get_email(self,instance):
        return User.objects.get(id=instance.id).email
    def get_rate(self,instance):
        a = Review.objects.filter(servicesproviderid=instance.id,type='0').count()*100
        b=Review.objects.filter(servicesproviderid=instance.id).count()
        if b==0:
            return 100        
        return 100-a/b
    def get_price(self,instance):
        request = self.context.get('request')
        instance = Price.objects.filter(userid=instance.id)
        if request.GET.get('ordertype'):
            instance = instance.filter(ordertypeid=request.GET['ordertype'])
        if len(instance)==0:
            price = 300
        else:
            price = instance.aggregate(Min('price')).values()[0]
        return price
    def get_idcardimg(self,instance):
        path = instance.idcardimgpath.split(',') if instance.idcardimgpath else []
        for i in range(len(path)):
            if 'idcardimg.' in path[i]:
                return path[i]                    
        return None
    def get_idcardimg_opp(self,instance):
        path = instance.idcardimgpath.split(',') if instance.idcardimgpath else []
        for i in range(len(path)):
            if 'idcardimg_opp.' in path[i]:
                return path[i]                    
        return None
    def get_accountantimg(self,instance):
        path = instance.accountantimgpath.split(',') if instance.accountantimgpath else []
        for i in range(len(path)):
            if 'accountantimg.' in path[i]:
                return path[i]                    
        return None
    def get_accountantimg_opp(self,instance):
        path = instance.accountantimgpath.split(',') if instance.accountantimgpath else []
        for i in range(len(path)):
            if 'accountantimg_opp.' in path[i]:
                return path[i]                    
        return None
    def get_certificateimg(self,instance):
        path = instance.certificateimgpath.split(',') if instance.certificateimgpath else []
        for i in range(len(path)):
            if 'certificateimg.' in path[i]:
                return path[i]                    
        return None
    def get_certificateimg_opp(self,instance):
        path = instance.certificateimgpath.split(',') if instance.certificateimgpath else []
        for i in range(len(path)):
            if 'certificateimg_opp.' in path[i]:
                return path[i]                    
        return None
    class Meta:
        model = Financeuser
        exclude = ('idcardimgpath','accountantimgpath','certificateimgpath')
        
class UserWithdrawalSerializer(serializers.ModelSerializer):
    remaintime = serializers.SerializerMethodField()
    money = serializers.SerializerMethodField()
    def get_remaintime(self,instance):
        start = timezone.now().date()
        end = start + timezone.timedelta(days=1)
        withdrawalnum = Withdrawal.objects.filter(userid=instance.id\
                        ,createtime__range=(start.strftime("%Y-%m-%d %H:%M:%S"), end.strftime("%Y-%m-%d %H:%M:%S"))).count()
        return 3-withdrawalnum
    def get_money(self,instance):
        amountsum = Order.objects.filter(servicesproviderid=instance.id,order_status__in=['2','3']).aggregate(Sum('order_amount')).values()[0] or 0
        withdrawalsum = Withdrawal.objects.filter(userid=instance.id).exclude(status='4').aggregate(Sum('amount')).values()[0] or 0
        return amountsum-withdrawalsum
    class Meta:
        model = User
        fields = ('money','remaintime')


class ServiceOrderSerializer(serializers.ModelSerializer):
#     amount = serializers.SerializerMethodField()
#     def get_amount(self,instance):
#         amountsum = getattr(instance, "amount"\
#                     ,Order.objects.filter(servicesproviderid=instance.servicesproviderid,order_status__in=['2','3']).aggregate(Sum('order_amount')).values()[0])
#         return amountsum
    class Meta:
        model = Order
                
class ServiceReportSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    orderby = serializers.SerializerMethodField()
    servicenum = serializers.SerializerMethodField()
    service1 = serializers.SerializerMethodField()
    service2 = serializers.SerializerMethodField()
    service3 = serializers.SerializerMethodField()
    service4 = serializers.SerializerMethodField()
    service5 = serializers.SerializerMethodField()
    service6 = serializers.SerializerMethodField()
    service7 = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    def datetime(self):
        return timezone.now().replace(day=1,hour=0,minute=0,second=0,microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
    def get_amount(self,instance):
        amountsum = Order.objects.filter(servicesproviderid=instance.id,order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return amountsum.values()[0]
    def previous_amount(self,instance):        
        amountsum = Order.objects.filter(servicesproviderid=instance.id,order_status__in=['2','3'],order_createtime__lt=self.datetime).aggregate(Sum('order_amount'))
        return amountsum.values()[0]
    def get_orderby(self,instance):
        amountsum = Order.objects.filter(order_status__in=['2','3']).values('servicesproviderid').annotate(amount=Sum('order_amount')).order_by('-amount')
        for i in range(len(amountsum)):
            if amountsum[i]['servicesproviderid']==instance.id:
                return i+1
                break
            return None
    def previous_orderby(self,instance):
        amountsum = Order.objects.filter(order_status__in=['2','3'],order_createtime__lt=self.datetime).values('servicesproviderid').annotate(amount=Sum('order_amount')).order_by('-amount')
        for i in range(len(amountsum)):
            if amountsum[i]['servicesproviderid']==instance.id:
                return i+1
                break
            return None
    def get_progress(self,instance):
        try:
            progress = self.previous_orderby(instance)-self.get_orderby(instance)
            return progress
        except:
            return None
    def get_servicenum(self,instance):
        serviceno = Order.objects.filter(servicesproviderid=instance.id,order_status__in=['2','3']).count()
        return serviceno
    def get_service1(self,instance):
        service1 = Order.objects.filter(servicesproviderid=instance.id,order_type='1',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service1.values()[0]
    def get_service2(self,instance):
        service2 = Order.objects.filter(servicesproviderid=instance.id,order_type='2',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service2.values()[0]
    def get_service3(self,instance):
        service3 = Order.objects.filter(servicesproviderid=instance.id,order_type='3',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service3.values()[0]
    def get_service4(self,instance):
        service4 = Order.objects.filter(servicesproviderid=instance.id,order_type='4',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service4.values()[0]
    def get_service5(self,instance):
        service5 = Order.objects.filter(servicesproviderid=instance.id,order_type='5',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service5.values()[0]
    def get_service6(self,instance):
        service6 = Order.objects.filter(servicesproviderid=instance.id,order_type='6',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service6.values()[0]
    def get_service7(self,instance):        
        service7 = Order.objects.filter(servicesproviderid=instance.id,order_type='7',order_status__in=['2','3']).aggregate(Sum('order_amount'))
        return service7.values()[0]
    class Meta:
        model = User
        fields = ('id','name','amount', 'orderby', 'progress', 'servicenum', 'service1', 'service2', 'service3', 'service4', 'service5', 'service6', 'service7')  
        
class OrderstatusSerializer(serializers.ModelSerializer):
    ordercount = serializers.SerializerMethodField()
    orderstatus0 = serializers.SerializerMethodField()
    orderstatus2 = serializers.SerializerMethodField()
    orderstatus3 = serializers.SerializerMethodField()
    orderstatus4 = serializers.SerializerMethodField()
    def get_ordercount(self,instance):
            return Order.objects.filter(Q(user=instance.user) | Q(services_provider=instance.user)).count()
    def get_orderstatus0(self,instance):
            return Order.objects.filter(Q(user=instance.user) | Q(services_provider=instance.user), order_status='0').count()            
    def get_orderstatus2(self,instance):
            return Order.objects.filter(Q(user=instance.user) | Q(services_provider=instance.user), order_status='2').count()
    def get_orderstatus3(self,instance):
            return Order.objects.filter(Q(user=instance.user) | Q(services_provider=instance.user), order_status='3').count()
    def get_orderstatus4(self,instance):
            return Order.objects.filter(Q(user=instance.user) | Q(services_provider=instance.user), order_status='4').count()
    class Meta:
        model = User
        fields = ('ordercount','orderstatus0', 'orderstatus2', 'orderstatus3', 'orderstatus4')
        
class ExpressaddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expressadd
        exclude = ()
        
class WorkexperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexperience
        exclude = ()