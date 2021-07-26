import logging
import os.path

import pyautogui
import time
import pytest
import sys
from page import ResEditorPage
from public.common import get_json_data, get_now_str
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
        elif kwargs['type'] == 'db2':
            self.page.res_type_db2.click()
            self.page.db_server_input = kwargs['server_name']
        elif kwargs['type'] == 'postgresql':
            self.page.res_type_postgresql.click()
        elif kwargs['type'] == 'hana':
            self.page.res_type_hana.click()
        elif kwargs['type'] == 'tidb':
            self.page.res_type_tidb.click()
        elif kwargs['type'] == 'dm':
            self.page.res_type_dm.click()
        else:
            print('抛出异常，所添加类型不符合要求')
        self.page.db_host_input = kwargs['host']
        self.page.db_port_input = kwargs['port']
        self.page.db_username_input = kwargs['username']
        self.page.db_password_input = kwargs['password']
        self.__connect_success_and_save()

    def add_ftp_common(self, **kwargs):
        self.__click_add_res_button()
        self.page.res_name_input = kwargs['res_name']
        self.page.res_type_select.click()
        self.page.res_type_other_menu.click()
        self.page.res_type_ftp.click()
        if kwargs['type'] == 'sftp':
            self.page.protocol_select.click()
            self.page.protocol_sftp.click()
        self.page.ftp_host_input = kwargs['host']
        self.page.ftp_port_input = kwargs['port']
        self.page.ftp_username_input = kwargs['username']
        self.page.ftp_password_input = kwargs['password']
        self.__connect_success_and_save()

    def add_s3_common(self, **kwargs):
        pass

    def add_hdfs_common(self, **kwargs):
        self.__click_add_res_button()
        self.page.res_name_input = kwargs['res_name']
        self.page.res_type_select.click()
        self.page.res_type_bigdata_menu.click()
        self.page.res_type_hdfs.click()
        self.page.core_site_upload_button.click()
        core_site_file_path = os.path.join(base_path, 'test_case', 'data', 'core-site.xml')
        hdfs_site_file_path = os.path.join(base_path, 'test_case', 'data', 'hdfs-site.xml')
        self.page.upload_file(core_site_file_path)
        time.sleep(2)
        # pyautogui.hotkey('shift', 'command', 'g')
        # pyautogui.typewrite(kwargs['core-site'])
        # pyautogui.press('enter')
        # pyautogui.press('enter')
        self.page.hdfs_site_upload_button.click()
        self.page.upload_file(hdfs_site_file_path)
        # pyautogui.hotkey('shift', 'command', 'g')
        # pyautogui.typewrite(kwargs['hdfs-site'])
        # pyautogui.press('enter')
        # pyautogui.press('enter')
        self.page.hdfs_username_input = kwargs['username']
        self.__connect_success_and_save()

    def add_hive_common(self, **kwargs):
        pass

    def add_hbase_common(self, **kwargs):
        pass

    # 判断资源是否添加成功
    def check_add_success(self, res_name):
        self.page.toast_elem.is_displayed()
        assert self.page.toast_elem.text == '保存成功'
        self.page.table_tr1_td1.is_displayed()
        assert self.page.table_tr1_td1.text == res_name

    # res_type = ['mysql', 'oracle', 'sqlserver', 'db2', 'postgresql', 'hana', 'tidb', 'dm', 'ftp', 'sftp']
    res_type = ['hdfs']

    # @pytest.mark.skip
    @pytest.mark.parametrize('res_type', res_type, ids=res_type)
    def test_add(self, res_type):
        """
        用例名称：添加资源
        步骤：1.填写完相关参数 2.点击测试连接，等待连接通过后点击保存按钮
        检查点：1.toast提示保存成功 2.表格第一列为新增的资源名
        """
        params = self.res_data_dict[res_type]
        params['res_name'] = res_type + get_now_str()
        if res_type in ['ftp', 'sftp']:
            self.add_ftp_common(**params)
        elif res_type == 's3':
            self.add_s3_common(**params)
        elif res_type == 'hdfs':
            self.add_hdfs_common(**params)
        elif res_type == 'hive':
            self.add_hive_common(**params)
        elif res_type == 'hbase':
            self.add_hbase_common(**params)
        else:
            self.add_rds_common(**params)
        self.check_add_success(params['res_name'])

    def test_add_res_name_exist(self):
        params = self.res_data_dict['mysql']
        params['res_name'] = self.page.table_tr1_td1.text
        self.add_rds_common(**params)


    @pytest.mark.skip
    def test_add_oracle(self, browser):
        """
        用例名称：添加oracle资源
        步骤：
        1.资源类型选择oracle，填写完相关参数
        2.点击测试连接，等待连接通过后点击保存按钮
        检查点：
        """
        params = self.res_data_dict['oracle']
        params['res_name'] = 'oracle-ui-' + get_now_str()
        self.add_rds_common(**params)
        self.check_add_success(params['res_name'])

    @pytest.mark.skip
    def test_add_sqlserver(self, browser):
        """
        用例名称：添加sqlserver资源
        步骤：
        1.资源类型选择sqlserver，填写完相关参数
        2.点击测试连接，等待连接通过后点击保存按钮
        检查点：
        """
        params = self.res_data_dict['sqlserver']
        params['res_name'] = 'sqlserver-ui-' + get_now_str()
        self.add_rds_common(**params)
        self.check_add_success(params['res_name'])

