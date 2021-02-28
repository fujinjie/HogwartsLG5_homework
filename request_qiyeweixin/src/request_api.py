# -*- coding: utf-8 -*-
import pytest
import requests

from base import Base

class RequestApi(Base):

    def get_api(self, url, params=None):
        url = url
        r = requests.get(url, params)
        return r


    def post_api(self, url, data):
        url = url
        datas = data
        r = requests.post(url, json=datas)
        return r


    def put_api(self):
        pass


    def delete_api(self):
        pass


    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww4fbc31a57f29a32b" \
              "&corpsecret=xKsi-wJ6ZUt2uSYo5R49kE8lJlGqrMjHs5SbjmC6P04"
        r = self.get_api(url)
        token = r.json()['access_token']
        print('成功获取到token：', token)
        return token

if __name__ == '__main__':
    r = RequestApi().get_token()
