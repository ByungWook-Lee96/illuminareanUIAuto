from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
import create_driver


# 팝업에서 [X] 버튼 클릭_TC_2
def popup():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))
        )
        element.click()
        result_message = "popup() - PASS"
    except Exception as e:
        result_message = "popup() - Fail"

    print(result_message)
    return result_message


# Work 클릭_TC_3
def click_work():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Work'))
        )
        element.click()

        if create_driver.driver.current_url == 'https://illuminarean.com/work':
            result_message = "click_work() - PASS"
        else:
            result_message = "click_apply() - Fail"
    except Exception as e:
        print("Work 링크가 없습니다.")

    print(result_message)
    return result_message


# [GOODVIBE WORKS 바로가기] 버튼 클릭_TC_4
def click_goodvibe_works():
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'GOODVIBE WORKS 바로가기'))
        )
        element.click()
    except Exception as e:
        print("[GOODVIBE WORKS 바로가기] 버튼이 없습니다.")


# 드라이버의 탭을 새로운 탭으로 변경_TC_4-1
def change_tab():
    result_message = ""
    try:
        create_driver.driver.switch_to.window(create_driver.driver.window_handles[1])

        if create_driver.driver.current_url == "https://works.goodvibe.kr/":
            result_message = "click_goodvibe_works(), change_tab() - PASS"
        else:
            result_message = f"click_goodvibe_works(), change_tab() - Fail " \
                             f"현재 탭은 {create_driver.driver.current_url} 입니다."
    except Exception as e:
        print("새로운 tab으로 변경되지 않았습니다.")

    print(result_message)
    return result_message


# [무료 체험 신청하기] 버튼 클릭_TC_5
def click_apply():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='무료 체험 신청']"))
        )
        element.click()
        if create_driver.driver.find_element(By.XPATH,
                                             "/html/body/div[5]/div/div/div/div/div/div/div/div[1]/h2").text == "서비스 이용신청":
            result_message = "click_apply() - PASS"
        else:
            result_message = "click_apply() - Fail"
    except Exception as e:
        print("[무료 체험 신청하기] 버튼이 없습니다.")

    print(result_message)
    return result_message


# 내용 입력 - 회사명_TC_6
def input_company_name():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'companyName'))
        )
        element.clear()
        element.send_keys(f'테스트회사{create_driver.randomNum}')

        if create_driver.driver.find_element(By.ID, 'companyName').get_attribute("value") == \
                "테스트회사" + str(create_driver.randomNum):
            result_message = "input_company_name() - PASS"
        else:
            result_message = f"input_company_name() - Fail 현재 입력된 값은 " \
                             f"{create_driver.driver.find_element(By.ID, 'companyName').get_attribute('value')} 입니다."
    except Exception as e:
        print("내용 입력 - 회사명이 없습니다.")

    print(result_message)
    return result_message


# 내용 입력 - 대표자명_TC_7
def input_ceo_name():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'ceoName'))
        )
        element.clear()
        element.send_keys(f'테스트이름{create_driver.randomNum}')

        if create_driver.driver.find_element(By.ID, 'ceoName').get_attribute("value") == \
                "테스트이름" + str(create_driver.randomNum):
            result_message = "input_ceo_name() - PASS"
        else:
            result_message = f"input_ceo_name() - Fail 현재 입력된 값은 " \
                             f"{create_driver.driver.find_element(By.ID, 'ceoName').get_attribute('value')} 입니다."
    except Exception as e:
        print("내용 입력 - 대표자명이 없습니다.")

    print(result_message)
    return result_message


# 내용 선택 - 사업자 유형(개인)_TC_8
def select_business_type():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'businessType'))
        )
        element.click()
    except Exception as e:
        print("내용 선택 - 사업자 유형이 없습니다.")

    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='개인']"))
        )
        element.click()

        if create_driver.driver.find_element(By.XPATH, '//*[@id="businessType"]/div/div[1]/div').text == '개인':
            result_message = "select_business_type() - PASS"
        else:
            result_message = f"select_business_type() - Fail 선택된 값은 개인이 아닌 {element.text} 입니다."
    except Exception as e:
        print("내용 선택 - 사업자 유형에 '개인'이 없습니다.")

    print(result_message)
    return result_message


# 내용 선택 - 직원수(21-50명)_TC_9
def select_scale():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'scale'))
        )
        element.click()
    except Exception as e:
        print("내용 선택 - 직원수가 없습니다.")

    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='51-100 명']"))
        )
        element.click()

        if create_driver.driver.find_element(By.XPATH, '//*[@id="scale"]/div/div[1]/div').text == "51-100 명":
            result_message = "select_scale() - PASS"
        else:
            result_message = f"select_scale() - Fail 선택된 값은 '51-100 명'이 아닌 {element.text} 입니다."
    except Exception as e:
        print("내용 선택 - 직원수에 '51-100 명'이 없습니다.")

    print(result_message)
    return result_message


