from poium import Element
from .load_rds_page import LoadRdsPage


class LoadComponentPage(LoadRdsPage):
    hive_load_component = Element(xpath='//span[text()="Hive加载"]', describe='Hive加载组件')
    hdfs_load_component = Element(xpath='//span[text()="HDFS加载"]', describe='HDFS加载组件')
    rds_load_component = Element(xpath='//span[text()="RDS加载"]', describe='RDS加载组件')