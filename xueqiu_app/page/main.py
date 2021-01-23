# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.hangqing_page import HangQingPage
from xueqiu_app.page.jiaoyi_page import JiaoYiPage


class Main(BasePage):

    def goto_hangqing_page(self):
        self.find_and_click(MobileBy.ID, "com.xueqiu.android:id/action_message")
        self.find_and_click(MobileBy.XPATH, '//*[@text = "行情"]')
        return HangQingPage(self.driver)

    def goto_jiaoyi_page(self):
        self.find_and_click(MobileBy.XPATH, '//*[@text = "交易"]')
        return JiaoYiPage(self.driver)