import pyautogui
from poium import Page, Element
from selenium.webdriver.common.action_chains import ActionChains


class MenuPage(Page):
    job_manager_button = Element(xpath='//ul[@class="main-nav"]/li[1]/div', describe='任务管理按钮')
    res_manager_button = Element(xpath='//ul[@class="main-nav"]/li[2]/div', describe='资源管理按钮')

    # 定义自己的方法，根据pyautogui采用绝对坐标来拖拽元素
    def drag_and_drop_by_offset_by_pyautogui(self, elem, x, y):
        elem_location = self.switch_elem(elem).location
        browser_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        y_absolute_coord = elem_location['y'] + browser_height
        pyautogui.moveTo(x=elem_location['x'], y=y_absolute_coord, duration=1, tween=pyautogui.linear)
        pyautogui.dragTo(x=x, y=y, duration=1, button='left')  # 鼠标拖拽

    # 定义自己的方法，模拟两个元素进行连线的方法
    def connect_elem(self, source_elem, target_elem):
        ActionChains(self.driver).click_and_hold(self.switch_elem(source_elem)).release(
            self.switch_elem(target_elem)).perform()

    @staticmethod
    def switch_elem(elem):
        """
        将poium里面的Element对象转成selenium里面的WebElement对象
        :return:
        """
        return elem._Element__get_element(elem.k, elem.v)
