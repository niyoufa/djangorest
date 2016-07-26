# -*- coding: utf-8 -*-
import datetime
from rest_framework import serializers
from business.models import (
                             Balancesheet, Order, Order_Personnelinf, Personnelinf, Review, 
                             Childorder, Drawback, LegalOrderdetail, OrderCompany, Parkhireorder, 
                             RegisterChannel, Withdrawal,BussinessReviewTags, Express
                             )
from rr_user.models import UserCompany,User, Expressadd
from rr_manage.models import Park, Legalservice, Tags
from rr_manage.serializers import TagsSerializer
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
)

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        exclude = ()


class PersonnelinfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnelinf
        exclude = ()
        
class Order_PersonnelinfSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    idcard = serializers.SerializerMethodField()
    household_type = serializers.SerializerMethodField()
    def get_status(self,instance):
        today=datetime.date.today().strftime("%Y-%m")
        if instance.starttime>today:
            status = u"待缴"
        else :
            status = u"正常"
        return status
    def get_name(self,instance):
        try:
            return Personnelinf.objects.get(id=instance.employeeid).name
        except Personnelinf.DoesNotExist:
            return None
    def get_idcard(self,instance):
        try:
            return Personnelinf.objects.get(id=instance.employeeid).idcard
        except Personnelinf.DoesNotExist:
            return None
    def get_household_type(self,instance):
        try:
            return Personnelinf.objects.get(id=instance.employeeid).household_type
        except Personnelinf.DoesNotExist:
            return None
    class Meta:
        model = Order_Personnelinf
        exclude = ()
        
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    ordertype = serializers.SerializerMethodField()
    tagsname = serializers.SerializerMethodField()
    def get_username(self,instance):
        try:
            return User.objects.get(id=instance.userid).get_short_name()
        except User.DoesNotExist:
            return None
    def get_ordertype(self,instance):
        try:
            order=Childorder.objects.get(id=instance.childorder).parentid
            return Order.objects.get(id=order).order_type
        except:
            return None
    def get_tagsname(self,instance):
        try:
            tags = BussinessReviewTags.objects.filter(reviewid=instance.id).values_list('tagsid', flat=True)
            return TagsSerializer(Tags.objects.filter(id__in=tags),many=True,read_only=True).data
        except:
            return None
        
    class Meta:
        model = Review
        exclude = ()
        
class LawinfshipSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    servicecount = serializers.SerializerMethodField()
    def get_content(self,instance):
        try:
            return Legalservice.objects.get(id=instance.legalserviceid).content
        except Legalservice.DoesNotExist:
            return None
    def get_servicecount(self,instance):
        try:
            return Legalservice.objects.get(id=instance.legalserviceid).servicecount
        except Legalservice.DoesNotExist:
            return None
    class Meta:
        model = LegalOrderdetail
        exclude = ()
        
class ChildOrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    iscomments = serializers.SerializerMethodField()
    def get_status(self,instance):        
        if str(instance.status)=="2":
            status = u"服务中"
        elif str(instance.status)=="3":
            status = u"交付中"
        elif str(instance.status)=="4":
            status = u"已完成" 
        else :
            status = u"未开始"
        return status
    def get_review(self,instance):
        try:
            review=Review.objects.get(childorder=instance.id)
            serializers=ReviewSerializer(review, read_only=True)
            return serializers.data
        except Review.DoesNotExist:
            return None
    def get_iscomments(self,instance):
        try:
            Review.objects.get(childorder=instance.id)
            return '1'
        except Review.DoesNotExist:
            return '0'
    class Meta:
        model = Childorder
        exclude = ()
        
class ChildOrderlistSerializer(serializers.ModelSerializer):
    cp_name = serializers.SerializerMethodField()
    servicesproviderid = serializers.SerializerMethodField()
    userid = serializers.SerializerMethodField()
    taxpayerstype = serializers.SerializerMethodField()
    def get_cp_name(self,instance):
        companyid=Order.objects.get(id=instance.parentid).companyid
        if companyid:
            return UserCompany.objects.get(id=companyid).companyname
        else:
            return Order.objects.get(id=instance.parentid).cp_name
    def get_taxpayerstype(self,instance):
        companyid=Order.objects.get(id=instance.parentid).companyid
        if companyid:
            return UserCompany.objects.get(id=companyid).taxpayerstype
        else:
            return Order.objects.get(id=instance.parentid).taxpayerstype
    def get_servicesproviderid(self,instance):
        return Order.objects.get(id=instance.parentid).servicesproviderid
    def get_userid(self,instance):
        return Order.objects.get(id=instance.parentid).userid
 
    class Meta:
        model = Childorder
        exclude = ()
        
