import unittest
import time
import exam
import create_driver


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
    unittest.main()