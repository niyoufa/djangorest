# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rr_user.models import User, UserCompany, Financeuser, Expressadd, Workexperience, Price, BCompany
from rest_framework.authtoken.models import Token
from rr_user.serializers import ( 
                        UserSerializer, CompanySerializer, ServiceReportSerializer, ServiceOrderSerializer, UserWithdrawalSerializer,
                        FinanceuserSerializer, ExpressaddSerializer, WorkexperienceSerializer, OrderstatusSerializer
                        )
from rest_framework import generics
from rest_framework import filters
from django.db.models import Q
from map import getlocation
from map.getdistance import *
from business.models import Order, Withdrawal
from business.serializers import WithdrawalSerializer
from others.models import CompanyUser
import datetime
from django.db.models import Sum, Min
from decimal import Decimal
from functools import reduce
from register import run


pttj={
        "id": 10779,
        "servicenum": 700,
        "rate": 100,
        "icon": 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/pttj_icon.png',
        "name": u"平台推荐",
        "sex": "2",
        "certificatename": u"--",
        "price": 300,
        "workage": "14",
        "distance": 0,
        "specialty": u"--"
        
    }
class Userexpressadd(generics.ListAPIView):
    def get_queryset(self):
        queryset = super(Userexpressadd, self).get_queryset()
        default_exadd=User.objects.get(id=self.kwargs.get('pk')).default_exadd
        return queryset.filter(userid=self.kwargs.get('pk')).exclude(id=default_exadd)
    queryset = Expressadd.objects.all()
    serializer_class = ExpressaddSerializer  
  
class ExpressaddList(generics.ListCreateAPIView):
    queryset = Expressadd.objects.all()
    serializer_class = ExpressaddSerializer
    def post(self, request, *args, **kwargs):
        if request.data.get('id'):
            instance = Expressadd.objects.get(pk=request.data.get('id'))
            serializer = ExpressaddSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return self.create(request, *args, **kwargs)
        
class ExpressaddDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expressadd.objects.all()
    serializer_class = ExpressaddSerializer  
#####################################################################
class Userworkexperience(generics.ListAPIView):
    def get_queryset(self):
        queryset = super(Userworkexperience, self).get_queryset()
        return queryset.filter(userid=self.kwargs.get('pk'))
    queryset = Workexperience.objects.all()
    serializer_class = WorkexperienceSerializer  
 
class WorkexperienceList(generics.CreateAPIView):
    queryset = Workexperience.objects.all()
    serializer_class = WorkexperienceSerializer
        
class WorkexperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workexperience.objects.all()
    serializer_class = WorkexperienceSerializer  
