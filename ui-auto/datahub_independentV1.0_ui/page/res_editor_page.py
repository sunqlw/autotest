from poium import Element
from .menu_page import MenuPage


class ResEditorPage(MenuPage):
    add_res_button = Element(xpath='//*[@id="sourceManage"]/div/div[2]/button', describe='新建资源按钮')
    res_name_input = Element(xpath='//*[@id="pane-baseInfoTab"]/div[1]/form[1]/div[1]/div/div/input',
                             describe='资源名输入框')
    res_type_select = Element(xpath='//*[@id="pane-baseInfoTab"]/div[1]/form[1]/div[2]/div/div/div[1]/input',
                              describe='资源类型下拉框')
    res_type_rds_menu = Element(xpath='/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li[1]', describe='类型一级菜单RDS数据库')
    res_type_bigdata_menu = Element(xpath='/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li[2]',
                                    describe='类型一级菜单大数据平台')
    # 此滑动菜单里面必须引入last()函数，会因为操作不同导致div层级不同，比如先执行了删除操作，div就层级就变成4了，不执行删除操作，div层级就是3
    # 但是他们的现象是都是最后一个div层，所以因为last()函数来控制
    res_type_other_menu = Element(xpath='/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li[3]',
                                  describe='类型一级菜单其他')
    res_type_mysql = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[1]', describe='类型二级菜单mysql')
    res_type_oracle = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[2]', describe='类型二级菜单oracle')
    res_type_sqlserver = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[3]',
                                 describe='类型二级菜单sqlserver')
    res_type_db2 = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[4]', describe='类型二级菜单db2')
    res_type_postgresql = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[5]',
                                  describe='类型二级菜单postgresql')
    res_type_hana = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[6]', describe='类型二级菜单hana')
    res_type_tidb = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[7]', describe='类型二级菜单tidb')
    res_type_dm = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[8]', describe='类型二级菜单达梦')
    res_type_hive = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[1]', describe='类型二级菜单hive')
    res_type_hbase = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[2]', describe='类型二级菜单hbase')
    res_type_hdfs = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[3]', describe='类型二级菜单hdfs')
    res_type_ftp = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[1]', describe='类型二级菜单ftp')
    res_type_aws_s3 = Element(xpath='/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[1]', describe='类型二级菜单aws s3')
    db_host_input = Element(xpath='//input[@placeholder="请输入服务地址"]', describe='数据库服务器名输入框')
    db_port_input = Element(xpath='//input[@placeholder="请输入端口"]', describe='数据库端口输入框')
    db_server_input = Element(xpath='//input[@placeholder="请输入服务名"]', describe='数据库服务名输入框')
    db_username_input = Element(xpath='//input[@placeholder="请输入用户名"]', describe='数据库用户名输入框')
    db_password_input = Element(xpath='//input[@placeholder="请输入密码"]', describe='数据库密码输入框')
    max_connects_input = Element(xpath='//input[@placeholder="最大连接数最多为200"]', describe='最大连接数输入框')
    connect_button = Element(xpath='//*[@id="pane-baseInfoTab"]/div[2]/div[1]/button', describe='测试连接按钮')
    save_button = Element(xpath='//div[@class="btns"]/button[2]', describe='保存按钮')
    connect_success_sign = Element(class_name='el-icon-circle-check', describe='测试连接通过标志')
