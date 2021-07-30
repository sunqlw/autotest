import logging
import os.path
import time
import pytest
import sys
from page import ResEditorPage
from public.common import get_json_data, get_now_str
from os.path import dirname, abspath
from selenium.common import exceptions

sys.path.insert(0, dirname(dirname(abspath(__file__))))  # 这行代码在干啥？？
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
base_path = dirname(dirname(abspath(__file__)))
res_data_dict = get_json_data(base_path + "/test_case/data/add_res_data.json")
message_data_dict = get_json_data(base_path + "/test_case/data/message.json")


# 添加资源前点击新建资源按钮并填写资源名和填写完参数后点击测试连接和保存按钮
def deco_add_res(func):
    def wrapper(self, *args, **kwargs):
        self.click_add_res_button()
        self.page.res_name_input = kwargs['res_name']
        f = func(self, *args, **kwargs)
        self.connect_success_and_save()
        return f
    return wrapper


class TestResEditorCase:

    page = ResEditorPage(driver=None)

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了，
    # @classmethod 为什么fixture不能作用在类方法上
    def setup_class(self, browser):
        self.__class__.page = ResEditorPage(browser)
        self.__class__.page.res_manager_button.click()

    # 点击新增资源按钮
    def click_add_res_button(self):
        # 增加try，如果新建资源按钮不能点击，则刷新界面
        try:
            self.page.add_res_button.click()
        except exceptions.ElementClickInterceptedException:
            self.page.refresh_page()
            self.page.add_res_button.click()

    # 点击测试连接等待通过后点击保存按钮
    def connect_success_and_save(self):
        self.page.connect_button.click()
        # 在这里应该增加判断，如果出现了测试连接失败，则应该直接抛出异常了
        self.page.connect_success_sign.timeout = 10
        self.page.connect_success_sign.is_displayed()
        self.page.save_button.click()
        # 等待成功的标志出现，如果测试连接失败标志出现了，则直接失败
        # 如何实现该功能？
        # for x in range(5):
        #     try:
        #         self.page.connect_success_sign.is_displayed()
        #         self.page.save_button.click()
        #         break
        #     except exceptions.NoSuchElementException:
        #         try:
        #             self.page.connect_fail_box.is_displayed()
        #             assert False
        #             # break
        #         except exceptions.NoSuchElementException:
        #             time.sleep(1)

    # 根据zk串输入zk地址通用方法
    def input_zk_host(self, zk_str):
        zk_list = zk_str.split(',')
        if len(zk_list) >= 1:
            self.page.first_zk_input = zk_list[0]
        if len(zk_list) >= 2:
            self.page.zk_add_button.click()
            self.page.second_zk_input = zk_list[1]
        if len(zk_list) >= 3:
            self.page.zk_add_button.click()
            self.page.third_zk_input = zk_list[2]
        if len(zk_list) >= 4:
            print("抛出异常，最多只支持3个zk地址")

    # 选择大数据类型
    def select_bigdata_type(self, res_type):
        self.page.res_type_select.click()
        self.page.res_type_bigdata_menu.click()
        if res_type == 'hdfs':
            self.page.res_type_hdfs.click()
        elif res_type == 'hive':
            self.page.res_type_hive.click()
        elif res_type == 'hbase':
            self.page.res_type_hbase.click()
        else:
            print("抛出异常，只支持上述三种类型")

    # 正常添加关系型数据库的通用方法
    @deco_add_res
    def add_rds_common(self, **kwargs):
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

    @deco_add_res
    def add_ftp_common(self, **kwargs):
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

    @deco_add_res
    def add_s3_common(self, **kwargs):
        self.page.res_type_select.click()
        self.page.res_type_other_menu.click()
        self.page.res_type_aws_s3.click()
        self.page.s3_accesskey_input = kwargs['accesskey']
        self.page.s3_secretkey_input = kwargs['secretkey']
        self.page.s3_region_select.click()
        if kwargs['region'] == 'china':
            self.page.focus(self.page.s3_region_china)
            self.page.s3_region_china.click()
        else:
            print("抛出异常，暂不支持其他区域")

    @deco_add_res
    def add_hdfs_common(self, **kwargs):
        # self.__click_add_res_button()
        self.select_bigdata_type('hdfs')
        self.page.core_site_upload_button.click()
        core_site_file_path = os.path.join(base_path, 'test_case', 'data', 'core-site.xml')
        hdfs_site_file_path = os.path.join(base_path, 'test_case', 'data', 'hdfs-site.xml')
        self.page.upload_file(core_site_file_path)
        self.page.hdfs_site_upload_button.click()
        self.page.upload_file(hdfs_site_file_path)
        self.page.hdfs_username_input = kwargs['username']
        # self.__connect_success_and_save()

    @deco_add_res
    def add_hive_common(self, **kwargs):
        self.select_bigdata_type('hive')
        self.page.hive_hdfs_select.click()
        self.page.hive_bind_hdfs.click()
        self.page.hive_username_input = kwargs['username']
        if kwargs['service_model'] == 'HA模式':
            self.page.hive_service_model_select.click()
            self.page.hive_ha_service.click()
            self.page.hive_space_name_input = kwargs['space_name']
            self.input_zk_host(kwargs['zk_host'])
        elif kwargs['service_model'] == '普通模式':
            self.page.hive_host_input = kwargs['host']
        else:
            print("抛出异常，只支持HA模式和普通模式")
        self.page.hive_port_input = kwargs['port']

    @deco_add_res
    def add_hbase_common(self, **kwargs):
        self.select_bigdata_type('hbase')
        self.page.hbase_username_input = kwargs['username']
        self.input_zk_host(kwargs['zk_host'])
        self.page.hbase_port_input = kwargs['port']
        self.page.znode_input = kwargs['znode']

    # 判断资源是否添加成功
    def check_add_success(self, res_name):
        self.page.toast_elem.is_displayed()
        assert self.page.toast_elem.text == message_data_dict['save_success']
        self.page.table_tr1_td1.is_displayed()
        assert self.page.table_tr1_td1.text == res_name

    # res_type_list = ['mysql', 'oracle', 'sqlserver', 'db2', 'postgresql', 'hana', 'tidb', 'dm', 'ftp', 'sftp', 's3',
    #                  'hdfs', 'hive', 'hive_ha', 'hbase']

    res_type_list = ['mysql', 'oracle', 'sqlserver', 'db2']

    # @pytest.mark.skip
    @pytest.mark.parametrize('res_type', res_type_list, ids=res_type_list)
    def test_add(self, res_type):
        """
        用例名称：添加资源
        步骤：1.填写完相关参数 2.点击测试连接，等待连接通过后点击保存按钮
        检查点：1.toast提示保存成功 2.表格第一列为新增的资源名
        """
        params = res_data_dict[res_type]
        params['res_name'] = res_type + get_now_str()
        if 'ftp' in res_type:
            self.add_ftp_common(**params)
        elif res_type == 's3':
            self.add_s3_common(**params)
        elif res_type == 'hdfs':
            self.add_hdfs_common(**params)
        elif 'hive' in res_type:
            self.add_hive_common(**params)
        elif 'hbase' in res_type:
            self.add_hbase_common(**params)
        else:
            self.add_rds_common(**params)
        self.check_add_success(params['res_name'])

    # @pytest.mark.skip
    def test_add_res_name_exist(self):
        """
        用例名称：新建资源重名检查
        步骤：1.资源连接名填写一个已存在的名字，填写完相关参数 2.点击测试连接，等待连接通过后点击保存按钮
        检查点：1.保存失败，弹窗提示资源名已存在
        """
        params = res_data_dict['mysql']
        self.page.table_tr1_td1.refresh_element()
        params['res_name'] = self.page.table_tr1_td1.text
        self.add_rds_common(**params)
        assert self.page.box_text_ele.text == message_data_dict['res_name_exist']

    @pytest.mark.skip
    def test_add_oracle(self, browser):
        """
        用例名称：添加oracle资源
        步骤：
        1.资源类型选择oracle，填写完相关参数
        2.点击测试连接，等待连接通过后点击保存按钮
        检查点：
        """
        params = res_data_dict['oracle']
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
        params = res_data_dict['sqlserver']
        params['res_name'] = 'sqlserver-ui-' + get_now_str()
        self.add_rds_common(**params)
        self.check_add_success(params['res_name'])

