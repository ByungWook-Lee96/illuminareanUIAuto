from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from selenium.webdriver.common.keys import Keys  # 키보드 클릭할 때 쓸 부분
from selenium.webdriver.chrome.options import Options

import time
import random

randomNum = random.randrange(1,100)

# driver 옵션 추가(시스템에 부착된 장치가 작동하지 않습니다. 삭제하기 위한 옵션)
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# driver 바로 꺼지지 않게 함.
# options.add_experimental_option("detach", True)

# 전체화면 옵션
options.add_argument("--start-maximized")

# driver 옵션 설정
driver = webdriver.Chrome(options=options)

# driver에 url 넣음
url = 'https://illuminarean.com/'
driver.get(url)

# 팝업이 노출될 수 있어서 팝업이 노출되면 클릭을 하고, 노출되지 않으면 해당 부분 지나감.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))
    )
    element.click()
except Exception as e:
    print("팝업의 요소가 없거나 팝업이 없음")
time.sleep(1)

# Work 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Work'))
    )
    element.click()
except Exception as e:
    print("Work 링크가 없습니다.")
time.sleep(1)

# [GOODVIBE WORKS 바로가기] 버튼 클릭(a링크)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'GOODVIBE WORKS 바로가기'))
    )
    element.click()
except Exception as e:
    print("[GOODVIBE WORKS 바로가기] 버튼이 없습니다.")
time.sleep(1)

# 드라이버의 탭을 새로운 탭으로 변경
driver.switch_to.window(driver.window_handles[1])

# [무료 체험 신청하기] 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='무료 체험 신청']"))
    )
    element.click()
except Exception as e:
    print("[무료 체험 신청하기] 버튼이 없습니다.")
time.sleep(1)

# 내용 입력 - 회사명
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'companyName'))
    )
    element.clear()
    element.send_keys(f'테스트회사{randomNum}')
except Exception as e:
    print("내용 입력 - 회사명이 없습니다.")
time.sleep(1)

# 내용 입력 - 대표자명
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ceoName'))
    )
    element.clear()
    element.send_keys(f'테스트이름{randomNum}')
except Exception as e:
    print("내용 입력 - 대표자명이 없습니다.")
time.sleep(1)

# 내용 선택 - 사업자 유형(개인)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'businessType'))
    )
    element.click()
except Exception as e:
    print("내용 선택 - 사업자 유형이 없습니다.")
time.sleep(1)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[text()='개인']"))
    )
    element.click()
    if element.text == '개인':
        print("선택된 값은 개인입니다.")
    else:
        print(f"선택된 값은 개인이 아닌 {element.text} 입니다.")
except Exception as e:
    print("내용 선택 - 사업자 유형에 '개인'이 없습니다.")
time.sleep(1)


# 내용 선택 - 직원수(21-50명)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'scale'))
    )
    element.click()
except Exception as e:
    print("내용 선택 - 직원수가 없습니다.")
time.sleep(1)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//*[text()='51-100 명']"))
    )
    element.click()
    if element.text == '51-100 명':
        print("선택된 값은 51-100 명입니다.")
    else:
        print(f"선택된 값은 '51-100 명'이 아닌 {element.text} 입니다.")
except Exception as e:
    print("내용 선택 - 직원수에 '51-100 명'이 없습니다.")
time.sleep(1)

# 내용 입력 - 담당자명
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'name'))
    )
    element.clear()
    element.send_keys(f'테스트담당자명{randomNum}')
except Exception as e:
    print("내용 입력 - 담당자명이 없습니다.")
time.sleep(1)

# 내용 입력 - 이메일
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    element.clear()
    element.send_keys(f'test{randomNum}@test.com')
except Exception as e:
    print("내용 입력 - 이메일이 없습니다.")
time.sleep(1)

# 내용 입력 - 휴대폰 번호
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'mobile'))
    )
    element.clear()
    element.send_keys('010-0000-0000') # 실제 번호가 있을 수 있어서 해당 부분은 randomNum을 사용하지 않음
except Exception as e:
    print("내용 입력 - 휴대폰 번호가 없습니다.")
time.sleep(1)


# 내용 선택 및 검색 - 담당 업무
# 먼저 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div/div/div/div'
                                                  '/div[2]/dl[8]/dd/div/div[2]/button'))
    )
    element.click()
except Exception as e:
    print("내용 선택 및 검색 - 담당 업무 버튼이 없습니다.")
time.sleep(1)

# 담당 업무명 선택
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='스타일리스트']"))
    )
    element.click()
    if element.text == '스타일리스트':
        print("선택된 값은 스타일리스트 입니다.")
    else:
        print(f"선택된 값은 '스타일리스트'이 아닌 {element.text} 입니다.")
except Exception as e:
    print("담당 업무명에 '스타일리스트'가 없습니다.")
time.sleep(1)

# 담당 업무명 검색
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div/div/div/div/'
                                                  'div[2]/dl[8]/dd/div/div[2]/button/p/div/input'))
    )
    element.clear()
    element.send_keys('대표')
except Exception as e:
    print("담당 업무명 검색 input box가 없습니다.")
time.sleep(1)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='대표']"))
    )
    element.click()
    if element.text == '대표':
        print("선택된 값은 대표 입니다.")
    else:
        print(f"선택된 값은 '대표'이 아닌 {element.text} 입니다.")
except Exception as e:
    print("담당 업무명에 '대표'가 없습니다.")
time.sleep(1)

# 담당 업무명 [등록] 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='등록']"))
    )
    element.click()
except Exception as e:
    print("담당 업무명 [등록] 버튼이 없습니다.")
time.sleep(1)

# 이용동의약관 체크박스 선택
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'agreeTermsOfUse'))
    )
    element.click()
except Exception as e:
    print("약관 동의 이용동의약관 이 없습니다.")
time.sleep(1)

# 개인정보동의약관 체크박스 선택
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'agreePrivacyStatement'))
    )
    element.click()
except Exception as e:
    print("약관 동의 개인정보동의약관 동의 체크박스가 없습니다.")
time.sleep(1)


# [신청 취소] 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/button'))
    )
    element.click()
except Exception as e:
    print("[신청 취소] 버튼이 없습니다.")
time.sleep(1)

# [신청 취소] 버튼 클릭 후 [확인] 버튼 클릭
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='확인']"))
    )
    element.click()
except Exception as e:
    print("[신청 취소] 버튼 클릭 후 노출되는 팝업의 [확인] 버튼이 없습니다.")
time.sleep(3)


