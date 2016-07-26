#-*- coding:utf-8 -*-
import six, re, time, datetime
import logging
import xml.etree.ElementTree as ET
#############alipay##################
from pay.conf import wapalipay
#############wxpay#######################
from weixin.backends.dj import Helper, sns_userinfo
from weixin import WeixinHelper, JsApi_pub, WxPayConf_pub, UnifiedOrder_pub, Notify_pub, catch
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rr_user.models import User,UserCompany
from others.models import CompanyUser
from business.models import Order, Express, Express_Order
from others.models import News
from django.core.urlresolvers import reverse
from urlparse import unquote
from register.run import aliyun_sendmsg

logger1 =logging.getLogger(settings.LOGGING_ALIPAY)
logger1.setLevel(logging.INFO)
logger1.addHandler (logging.FileHandler(settings.LOGGING_ALIPAY))
logger2 =logging.getLogger(settings.LOGGING_WXIPAY)
logger2.setLevel(logging.INFO)
logger2.addHandler (logging.FileHandler(settings.LOGGING_WXIPAY))
# Create your views here.第一个发送给四个联系人：张峻18101846677，慈一林：13122111314，张明：18516114095，韦凯：13980996408
name = '胡霞'
tel1 = '18101846677'#张峻
tel2 = '13122111314'#慈一林
tel3 = '18516114095'#张明
tel4 = '13980996408'#韦凯
def arrayToXml(**arr):
        """array转xml"""
        xml = ["<xml>"]
        for k, v in arr.items():
            if v.isdigit():
                xml.append("<%s>%s</%s>"%(k,v,k))
            else:
                xml.append("<%s><![CDATA[%s]]></%s>"%(k,v,k))
        xml.append("</xml>")
        return "".join(xml)
