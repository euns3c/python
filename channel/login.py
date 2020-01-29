#-*- Encoding: UTF-8 -*-#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://admin.ch.atomystg.com/login?error=error&jisa=KR&successUrl=%2Ftemplates%3Fjisa%3DKR'
driver.get(url)

#name=id
#name=pwd

adm_id=''
adm_pw=''

driver.set_window_size(1920, 1080)
driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

driver.find_element(By.LINK_TEXT, "메뉴관리").click()

# (1) 애터미 소식
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .switch").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn-primary").click()
# driver.implicitly_wait(3000)

# [Front] 애터미 소식 ON/OFF 확인
#driver.get('https://ch.atomystg.com/kr/notices')


# [취소]
# driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .switch").click()
# driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .btn-default").click()