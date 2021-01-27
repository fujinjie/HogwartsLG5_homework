# -*- coding: utf-8 -*-
'''
basepage.find 函数的装饰器 ：： 用于处理黑名单弹框，保证业务进行
'''
from selenium.webdriver.common.by import By


def handle_black(fun):
    def run(*args, **kwargs):
        # 黑名单列表
        black_list = [(By.ID, "com.xueqiu.android:id/action_back")]
        by_self = args[0]
        try:
            # 如果找到对象就把对象返回
            ele = fun(*args, **kwargs)
            return ele
        except Exception as e:
            # 如果没有找到对象就遍历黑名单列表
            for black in black_list:
                eles = by_self.driver.find_elements(*black)
                # 如果黑名单中的元素存在，就对该元素进行处理
                if len(eles) > 0:
                    eles[0].click()
                    ele = fun(*args, **kwargs)
                    return ele
            raise e
    return run
