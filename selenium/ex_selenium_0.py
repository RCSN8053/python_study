#셀레니움
#웹 브라우저를 자동으로 제어할 수 있는 도구
#웹 브라우저 실행 및 페이지 이동
#버튼 및 링크 클릭
#검색창에 문자 입력
#웹페이지의 텍스트 추출
#스크롤 및 페이지 이동
# JS로 생성된 동적 콘텐츠 처리

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#페이지 접속
driver.get('https://quotes.toscrape.com/')

#요소찾기
quote = driver.find_element(By.CLASS_NAME, "text")
print(quote.text)

#요소 여러개 찾기
quotes = driver.find_elements(By.CLASS_NAME, "text")
for quotes_ in quotes:
    print(quotes_.text)

#브라우저 종료
driver.quit()#권장