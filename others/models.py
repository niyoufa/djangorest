# -*- coding: utf-8 -*-

from django.db import models

#消息        
class News(models.Model):
    content = models.CharField(max_length=200, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=20, blank=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='receiver', max_length=20, blank=True)
    title = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    user1 = models.CharField(db_column='sender', max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'news'

class Sysnews(models.Model):
    content = models.CharField(max_length=600, blank=True)
    createtime = models.CharField(db_column='createTime', max_length=60, blank=True)  # Field name made lowercase.
    isread = models.CharField(db_column='isRead', max_length=60, blank=True)  # Field name made lowercase.
    receiver = models.CharField(max_length=60, blank=True)
    title = models.CharField(max_length=150, blank=True)

    class Meta:
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



class Usertest(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=50, blank=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20, blank=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usertest'
class CompanyUser(models.Model): 
    companyType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"公司性质")
    unifiedSocialCredit = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"统一社会信用证代码")
    taxRegistration = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"税务登记证号")
    registerCode = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"注册号")
    organizationCode = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"组织机构代码")
    mattersSummary = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"委托事项汇总")
    accountServiceStartTime = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键记账服务期限开始时间")
    accountServiceEndTime = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键记账服务期限结束时间")
    accountContactAmount = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"一键记帐合同总金额")
    accountContactPayType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键记账付款方式")
    accountMonthFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"一键记账月收费")
    billServiceStartTime = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键开票服务期限开始时间")
    billServiceeEndTime = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键开票服务期限结束时间")
    billContactAmount = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"一键开票合同总金额")
    billContactPayType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"一键开票付款方式")
    billMonthFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"一键开票月收费")
    changeType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"注册及变更付款方式")
    changeFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"客户注册及变更总收费")
    logoutPayType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"注销公司付款方式")
    logoutFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"客户注销公司总收费")
    personnelAgencyPayType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"人事代理付款方式")
    personnelAgencyFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"人事代理总收费")
    otherItemPayType = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"其他项目付款方式")
    otherItemFee = models.DecimalField(null=True, max_digits=10,decimal_places=2, verbose_name = u"其他项目总收费")
    signDate = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"合同签订日期")
    signPerson = models.IntegerField(blank=True, null=True, verbose_name = u"合同签订人")
    baseSituation = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"基本情况")
    billSituation = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"开票清卡认证情况")
    changeSituation = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"客户名称变更情况")
    remark = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"备注")
    isHaveContact = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"是否有合同")
    isRealCustomer = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"是否有效客户")
    connector = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"联系人姓名")
    connectorTel = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"联系人电话")
    connectorEmail = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"联系人邮箱")
    oldConnector = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"原联系人")
    oldConnectorTel = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"原联系人电话")
    agencyItem = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"外派事项")
    agencySituation = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"派单情况")
    operator = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"操作员")
    customerServicer = models.IntegerField(blank=True, null=True, verbose_name = u"客服")
    isPayBonus = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"是否支付工资")
    failReason = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"未能派单的原因")
    revenueArea = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"所在地的税务所")
    powermanName = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"专管员姓名")
    powermanTel = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"专管员电话")
    aboutTaxSituation = models.CharField(blank=True, null=True, max_length=500, verbose_name = u"涉税情况")
    financeBankCode = models.CharField(blank=True, null=True, max_length=100, verbose_name = u"外派记账员银行账号")
    
    class Meta:
        db_table = 'companyuser'