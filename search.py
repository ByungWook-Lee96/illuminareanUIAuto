from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from selenium.webdriver.common.keys import Keys  # 키보드 클릭할 때 쓸 부분
import time

# driver 옵션 추가(시스템에 부착된 장치가 작동하지 않습니다. 삭제하기 위한 옵션)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 전체화면 옵션
options.add_argument("--start-maximized")

# driver 옵션 설정
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# 주식 검색 후 해당 주식 상세 확인
def search_stock():


    # 주식 변수 생성
    stock = "테슬라"


    # driver에 url 넣음
    url = 'https://wts.tossinvest.com/'
    driver.get(url)

    try:
        # 해당 돋보기 버튼이 있는지 10초 동안 확인
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[1]/div/div/div[1]/div/nav/ul/li[1]/div')))

        # 돋보기 버튼 클릭
        driver.find_element(By.XPATH, value='//*[@id="__next"]/div[1]'
                                            '/div/div/div[1]/div/nav/ul/li[1]/div').click()
        time.sleep(1)

        # 주식 입력 및 검색
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'search')))

        driver.find_element(By.NAME, value="search").clear()  # 값이 있을 수 있으니 clear 먼저해줌
        driver.find_element(By.NAME, value="search").send_keys(stock)
        driver.find_element(By.NAME, value="search").send_keys(Keys.RETURN)
        time.sleep(1)

        # 주식 상세 확인(검색한 주식이 맞는지 확인)
        # li[i]를 넣어서 1~3 숫자를 돌리면서 stock 변수와 동일한 주식명을 찾음.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div[2]/section[2]/ul/li[1]/span[2]/span[1]/span')))

        for i in range(1,4):
            result = driver.find_element(By.XPATH, value='//*[@id="__next"]/div[1]/div/div/main/div[2]'
                                                         '/section[2]/ul/li[' + str(i) + ']/span[2]/span[1]/span')\
                .get_attribute('innerText')  # text 값을 가져옴
            if stock == result:
                driver.find_element(By.XPATH,
                                    value='//*[@id="__next"]/div[1]/div/div/main/div[2]/section[2]/ul/li[' + str(
                                        i) + ']/span[2]/span[1]/span').click()
                break
            print(result) # 프린트로 로그 확인(범위를 2~4로 하면 제대로 구축했는지 알 수 있음)
            time.sleep(1)

        # 해당 주식이 맞는지 확인
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div[1]/div/div/main/div/header/div[1]/span/span')))

        stock_detail = driver.find_element(By.XPATH, value='//*[@id="__next"]/div[1]'
                                            '/div/div/main/div/header/div[1]/span/span').get_attribute('innerText')
        if stock == stock_detail:
            print("PASS, 검색한 주식의 상세화면입니다.")
            print(stock+" 상세화면입니다.")
        else:
            print("Fail, 검색한 주식의 상세화면이 아닙니다.")
            print(stock_detail + " 상세화면입니다.")

        time.sleep(1)
        return True

    # 이슈 발생 시 에러 출력
    except Exception as e:
        print(e)
        return False



