import logging
import os.path
import time
import pytest
import sys
from page import ResListPage
from public.common import get_json_data, get_now_str
from os.path import dirname, abspath
from selenium.common import exceptions

base_path = dirname(dirname(abspath(__file__)))
sign_data_dict = get_json_data(base_path + "/test_case/data/sign.json")
message_data_dict = get_json_data(base_path + "/test_case/data/message.json")


class TestResSearchCase:

    page = ResListPage(driver=None)

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了，
    def setup_class(self, browser):
        self.__class__.page = ResListPage(browser)
        self.__class__.page.res_manager_button.click()

    # 按类型搜索通用方法
    def search_by_res_type(self, res_type):
        self.page.reset_button.click()
        self.page.res_type_search_select.click()
        if res_type in ['mysql', 'oracle', 'sqlserver', 'db2', 'postgresql', 'hana', 'tidb', 'dm']:
            self.page.res_type_search_rds_menu.click()
            if res_type == 'mysql':
                self.page.res_type_search_mysql.click()
            elif res_type == 'oracle':
                self.page.res_type_search_oracle.click()
            elif res_type == 'sqlserver':
                self.page.res_type_search_sqlserver.click()
            elif res_type == 'db2':
                self.page.res_type_search_db2.click()
            elif res_type == 'postgresql':
                self.page.res_type_search_postgresql.click()
            elif res_type == 'hana':
                self.page.res_type_search_hana.click()
            elif res_type == 'tidb':
                self.page.res_type_search_tidb.click()
            else:
                self.page.res_type_search_dm.click()
        elif res_type in ['hdfs', 'hive', 'hbase']:
            self.page.res_type_search_bigdata_menu.click()
            if res_type == 'hdfs':
                self.page.res_type_search_hdfs.click()
            elif res_type == 'hive':
                self.page.res_type_search_hive.click()
            else:
                self.page.res_type_search_hbase.click()
        elif res_type in ['ftp', 's3']:
            self.page.res_type_search_other_menu.click()
            if res_type == 'ftp':
                self.page.res_type_search_ftp.click()
            else:
                self.page.res_type_search_aws_s3.click()
        else:
            print("抛出异常，输入类型不合法")
        self.page.search_button.click()

    # 检查搜索结果
    def check_search_result(self, res_name=None, res_type=None):
        if res_name:
            results = self.page.return_table_col(self.page.table_ele, 1)
            for x in range(len(results)):
                assert res_name.lower() in results[x].lower()
        if res_type:
            results = self.page.return_table_col(self.page.table_ele, 2)
            for y in range(len(results)):
                assert sign_data_dict[res_type] == results[y]

    def test_search_by_res_name(self):
        """
        用例名称：根据资源名搜索关键字不存在的资源
        步骤：1.输入一个不存在的关键字 2.点击搜索
        检查点：1.列表里面显示无数据
        """
        self.page.res_name_search_input = '关键字不存在的'
        self.page.search_button.click()
        assert self.page.no_data_sign.text == '暂无数据'

    res_type_list = ['mysql', 'oracle', 'sqlserver', 'db2', 'postgresql', 'hana', 'tidb', 'dm', 'ftp', 's3',
                     'hdfs', 'hive', 'hbase']

    @pytest.mark.parametrize('res_type', res_type_list, ids=res_type_list)
    def test_search_by_res_type(self, res_type):
        """
        用例名称：根据资源类型搜索
        步骤：1.选择资源类型 2.点击搜索
        检查点：1.列表里的都是所搜索类型的资源
        """
        self.search_by_res_type(res_type)
        self.check_search_result(res_type=res_type)

    def test_delete_res_cancel(self):
        """
        用例名称：取消删除资源验证
        步骤：1.点击第一行数据的删除按钮 2.弹窗后点击取消按钮
        检查点：1.弹窗消失 2.数据没有删除
        """
        self.page.table_tr1_td1.refresh_element()
        res_name_first = self.page.table_tr1_td1.text
        self.page.res_delete_button.click()
        self.page.delete_cancel_button.click()
        self.page.wait_elem_not_visibility(self.page.box_text_ele)
        res_name_check = self.page.table_tr1_td1.text
        assert res_name_first == res_name_check

    def test_delete_res_sure(self):
        """
        用例名称：确定删除资源验证
        步骤：1.点击第一行数据的删除按钮 2.弹窗后点击确定按钮
        检查点：1.弹窗消失 2.toast弹窗提示删除成功 3.数据从列表中移除
        """
        self.page.table_tr1_td1.refresh_element()
        res_name_first = self.page.table_tr1_td1.text
        self.page.res_delete_button.click()
        self.page.delete_sure_button.click()
        self.page.wait_elem_not_visibility(self.page.box_text_ele)
        self.page.toast_elem.is_displayed()
        assert self.page.toast_elem.text == '删除成功'
        res_name_check = self.page.table_tr1_td1.text
        assert res_name_first != res_name_check

