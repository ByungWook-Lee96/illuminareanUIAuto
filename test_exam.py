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

    @classmethod
    def setUp(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # 드라이버 종료
        create_driver.driver.quit()

    def test001(self):
        result_message = exam.popup()
        logging.info(result_message)

    def test002(self):
        result_message = exam.click_work()
        logging.info(result_message)

    def test003(self):
        exam.click_goodvibe_works()

    def test004(self):
        result_message = exam.change_tab()
        logging.info(result_message)

    def test005(self):
        result_message = exam.click_apply()
        logging.info(result_message)

    def test006(self):
        result_message = exam.input_company_name()
        logging.info(result_message)

    def test007(self):
        result_message = exam.input_ceo_name()
        logging.info(result_message)

    def test008(self):
        result_message = exam.select_business_type()
        logging.info(result_message)

    def test009(self):
        result_message = exam.select_scale()
        logging.info(result_message)

    def test010(self):
        result_message = exam.input_name()
        logging.info(result_message)

    def test011(self):
        result_message = exam.input_email()
        logging.info(result_message)

    def test012(self):
        result_message = exam.input_mobile()
        logging.info(result_message)

    def test013(self):
        result_message = exam.select_responsibility()
        logging.info(result_message)

    def test014(self):
        result_message = exam.search_responsibility()
        logging.info(result_message)

    def test015(self):
        result_message = exam.click_registration()
        logging.info(result_message)

    def test016(self):
        result_message = exam.click_agree_terms_of_use()
        logging.info(result_message)

    def test017(self):
        result_message = exam.click_agree_privacy_statement()
        logging.info(result_message)

    def test018(self):
        result_message = exam.click_unsubscribe_button()
        logging.info(result_message)


if __name__ == '__main__':
    # 로그 생성하기 위해서 작성한 부분(pyCharm에서 실행하지 않고, 터미널에서 python3 test_exam.py 로 실행 시 test_log.txt 파일 생성됨)
    # os.getcwd()는 현재 작업 디렉토리를 얻기 위한 함수
    log_file_path = os.path.join(os.getcwd(), 'test_log.txt')
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 테스트 실행
    unittest.main()

    # 로그 파일 위치 출력
    print("로그 파일 위치:", log_file_path)
