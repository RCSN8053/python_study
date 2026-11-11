#요소를 찾는 방법
#태그이름(TAGE_NAME)
#class / id(CLASS_NAME, ID)
#xPath

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

#태그 이름으로 찾기
# - html 태그요소로 찾기(실무는 잘 안씀)
div_elements = driver.find_elements(By.TAG_NAME, "div")
print("TAG_NAME :", len(div_elements))

#class로 찾기(CLASS_NAME)
# - html에서 class='text' 처럼 지정된 class이름으로 요소 찾기
# - 가장 자주 사용함
# - class에 공백이 포함된 경우는 CLASS_NAME으로 바로 찾기 어려움
first_quote_text = driver.find_element(By.CLASS_NAME, 'text')
print('CLASS_NAME :',first_quote_text.text)

# id로 요소 찾기
# - 보통 페이지에서 유일하게 존재
# - 정확하게 찾고 싶을때 가장 안정적
# id_element = driver.find_element(By.ID, 'username')
# print("ID :", id_element) #현제 사이트는 ID가 없어서 에러가남

#find_element : 요소 1개만 찾음(없으면 에러)
#find_elements : 요소 여러개를 찾고 리스트로 변환(없으면 빈 리스트가 됨)

quote_ = driver.find_element(By.CLASS_NAME, 'quote')
quote_s = driver.find_elements(By.CLASS_NAME, 'quote')
print('find_element :', type(quote_))
print('find_elements :', len(quote_s))

#xPath
# - xPath는 HTML의 구조(경로)를 이용해서 요소를 찾는 방법
# - id나 class로 찾기 어려울 때 사용
#장점 : 조건이나 경로로 정확하게 요소 선택이 가능함
#단점 : 페이지 구조가 바뀌면 xPath도 같이 깨질 수 있다.

xpath_quote_text = driver.find_element(By.XPATH,"//div[@class='quote']/span[@class='text']")
'''
- // 문서 전체에서 검색
- div[@class='quote'] : dive 태그 중 class='quote'인 요소
- / : 바로 아래 자식(child) 관계
- span[@class='text] : 위에서 찾은 div바로 아래에 있는 span 중에서 class='text'인 요소

의미
- class='quote'인 div 자식 중에서 class='text'인 spanㅇㄹ 찾아라
'''
print("xpath :", xpath_quote_text.text)

xpath_block = driver.find_element(
    By.XPATH, "(//div[@class='quote'])[1]"
)
xpath_block_author = xpath_block.find_element(
    By.CLASS_NAME,'author'
)
print("xPath의 저자 :", xpath_block_author.text)


driver.quit()