#####################################################################      
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FinanceuserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Financeuser.objects.all()
    serializer_class = FinanceuserSerializer
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        user=User.objects.get(id=instance.id)
        financeuser=Financeuser.objects.get(id=instance.id)
        address=request.data.get('address')
        city=request.data.get('city')
        if address is not None:
            try:
                location=getlocation(address,city)
                user.longitude=location['lng']
                user.latitude=location['lat']
            except : 
                pass 
        if request.data.get('name'):
            user.name=request.data.get('name')
        if request.data.get('email'):
            user.email=request.data.get('email')
        if request.data.get('sex'):
            user.sex=request.data.get('sex')
        for i in ['idcardimg','idcardimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.idcardimgpath.split(',') if financeuser.idcardimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.idcardimgpath = ','.join(path)
        for i in ['accountantimg','accountantimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.accountantimgpath.split(',') if financeuser.accountantimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.accountantimgpath = ','.join(path)
        for i in ['certificateimg','certificateimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.certificateimgpath.split(',') if financeuser.certificateimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.certificateimgpath = ','.join(path)
        user.save()
        financeuser.save()
        return self.update(request, *args, **kwargs)
        
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user=User.objects.get(id=instance.id)
        financeuser=Financeuser.objects.get(id=instance.id)
        address=request.data.get('address')
        city=request.data.get('city')
        if address is not None:
            try:
                location=getlocation(address,city)
                user.longitude=location['lng']
                user.latitude=location['lat']
            except :
                pass
        if request.data.get('name'):
            user.name=request.data.get('name')
        if request.data.get('email'):
            user.email=request.data.get('email')
        if request.data.get('sex'):
            user.sex=request.data.get('sex')
        for i in ['idcardimg','idcardimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.idcardimgpath.split(',') if financeuser.idcardimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.idcardimgpath = ','.join(path)
        for i in ['accountantimg','accountantimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.accountantimgpath.split(',') if financeuser.accountantimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.accountantimgpath = ','.join(path)
        for i in ['certificateimg','certificateimg_opp']:
            if request.data.get(i)=='':
                path = financeuser.certificateimgpath.split(',') if financeuser.certificateimgpath else []
                for j in path:
                    if '%s.'%i in j:
                        path.remove(j)
                financeuser.certificateimgpath = ','.join(path)
        user.save()
        financeuser.save()
        return self.partial_update(request, *args, **kwargs)
        
    
class UserSearch(generics.ListAPIView):
    serializer_class = FinanceuserSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id','city','area')
    ordering_fields = '__all__'
    def get_queryset(self):
        user = Financeuser.objects.filter(user_status='1',isacceptorder='1')\
                .exclude(certificateid__isnull=True).exclude(id=pttj['id'])\
                .distinct()
        city = self.request.query_params.get('city__startswith')
        name = self.request.query_params.get('name')
        if city:
            user = user.filter(city__startswith=city)
        if name:
            userlist=User.objects.filter(name__icontains=name).values_list('id',flat=True)
            user = user.filter(id__in=userlist)
        return user
        
    def get(self, request, format=None):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#         else:
        serializer = self.get_serializer(queryset, many=True)
        lis = serializer.data
        ordering=self.request.query_params.get('ordering', None)
        if not ordering or ordering=="distance":
            try:
                lis = sorted(serializer.data, key=lambda s: s['distance'])  
            except:
                pass
        elif ordering=="price":
            try:
                lis = sorted(serializer.data, key=lambda s: s['price'])  
            except:
                pass
        elif ordering=="rate":
            try:
                lis = sorted(serializer.data, key=lambda s: s['rate'], reverse=True)  
            except:
                pass
        elif ordering=="servicenum":
            try:
                lis = sorted(serializer.data, key=lambda s: s['servicenum'], reverse=True)  
            except:
                pass
#         lis.insert( 0, pttj)
        if request.GET.get('limit'):
            limit = int(request.GET['limit'])
            if request.GET.get('offset'):
                offset = int(request.GET['offset'])
            else:
                offset = 0
            return self.get_paginated_response(lis[offset:offset+limit])    
        return Response(lis)            
    
class UserKey(APIView):               
    def get(self, request, mobile, format=None):
        code=self.request.query_params.get('code', None)
        domain=self.request.query_params.get('domain', None)
        result={}
        try:
            user = User.objects.get(username=mobile)
        except User.DoesNotExist:
            result=u'手机号尚未注册'
        else:
            if code:
                phone=mobile[:-2]
                req =run.aliyun_checkcode(phone, code, domain)
                if req['open_sms_checkvercode_response']['result']['successful']:
                    result['result']={'successful': True, 'message': 'SUCCESS','userid':user.id}
                else:
                    result['result']=req['open_sms_checkvercode_response']['result']
            else:
                result['result']={'successful': False, 'message': u'手机号已注册'}
        return Response(result) 
##################################################################### 
class CompanyList(generics.ListCreateAPIView):
    queryset = UserCompany.objects.all()
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        queryset = super(CompanyList, self).get_queryset()
        cp_name = self.request.query_params.get('cp_name', None)
        if cp_name:
            queryset = queryset.filter(companyname__icontains=cp_name)
        return queryset.order_by('companyname')[:10]
    def post(self, request, *args, **kwargs):
        cp=UserCompany.objects.filter(companyname=request.data["cp_name"])            
        if not cp:
            now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.data["userid"]=request.data["user"]
            request.data["companyname"]=request.data["cp_name"]
            request.data["createtime"]=request.data["modifytime"]=now            
            ret = self.create(request, *args, **kwargs)
            CompanyUser.objects.create(id=ret.data['id'],revenueArea=request.data.get("cp_name"))
            BCompany.objects.create(bid=request.data["user"],cmid=ret.data['id'])
            return ret
        else:
            obj, created = BCompany.objects.get_or_create(bid=request.data["user"],cmid=cp[0].id)
            if created:
                serializers=CompanySerializer(cp[0])
                return Response(serializers.data)
            return Response("已存在")
class ServiceCompanyList(generics.ListAPIView):
    def get_queryset(self):
        try:
            user = self.kwargs['user']
            cpid=BCompany.objects.filter(bid=user).values_list('cmid', flat=True)
            queryset = UserCompany.objects.filter(id__in=cpid)
            return queryset
        except UserCompany.DoesNotExist:
            raise Http404
    serializer_class = CompanySerializer
       
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserCompany.objects.all()
    serializer_class = CompanySerializer
    def put(self, request, *args, **kwargs):
        if request.data.get("cp_name"):
            request.data["companyname"]=request.data.get("cp_name")
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["modifytime"]=now 
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if request.data.get("cp_name"):
            request.data["companyname"]=request.data.get("cp_name")
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["modifytime"]=now 
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        BCompany.objects.filter(cmid=instance.id).delete()
        return self.destroy(request, *args, **kwargs)
    
class CompanyDelete(generics.DestroyAPIView):
    def get_object(self):
        bid=self.kwargs['user']
        cmid=self.kwargs['pk']
        try:
            b_cm = BCompany.objects.filter(bid=bid,cmid=cmid)
            return b_cm
        except:
            raise Http404
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
##################################################################### 
class ServicePrice(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        service = self.kwargs['user']
        ordertype = self.request.query_params.get('ordertype', None)
        taxpayerstype = self.request.query_params.get('taxpayerstype', None)
        instance = Price.objects.filter(userid=service)       
        if ordertype:
            instance = instance.filter(ordertypeid=ordertype)
        if taxpayerstype:
            instance = instance.filter(taxpayerstype=taxpayerstype)
        if len(instance)==0:
            price = 300
        else:
            price = instance.aggregate(Min('price')).values()[0]
        period = self.request.query_params.get('period', None)
        if period:
            price = int(price)*int(period)
        return Response(price)    

##################################################################### 
class WithdrawalList(generics.ListCreateAPIView):
    queryset = Withdrawal.objects.all()
    serializer_class = WithdrawalSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now
        request.data["status"]='1'
        create=self.create(request, *args, **kwargs)
        return create
#     
class ServiceWithdrawal(generics.ListAPIView):
    def get_queryset(self):
        try:
            user = self.kwargs['user']
            queryset = Withdrawal.objects.filter(userid=user)
            return queryset
        except Withdrawal.DoesNotExist:
            raise Http404
    serializer_class = WithdrawalSerializer
#         
# class WithdrawalDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Withdrawal.objects.all()
#     serializer_class = WithdrawalSerializer
#     
class UserWithdrawalDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithdrawalSerializer
#####################################################################   
class ServiceReport(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        service = self.kwargs['user']
        instance = User.objects.get(id=service)
        serializer = ServiceReportSerializer(instance)        
        date = self.request.query_params.get('date', None)
        type = self.request.query_params.get('type', None)
        result={}
        result.update(serializer.data)
        d=datetime.datetime.now()
        toyear=d.year
        yeyear=d.year
        tomonth=d.month
        yemonth=tomonth-1
        if tomonth==1:
            yeyear-=1
            yemonth=12
        order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3']).order_by().values('companyid')
        if type=="year":
            order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3']\
                                    ,order_createtime__range=('%s-01-01 00:00:00'%toyear,'%s-12-31 23:59:59'%toyear)).order_by().values('companyid')
        elif type=="month":
            order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3']\
                                    ,order_createtime__range=('%s-%s-01 00:00:00'%(yeyear,yemonth),'%s-%s-31 23:59:59'%(yeyear,yemonth))
                                   ).order_by().values('companyid')
        sum_amount=order.aggregate(Sum('order_amount')).values()[0]
        if sum_amount is None:
            sum_amount=0
        result['userorder']=list(order.annotate(amount=Sum('order_amount')).order_by('amount')[:3])
        if result['userorder']:
            for i in range(len(result['userorder'])):
                result['userorder'][i]['company__cp_name']=None
                try:
                    result['userorder'][i]['company__cp_name']=UserCompany.objects.get(id=result['userorder'][i]['companyid']).companyname
                except:
                    pass
            other_amount=sum_amount-reduce(lambda x,y:x+y,[i['amount'] for i in result['userorder']])
            if other_amount>0:
                result['userorder'].append({"company__cp_name": u'其他',"amount": other_amount})
        period = self.request.query_params.get('period', None)
        if date:
            if len(date.split('-'))==2:
                [year,month]=date.split('-')
                date = datetime.date(int(year), int(month), 1)
                order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3'])\
                .filter(order_createtime__range=('%s-01 00:00:00'%date.strftime("%Y-%m"),'%s-31 23:59:59'%date.strftime("%Y-%m")))
                l={"date":date.strftime("%Y-%m"),"amount": order.aggregate(Sum('order_amount')).values()[0]}
                if period:
                    if int(period):
                        l=[l]
                        for i in range(int(period)-1):
                            month = date.month - 2
                            year = date.year + month / 12
                            month = month % 12 + 1
                            date = datetime.date(year, month, 1)
                            order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3'])\
                            .filter(order_createtime__range=('%s-01 00:00:00'%date.strftime("%Y-%m"),'%s-31 23:59:59'%date.strftime("%Y-%m")))
                            l.append({"date":date.strftime("%Y-%m"),"amount": order.aggregate(Sum('order_amount')).values()[0]}) 
                result['datedetail']=l
            elif len(date.split('-'))==1:
                date=int(date)
                order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3'])\
                .filter(order_createtime__range=('%s-01-01 00:00:00'%date,'%s-12-31 23:59:59'%date))
                l={"date":date,"amount": order.aggregate(Sum('order_amount')).values()[0]}
                if period:
                    if int(period):
                        l=[l]
                        for i in range(int(period)-1):
                            date -= 1
                            order = Order.objects.filter(servicesproviderid=service,order_status__in=['2','3'])\
                            .filter(order_createtime__range=('%s-01-01 00:00:00'%date,'%s-12-31 23:59:59'%date))
                            l.append({"date":date,"amount": order.aggregate(Sum('order_amount')).values()[0]}) 
                result['datedetail']=l
        return Response(result)
class ServiceReportList(generics.ListAPIView):
    def get_queryset(self):
        target = Order.objects.filter(order_status__in=['2','3'])\
        .exclude(servicesproviderid__in=[2,3,4,5,6]).values('servicesproviderid')
        type = self.request.query_params.get('type', None)
        user = self.request.query_params.get('user', None)
        d=datetime.datetime.now()
        toyear=d.year
        yeyear=d.year
        tomonth=d.month
        yemonth=tomonth-1
        if tomonth==1:
            yeyear-=1
            yemonth=12        
        if type=="year":
            target = Order.objects.filter(order_status__in=['2','3']\
                    ,order_createtime__range=('%s-01-01 00:00:00'%toyear,'%s-12-31 23:59:59'%toyear))\
                    .exclude(servicesproviderid__in=[2,3,4,5,6]).values('servicesproviderid')
        elif type=="month":
            target = Order.objects.filter(order_status__in=['2','3']\
                    ,order_createtime__range=('%s-%s-01 00:00:00'%(yeyear,yemonth),'%s-%s-31 23:59:59'%(yeyear,yemonth)))\
                    .exclude(servicesproviderid__in=[2,3,4,5,6]).values('servicesproviderid')
        self.queryset=target.annotate(amount=Sum('order_amount')).order_by('-amount')
        count=self.queryset.count()
        self.querysetlist = list(self.queryset)
        if user:
            try:
                userdetail=self.queryset.get(servicesproviderid=user)
                userindex = self.querysetlist.index(userdetail)+1
            except:
                userindex = 1
            if count<3:
                return self.queryset
            if userindex==1:
                return self.queryset[:3]
            elif userindex<6:
                return self.queryset[:userindex+1]
            else:
                return list(self.queryset[:3])+list(self.queryset[userindex-2:userindex+1])
        return self.queryset[:3]
    serializer_class = ServiceOrderSerializer
    def get(self, request, *args, **kwargs):
        res = self.get_queryset()
        for i in res:
            userdetail=self.queryset.get(servicesproviderid=i['servicesproviderid'])
            i['orderby']= self.querysetlist.index(userdetail)+1
            try:
                i['name']= User.objects.get(id=i['servicesproviderid']).name
            except:
                i['name']= None
        return Response(res)
#####################################################################   
class Orderstatus(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = OrderstatusSerializer
    lookup_field='user'  