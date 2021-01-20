# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from qiyeweixin_app.page.base_page import BasePage


class AddressPage(BasePage):

    def add_member(self):
        self.scroll_find_click("添加成员")
        self.find_and_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        self.finds(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b78"]')[0].send_keys("小源03") # 在姓名输入框中输入
        self.find_and_send(MobileBy.XPATH, '//*[@text="手机号"]', '13200000006') # 输入手机号
        self.find_and_click(MobileBy.XPATH, '//*[@text="设置部门"]')
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"确定")]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/idp"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/idp"]')
        return self.member_list()

    def member_list(self):
        memberlist = []
        locator = (MobileBy.XPATH, '//*[@class="android.widget.TextView"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        elements = self.finds(*locator)
        for element in elements:
            try:
                ele_text = element.get_attribute("text")
                memberlist.append(ele_text)
            except:
                print("该元素无text")
        print(memberlist)
        return memberlist


