#-*- Encoding: UTF-8 -*-#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://admin.atomyticketdev.com/login?error=error&successUrl=%2Fnoticeboard")

#name=id
#name=pwd

driver.find_element_by_name('id').send_keys('baebs')
driver.find_element_by_name('pwd').send_keys('mz@0803')
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

#.panel-heading
driver.find_elements_by_css_selector('.panel-heading')[3].click()
#.nav-second>li>a
#XPATH=//*[@id="collapse3"]/ul/li[1]/a

driver.find_element_by_css_selector('//*[@id="collapse3"]/ul/li[1]/a').click()