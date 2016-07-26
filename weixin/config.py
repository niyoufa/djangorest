#coding:utf-8
'''
Created on 2014-5-13

@author: skycrab
'''

class WxPayConf_pub(object):
    """配置账号信息"""

    #=======【基本信息设置】=====================================
    #微信公众号身份的唯一标识。审核通过后，在微信发送的邮件中查看
    APPID = "wx64044fed7dce3c24"
    #JSAPI接口中获取openid，审核后在公众平台开启开发模式后可查看
    APPSECRET = "ed4ac3afd566f266e45719754eb333c8"
    #接口配置token
    TOKEN = "wang123qwe"
    #受理商ID，身份标识
    MCHID = "1313787401"
    #商户支付密钥Key。审核通过后，在微信发送的邮件中查看
    KEY = "icaiwuzixunshanghaiyouxiangongsi"
   

    #=======【异步通知url设置】===================================
    #异步通知url，商户根据实际开发过程设定
    NOTIFY_URL = "http://dev.i-caiwu.com:8100/pay/weixinnotify/"

    #=======【证书路径设置】=====================================
    #证书路径,注意应该填写绝对路径
    SSLCERT_PATH = "/var/www/api/util/wxpay/cacert/apiclient_cert.pem"
    SSLKEY_PATH = "/var/www/api/util/wxpay/cacert/apiclient_key.pem"

    #=======【curl超时设置】===================================
    CURL_TIMEOUT = 30

    #=======【HTTP客户端设置】===================================
    HTTP_CLIENT = "CURL"  # ("URLLIB", "CURL", "REQUESTS")


