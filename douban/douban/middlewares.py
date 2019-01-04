# -*- coding: utf-8 -*-
import base64
import random
from settings import USER_AGENTS
from settings import PROXYS

class RandomUserAgent(object):
    def process_request(self,request,spider):
        #随机选择useragent
        useragent = random.choice(USER_AGENTS)
        #print useragent
        #修改useragent
        request.headers.setdefault("User-Agent",useragent)

class RandomProxy(object):
    def process_request(self, request, spider):

        pass
        """
        
        #随机选择代理
        proxy = random.choice(PROXYS)
        #print proxy
        #如果没有账号验证
        if proxy['user_passwd'] is None:
            request.meta['proxy'] = "http://" + proxy['ip_port']

        else:
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            request.meta['proxy'] = "http://" + proxy['ip_port']
            #basic后面有个空格
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

        """