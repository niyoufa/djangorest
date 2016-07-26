# -*- coding: utf-8 -*-
from django.db import models

class Area(models.Model):
    linkageid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=90, blank=True)
    parentid = models.IntegerField(blank=True, null=True)
    keyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'

class Tags(models.Model):
    tags = models.CharField(max_length=50, blank=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'manage_tags'
                
class Version(models.Model):
    versionname = models.CharField(db_column='versionName', max_length=100, blank=True)  # Field name made lowercase.
    versioncode = models.CharField(db_column='versionCode', max_length=100, blank=True)  # Field name made lowercase.
    versiontype = models.CharField(db_column='versionType', max_length=1, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    content = models.TextField(blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'manage_version'

#法律服务内容
class Legalservice(models.Model):
    content = models.CharField(max_length=500, blank=True)
    servicecount = models.IntegerField(db_column='serviceCount', blank=True, null=True)  # Field name made lowercase.
    ordertype = models.IntegerField(db_column='orderType', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'legalservice'

#技术职称
class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'manage_certificate'
#订单类型列表
class Ordertype(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        db_table = 'manage_ordertype'

#报表列表
class Reporttype(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    reportname = models.CharField(db_column='reportName', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'reporttype'

#擅长领域列表
class Skilledfield(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    business = models.CharField(db_column='discription', max_length=500, blank=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skilledfield'

#用户反馈
class Comments(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'manage_comments'

#园区信息
class Park(models.Model):
    icon = models.CharField(max_length=100, blank=True)
    park_name = models.CharField(db_column='parkName', max_length=100, blank=True)  # Field name made lowercase.
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    renrenid = models.IntegerField(db_column='renrenId', blank=True, null=True)  # Field name made lowercase.
    park_company = models.IntegerField(db_column='companyCount', blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    area = models.CharField(db_column='cityarea', max_length=100, blank=True)
    park_address = models.CharField(db_column='address', max_length=100, blank=True)
    park_area = models.CharField(db_column='area', max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    park_introduction = models.TextField(db_column='introduction', blank=True)
    content = models.TextField(blank=True)
    imagepaths = models.CharField(db_column='imagePaths', max_length=500, blank=True)  # Field name made lowercase.
    park_price = models.DecimalField(db_column='parkWorkPrice', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'manage_park'

class Bank(models.Model):
    bank = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    createtime = models.DateField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True)  # Field name made lowercase.
    modifytime = models.DateField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=10, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'manage_bank'

class Indexpic(models.Model):
    image = models.CharField(db_column='imagePath', max_length=200, blank=True)  # Field name made lowercase.
    isused = models.IntegerField(db_column='isUsed', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=200, blank=True)
    type = models.CharField(db_column='TYPE', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=10, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='remark', max_length=500, blank=True)

    class Meta:
        db_table = 'manage_indexpic'