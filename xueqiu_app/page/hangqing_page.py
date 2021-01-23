# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu_app.page.base_page import BasePage


class HangQingPage(BasePage):

    def search(self):
        self.find_and_click(MobileBy.ID, "com.xueqiu.android:id/action_search") # 点击搜索icon
        self.find_and_send(MobileBy.ID, "com.xueqiu.android:id/search_input_text", '阿里巴巴') # 在搜索框输入
        return self.search_results_list()

    def search_results_list(self):
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