@csrf_exempt
def notify(request,payway='alipay'):
    success={'return_code':'SUCCESS'}
    fail={'return_code':'FAIL'}
    if request.method == "POST":
        result_code="FAIL"
        if payway=='alipay':
            logger=logger1
            logger.info ('>>进入支付宝异步通知接口...')
            params=request.POST.copy()
            tree={}
            for p in params:
                try:
                    tree[p.encode('utf-8')]=params[p].encode('utf-8')
                except:
                    tree[p.encode('utf-8')]=params[p][0].encode('utf-8')
            out_trade_no = tree['out_trade_no'].split('_')[0]
            attach = tree['out_trade_no'].split('_')[1]
            paytime = tree.get('gmt_payment')
            apamount = tree['total_fee']
            logger1.info(tree['trade_status'])
            if tree['trade_status']=="TRADE_SUCCESS":
                result_code="SUCCESS"
        elif payway=='wap':
            logger=logger1
            logger.info ('>>进入支付宝网页支付异步通知接口...')
            params=request.POST.copy()
            if wapalipay.verify_notify(**params):
                if 'notify_data' in params:
                    notifydata = unquote(params['notify_data'])
                    if isinstance(notifydata, str):
                        notifydata = six.u(notifydata).encode('utf-8')
                    elif isinstance(notifydata, six.string_types):
                        notifydata = notifydata.encode('utf-8')
                    tree = ET.ElementTree(ET.fromstring(notifydata))
                    out_trade_no = tree.find("out_trade_no").text.split('_')[0]
                    attach = tree.find("out_trade_no").text.split('_')[1]
                    paytime = tree.get('gmt_payment')
                    apamount = tree['total_fee']
                    trade_status = tree.find("trade_status").text
                    logger1.info(trade_status)
                    if trade_status == 'TRADE_SUCCESS':
                        result_code="SUCCESS"
        elif payway=='weixin':
            logger=logger2
            logger.info ('>>进入微信支付异步通知接口...')
            params = request.body
            tree = ET.ElementTree(ET.fromstring(params))
            return_code = tree.find("return_code").text
            if return_code=="SUCCESS":
                result_code = tree.find("result_code").text
                out_trade_no = tree.find("out_trade_no").text
                attach = tree.find("attach").text
                paytime = datetime.datetime.strptime(tree.find("time_end").text, '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
                apamount = float(tree.find("total_fee").text)/100
        if result_code=="SUCCESS":
            logger.info('>>订单 %s 支付成功,订单长度%s'%(out_trade_no,len(out_trade_no)))
            if len(out_trade_no)==18:
                neworder = Order.objects.get(orderNo=out_trade_no)
                logger.info('更改订单状态...')
                neworder.order_status ='3'
                neworder.paytime =paytime
                neworder.apamount =apamount
                neworder.save ()
                logger.info('>>订单 %s 的状态改为 服务中'%out_trade_no)
                usertype=out_trade_no[-5]
                context={'tel':'13248268832'}
                c1 = {}
                user=servicesprovider=None
                if neworder.userid:
                    user=User.objects.get(id=neworder.userid)
                if neworder.servicesproviderid:
                    servicesprovider=User.objects.get(id=neworder.servicesproviderid)
                if user:
                    context['tel'] = user.username[:-2].encode('utf-8')
                    if user.name:
                        context['name'] = user.name.encode('utf-8')
                if servicesprovider:
                    c1['tel'] = servicesprovider.username[:-2].encode('utf-8')
                    if servicesprovider.name:
                        c1['name'] = servicesprovider.name.encode('utf-8')
                p=re.compile('^(0|86|17951)?(13[0-9]|15[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}$')
                mobilematch=p.match(context['tel'])
                if mobilematch:
                    if usertype in ['1','6','7','8','9']:
                        if servicesprovider:
                            aliyun_sendmsg(context['tel'], 1270, **c1)
                            aliyun_sendmsg(c1['tel'], 1268, **context)
                        else:
                            aliyun_sendmsg(context['tel'], 1451)
                            # aliyun_sendmsg(tel3, 1268,**context)

                    elif usertype in ['3','4','5']:
                        aliyun_sendmsg(context['tel'], 1451)
                if float(apamount) == 1:
                    aliyun_sendmsg('13248268832', 1268, **context)
                    orderdetail = {'customer':context.get(name),'orderNumber':out_trade_no,'customerTel':context['tel']}
                    companyid=neworder.companyid
                    try:
                        orderdetail['businessAdd'] = UserCompany.objects.get(id=companyid).address
                    except:
                        pass
                    try:
                        orderdetail['registereAdd'] = CompanyUser.objects.get(id=companyid).revenueArea
                    except:
                        pass
                    aliyun_sendmsg(tel1, 3821, **orderdetail)
                    aliyun_sendmsg(tel2, 3821, **orderdetail)
                    aliyun_sendmsg(tel3, 3821, **orderdetail)
                    aliyun_sendmsg(tel4, 3821, **orderdetail)
                else:
                    aliyun_sendmsg(tel1, 1267, **context)
                if attach!=out_trade_no:
                    oldorder = Order.objects.get(orderNo=attach)
                    oldorder.isrenewal = '1'
                    oldorder.save()
                    logger.info('>>订单 %s 的状态改为 已续费'%attach)
            elif len(out_trade_no)==14:
                express = Express.objects.get(expressorderNo=out_trade_no)
                order = Express_Order.objects.filter(expressid=express.id).values_list('id', flat=True)
                logger.info('更改快递订单的订单状态...')
                Order.objects.filter(id__in=order).update(ismkinvoice="已开票")
                logger.info('>>快递订单 %s 中的订单改为 已开票'%out_trade_no)
            else:
                logger.info('这是什么订单？')
            if payway=='weixin':
                logger.info('>>返回 %s '%arrayToXml(**success))
                return HttpResponse (arrayToXml(**success))
            logger.info('>>返回 success ')
            return HttpResponse ("success")
        else:
            logger.info('>>订单 %s 支付失败'%out_trade_no)
    if payway=='weixin':
        logger.info('>>返回 %s '%arrayToXml(**fail))
        return HttpResponse (arrayToXml(**fail))
    logger.info('>>返回 fail ')
    return HttpResponse ("fail")

@csrf_exempt
def create_direct_pay(request):
    if request.method == "POST":
        return_url='http://139.196.33.243/pay.html'
        notify_url='http://121.40.219.131:8100/pay/notify/'
        params = {'out_trade_no': request.POST.get('orderNo'),
                  'subject': u'测试',
                  'total_fee': request.POST.get('amount'),
                  'seller_account_name': wapalipay.seller_email,
                  'call_back_url': return_url,
                  'notify_url': notify_url}       
        url=wapalipay.create_direct_pay_by_user_url(**params)
        return HttpResponse (url)
    return HttpResponseRedirect (reverse ('pay_error'))
# @csrf_exempt
# @sns_userinfo
# @catch
def jspay(request):
    openid = request.GET.get('openid')
    print openid
    amount = request.GET.get("amount") or "0.01"  
    money = int(float(amount)*100)
    jsApi = JsApi_pub()
    unifiedOrder = UnifiedOrder_pub()
    unifiedOrder.setParameter("openid",openid) #商品描述
    unifiedOrder.setParameter("body",request.GET.get('subject','一元财税包')) #商品描述
    timeStamp = time.time()
    out_trade_no = "{0}{1}".format(WxPayConf_pub.APPID, int(timeStamp*100))
    unifiedOrder.setParameter("out_trade_no", request.GET.get('order_sn', out_trade_no)) #商户订单号
    unifiedOrder.setParameter("total_fee", str(money)) #总金额
    unifiedOrder.setParameter("notify_url", WxPayConf_pub.NOTIFY_URL) #通知地址 
    unifiedOrder.setParameter("trade_type", "JSAPI") #交易类型
    unifiedOrder.setParameter("attach", request.GET.get('order_id','test')) #附件数据，可分辨不同商家(string(127))
    try:
        prepay_id = unifiedOrder.getPrepayId()
        if isinstance(prepay_id, dict):
            return HttpResponse(prepay_id.get("err_code_des"))
        jsApi.setPrepayId(prepay_id)
        jsApiParameters = jsApi.getParameters()
    except Exception as e:
        print(e)
    else:
        print jsApiParameters
        return HttpResponse(jsApiParameters)
    
# @csrf_exempt
@sns_userinfo
def paytest(request):
    response = render_to_response("pay/pay.html",{'openid': request.openid})
    response.set_cookie("openid", request.openid)
    return response

@sns_userinfo
def paytestb(request):
    return redirect("http://dev.i-caiwu.com/wxpay/wx/www/index.html#/app/index?openid={0}".format(request.openid))