# 내용 입력 - 담당자명_TC_10
def input_name():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'name'))
        )
        element.clear()
        element.send_keys(f'테스트담당자명{create_driver.randomNum}')

        if create_driver.driver.find_element(By.ID, 'name').get_attribute("value") == \
                "테스트담당자명" + str(create_driver.randomNum):
            result_message = "input_name() - PASS"
        else:
            result_message = "input_name() - Fail"
    except Exception as e:
        print("내용 입력 - 담당자명이 없습니다.")

    print(result_message)
    return result_message


# 내용 입력 - 이메일_TC_11
def input_email():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        element.clear()
        element.send_keys(f'test{create_driver.randomNum}@test.com')

        if create_driver.driver.find_element(By.ID, 'email').get_attribute("value") == \
                "test" + str(create_driver.randomNum) + "@test.com":
            result_message = "input_email() - PASS"
        else:
            result_message = "input_email() - Fail"

    except Exception as e:
        print("내용 입력 - 이메일이 없습니다.")

    print(result_message)
    return result_message


# 내용 입력 - 휴대폰 번호_TC_12
def input_mobile():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'mobile'))
        )
        element.clear()
        element.send_keys('010-0000-0000')  # 실제 번호가 있을 수 있어서 해당 부분은 randomNum을 사용하지 않음

        if create_driver.driver.find_element(By.ID, 'mobile').get_attribute("value") == '010-0000-0000':
            result_message = "input_mobile() - PASS"
        else:
            result_message = "input_mobile() - Fail"

    except Exception as e:
        print("내용 입력 - 휴대폰 번호가 없습니다.")

    print(result_message)
    return result_message


# 내용 선택 - 담당 업무_TC_13
def select_responsibility():
    result_message = ""
    # [담당 업무] 버튼 클릭
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
            result_message = "select_responsibility() - PASS"
        else:
            result_message = f"select_responsibility() - Fail 선택된 값은 {element.text} 입니다."
    except Exception as e:
        print("담당 업무명에 '스타일리스트'가 없습니다.")

    print(result_message)
    return result_message


# 내용 검색 - 담당 업무_TC_14
def search_responsibility():
    result_message = ""
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
            result_message = "search_responsibility() - PASS"
        else:
            result_message = f"search_responsibility() - Fail 선택된 값은 {element.text} 입니다."
    except Exception as e:
        print("담당 업무명에 '대표'가 없습니다.")

    print(result_message)
    return result_message


# 담당 업무명 [등록] 버튼 클릭_TC_15
def click_registration():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='등록']"))
        )
        element.click()

        if create_driver.driver.find_element(By.XPATH,
                                             "/html/body/div[5]/div/div/div/div/div/div/div/"
                                             "div[2]/dl[8]/dd/div/div[2]/ul/li/span").text == "스타일리스트":
            result_message = "click_registration() - PASS"
        else:
            result_message = "click_registration() - Fail"

    except Exception as e:
        print("담당 업무명 [등록] 버튼이 없습니다.")

    print(result_message)
    return result_message


# 이용동의약관 체크박스 선택_TC_16
def click_agree_terms_of_use():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'agreeTermsOfUse'))
        )
        element.click()

        if create_driver.driver.find_element(By.ID, 'agreeTermsOfUse').is_selected():
            result_message = "click_agree_terms_of_use() - PASS"
        else:
            result_message = "click_agree_terms_of_use() - Fail"

    except Exception as e:
        print("약관 동의 이용동의약관 이 없습니다.")

    print(result_message)
    return result_message


# 개인정보동의약관 체크박스 선택_TC_17
def click_agree_privacy_statement():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'agreePrivacyStatement'))
        )
        element.click()

        if create_driver.driver.find_element(By.ID, 'agreePrivacyStatement').is_selected():
            result_message = "click_agree_privacy_statement() - PASS"
        else:
            result_message = "click_agree_privacy_statement() - Fail"

    except Exception as e:
        print("약관 동의 개인정보동의약관 동의 체크박스가 없습니다.")

    print(result_message)
    return result_message


# [신청 취소] 버튼 클릭_TC_18,19
def click_unsubscribe_button():
    result_message = ""
    try:
        element = WebDriverWait(create_driver.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/button'))
        )
        element.click()
        if create_driver.driver.find_element(By.XPATH, "//button[text()='확인']").text == "확인":
            print("신청 취소 alert 노출 - PASS")
        else:
            print("신청 취소 alert 노출 - Fail")


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
            result_message = "click_unsubscribe_button() - PASS"
        else:
            result_message = "click_unsubscribe_button() - Fail"
    except Exception as e:
        print("현재 페이지에 로그인 버튼이 없습니다.")

    print(result_message)
    return result_message
