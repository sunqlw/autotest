import pytest
import sys

from page import ResListPage
from time import sleep
from os.path import dirname, abspath
#
# sys.path.insert(0, dirname(dirname(abspath(__file__))))  # 这行代码在干啥？？


class TestResEditorCase:

    page = None

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了，
    def setup_class(self, browser):
        self.__class__.page = ResListPage(browser)
        self.__class__.page.res_manager_button.click()

    def test_delete_res(self, browser):
        """
        用例名称：删除资源连接
        步骤：
        1.选择列表中第一行资源点击删除按钮
        2.二次弹窗后点击确定
        检查点：
        1.出现删除成功toast
        :param browser:
        :return:
        """
        self.page = ResListPage(browser)
        self.page.res_delete_button.click()
        self.page.delete_sure_button.click()
        self.page.delete_success_sign.is_displayed()
        assert self.page.delete_success_sign.text == '删除成功'





if __name__ == '__main__':
    pytest.main()
