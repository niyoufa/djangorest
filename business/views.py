# -*- coding: utf-8 -*-
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from business.models import (
                             Balancesheet, Order, Order_Personnelinf, Personnelinf, Review, 
                             Childorder, Drawback, LegalOrderdetail, OrderCompany, Parkhireorder, 
                             RegisterChannel, Withdrawal,BussinessReviewTags, Express, Express_Order
                             )
from business.serializers import (
                                     PersonnelinfSerializer, OrderSerializer, ReviewSerializer, 
                                     BalancesheetSerializer, ChildOrderSerializer, LawinfshipSerializer,
                                     ChildOrderlistSerializer, ExpressSerializer, UserrecentorderSerializer
                                     )
from rr_manage.models import Legalservice
from rr_user.models import User
from rest_framework import generics
from django.db.models import Q
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView
import random
from django.utils import timezone
import datetime
from rest_framework import filters
#####################################################################
class UserpersonnelinfList(generics.ListCreateAPIView):
    queryset = Personnelinf.objects.all()
    serializer_class = PersonnelinfSerializer
    
    def get_queryset(self):
        queryset = super(UserpersonnelinfList, self).get_queryset()
        return queryset.filter(userid=self.kwargs.get('pk'))   
    
class PersonnelinfList(generics.CreateAPIView):
    queryset = Personnelinf.objects.all()
    serializer_class = PersonnelinfSerializer
    
class PersonnelinfDetail(generics.RetrieveUpdateDestroyAPIView):
    def perform_update(self, serializer):
        serializer.save() 
    queryset = Personnelinf.objects.all()
    serializer_class = PersonnelinfSerializer
    
class LawinfshipDetail(generics.RetrieveUpdateAPIView):
    queryset = LegalOrderdetail.objects.all()
    serializer_class = LawinfshipSerializer
