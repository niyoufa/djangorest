# coding=utf-8
import os
import json
import unittest
import logging


from others.rong import ApiClient

app_key = "vnroth0krxl2o"
app_secret = "3oU3Ca4uNij"

#您应该将key 和 secret 保存在服务器的环境变量中    
os.environ.setdefault('rongcloud_app_key', app_key)
os.environ.setdefault('rongcloud_app_secret', app_secret)

logging.basicConfig(level=logging.INFO)

api = ApiClient()