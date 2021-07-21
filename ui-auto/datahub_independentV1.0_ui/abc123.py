from page import LoginPage, ResEditorPage
from public.common import login
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options)
login(driver)
page = ResEditorPage(driver)
page.res_manager_button.click()
page.add_res_button.click()
page.res_name_input = 'mysql_1232'
# page.res_type_select.click()
# page.res_type_bigdata_menu.move_to_element()
# page.res_type_oracle.click()
page.db_host_input = '172.17.177.22'
page.db_port_input = '3306'
# page.db_server_input = ''
page.db_username_input = 'root'
page.db_password_input = 'bigData@123'
page.connect_button.click()
page.connect_success_sign.is_displayed()
page.save_button.click()
sleep(2)
driver.close()
