# -*- coding: utf-8 -*-
import pytest

from xueqiu_app.page.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.app_start = self.app.start()

    def teardown(self):
        self.app.stop()


    def test_search(self):
        results = self.app_start.goto_hangqing_page().search()
        exc = "阿里巴巴"
        assert exc in results


if __name__ == "__main__":

    pytest.main(['-v', '-s', 'test_search.py'])