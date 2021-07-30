from selenium import webdriver
import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get('http://demo14.test.com:4018/datahub')
time.sleep(1)
driver.find_element_by_xpath('//ul[@class="main-nav"]/li[2]/div').click()
time.sleep(1)
ele = driver.find_element_by_xpath('//i[@title="删除"]')
ele.click()
# ele = driver.find_element_by_class_name('el-message-box')
driver.find_element_by_xpath('//div[@class="el-message-box__btns"]/button[1]').click()
WebDriverWait(driver, 1).until_not(ec.visibility_of(ele), '元素未消失')
time.sleep(2)
driver.quit()