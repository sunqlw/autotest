from poium import Element
from .menu_page import MenuPage


class JobEditorPage(MenuPage):
    add_job_button = Element(xpath='//button[@type="button"]', describe='新建任务按钮', index=2)
    add_new_canvas_button = Element(class_name='new-box', describe='新建空白画布按钮')
    job_name_input = Element(xpath='//input[@placeholder="请输入任务名"]', describe='任务名输入框')
    job_describe_input = Element(xpath='//input[@placeholder="请输入描述"]', describe='描述输入框')
    add_sure_button = Element(xpath='//div[@class="btn-wrap own-btn-wrap"]/button[2]', describe='新建任务确定按钮')
    add_cancel_button = Element(xpath='//div[@class="btn-wrap own-btn-wrap"]/button[1]', describe='新建任务取消按钮')
    work_place = Element(id_='workplace', describe='画布')
    # rds_extract_component = Element(xpath='//div[@role="tablist"]/div[1]/div[2]/div/div/div[1]', describe='RDS抽取组件')
    rds_extract_component = Element(xpath='//span[text()="RDS抽取"]', describe='RDS抽取组件')
    merge_component = Element(xpath='//span[text()="合并"]', describe='合并组件')
    hbase_load_component = Element(xpath='//div[@role="tablist"]/div[4]/div[2]/div/div/div[1]', describe='HBase加载组件')
    hive_load_component = Element(xpath='//div[@role="tablist"]/div[4]/div[2]/div/div/div[2]', describe='Hive加载组件')
    hdfs_load_component = Element(xpath='//div[@role="tablist"]/div[4]/div[2]/div/div/div[3]', describe='HDFS加载组件')
    rds_load_component = Element(xpath='//div[@role="tablist"]/div[4]/div[2]/div/div/div[4]', describe='RDS加载组件')
    canvas_rds_extract = Element(xpath='//div[@alias="RDS抽取"]', describe='画布上的RDS抽取组件')
    canvas_merge = Element(xpath='//div[@alias="合并"]', describe='画布上的合并组件')
    first_right = Element(tag='circle', describe='第一个组件右边点', index=0)
    second_left = Element(tag='circle', describe='第二个组件左边点', index=2)
    second_right = Element(tag='circle', describe='第二个组件右边点', index=1)
