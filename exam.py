from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from selenium.webdriver.common.keys import Keys  # 키보드 클릭할 때 쓸 부분
from selenium.webdriver.chrome.options import Options

import time
import random
import create_driver


# 팝업이 노출될 수 있어서 팝업이 노출되면 클릭을 하고, 노출되지 않으면 해당 부분 지나감.
def popup():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))
        )
        element.click()
        print("popup() - PASS")
    except Exception as e:
        print("popup() - Fail")


# Work 클릭
def click_work():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Work'))
        )
        element.click()
    except Exception as e:
        print("Work 링크가 없습니다.")

    if create_driver.driver.current_url == 'https://illuminarean.com/work':
        print("click_work() - PASS")
    else:
        print("click_apply() - Fail")


# [GOODVIBE WORKS 바로가기] 버튼 클릭
def click_goodvibe_works():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'GOODVIBE WORKS 바로가기'))
        )
        element.click()
    except Exception as e:
        print("[GOODVIBE WORKS 바로가기] 버튼이 없습니다.")


# 드라이버의 탭을 새로운 탭으로 변경
def change_tab():
    create_driver.driver.switch_to.window(create_driver.driver.window_handles[1])

    if create_driver.driver.current_url == "https://works.goodvibe.kr/":
        print("click_goodvibe_works(), change_tab() - PASS")
    else:
        print("click_goodvibe_works(), change_tab() - Fail", end=" ")
        print(f"현재 탭은 {create_driver.driver.current_url} 입니다.")


# [무료 체험 신청하기] 버튼 클릭
def click_apply():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='무료 체험 신청']"))
        )
        element.click()
    except Exception as e:
        print("[무료 체험 신청하기] 버튼이 없습니다.")

    if create_driver.driver.find_element(By.XPATH,
                                         "/html/body/div[5]/div/div/div/div/div/div/div/div[1]/h2").text == "서비스 이용신청":
        print("click_apply() - PASS")
    else:
        print("click_apply() - Fail")


# 내용 입력 - 회사명
def input_company_name():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'companyName'))
        )
        element.clear()
        element.send_keys(f'테스트회사{create_driver.randomNum}')
    except Exception as e:
        print("내용 입력 - 회사명이 없습니다.")

    if create_driver.driver.find_element(By.ID, 'companyName').get_attribute("value") == \
            "테스트회사"+str(create_driver.randomNum):
        print("input_company_name() - PASS")
    else:
        print("input_company_name() - Fail", end=" ")
        print(f"현재 입력된 값은 {create_driver.driver.find_element(By.ID, 'companyName').get_attribute('value')} 입니다.")


# 내용 입력 - 대표자명
def input_ceo_name():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'ceoName'))
        )
        element.clear()
        element.send_keys(f'테스트이름{create_driver.randomNum}')
    except Exception as e:
        print("내용 입력 - 대표자명이 없습니다.")

    if create_driver.driver.find_element(By.ID, 'ceoName').get_attribute("value") == \
            "테스트이름" + str(create_driver.randomNum):
        print("input_ceo_name() - PASS")
    else:
        print("input_ceo_name() - Fail", end=" ")
        print(f"현재 입력된 값은 {create_driver.driver.find_element(By.ID, 'ceoName').get_attribute('value')} 입니다.")


# 내용 선택 - 사업자 유형(개인)
def select_business_type():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'businessType'))
        )
        element.click()
    except Exception as e:
        print("내용 선택 - 사업자 유형이 없습니다.")

    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[text()='개인']"))
        )
        element.click()

        if create_driver.driver.find_element(By.XPATH, '//*[@id="businessType"]/div/div[1]/div').text == '개인':
            print("select_business_type() - PASS")
        else:
            print("select_business_type() - Fail", end=" ")
            print(f"선택된 값은 개인이 아닌 {element.text} 입니다.")
    except Exception as e:
        print("내용 선택 - 사업자 유형에 '개인'이 없습니다.")


# 내용 선택 - 직원수(21-50명)
def select_scale():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'scale'))
        )
        element.click()
    except Exception as e:
        print("내용 선택 - 직원수가 없습니다.")

    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[text()='51-100 명']"))
        )
        element.click()

        if create_driver.driver.find_element(By.XPATH, '//*[@id="scale"]/div/div[1]/div').text == '51-100 명':
            print("select_scale() - PASS")
        else:
            print("select_scale() - Fail", end=" ")
            print(f"선택된 값은 '51-100 명'이 아닌 {element.text} 입니다.")
    except Exception as e:
        print("내용 선택 - 직원수에 '51-100 명'이 없습니다.")


