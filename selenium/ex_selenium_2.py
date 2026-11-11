#브라우저 실행 + 페이지 접속
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

#한페이지에서 여러 명언 수집하기
results = [] #수집한 데이터 저장할 리스트

quote_blocks = driver.find_elements(By.CLASS_NAME, "quote")
for block in quote_blocks:
    qoute_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text
    tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
    tags = [t.text for t in tag_elements]
    # 리스트 컴프리핸션을 사용하여 각 tag 요소의 텍스트만 추출
    # 컴프리핸션 : 반복문을 이용해 새로운 컬렉션을 만드는 축약 문법
    #[표현식 for 변수 in 반복가능객체]
    #tags = []
    #for t in tag_elements:
    #   tags.append(t.text)
    #와 같은 말임

    results.append({
        'page': 1,
        'quote': qoute_text,
        'author': author,
        'tags': tags
    })
    print(f'{author} : {qoute_text} / tag {tags}')
print('현재까지 수집된 개수 :', len(results))

driver.quit()