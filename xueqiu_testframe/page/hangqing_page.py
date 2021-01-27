# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu_testframe.page.base_page import BasePage


class HangQingPage(BasePage):

    def search(self):
        self.run_steps("../page/hangqing_page.yaml", "search")
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
                print("该元素无text属性")
        print(memberlist)
        return memberlist


