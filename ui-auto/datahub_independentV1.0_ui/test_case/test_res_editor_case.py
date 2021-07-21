import logging
import time
import pytest
import sys
from page import ResEditorPage
from public.common import get_json_data
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))  # 这行代码在干啥？？
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
base_path = dirname(dirname(abspath(__file__)))


class TestResEditorCase:

    page = ResEditorPage(driver=None)
    res_data_dict = {}

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了，
    # @classmethod 为什么fixture不能作用在类方法上
    def setup_class(self, browser):
        self.__class__.page = ResEditorPage(browser)
        self.__class__.page.res_manager_button.click()
        self.__class__.res_data_dict = get_json_data(base_path + "/test_case/data/add_res_data.json")

    # 点击新增资源按钮
    def __click_add_res_button(self):
        self.page.add_res_button.click()

    # 点击测试连接等待通过后点击保存按钮
    def __connect_success_and_save(self):
        self.page.connect_button.click()
        self.page.connect_success_sign.is_displayed()
        self.page.save_button.click()

    @staticmethod
    def __get_now_str():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # 正常添加关系型数据库的通用方法
    def add_rds_common(self, **kwargs):
        self.__click_add_res_button()
        self.page.res_name_input = kwargs['res_name']
        if kwargs['type'] != 'mysql':
            self.page.res_type_select.click()
        if kwargs['type'] == 'oracle':
            self.page.res_type_oracle.click()
            self.page.db_server_input = kwargs['server_name']
        elif kwargs['type'] == 'sqlserver':
            self.page.res_type_sqlserver.click()
        else:
            print('no')
        self.page.db_host_input = kwargs['host']
        self.page.db_port_input = kwargs['port']
        self.page.db_username_input = kwargs['username']
        self.page.db_password_input = kwargs['password']
        self.__connect_success_and_save()

    def test_add_mysql(self, browser):
        """
        用例名称：添加mysql资源
        步骤：
        1.填写完相关参数
        2.点击测试连接，等待连接通过后点击保存按钮
        检查点：
        """
        params = self.res_data_dict['mysql']
        params['res_name'] = 'mysql-ui-' + self.__get_now_str()
        self.add_rds_common(**params)

    def test_add_oracle(self, browser):
        """
        用例名称：添加oracle资源
        步骤：
        1.资源类型选择oracle，填写完相关参数
        2.点击测试连接，等待连接通过后点击保存按钮
        检查点：
        """
        params = self.res_data_dict['oracle']
        params['res_name'] = 'oracle-ui-' + self.__get_now_str()
        self.add_rds_common(**params)
