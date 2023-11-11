from selenium.webdriver.chrome.options import Options
from selenium import webdriver
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
