from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup


def load_chrome(url):
    driver = webdriver.Chrome('C:/chromedriver.exe')
    return driver.get(url)


def login(id, pw):
    load_chrome()
    driver.find_element_by_name('id').send_keys(id)
    driver.find_element_by_name('pwd').send_keys(pw)
    driver.find_element_by_name('pwd').send_keys(Keys.ENTER)