# 베이스 이미지 선택
FROM arm64v8/python:3.12

# 작업 디렉토리 설정
WORKDIR /app

# Selenium 및 필요한 Python 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade webdriver_manager

# 소스 코드 복사
COPY . .

# 실행 명령어 설정
CMD ["python3", "test_exam.py"]