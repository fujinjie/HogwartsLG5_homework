# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from qiyeweixin_app.page.address_page import AddressPage
from qiyeweixin_app.page.base_page import BasePage
from qiyeweixin_app.page.message_page import MessagePage



class Main(BasePage):

    def goto_message_page(self):
        self.find_and_click(MobileBy.XPATH, '//*[@text = "消息"]')
        return MessagePage(self.driver)

    def goto_address_page(self):
        self.find_and_click(MobileBy.XPATH, '//*[@text = "通讯录"]')
        return AddressPage(self.driver)