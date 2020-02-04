#-*- Encoding: UTF-8 -*-#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://admin.ch.atomystg.com/login?error=error&jisa=KR&successUrl=%2Ftemplates%3Fjisa%3DKR'
driver.get(url)

#name=id
#name=pwd

adm_id=''
adm_pw=''

#driver.set_window_size(1920, 1080)
# driver.maximize_window()  # 창크기 최대화
driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

ck_log = driver.find_element_by_link_text("로그아웃")

if ck_log.is_displayed():
    print("로그아웃 있다")
    ck_log.click()
else:
    print("로그아웃 없다")

time.sleep(3)

driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)