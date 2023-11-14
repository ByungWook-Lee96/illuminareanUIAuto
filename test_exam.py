import unittest
import time
import exam
import create_driver
import logging
import os


class TestApplyService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # driver에 url 넣음
        url = 'https://illuminarean.com/'
        create_driver.driver.get(url)

        if create_driver.driver.current_url == url:
            print("TC_1_https://illuminarean.com 경로 접속 - PASS")
        else:
            print("TC_1_https://illuminarean.com 경로 접속 - Fail")

    @classmethod
    def setUp(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # 드라이버 종료
        create_driver.driver.quit()

    def test001(self):
        exam.popup()

    def test002(self):
        exam.click_work()

    def test003(self):
        exam.click_goodvibe_works()

    def test004(self):
        exam.change_tab()

    def test005(self):
        exam.click_apply()

    def test006(self):
        exam.input_company_name()

    def test007(self):
        exam.input_ceo_name()

    def test008(self):
        exam.select_business_type()

    def test009(self):
        exam.select_scale()

    def test010(self):
        exam.input_name()

    def test011(self):
        exam.input_email()

    def test012(self):
        exam.input_mobile()

    def test013(self):
        exam.select_responsibility()

    def test014(self):
        exam.search_responsibility()

    def test015(self):
        exam.click_registration()

    def test016(self):
        exam.click_agree_terms_of_use()

    def test017(self):
        exam.click_agree_privacy_statement()

    def test018(self):
        exam.click_unsubscribe_button()


if __name__ == '__main__':
    # 로그 생성하기 위해서 작성한 부분(pyCharm에서 실행하지 않고, 터미널에서 python3 test_exam.py 로 실행 시 test_log.txt 파일 생성됨)
    # os.getcwd()는 현재 작업 디렉토리를 얻기 위한 함수
    # log_file_path = os.path.join(os.getcwd(), 'test_log.txt')
    # logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 테스트 실행
    unittest.main()

