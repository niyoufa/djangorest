# -*- coding: utf-8 -*-
from django.db import models

class Coupons(models.Model):
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
        db_table = 'register_coupons'