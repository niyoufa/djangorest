# -*- coding: utf-8 -*-
from rest_framework import serializers
from register.models import Coupons
import datetime

class CouponsSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    def get_status(self,instance):
        today=datetime.date.today().strftime("%Y-%m-%d")
        if today>instance.endtime:
            status = u"已失效"
        elif today<instance.starttime:
            status = u"未生效"
        else :
            status = u"未使用"
        if instance.status=="0":
            status = u"已使用"
        if instance.status=="1":
            status = u"未使用"
        if instance.status=="2":
            status = u"已失效"
        return status
    class Meta:
        model = Coupons
        exclude = ()

