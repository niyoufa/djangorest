# -*- coding: utf-8 -*-
from django import forms

class UploadImg(forms.Form):
    img = forms.FileField()
    obj = forms.CharField()
    pk = forms.IntegerField()
    type = forms.CharField()
    
def size(w,h):
    x = (h-w)/2
    if x>=0:
        x1=0
        y1=x
        x2=w
        y2=(h+w)/2
        a=w
    elif x<0:
        x1=-x
        y1=0
        x2=(h+w)/2
        y2=h
        a=h
    else:
        return u'系统错误'
    return [a,(x1,y1,x2,y2)]
        
        

    
    