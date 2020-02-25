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

adm_id = ''
adm_pw = ''
driver.find_element_by_name('id').send_keys(adm_id)
driver.find_element_by_name('pwd').send_keys(adm_pw)
driver.find_element_by_name('pwd').send_keys(Keys.ENTER)

driver.find_element(By.LINK_TEXT, "메뉴관리").click()

# html = urlopen('https://admin.ch.atomystg.com/menus?jisa=KR')
# bsObject = BeautifulSoup(html, 'html.parser')
#
# print(bsObject.body.find().get('content'))

# (1) 애터미 소식
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .switch").click()
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn-primary").click()
# driver.implicitly_wait(3000)

time.sleep(2)

driver.find_element_by_css_selector('.confirm.btn.btn-lg.btn-primary').click()  # [확인]

# driver.__getattribute__()

# if #첫번째 요소가 노출이면:
#    print("노출 ON")


# [취소]
# driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .switch").click()
# driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .btn-default").click()
