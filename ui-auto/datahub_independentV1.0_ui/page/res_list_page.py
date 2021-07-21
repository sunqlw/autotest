from poium import Element
from .menu_page import MenuPage


class ResListPage(MenuPage):
    res_name_search_input = Element(xpath='//input[@placeholder="请输入资源名"]', describe='资源名搜索框')
    res_type_search_select = Element(xpath='//input[@placeholder="请选择"]', describe='资源类型搜索下拉框')
    res_type_search_rds_menu = Element(xpath='//div[@class="el-cascader-panel"]/div[1]/div[1]/ul/li[1]',
                                       describe='搜索类型一级菜单RDS数据库')
    res_type_search_bigdata_menu = Element(xpath='//div[@class="el-cascader-panel"]/div[1]/div[1]/ul/li[2]',
                                           describe='搜索类型一级菜单大数据平台')
    res_type_search_other_menu = Element(xpath='//div[@class="el-cascader-panel"]/div[1]/div[1]/ul/li[3]',
                                         describe='搜索类型一级菜单其他')
    res_type_search_mysql = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[1]',
                                    describe='搜索类型二级菜单mysql')
    res_type_search_oracle = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[2]',
                                     describe='搜索类型二级菜单oracle')
    res_type_search_sqlserver = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[3]',
                                        describe='搜索类型二级菜单sqlserver')
    res_type_search_db2 = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[4]',
                                  describe='搜索类型二级菜单db2')
    res_type_search_postgresql = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[5]',
                                         describe='搜索类型二级菜单postgresql')
    res_type_search_hana = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[6]',
                                   describe='搜索类型二级菜单hana')
    res_type_search_tidb = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[7]',
                                   describe='搜索类型二级菜单tidb')
    res_type_search_dm = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[8]',
                                 describe='搜索类型二级菜单dm')
    res_type_search_hive = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[1]',
                                   describe='搜索类型二级菜单hive')
    res_type_search_hbase = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[2]',
                                    describe='搜索类型二级菜单habse')
    res_type_search_hdfs = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[3]',
                                   describe='搜索类型二级菜单hdfs')
    res_type_search_ftp = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[1]',
                                  describe='搜索类型二级菜单ftp')
    res_type_search_aws_s3 = Element(xpath='//div[@class="el-cascader-panel"]/div[2]/div[1]/ul/li[2]',
                                     describe='搜索类型二级菜单aws s3')
    search_button = Element(xpath='//div[@class="flexRow el-row"]/div[3]/button[1]', describe='搜索按钮')
    reset_button = Element(xpath='//div[@class="flexRow el-row"]/div[3]/button[2]', describe='重置按钮')
    res_delete_button = Element(xpath='//i[@title="删除"]', describe='资源删除按钮')
    delete_cancel_button = Element(xpath='//div[@class="el-message-box__btns"]/button[1]', describe='删除资源取消按钮')
    delete_sure_button = Element(xpath='//div[@class="el-message-box__btns"]/button[2]', describe='删除资源确认按钮')
    delete_success_sign = Element(xpath='//p[text()="删除成功"]', describe='删除成功toast')
    res_total_span = Element(class_name='el-pagination__total', describe='总条数标签')