# 내용 입력 - 담당자명
def input_name():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )
        element.clear()
        element.send_keys(f'테스트담당자명{create_driver.randomNum}')
    except Exception as e:
        print("내용 입력 - 담당자명이 없습니다.")

    if create_driver.driver.find_element(By.ID, 'name').get_attribute("value") == \
            "테스트담당자명" + str(create_driver.randomNum):
        print("input_name() - PASS")
    else:
        print("input_name() - Fail")


# 내용 입력 - 이메일
def input_email():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        element.clear()
        element.send_keys(f'test{create_driver.randomNum}@test.com')
    except Exception as e:
        print("내용 입력 - 이메일이 없습니다.")

    if create_driver.driver.find_element(By.ID, 'email').get_attribute("value") == \
            "test" + str(create_driver.randomNum) + "@test.com":
        print("input_email() - PASS")
    else:
        print("input_email() - Fail")


# 내용 입력 - 휴대폰 번호
def input_mobile():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'mobile'))
        )
        element.clear()
        element.send_keys('010-0000-0000') # 실제 번호가 있을 수 있어서 해당 부분은 randomNum을 사용하지 않음
    except Exception as e:
        print("내용 입력 - 휴대폰 번호가 없습니다.")

    if create_driver.driver.find_element(By.ID, 'mobile').get_attribute("value") == '010-0000-0000':
        print("input_mobile() - PASS")
    else:
        print("input_mobile() - Fail")


# 내용 선택 - 담당 업무
def select_responsibility():
    # 먼저 버튼 클릭
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div/div/div/div'
                                                      '/div[2]/dl[8]/dd/div/div[2]/button'))
        )
        element.click()
    except Exception as e:
        print("내용 선택 및 검색 - 담당 업무 버튼이 없습니다.")

    # 담당 업무명 선택
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='스타일리스트']"))
        )
        element.click()

        if element.text == '스타일리스트':
            print("select_responsibility() - PASS")
        else:
            print("select_responsibility() - Fail", end=" ")
            print(f"선택된 값은 {element.text} 입니다.")
    except Exception as e:
        print("담당 업무명에 '스타일리스트'가 없습니다.")


# 내용 검색 - 담당 업무
def search_responsibility():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div/div/div/div/'
                                                      'div[2]/dl[8]/dd/div/div[2]/button/p/div/input'))
        )
        element.clear()
        element.send_keys('대표')
    except Exception as e:
        print("담당 업무명 검색 input box가 없습니다.")

    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='대표']"))
        )
        element.click()

        if element.text == '대표':
            print("search_responsibility() - PASS")
        else:
            print("search_responsibility() - Fail", end=" ")
            print(f"선택된 값은 {element.text} 입니다.")
    except Exception as e:
        print("담당 업무명에 '대표'가 없습니다.")


# 담당 업무명 [등록] 버튼 클릭
def click_registration():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='등록']"))
        )
        element.click()
    except Exception as e:
        print("담당 업무명 [등록] 버튼이 없습니다.")

    if create_driver.driver.find_element(By.XPATH,
                                         "/html/body/div[5]/div/div/div/div/div/div/div/"
                                         "div[2]/dl[8]/dd/div/div[2]/ul/li/span").text == "스타일리스트":
        print("click_registration() - PASS")
    else:
        print("click_registration() - Fail")


# 이용동의약관 체크박스 선택
def click_agree_terms_of_use():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID,'agreeTermsOfUse'))
        )
        element.click()
    except Exception as e:
        print("약관 동의 이용동의약관 이 없습니다.")

    if create_driver.driver.find_element(By.ID,'agreeTermsOfUse').is_selected():
        print("click_agree_terms_of_use() - PASS")
    else:
        print("click_agree_terms_of_use() - Fail")


# 개인정보동의약관 체크박스 선택
def click_agree_privacy_statement():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID,'agreePrivacyStatement'))
        )
        element.click()
    except Exception as e:
        print("약관 동의 개인정보동의약관 동의 체크박스가 없습니다.")

    if create_driver.driver.find_element(By.ID, 'agreePrivacyStatement').is_selected():
        print("click_agree_privacy_statement() - PASS")
    else:
        print("click_agree_privacy_statement() - Fail")


# [신청 취소] 버튼 클릭
def click_unsubscribe_button():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/button'))
        )
        element.click()
    except Exception as e:
        print("[신청 취소] 버튼이 없습니다.")

    # [신청 취소] 버튼 클릭 후 [확인] 버튼 클릭
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='확인']"))
        )
        element.click()
    except Exception as e:
        print("[신청 취소] 버튼 클릭 후 노출되는 팝업의 [확인] 버튼이 없습니다.")

    # 서비스 이용신청 팝업 종료된 것 확인
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, '로그인'))
        )
        if element.text == "로그인":
            print("click_unsubscribe_button() - PASS")
        else:
            print("click_unsubscribe_button() - Fail")
    except Exception as e:
        print("현재 페이지에 로그인 버튼이 없습니다.")