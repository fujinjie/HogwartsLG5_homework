# -*- coding: utf-8 -*-
import pytest

from xueqiu_testframe.page.app import App


class TestSearch:

    def setup(self):
        self.app = App()
        self.app_start = self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("text", ["阿里巴巴", "字节跳动", "腾讯"])
    def test_search(self, text):
        results = self.app_start.goto_hangqing_page().search(text)
        exc = text
        assert exc in results


if __name__ == "__main__":

    pytest.main(['-v', '-s', 'test_search.py'])