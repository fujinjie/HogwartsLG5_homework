# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from xueqiu_app.handle_black import handle_black


class BasePage:


    def __init__(self, driver:webdriver = None):
            self.driver = driver

    def teardown(self):
        self.driver.quit()

    @handle_black
    def find(self, by, locator):
        by_locator = (by, locator)
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(by_locator))
        return ele

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_and_clear(self, by, locator):
        self.find(by, locator).clear()

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(*element)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)