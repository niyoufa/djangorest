# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccountEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(unique=True, max_length=75)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('RenrenUser')

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Area(models.Model):
    linkageid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=90, blank=True)
    parentid = models.IntegerField(blank=True, null=True)
    keyid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('RenrenUser', unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BusinessBalancesheet(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    periodid = models.IntegerField(db_column='periodId', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(max_length=100, blank=True)
    itembpbalance = models.DecimalField(db_column='itemBPbalance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itemepbalance = models.DecimalField(db_column='itemEPbalance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='parentId', max_length=100, blank=True)  # Field name made lowercase.
    tabletypeid = models.IntegerField(db_column='tableTypeId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    remark = models.CharField(max_length=500, blank=True)
    monthtotalamouont = models.DecimalField(db_column='monthTotalAmouont', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    monthamount = models.DecimalField(db_column='monthAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'business_balancesheet'


class BusinessExpress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    invoiceid = models.IntegerField(db_column='invoiceId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True)
    expressno = models.CharField(db_column='expressNo', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modityby = models.CharField(db_column='modityBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)
    expressaddid = models.IntegerField(db_column='expressaddId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    cp_name = models.CharField(max_length=255, blank=True)
    invoicetype = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'business_express'


class BusinessExpressOrder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    expressid = models.IntegerField(db_column='expressId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'business_express_order'


class BusinessOrder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    orderno = models.CharField(db_column='orderNo', max_length=100, blank=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    apamount = models.DecimalField(db_column='APamount', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    paytime = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    orderprogress = models.CharField(db_column='orderProgress', max_length=100, blank=True)  # Field name made lowercase.
    canceltime = models.CharField(db_column='cancelTime', max_length=100, blank=True)  # Field name made lowercase.
    cancelreason = models.TextField(db_column='cancelReason', blank=True)  # Field name made lowercase.
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    iscomments = models.CharField(db_column='isComments', max_length=100, blank=True)  # Field name made lowercase.
    ismkinvoice = models.CharField(db_column='isMkInvoice', max_length=100, blank=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=100, blank=True)  # Field name made lowercase.
    companyid = models.CharField(db_column='companyId', max_length=100, blank=True)  # Field name made lowercase.
    companyaddress = models.CharField(db_column='companyAddress', max_length=100, blank=True)  # Field name made lowercase.
    taxpayerstype = models.CharField(max_length=100, blank=True)
    paytype = models.CharField(max_length=100, blank=True)
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True)  # Field name made lowercase.
    period = models.CharField(max_length=100, blank=True)
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True)  # Field name made lowercase.
    isrenewal = models.CharField(db_column='isRenewal', max_length=10, blank=True)  # Field name made lowercase.
    isusecoupon = models.CharField(db_column='isUseCoupon', max_length=10, blank=True)  # Field name made lowercase.
    couponid = models.CharField(db_column='couponId', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'business_order'


class BusinessOrderPersonnelinf(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'business_order_personnelinf'


class BusinessPersonnelinf(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True)
    idcard = models.CharField(max_length=100, blank=True)
    householdtype = models.CharField(db_column='householdType', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'business_personnelinf'


class BusinessReview(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    periodid = models.IntegerField(db_column='periodId', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=1, blank=True)
    supplierid = models.IntegerField(db_column='supplierId', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'business_review'


class BussinessReviewTags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tagsid = models.IntegerField(db_column='tagsId', blank=True, null=True)  # Field name made lowercase.
    reviewid = models.IntegerField(db_column='reviewId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bussiness_review_tags'


class Childorder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parentid = models.CharField(db_column='parentId', max_length=100, blank=True)  # Field name made lowercase.
    status = models.TextField(blank=True)
    isconfirm = models.IntegerField(db_column='isConfirm', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(max_length=100, blank=True)
    filename = models.CharField(db_column='fileName', max_length=100, blank=True)  # Field name made lowercase.
    reportfilepath = models.CharField(db_column='reportFilePath', max_length=500, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)
    types = models.CharField(max_length=10, blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'childorder'


class CommunityArticle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100)  # Field name made lowercase.
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'community_article'


class CommunityArticleImages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    articleid = models.IntegerField(db_column='articleId', blank=True, null=True)  # Field name made lowercase.
    pictureid = models.IntegerField(db_column='pictureId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community_article_images'


class CommunityComments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    articleid = models.IntegerField(db_column='articleId', blank=True, null=True)  # Field name made lowercase.
    commentsid = models.IntegerField(db_column='commentsId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100)  # Field name made lowercase.
    content = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'community_comments'


class CommunityComplaints(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    articleid = models.IntegerField(db_column='articleId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100)  # Field name made lowercase.
    content = models.TextField(blank=True)
    isread = models.CharField(max_length=10)
    modifyby = models.CharField(db_column='modifyBy', max_length=100)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community_complaints'


class CommunityPicture(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100)  # Field name made lowercase.
    image = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'community_picture'


class Companyuser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    companytype = models.CharField(db_column='companyType', max_length=100, blank=True)  # Field name made lowercase.
    unifiedsocialcredit = models.CharField(db_column='unifiedSocialCredit', max_length=100, blank=True)  # Field name made lowercase.
    taxregistration = models.CharField(db_column='taxRegistration', max_length=100, blank=True)  # Field name made lowercase.
    registercode = models.CharField(db_column='registerCode', max_length=100, blank=True)  # Field name made lowercase.
    organizationcode = models.CharField(db_column='organizationCode', max_length=100, blank=True)  # Field name made lowercase.
    matterssummary = models.CharField(db_column='mattersSummary', max_length=100, blank=True)  # Field name made lowercase.
    accountservicestarttime = models.CharField(db_column='accountServiceStartTime', max_length=100, blank=True)  # Field name made lowercase.
    accountserviceendtime = models.CharField(db_column='accountServiceEndTime', max_length=100, blank=True)  # Field name made lowercase.
    accountcontactamount = models.DecimalField(db_column='accountContactAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accountcontactpaytype = models.CharField(db_column='accountContactPayType', max_length=100, blank=True)  # Field name made lowercase.
    accountmonthfee = models.DecimalField(db_column='accountMonthFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    billservicestarttime = models.CharField(db_column='billServiceStartTime', max_length=100, blank=True)  # Field name made lowercase.
    billserviceeendtime = models.CharField(db_column='billServiceeEndTime', max_length=100, blank=True)  # Field name made lowercase.
    billcontactamount = models.DecimalField(db_column='billContactAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    billcontactpaytype = models.CharField(db_column='billContactPayType', max_length=100, blank=True)  # Field name made lowercase.
    billmonthfee = models.DecimalField(db_column='billMonthFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    changetype = models.CharField(db_column='changeType', max_length=100, blank=True)  # Field name made lowercase.
    changefee = models.DecimalField(db_column='changeFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    logoutpaytype = models.CharField(db_column='logoutPayType', max_length=100, blank=True)  # Field name made lowercase.
    logoutfee = models.DecimalField(db_column='logoutFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    personnelagencypaytype = models.CharField(db_column='personnelAgencyPayType', max_length=100, blank=True)  # Field name made lowercase.
    personnelagencyfee = models.DecimalField(db_column='personnelAgencyFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    otheritempaytype = models.CharField(db_column='otherItemPayType', max_length=100, blank=True)  # Field name made lowercase.
    otheritemfee = models.DecimalField(db_column='otherItemFee', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signdate = models.CharField(db_column='signDate', max_length=100, blank=True)  # Field name made lowercase.
    signperson = models.CharField(db_column='signPerson', max_length=100, blank=True)  # Field name made lowercase.
    basesituation = models.CharField(db_column='baseSituation', max_length=500, blank=True)  # Field name made lowercase.
    billsituation = models.CharField(db_column='billSituation', max_length=500, blank=True)  # Field name made lowercase.
    changesituation = models.CharField(db_column='changeSituation', max_length=500, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)
    ishavecontact = models.CharField(db_column='isHaveContact', max_length=10, blank=True)  # Field name made lowercase.
    isrealcustomer = models.CharField(db_column='isRealCustomer', max_length=10, blank=True)  # Field name made lowercase.
    connector = models.CharField(max_length=100, blank=True)
    connectortel = models.CharField(db_column='connectorTel', max_length=100, blank=True)  # Field name made lowercase.
    connectoremail = models.CharField(db_column='connectorEmail', max_length=100, blank=True)  # Field name made lowercase.
    oldconnector = models.CharField(db_column='oldConnector', max_length=100, blank=True)  # Field name made lowercase.
    oldconnectortel = models.CharField(db_column='oldConnectorTel', max_length=100, blank=True)  # Field name made lowercase.
    agencyitem = models.CharField(db_column='agencyItem', max_length=100, blank=True)  # Field name made lowercase.
    agencysituation = models.CharField(db_column='agencySituation', max_length=500, blank=True)  # Field name made lowercase.
    operator = models.CharField(max_length=100, blank=True)
    customerservicer = models.CharField(db_column='customerServicer', max_length=100, blank=True)  # Field name made lowercase.
    ispaybonus = models.CharField(db_column='isPayBonus', max_length=10, blank=True)  # Field name made lowercase.
    failreason = models.CharField(db_column='failReason', max_length=500, blank=True)  # Field name made lowercase.
    revenuearea = models.CharField(db_column='revenueArea', max_length=100, blank=True)  # Field name made lowercase.
    powermanname = models.CharField(db_column='powermanName', max_length=100, blank=True)  # Field name made lowercase.
    powermantel = models.CharField(db_column='powermanTel', max_length=100, blank=True)  # Field name made lowercase.
    abouttaxsituation = models.CharField(db_column='aboutTaxSituation', max_length=500, blank=True)  # Field name made lowercase.
    financebankcode = models.CharField(db_column='financeBankCode', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companyuser'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey('RenrenUser')

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drawback(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amountno = models.CharField(db_column='amountNo', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    applyway = models.CharField(max_length=100, blank=True)
    reason = models.CharField(max_length=500, blank=True)
    accountcode = models.CharField(db_column='accountCode', max_length=50, blank=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=50, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    remark = models.CharField(max_length=500, blank=True)
    aduittime = models.CharField(db_column='aduitTime', max_length=100, blank=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drawback'


class Financeruserprice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ordertypeid = models.IntegerField(db_column='orderTypeId', blank=True, null=True)  # Field name made lowercase.
    taxpayerstype = models.CharField(max_length=100, blank=True)
    status = models.CharField(db_column='STATUS', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'financeruserprice'


class Financeuser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    isacceptorder = models.CharField(db_column='isAcceptOrder', max_length=100, blank=True)  # Field name made lowercase.
    idcard = models.CharField(max_length=18, blank=True)
    idcardimgpath = models.CharField(db_column='idCardImgPath', max_length=500, blank=True)  # Field name made lowercase.
    accountantno = models.CharField(db_column='accountantNo', max_length=50, blank=True)  # Field name made lowercase.
    accountantimgpath = models.CharField(db_column='accountantImgPath', max_length=500, blank=True)  # Field name made lowercase.
    degree = models.CharField(max_length=10, blank=True)
    workage = models.CharField(max_length=100, blank=True)
    certificateid = models.CharField(db_column='certificateId', max_length=20, blank=True)  # Field name made lowercase.
    certificateimgpath = models.CharField(db_column='certificateImgPath', max_length=500, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    specialty = models.CharField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    province = models.CharField(max_length=1000, blank=True)
    city = models.CharField(max_length=1000, blank=True)
    area = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    createtime = models.CharField(max_length=100, blank=True)
    modifytime = models.CharField(max_length=100, blank=True)
    aduittime = models.CharField(max_length=100, blank=True)
    auditcontent = models.CharField(db_column='auditContent', max_length=1000, blank=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True)  # Field name made lowercase.
    states = models.CharField(max_length=10, blank=True)
    connectaddress = models.CharField(db_column='connectAddress', max_length=500, blank=True)  # Field name made lowercase.
    isreceiveresume = models.CharField(db_column='isReceiveResume', max_length=10, blank=True)  # Field name made lowercase.
    ishavelicense = models.CharField(db_column='isHaveLicense', max_length=10, blank=True)  # Field name made lowercase.
    ishavecertificate = models.CharField(db_column='isHaveCertificate', max_length=10, blank=True)  # Field name made lowercase.
    isallservice = models.CharField(db_column='isAllService', max_length=10, blank=True)  # Field name made lowercase.
    isvisit = models.CharField(db_column='isVisit', max_length=10, blank=True)  # Field name made lowercase.
    visittime = models.CharField(db_column='visitTime', max_length=100, blank=True)  # Field name made lowercase.
    ishaveexp = models.CharField(db_column='isHaveExp', max_length=100, blank=True)  # Field name made lowercase.
    servicer = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=100, blank=True)
    idcardstarttime = models.CharField(db_column='idcardStartTime', max_length=100, blank=True)  # Field name made lowercase.
    idcardendtime = models.CharField(db_column='idcardEndTime', max_length=100, blank=True)  # Field name made lowercase.
    idcardagency = models.CharField(db_column='idcardAgency', max_length=100, blank=True)  # Field name made lowercase.
    idcardagencycode = models.CharField(db_column='idcardAgencyCode', max_length=100, blank=True)  # Field name made lowercase.
    idcardaddress = models.CharField(db_column='idcardAddress', max_length=100, blank=True)  # Field name made lowercase.
    idcardpostcode = models.CharField(db_column='idcardPostcode', max_length=100, blank=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=100, blank=True)  # Field name made lowercase.
    bankid = models.CharField(db_column='bankId', max_length=100, blank=True)  # Field name made lowercase.
    iscommitcmbc = models.CharField(db_column='isCommitCMBC', max_length=10, blank=True)  # Field name made lowercase.
    cmbcaccountid = models.CharField(db_column='CMBCaccountId', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financeuser'


class LegalOrderdetail(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    legalserviceid = models.IntegerField(db_column='legalServiceId', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'legal_orderdetail'


class Legalservice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
        managed = False
        db_table = 'legalservice'


class ManageBank(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    bank = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'manage_bank'


class ManageCertificate(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    createtime = models.CharField(db_column='createTime', max_length=100)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manage_certificate'


class ManageComments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'manage_comments'


class ManageIndexpic(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    imagepath = models.CharField(db_column='imagePath', max_length=500, blank=True)  # Field name made lowercase.
    isused = models.CharField(db_column='isUsed', max_length=100, blank=True)  # Field name made lowercase.
    url = models.CharField(max_length=500, blank=True)
    type = models.CharField(db_column='TYPE', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'manage_indexpic'


class ManageOrdertype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=100, blank=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manage_ordertype'


class ManagePark(models.Model):
    id = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=300, blank=True)
    parkname = models.CharField(db_column='parkName', max_length=300, blank=True)  # Field name made lowercase.
    servicesproviderid = models.IntegerField(db_column='servicesProviderId', blank=True, null=True)  # Field name made lowercase.
    renrenid = models.IntegerField(db_column='renrenId', blank=True, null=True)  # Field name made lowercase.
    companycount = models.IntegerField(db_column='companyCount', blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300, blank=True)
    cityarea = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=300, blank=True)
    area = models.CharField(max_length=300, blank=True)
    type = models.CharField(max_length=300, blank=True)
    introduction = models.TextField(blank=True)
    content = models.TextField(blank=True)
    imagepaths = models.CharField(db_column='imagePaths', max_length=1500, blank=True)  # Field name made lowercase.
    parkworkprice = models.DecimalField(db_column='parkWorkPrice', max_digits=22, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=22, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=12, blank=True, null=True)
    status = models.CharField(max_length=3, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=300, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=300, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=300, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=300, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=1500, blank=True)

    class Meta:
        managed = False
        db_table = 'manage_park'


class ManageTags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tags = models.CharField(max_length=50, blank=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage_tags'


class ManageVersion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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
        managed = False
        db_table = 'manage_version'


class News(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(max_length=200, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=20, blank=True)  # Field name made lowercase.
    receiver = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    sender = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'news'


class OrderCompany(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    orderid = models.CharField(max_length=100, blank=True)
    companyid = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    reportfilepath = models.CharField(db_column='reportFilePath', max_length=500, blank=True)  # Field name made lowercase.
    types = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'order_company'


class Parkhireorder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    orderid = models.IntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    parkid = models.IntegerField(db_column='parkId', blank=True, null=True)  # Field name made lowercase.
    station = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parkhireorder'


class RegisterChannel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    channel = models.CharField(max_length=255, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'register_channel'


class RegisterCoupons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(max_length=100, blank=True)
    quota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    conditions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True)  # Field name made lowercase.
    properties = models.CharField(max_length=100, blank=True)
    activityid = models.CharField(db_column='activityId', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'register_coupons'


class RenrenUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=200, blank=True)
    iconpath = models.CharField(db_column='iconPath', max_length=100, blank=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    remark = models.CharField(max_length=500, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=12, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    last_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    defaultexaddid = models.IntegerField(db_column='defaultexaddId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'renren_user'


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


class Skilledfield(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    discription = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=1, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skilledfield'


class Sysnews(models.Model):
    id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=600, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=60, blank=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=60, blank=True)  # Field name made lowercase.
    receiver = models.CharField(max_length=60, blank=True)
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'sysnews'


class TDepartment(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    number = models.CharField(db_column='NUMBER', max_length=100, blank=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=100, blank=True)  # Field name made lowercase.
    create_date = models.CharField(db_column='CREATE_DATE', max_length=100, blank=True)  # Field name made lowercase.
    create_user = models.CharField(db_column='CREATE_USER', max_length=200, blank=True)  # Field name made lowercase.
    modify_date = models.CharField(db_column='MODIFY_DATE', max_length=100, blank=True)  # Field name made lowercase.
    modify_user = models.CharField(db_column='MODIFY_USER', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_department'


class TJob(models.Model):
    job_id = models.BigIntegerField(db_column='JOB_ID', primary_key=True)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=50, blank=True)  # Field name made lowercase.
    group_id = models.BigIntegerField(db_column='GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.BigIntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    job_type = models.BigIntegerField(db_column='JOB_TYPE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=200, blank=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=32, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_job'


class TJobRole(models.Model):
    job_id = models.BigIntegerField(db_column='JOB_ID')  # Field name made lowercase.
    role_id = models.BigIntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_job_role'


class TJobUser(models.Model):
    job_id = models.BigIntegerField(db_column='JOB_ID')  # Field name made lowercase.
    user_id = models.BigIntegerField(db_column='USER_ID')  # Field name made lowercase.
    default_job = models.BigIntegerField(db_column='DEFAULT_JOB', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    expand1 = models.CharField(db_column='EXPAND1', max_length=32, blank=True)  # Field name made lowercase.
    expand2 = models.CharField(db_column='EXPAND2', max_length=32, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_job_user'


class TOrganization(models.Model):
    group_id = models.BigIntegerField(db_column='GROUP_ID', primary_key=True)  # Field name made lowercase.
    admins_code = models.CharField(db_column='ADMINS_CODE', max_length=10, blank=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=50, blank=True)  # Field name made lowercase.
    parent_id = models.BigIntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True)  # Field name made lowercase.
    contact_name = models.CharField(db_column='CONTACT_NAME', max_length=32, blank=True)  # Field name made lowercase.
    post_code = models.CharField(db_column='POST_CODE', max_length=10, blank=True)  # Field name made lowercase.
    group_type = models.BigIntegerField(db_column='GROUP_TYPE', blank=True, null=True)  # Field name made lowercase.
    group_type_name = models.CharField(db_column='GROUP_TYPE_NAME', max_length=128, blank=True)  # Field name made lowercase.
    priority = models.BigIntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=200, blank=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    expand1 = models.CharField(db_column='EXPAND1', max_length=32, blank=True)  # Field name made lowercase.
    expand2 = models.CharField(db_column='EXPAND2', max_length=32, blank=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=32, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_organization'


class TResource(models.Model):
    resource_id = models.BigIntegerField(db_column='RESOURCE_ID', blank=True, null=True)  # Field name made lowercase.
    resource_name = models.CharField(db_column='RESOURCE_NAME', max_length=600, blank=True)  # Field name made lowercase.
    resource_detail_name = models.CharField(db_column='RESOURCE_DETAIL_NAME', max_length=600, blank=True)  # Field name made lowercase.
    father_resource_id = models.BigIntegerField(db_column='FATHER_RESOURCE_ID', blank=True, null=True)  # Field name made lowercase.
    resource_type = models.BigIntegerField(db_column='RESOURCE_TYPE', blank=True, null=True)  # Field name made lowercase.
    resource_url = models.CharField(db_column='RESOURCE_URL', max_length=765, blank=True)  # Field name made lowercase.
    resource_order = models.BigIntegerField(db_column='RESOURCE_ORDER', blank=True, null=True)  # Field name made lowercase.
    resource_icon = models.CharField(db_column='RESOURCE_ICON', max_length=600, blank=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=1500, blank=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE', blank=True, null=True)  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=150, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_resource'


class TRole(models.Model):
    role_id = models.BigIntegerField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=50, blank=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=200, blank=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role'


class TRoleResource(models.Model):
    role_id = models.BigIntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    resource_id = models.BigIntegerField(db_column='RESOURCE_ID')  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    expand1 = models.CharField(db_column='EXPAND1', max_length=32, blank=True)  # Field name made lowercase.
    expand2 = models.CharField(db_column='EXPAND2', max_length=32, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_resource'


class TRoleUser(models.Model):
    role_id = models.BigIntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    user_id = models.BigIntegerField(db_column='USER_ID')  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE')  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.
    data_state = models.BigIntegerField(db_column='DATA_STATE', blank=True, null=True)  # Field name made lowercase.
    expand1 = models.CharField(db_column='EXPAND1', max_length=32, blank=True)  # Field name made lowercase.
    expand2 = models.CharField(db_column='EXPAND2', max_length=32, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_role_user'


class TUser(models.Model):
    user_id = models.BigIntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=200, blank=True)  # Field name made lowercase.
    login_name = models.CharField(db_column='LOGIN_NAME', max_length=200, blank=True)  # Field name made lowercase.
    register_time = models.DateTimeField(db_column='REGISTER_TIME', blank=True, null=True)  # Field name made lowercase.
    department_id = models.CharField(db_column='DEPARTMENT_ID', max_length=20, blank=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=200, blank=True)  # Field name made lowercase.
    is_leader = models.CharField(db_column='IS_LEADER', max_length=2, blank=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='HOME_PHONE', max_length=15, blank=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=15, blank=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=500, blank=True)  # Field name made lowercase.
    password_records = models.CharField(db_column='PASSWORD_RECORDS', max_length=200, blank=True)  # Field name made lowercase.
    user_state = models.BigIntegerField(db_column='USER_STATE', blank=True, null=True)  # Field name made lowercase.
    is_receive = models.CharField(db_column='IS_RECEIVE', max_length=10, blank=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    create_user = models.BigIntegerField(db_column='CREATE_USER', blank=True, null=True)  # Field name made lowercase.
    modify_date = models.DateTimeField(db_column='MODIFY_DATE', blank=True, null=True)  # Field name made lowercase.
    modify_user = models.BigIntegerField(db_column='MODIFY_USER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'


class UserCompany(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=100, blank=True)  # Field name made lowercase.
    taxpayerstype = models.CharField(db_column='taxPayersType', max_length=100, blank=True)  # Field name made lowercase.
    companyproperty = models.CharField(db_column='companyProperty', max_length=100, blank=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=2, blank=True)
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'user_company'


class UserExpressadd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    recipient = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    expressprovince = models.CharField(db_column='expressProvince', max_length=1000, blank=True)  # Field name made lowercase.
    expresscity = models.CharField(db_column='expressCity', max_length=1000, blank=True)  # Field name made lowercase.
    expressarea = models.CharField(db_column='expressArea', max_length=1000, blank=True)  # Field name made lowercase.
    expressstreet = models.CharField(db_column='expressStreet', max_length=1000, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'user_expressadd'


class UserWorkexperience(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(max_length=1000, blank=True)
    position = models.CharField(db_column='POSITION', max_length=1000, blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.
    modifytime = models.CharField(db_column='modifyTime', max_length=100, blank=True)  # Field name made lowercase.
    modifyby = models.CharField(db_column='modifyBy', max_length=100, blank=True)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'user_workexperience'


class Usertest(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=50, blank=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertest'


class Withdrawal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amountno = models.CharField(db_column='amountNo', max_length=100, blank=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=100, blank=True)  # Field name made lowercase.
    applyway = models.CharField(max_length=100, blank=True)
    accountcode = models.CharField(db_column='accountCode', max_length=50, blank=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=50, blank=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True)
    remark = models.CharField(max_length=500, blank=True)
    aduittime = models.CharField(db_column='aduitTime', max_length=100, blank=True)  # Field name made lowercase.
    aduitby = models.CharField(db_column='aduitBy', max_length=100, blank=True)  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=100, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'withdrawal'
