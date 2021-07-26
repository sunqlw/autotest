import pytest
import time
import logging
import pyautogui
from page import JobEditorPage
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestJobAddCase:
    page = JobEditorPage(driver=None)
    res_data_dict = {}
    driver = webdriver.Chrome()

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了
    def setup_class(self, browser):
        self.__class__.page = JobEditorPage(browser)
        self.__class__.driver = browser
        # self.__class__.res_data_dict = get_json_data(base_path + "/test_case/data/add_res_data.json")

    def test_add_rds_extract(self):
        self.page.add_job_button.click()
        self.page.add_new_canvas_button.click()
        self.page.job_name_input = '新建空白画布任务'
        self.page.add_sure_button.click()
        # 不行，这个获取到的是元素在html里面的坐标，而不是相对于整个浏览器的坐标
        self.page.drag_and_drop_by_offset_by_pyautogui(self.page.rds_extract_component, 380, 400)
        self.page.drag_and_drop_by_offset_by_pyautogui(self.page.merge_component, 600, 400)
        time.sleep(1)
        self.page.canvas_rds_extract.double_click()
        self.page.connect_elem(self.page.first_right, self.page.second_left)
