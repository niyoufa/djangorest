# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# class RRModelBackend(ModelBackend):
#     def authenticate(self, username=None, type=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             user = UserModel.objects.get(username=username,type=type)
#             if user.check_password(password):
#                 return user
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)

class UserManager(BaseUserManager):

    def _create_user(self, phone, type, email, password, **extra_fields):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not phone:
            raise ValueError('The given phone must be set')
        if not type:
            raise ValueError('The given usertype must be set')
        email = self.normalize_email(email)
        user = self.model(username="%s_%s"%(phone,type), email=email, phone=phone, type=type, 
                          createTime=now, modifyTime=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, phone, type, email=None, password=None, **extra_fields):
        return self._create_user(phone, type, email, password, **extra_fields)

    def create_superuser(self, username, phone, type, password, **extra_fields):
        return self._create_user(phone, type, None, password, **extra_fields)
    
class User(AbstractBaseUser):
    username = models.CharField(null=True,max_length=100, unique=True)
    phone = models.CharField(null=True,max_length=100)
    iconPath = models.CharField(null=True,max_length=100)
    nickname = models.CharField(null=True,max_length=100)
    name = models.CharField(null=True,max_length=100)
    sex = models.CharField(null=True,max_length=10)
    email = models.EmailField(null=True)
    type = models.CharField(null=True,max_length=100)
    status = models.CharField(null=True,max_length=100)
    remark = models.CharField(null=True,max_length=500)
    longitude = models.CharField(null=True,max_length=100)
    latitude = models.CharField(null=True,max_length=100)
    channel = models.CharField(null=True,max_length=100)
    createTime = models.CharField(null=True,max_length=100)
    createBy = models.CharField(null=True,max_length=100)
    modifyTime = models.CharField(null=True,max_length=100)
    modifyBy = models.CharField(null=True,max_length=100)
    default_exadd = models.IntegerField(db_column='defaultexaddId', null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('phone','type',)

    class Meta:
        ordering = ('-createTime',)
        db_table = 'renren_user'

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        if self.name:
            return self.name
        elif self.phone:
            return '%s****%s'%(self.phone[:3],self.phone[-4:])
        else:
            return '%s****%s'%(self.phone[:3],self.phone[-4:])
    
    def get_icon(self):
        if self.iconPath:
            return self.iconPath
        elif self.sex=='2':
            return 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/woman.png'
        else:
            return 'http://rrcw.oss-cn-hangzhou.aliyuncs.com/man.png'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True
    
#用户公司信息
class UserCompany(models.Model):
#     userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyscale = models.CharField(db_column='companyScale', max_length=200, blank=True)  # Field name made lowercase.
    specialty = models.CharField(max_length=200, blank=True)
    taxpayerstype = models.CharField(db_column='taxPayersType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=2, blank=True, null=True)
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_company'
#用户与公司关联表
class BCompany(models.Model):
    bid = models.CharField(max_length=100, blank=True, null=True)
    cmid = models.CharField(max_length=100, blank=True, null=True)
    btype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b_company'
        
#C端用户详情
class Financeuser(models.Model):
    isacceptorder = models.CharField(db_column='isAcceptOrder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(max_length=18, blank=True, null=True)
    idcardimgpath = models.CharField(db_column='idCardImgPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    accountantNo = models.CharField(db_column='accountantNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountantimgpath = models.CharField(db_column='accountantImgPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    degree = models.CharField(max_length=10, blank=True, null=True)
    workage = models.CharField(max_length=100, blank=True, null=True)
    certificateid = models.CharField(db_column='certificateId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    certificateimgpath = models.CharField(db_column='certificateImgPath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    discount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    specialty = models.CharField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    province = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    area = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    createtime = models.CharField(max_length=100, blank=True, null=True)
    modifytime = models.CharField(max_length=100, blank=True, null=True)
    aduittime = models.CharField(max_length=100, blank=True, null=True)
    auditcontent = models.CharField(db_column='auditContent', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_status = models.CharField(db_column='states', max_length=10, blank=True, null=True)
    connectaddress = models.CharField(db_column='connectAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isreceiveresume = models.CharField(db_column='isReceiveResume', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ishavelicense = models.CharField(db_column='isHaveLicense', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ishavecertificate = models.CharField(db_column='isHaveCertificate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isallservice = models.CharField(db_column='isAllService', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isvisit = models.CharField(db_column='isVisit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    visittime = models.CharField(db_column='visitTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ishaveexp = models.CharField(db_column='isHaveExp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicer = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.CharField(max_length=100, blank=True, null=True)
    idcardstarttime = models.CharField(db_column='idcardStartTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcardendtime = models.CharField(db_column='idcardEndTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcardagency = models.CharField(db_column='idcardAgency', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcardagencycode = models.CharField(db_column='idcardAgencyCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcardaddress = models.CharField(db_column='idcardAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcardpostcode = models.CharField(db_column='idcardPostcode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankid = models.CharField(db_column='bankId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iscommitcmbc = models.CharField(db_column='isCommitCMBC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cmbcaccountid = models.CharField(db_column='CMBCaccountId', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'financeuser'

class Price(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ordertypeid = models.IntegerField(db_column='orderTypeId', blank=True, null=True)  # Field name made lowercase.
    taxpayerstype = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'financeruserprice'

class Expressadd(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    recipient = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    express_province = models.CharField(db_column='expressProvince', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    express_city = models.CharField(db_column='expressCity', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    express_area = models.CharField(db_column='expressArea', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    express_street = models.CharField(db_column='expressStreet', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'user_expressadd'


class Workexperience(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(max_length=1000, blank=True, null=True)
    position = models.CharField(db_column='POSITION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'user_workexperience'
        