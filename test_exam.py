import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

class TestApplyService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 웹 드라이버 초기화
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        # 드라이버 종료
        cls.driver.quit()

    def setUp(self):
        # 테스트 메소드 실행 전에 실행되는 부분
        randomNum = random.randrange(1, 100)
        url = 'https://illuminarean.com/'
        self.driver.get(url)

        try:
            # 팝업이 노출될 수 있어서 팝업이 노출되면 클릭을 하고, 노출되지 않으면 해당 부분 지나감.
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))
            )
            element.click()
        except Exception as e:
            print("팝업의 요소가 없거나 팝업이 없음")
        time.sleep(1)

    def test_apply_service(self):
        # 예제로 'Work' 링크 클릭하는 부분 추가
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Work'))
            )
            element.click()
        except Exception as e:
            print("Work 링크가 없습니다.")
        time.sleep(1)

        # [GOODVIBE WORKS 바로가기] 버튼 클릭(a링크)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'GOODVIBE WORKS 바로가기'))
            )
            element.click()
        except Exception as e:
            print("[GOODVIBE WORKS 바로가기] 버튼이 없습니다.")
        time.sleep(1)

        # 나머지 테스트 코드를 여기에 추가

if __name__ == '__main__':
    unittest.main()