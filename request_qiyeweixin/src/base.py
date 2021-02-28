# -*- coding: utf-8 -*-
import requests

class Base:

    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww4fbc31a57f29a32b" \
              "&corpsecret=xKsi-wJ6ZUt2uSYo5R49kE8lJlGqrMjHs5SbjmC6P04"
        r = requests.get(url)
        token = r.json()['access_token']
        self.s = requests.Session()
        self.s.params = {'access_token' : token}
        # print('成功获取到token：', token)


    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()

