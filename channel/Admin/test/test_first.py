from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class mainTest(unittest.TestCase):

# 테스트 전 필요한 설정, 여러 TC가 공유하는 설정을 위해 사용 (웹 드라이버 설치 등)
    def setUp(self):
        self.chromeDriver = PATH('C:/chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=self.chromeDriver)
        self.wait = WebDriverWait(self.driver, 3)

# 테스트 코드를 작성하는 부분, assertion, exception 등이 발생하면 tearDown(self)을 실행
    def runTest(self):
        url = "https://admin.ch.atomystg.com/"

        self.driver.get(url)
        time.sleep(3)

# runTest(self) 종료 후 실행되는 메서드
    def tearDown(self):
        self.driver.quit()

