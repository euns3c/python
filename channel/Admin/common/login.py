from channel.Admin.common.loadWebdriver import loadChrome
from selenium.webdriver.common.keys import Keys

from channel.Admin.login import driver

loadChrome('https://admin.ch.atomystg.com/login?jisa=KR')


def login(id, pw):
    driver.find_element_by_name('id').send_keys(id)
    driver.find_element_by_name('pwd').send_keys(pw)
    driver.find_element_by_name('pwd').send_keys(Keys.ENTER)


