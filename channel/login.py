#-*- Encoding: UTF-8 -*-#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://admin.ch.atomystg.com/login?error=error&jisa=KR&successUrl=%2Ftemplates%3Fjisa%3DKR'
driver.get(url)

#name=id
#name=pwd

adm_id='baebs'
adm_pw='mz@0803'

driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

#.panel-heading
#driver.find_elements_by_css_selector('.panel-heading')[3].click()
#.nav-second>li>a
#XPATH=//*[@id="collapse3"]/ul/li[1]/a

#driver.find_element_by_css_selector('//*[@id="collapse3"]/ul/li[1]/a').click()