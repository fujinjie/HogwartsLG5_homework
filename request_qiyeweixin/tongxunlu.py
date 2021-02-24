# -*- coding: utf-8 -*-
from request_api import RequestApi

class TongXunLu(RequestApi):

    # 在通讯录查询用户
    def get_member(self, userid="FuJinJie"):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        param = {"access_token" : token, "userid" : userid}
        member = self.get_api(url=url, params=param).json()
        return member

    # 在通讯录添加用户
    def add_member(self):
        token = self.get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        data = {
                "userid": "jiejie1",
                "name": "Jie",
                "mobile": "+86 13200000002",
                "department": [2]
                }
        r = self.post_api(url=url, data=data).json()
        return r

    # 在通讯录更新一用户
    def update_member(self):
        token = self.get_token()
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        data = {
            "userid": "jiejie1",
            "name": "Jie1",
            "mobile": "+86 13200000002",
            "department": [2]
        }
        r = self.post_api(url=url, data=data).json()
        return r

    # 在通讯录删除用户
    def delete_member(self, userid):
        token = self.get_token()
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        param = {"access_token" : token, "userid" : userid}
        r = self.get_api(url=url, params=param).json()
        return r




if __name__ == "__main__":
    res = TongXunLu().delete_member("jiejie1")
    print(res)
