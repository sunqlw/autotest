import time

import pyautogui
import platform
import pyperclip
from poium import Page, Element
from selenium.webdriver.common.action_chains import ActionChains


class MenuPage(Page):
    job_manager_button = Element(xpath='//ul[@class="main-nav"]/li[1]/div', describe='任务管理按钮')
    res_manager_button = Element(xpath='//ul[@class="main-nav"]/li[2]/div', describe='资源管理按钮')
    toast_elem = Element(xpath='/html/body/div[last()]/p', describe='toast标签')
    table_tr1_td1 = Element(xpath='//tbody/tr[1]/td[1]/div', describe='表格第一行第一列')

    # 定义自己的方法，根据pyautogui采用绝对坐标来拖拽元素
    def drag_and_drop_by_offset_by_pyautogui(self, elem, x, y):
        elem_location = self.switch_elem(elem).location
        browser_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        y_absolute_coord = elem_location['y'] + browser_height
        pyautogui.moveTo(x=elem_location['x'], y=y_absolute_coord, duration=1, tween=pyautogui.linear)
        pyautogui.dragTo(x=x, y=y, duration=1, button='left')  # 鼠标拖拽

    def connect_elem(self, source_elem, target_elem):
        """
        模拟两个元素进行连线的方法
        :param source_elem: 源元素
        :param target_elem: 目标元素
        :return:
        """
        ActionChains(self.driver).click_and_hold(self.switch_elem(source_elem)).release(
            self.switch_elem(target_elem)).perform()

    @staticmethod
    def upload_file(filepath):
        """
        通过pyautogui键盘输入的方式控制模拟不同系统的上传文件的方式
        :return:
        """
        platform_str = platform.platform().lower()  # 首先获取到操作系统
        if 'mac' in platform_str:
            pyautogui.hotkey('shift', 'command', 'g')
            # 中文输入法下直接输入字符串是不行的，第一个/会变成、，所以通过复制粘贴的形式键入文件名
            pyperclip.copy(filepath)
            pyautogui.hotkey('command', 'v')
            pyautogui.press('enter')
            time.sleep(1)  # 必须停留一下，从粘贴到连续键入两个回车键有问题
            pyautogui.press('enter')
        elif 'windows' in platform_str:
            pyautogui.typewrite(filepath)
            pyautogui.press('enter')
        else:
            print('抛出异常，目前只支持mac和Windows的操作系统')

    @staticmethod
    def switch_elem(elem):
        """
        将poium里面的Element对象转成selenium里面的WebElement对象
        :return:
        """
        return elem._Element__get_element(elem.k, elem.v)
