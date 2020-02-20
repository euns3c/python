#-*- Encoding: UTF-8 -*-#

from importPack import *

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://admin.ch.atomystg.com/'
driver.get(url)

try:
    ck_log = driver.find_element_by_link_text("로그아웃")
    if ck_log.is_displayed():
        ck_log.click()
except:
    print('로그인 상태가 아닙니다.')

time.sleep(2)

adm_id = 'baebs'
adm_pw = 'mz@0803'
driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

driver.find_element(By.LINK_TEXT, "공지관리").click()
driver.find_element(By.LINK_TEXT, "등록").click()


title = "[Test] 공지 등록 테스트"
driver.find_element_by_name('title').send_keys(title)