#####################################################################
class Userorder(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('order_type','id')
    ordering_fields = '__all__'
    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            date = self.request.query_params.get('date', None)
            order_status = self.request.query_params.get('order_status', None)
            queryset = Order.objects.filter(Q(userid=pk) | Q(servicesproviderid=pk, order_status__in=['2','3'])).order_by('-order_createtime')
            if order_status:
                queryset = queryset.filter(order_status__in=order_status.split(','))
            if date is not None:
                queryset = queryset.filter(starttime__lte=date,endtime__gte=date)
            return queryset
        except Order.DoesNotExist:
            raise Http404
    serializer_class = OrderSerializer
    
class Userchildorder(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields = ('id',)
    ordering_fields = '__all__'
    def get_queryset(self):
        try:
            pk = self.kwargs['pk']
            date = self.request.query_params.get('date', None)
            order_type = self.request.query_params.get('order_type', None)
            q=Order.objects.filter(Q(userid=pk) | Q(servicesproviderid=pk,order_status__in=['2','3']))
            if order_type:
                q = q.filter(order_type=order_type)
            userlist = q.values_list('id', flat=True)
            queryset = Childorder.objects.filter(parentid__in=userlist)
            if date is not None:
                if len(date.split('-'))==2:
                    [year,month]=date.split('-')
                    date = "%s-%02d"%(year, int(month))
                    queryset = queryset.filter(period=date)
            return queryset
        except Childorder.DoesNotExist:
            raise Http404
    serializer_class = ChildOrderlistSerializer
    
class Userrecentorder(generics.ListAPIView):
    serializer_class = UserrecentorderSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        d=datetime.datetime.now()
        year,month=d.year,d.month
        date = "%s-%02d"%(year, int(month))
        q=Order.objects.filter(userid=pk,order_type='1',order_status__in=['2','3'],starttime__lte=date,endtime__gte=date)\
            .values_list('id', flat=True)
        queryset = Childorder.objects.filter(parentid__in=q,period=date)
        return queryset
#     def get(self, request, *args, **kwargs):
#         result={}
#         pk = self.kwargs['pk']
#         d=datetime.datetime.now()
#         year,month=d.year,d.month
#         date = "%s-%02d"%(year, int(month))
#         q=Order.objects.filter(userid=pk,order_type='1',order_status__in=['2','3'],starttime__lte=date,endtime__gte=date)\
#             .only("id", "servicesproviderid").defer("servicesproviderid")
#         userlist = q.values_list('id', flat=True)
#         queryset = Childorder.objects.filter(parentid__in=userlist,period=date).order_by('-id')
#         if queryset:
#             periodId=queryset[0].id
#             parentid=queryset[0].parentid
#             servicesproviderid=q.get(id=parentid).servicesproviderid
#             result.update(periodId=periodId)
#             if servicesproviderid:
#                 try:
#                     financeuser=User.objects.values('id','iconPath','name','sex').get(id=servicesproviderid)
#                     result.update(financeuser=financeuser)
#                 except:
#                     pass
#         return Response(result or None)

class OrderList(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def post(self, request, *args, **kwargs):
        obj1 = timezone.now().strftime("%y%m%d%H%M%S")
        obj2 = random.randint(0,9999)
        request.data["orderNo"]=obj1+'%02d' % int(request.data["order_type"])+'%04d' % obj2
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["order_createtime"]=request.data["modifytime"]=now
        request.data["remark"]='1'
        ret = self.create(request, *args, **kwargs)
        order = Order.objects.get(id=ret.data['id'])
        if request.data.get("cp_name"):
            order.cp_name=request.data.get("cp_name")
        if request.data.get("address"):
            order.address=request.data.get("address")
        if request.data.get("taxpayerstype"):
            order.taxpayerstype=request.data.get("taxpayerstype")
        if request.data.get("park") and request.data.get("station"):
            Parkhireorder.objects.get_or_create(orderid=order.id,parkid=request.data.get("park"),station=request.data.get("station"))
        if request.data.get("personnelinf"):
            for i in request.data.get("personnelinf"):
                Order_Personnelinf.objects.get_or_create(orderid=order.id,employeeid=i,starttime=request.data.get("starttime"))
        lawinf = Legalservice.objects.filter(ordertype=request.data["order_type"]).only('id')
        for i in lawinf:
            LegalOrderdetail.objects.get_or_create(orderid=order.id,legalserviceid=i.id,count=0)
        if request.data.get("starttime") and request.data.get("period"):
            [year,month]=[int(x.strip()) for x in str(request.data["starttime"]).split('-')]
            nyear=(month+int(request.data["period"])-2)/12
            nmonth=(month+int(request.data["period"])-2)%12+1
            endtime="%s-%02d"%(year+nyear,nmonth)
            order.endtime=endtime
            if str(request.data["order_type"]) in ['1','8','9']:
#                 amount=int(float(ret.data["order_amount"]))/int(ret.data["period"])
                Childorder.objects.get_or_create(parentid=order.id,period=ret.data["starttime"],order_progress=0)
                for i in range(int(ret.data["period"])-1):
                    nyear=month/12
                    month=month%12+1
                    year=year+nyear
                    servicetime='%s-%02d'%(year,month)
                    Childorder.objects.get_or_create(parentid=order.id,period=servicetime,order_progress=0)
        order.save()
        ret.data=self.get_serializer(order).data
        return ret
       
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class applyInvoiceorder(generics.ListAPIView):
       
    def get_queryset(self):
        queryset = super(applyInvoiceorder, self).get_queryset()
        return queryset.filter(userid=self.kwargs.get('pk'), order_status="2").exclude(id__in=Express_Order.objects.values_list('orderid', flat=True))
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

class ChildOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Childorder.objects.all()
    serializer_class = ChildOrderSerializer
    def put(self, request, *args, **kwargs):
        if request.data.get('status'):
            instance = self.get_object()
            childorder=Childorder.objects.get(id=instance.id)
            childorder.status=request.data.get('status')
            childorder.save()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if request.data.get('status'):
            instance = self.get_object()
            childorder=Childorder.objects.get(id=instance.id)
            childorder.status=request.data.get('status')
            childorder.save()
        return self.partial_update(request, *args, **kwargs)
        
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        if request.data.get("tags"):
            for i in request.data.get("tags"):
                BussinessReviewTags.objects.get_or_create(tagsid=i,reviewid=res.data['id'])
        return res
    
class ServiceReview(generics.ListCreateAPIView):
       
    def get_queryset(self):
        queryset = super(ServiceReview, self).get_queryset()
        return queryset.filter(servicesproviderid=self.kwargs.get('pk')) 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
# #####################################################################      
class BalancesheetList(generics.ListCreateAPIView):
#     filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
#     filter_fields = ('id','userid', 'periodId')
#     ordering_fields = '__all__'
    serializer_class = BalancesheetSerializer     
    def get_queryset(self):
        date = self.request.query_params.get('date', None)
        company = self.request.query_params.get('company', None)
        periodId = self.request.query_params.get('period', None)
        type = self.request.query_params.get('type', None)
        if company and date:
            order = Order.objects.filter(companyid=company).values_list('id', flat=True)
            [year,month]=date.split('-')
            date = '%s-%02d'%(year,int(month))
            if Childorder.objects.filter(parentid__in=order,period=date,status__in=['2','3','4','5']):
                periodId = Childorder.objects.filter(parentid__in=order,period=date,status__in=['2','3','4','5']).order_by('-id')[0].id     
        queryset = Balancesheet.objects.filter(periodId=periodId,tableTypeId=type)
        return queryset 

class AllsheetList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        periodId = self.kwargs['period']
        balancesheet = Balancesheet.objects.filter(periodId=periodId,tableTypeId__in=['1','3'])
        if balancesheet.count()==0:
            return Response([])
        else:
            sheetname=[u'货币资金期末余额', u'应收账款', u'存货', u'应付账款', u'应缴税费', u'营业收入', u'营业成本', u'管理费用', u'净利润', 
                  u'固定资产', u'其他应收款', u'其他应付款', u'资产', u'负债', u'所有者权益']
            itemname=[u'货币资金', u'应收账款', u'存货', u'应付账款', u'应交税费', u'一、营业收入', u'减：营业成本', u'管理费用', u'四：净利润（净亏损以“-”号填列）', 
                  u'固定资产账面价值', u'其他应收款', u'其他应付款', u'资产总计', u'负债合计', u'所有者权益（或股东权益）合计']
            sheeticon=[u'img/image/c_icon-37.png', u'img/image/c_icon-38.png', u'img/image/c_icon-39.png', 
                       u'img/image/c_icon-40.png', u'img/image/c_icon-41.png', u'img/image/c_icon-42.png', u'img/image/c_icon-43.png', 
                       u'img/image/c_icon-44.png', u'img/image/c_icon-45.png', u'img/image/c_icon-46.png', u'img/image/c_icon-47.png', 
                       u'img/image/c_icon-48.png', u'img/image/c_icon-49.png', u'img/image/c_icon-34.png', u'img/image/c_icon-33.png']
            sheet=[]
            for i in range(len(sheetname)):
                try:
                    if balancesheet.get(itemname=itemname[i]).itemEPbalance:
                        sheet.append({'sheetname':sheetname[i], 'icon':sheeticon[i], 'amount':balancesheet.get(itemname=itemname[i]).itemEPbalance})
                    else:
                        sheet.append({'sheetname':sheetname[i], 'icon':sheeticon[i], 'amount':0.00})
                except:
                    sheet.append({'sheetname':sheetname[i], 'icon':sheeticon[i], 'amount':0.00})
            return Response(sheet)
#####################################################################      
class Userexpress(generics.ListCreateAPIView):
    queryset = Express.objects.all()
    serializer_class = ExpressSerializer
    
    def get_queryset(self):
        queryset = super(Userexpress, self).get_queryset()
        return queryset.filter(userid=self.kwargs.get('pk'))   

class ExpressList(generics.CreateAPIView):
    queryset = Express.objects.all()
    serializer_class = ExpressSerializer
    def post(self, request, *args, **kwargs):
        now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        request.data["createtime"]=now 
        res = self.create(request, *args, **kwargs)
        if request.data.get("order"):
            for i in request.data.get("order"):
                Express_Order.objects.get_or_create(orderid=i,expressid=res.data['id'])
        return res
class ExpressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Express.objects.all()
    serializer_class = ExpressSerializer