class OrderSerializer(serializers.ModelSerializer):
    servicename = serializers.SerializerMethodField()
    personnelinfdetail = serializers.SerializerMethodField()
    cp_name = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    taxpayerstype = serializers.SerializerMethodField()
#     bankname = serializers.SerializerMethodField()
    childorder = serializers.SerializerMethodField()
    lawinf = serializers.SerializerMethodField()
    parkname = serializers.SerializerMethodField()
    def get_servicename(self,instance):
        try:
            return User.objects.get(id=instance.servicesproviderid).name
        except User.DoesNotExist:
            return None
    def get_parkname(self,instance):
        try:
            parkid=Parkhireorder.objects.get(orderid=instance.id).parkid
            return Park.objects.get(id=parkid).park_name
        except :
            return None
    def get_cp_name(self,instance):
        if instance.companyid:
            try:
                return UserCompany.objects.get(id=instance.companyid).companyname
            except:
                return instance.cp_name
        else:
            return instance.cp_name
    def get_address(self,instance):
        if instance.companyid:
            try:
                return UserCompany.objects.get(id=instance.companyid).address
            except:
                return instance.address
        else:
            return instance.address
    def get_taxpayerstype(self,instance):
        if instance.companyid:
            try:
                return UserCompany.objects.get(id=instance.companyid).taxpayerstype
            except:
                return instance.taxpayerstype
        else:
            return instance.taxpayerstype
    
    def get_lawinf(self,instance):
        lawinfdetail=LegalOrderdetail.objects.filter(orderid=instance.id)
        serializer=LawinfshipSerializer(lawinfdetail,many=True, read_only=True)
        return serializer.data
        
#     def get_bankname(self,instance):
#         if instance.bank:
#             return '%s%s'%(instance.bank.bank,instance.bank.branch)
#         else:
#             return None
        
    def get_childorder(self,instance):
        self.request = self.context.get('request')
        childorder = Childorder.objects.filter(parentid=instance.id).order_by('period')
        loadingcomplete = self.request.GET.get("complete")
        if loadingcomplete=='1':
            childorder = childorder.exclude(status=5).exclude(status=4)
        serializer=ChildOrderSerializer(childorder,many=True, read_only=True)
        return serializer.data
    
    def get_personnelinfdetail(self,instance):
        self.request = self.context.get('request')
        personnelinfdetail=Order_Personnelinf.objects.filter(orderid=instance.id)
        loadingcomplete = self.request.GET.get("complete")
        if loadingcomplete=='1':
            today=datetime.date.today().strftime("%Y-%m")
            personnelinfdetail = personnelinfdetail.filter(starttime__gt=today)
        serializer=Order_PersonnelinfSerializer(personnelinfdetail,many=True, read_only=True)
        return serializer.data
    class Meta:
        model = Order
        exclude = ()
        
class BalancesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balancesheet
        fields = ('itemname','itemBPbalance','itemEPbalance')
               
class ExpressSerializer(serializers.ModelSerializer):
    recipient = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    def get_address(self,instance):
        if instance.expressadd:
            try:
                express_province = Expressadd.objects.get(id=instance.expressadd).express_province
                express_city = Expressadd.objects.get(id=instance.expressadd).express_city
                express_area = Expressadd.objects.get(id=instance.expressadd).express_area
                express_street = Expressadd.objects.get(id=instance.expressadd).express_street
                return express_province+express_city+express_area+express_street
            except Expressadd.DoesNotExist:
                return None
        return None
    def get_recipient(self,instance):
        if instance.expressadd:
            try:
                return Expressadd.objects.get(id=instance.expressadd).recipient
            except Expressadd.DoesNotExist:
                return None 
        return None
    def get_phone(self,instance):
        if instance.expressadd:
            try:
                return Expressadd.objects.get(id=instance.expressadd).phone
            except Expressadd.DoesNotExist:
                return None 
        return None
            
    class Meta:
        model = Express
        exclude = ()
        
class UserrecentorderSerializer(serializers.ModelSerializer):
    periodId = serializers.SerializerMethodField()
    cp_name = serializers.SerializerMethodField()
    financeuser = serializers.SerializerMethodField()
    def get_periodId(self,instance):
        return instance.id
    def get_cp_name(self,instance):
        try:
            companyid = Order.objects.get(id=instance.parentid).companyid
            if companyid:
                return UserCompany.objects.get(id=companyid).companyname
            return Order.objects.get(id=instance.parentid).cp_name
        except:
            return None
    def get_financeuser(self,instance):
        try:
            servicesproviderid = Order.objects.get(id=instance.parentid).servicesproviderid
            if servicesproviderid:
                return User.objects.values('id','iconPath','name','sex').get(id=servicesproviderid)
            return None
        except:
            return None
    class Meta:
        model = Childorder
        fields = ('periodId','cp_name','financeuser')