# -*- coding: utf-8 -*-
from appium import webdriver
from qiyeweixin_app.page.base_page import BasePage
from qiyeweixin_app.page.main import Main


class App(BasePage):

    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps["noReset"] = 'true'
            # desired_caps["ensureWebviewsHavePages"] = True
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver.launch_app()
        return Main(self.driver)

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self.driver

    def stop(self):
        self.driver.quit()
        return self.driver


