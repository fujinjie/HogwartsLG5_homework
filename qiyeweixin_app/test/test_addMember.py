# -*- coding: utf-8 -*-
import pytest

from qiyeweixin_app.page.app import App


class TestAddMember:

    def setup(self):
        self.app = App()
        self.app_start = self.app.start()

    def teardown(self):
        self.app.stop()


    def test_add_member(self):
        results = self.app_start.goto_address_page().add_member()
        exc = "小源03"
        assert exc in results


if __name__ == "__main__":

    pytest.main(['-v', '-s', 'test_addMember.py'])