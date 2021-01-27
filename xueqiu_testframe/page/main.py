# -*- coding: utf-8 -*-
from xueqiu_testframe.page.base_page import BasePage
from xueqiu_testframe.page.hangqing_page import HangQingPage
from xueqiu_testframe.page.jiaoyi_page import JiaoYiPage


class Main(BasePage):

    def goto_hangqing_page(self):
        self.run_steps("../page/main.yaml", "goto_hangqing_page")
        return HangQingPage(self.driver)

    def goto_jiaoyi_page(self):
        self.run_steps("../page/main.yaml", "goto_jiaoyi_page")
        return JiaoYiPage(self.driver)