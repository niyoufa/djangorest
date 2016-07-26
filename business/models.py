# -*- coding: utf-8 -*-

from django.db import models
#表
class Balancesheet(models.Model):
    periodId = models.IntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=100, blank=True, null=True)
    itemBPbalance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itemEPbalance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    parentId = models.CharField(max_length=100, blank=True, null=True)
    tableTypeId = models.IntegerField(blank=True, null=True)
    createTime = models.CharField(max_length=100, blank=True, null=True)
    createBy = models.CharField(max_length=100, blank=True, null=True)
    modifyTime = models.CharField(max_length=100, blank=True, null=True)
    modifyBy = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    monthTotalAmouont = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthAmount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#订单
class Order(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    orderNo = models.CharField(db_column='orderNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_type = models.CharField(db_column='type', max_length=100, blank=True, null=True)
    order_amount = models.DecimalField(db_column='amount', max_digits=20, decimal_places=2, blank=True, null=True)
    apamount = models.DecimalField(db_column='APamount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    order_createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paytime = models.CharField(max_length=100, blank=True, null=True)
    order_status = models.CharField(db_column='status', max_length=100, blank=True, null=True)
    orderprogress = models.CharField(db_column='orderProgress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    canceltime = models.CharField(db_column='cancelTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cancelreason = models.TextField(db_column='cancelReason', blank=True, null=True)  # Field name made lowercase.
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    iscomments = models.CharField(db_column='isComments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ismkinvoice = models.CharField(db_column='isMkInvoice', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cp_name = models.CharField(db_column='companyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='companyId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='companyAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxpayerstype = models.CharField(max_length=100, blank=True, null=True)
    payway = models.CharField(db_column='paytype', max_length=100, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(max_length=100, blank=True, null=True)
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isrenewal = models.CharField(db_column='isRenewal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isusecoupon = models.CharField(db_column='isUseCoupon', max_length=10, blank=True, null=True)  # Field name made lowercase.
    couponid = models.CharField(db_column='couponId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=100, blank=True, null=True)
#订单与人事关系表
class Order_Personnelinf(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True)  # Field name made lowercase.

#人事信息
class Personnelinf(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    idcard = models.CharField(max_length=100, blank=True, null=True)
    household_type = models.CharField(db_column='householdType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

#子订单评价
class Review(models.Model):
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    childorder = models.IntegerField(db_column='periodId', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=1, blank=True, null=True)
    supplierid = models.IntegerField(db_column='supplierId', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.

class BussinessReviewTags(models.Model):
    tagsid = models.IntegerField(db_column='tagsId', blank=True, null=True)  # Field name made lowercase.
    reviewid = models.IntegerField(db_column='reviewId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'bussiness_review_tags'
        
#子订单
class Childorder(models.Model):
    parentid = models.CharField(db_column='parentId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(blank=True, null=True)
    order_progress = models.IntegerField(db_column='isConfirm', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(db_column='fileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reportfilepath = models.CharField(db_column='reportFilePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)
    types = models.CharField(max_length=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'childorder'


#退款订单
class Drawback(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amountno = models.CharField(db_column='amountNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    applyway = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    accountcode = models.CharField(db_column='accountCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    aduittime = models.CharField(db_column='aduitTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'drawback'


#法律服务订单详情
class LegalOrderdetail(models.Model):
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    legalserviceid = models.IntegerField(db_column='legalServiceId', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'legal_orderdetail'

#一键记账详情
class OrderCompany(models.Model):
    orderid = models.CharField(max_length=100, blank=True, null=True)
    companyid = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    reportfilepath = models.CharField(db_column='reportFilePath', max_length=500, blank=True, null=True)  # Field name made lowercase.
    types = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'order_company'

#园区注册详情
class Parkhireorder(models.Model):
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    parkid = models.IntegerField(db_column='parkId', blank=True, null=True)  # Field name made lowercase.
    station = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'parkhireorder'

#用户注册渠道列表
class RegisterChannel(models.Model):
    channel = models.CharField(max_length=255, blank=True, null=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'register_channel'


#提现
class Withdrawal(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amountno = models.CharField(db_column='amountNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    applyway = models.CharField(max_length=100, blank=True, null=True)
    account = models.CharField(db_column='accountCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='accountName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    aduittime = models.CharField(db_column='aduitTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'withdrawal'

class Express(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='invoiceId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    status = models.CharField(db_column='STATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    expressorderNo = models.CharField(db_column='expressNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=500, blank=True, null=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=500, blank=True, null=True)  # Field name made lowercase.
    modityby = models.CharField(db_column='modityBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='remark', max_length=500, blank=True, null=True)
    expressadd = models.IntegerField(db_column='expressaddId', null=True)
    cp_name = models.CharField(blank=True, null=True, max_length=100, verbose_name='发票抬头')
    invoicetype = models.CharField(blank=True, null=True, max_length=100, verbose_name='发票类型')
    class Meta:
        db_table = 'business_express'
        
class Express_Order(models.Model):
    expressid = models.IntegerField(db_column='expressId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'business_express_order'