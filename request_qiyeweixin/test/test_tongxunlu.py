# -*- coding: utf-8 -*-
from request_qiyeweixin.src.tongxunlu import TongXunLu
import pytest

class TestTongXunLu:

    def setup(self):
        self.tongxunlu = TongXunLu()

    @pytest.mark.parametrize("userid,name,mobile,department", [("JieFu","jiejie2","+86 13200000008",[2])])
    def test_add_member(self,userid:str, name:str, mobile:str, department:list ):
        try:
            # 数据清洗：先删除用户
            r = self.tongxunlu.delete_member(userid=userid)
            if r.get("errmsg") == "deleted":
                print(f"{userid} 删除成功")
        except:
            print("该用户不存在")
        finally:
            # 添加用户
            r = self.tongxunlu.add_member(userid, name, mobile, department)
            if r.get("errmsg") == "created":
                print(f"{userid} 添加成功")
            # 查询新添加的用户
            get_member = self.tongxunlu.get_member(userid=userid)
        assert get_member.get("userid") == userid


if __name__ == "__main__":
    pytest.main(['-v', '-s', 'test_tongxunlu.py'])