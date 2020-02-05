#-*- Encoding: UTF-8 -*-#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://ch.atomystg.com/kr/login'
driver.get(url)

adm_id=''
adm_pw=''

try:
    ck_log = driver.find_element_by_link_text("로그아웃")
    if ck_log.is_displayed():
        ck_log.click()
except:
    print('로그인 상태가 아닙니다.')

time.sleep(2)

driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

html = urlopen('https://ch.atomystg.com/kr')
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.find("meta", {"property":"og:url"}).get('content'))

try:
    if driver.find_element_by_link_text("애터미 소식").is_displayed():
        print("메인 > 애터미 소식 노출 ON")
except NoSuchElementException:
    print("메인 > 애터미 소식 노출 OFF")

url = 'https://ch.atomystg.com/kr/notices'
driver.get(url)

time.sleep(2)

try:
    if driver.find_element_by_css_selector(".error").is_displayed():
        print("애터미 소식 접근 불가")
except NoSuchElementException:
    print("애터미 소식 접근")
