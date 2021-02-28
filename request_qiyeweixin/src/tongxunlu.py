# -*- coding: utf-8 -*-
from request_qiyeweixin.src.base import Base

class TongXunLu(Base):

    # 在通讯录查询用户
    def get_member(self, userid="FuJinJie"):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        param = {"userid" : userid}
        member = self.send("get",url, params=param)
        return member

    # 在通讯录添加用户
    def add_member(self, userid:str, name:str, mobile:str, department:list):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
                }
        r = self.send("post",url, json=data)
        return r

    # 在通讯录更新一用户
    def update_member(self, userid:str, name:str, mobile:str, department:list):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send("post",url, json=data)
        return r

    # 在通讯录删除用户
    def delete_member(self, userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        param = {"userid" : userid}
        r = self.send("get",url, params=param)
        return r




if __name__ == "__main__":
    res = TongXunLu().get_member("JieFu")
    # res = TongXunLu().delete_member("JieFu")
    # res = TongXunLu().add_member("JieFu","jiejie2","+86 13200000008",[2])
    print(res)
