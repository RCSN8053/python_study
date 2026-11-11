from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

#다음페이지 이동 + 반복 수집

MAX_PAGES = 3
current_page = 1

results = []
while current_page <= MAX_PAGES:
    print(f"=== {current_page}페이지 수집중 ===")
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        qoute_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
        tags = [t.text for t in tag_elements]
        results.append({
            'page': current_page,
            'quote': qoute_text,
            'author': author,
            'tags': tags
        })
    #next 버튼 찾기
    #'li.ext a'는 class='next'를 가지고 li태그 안에 있는 a태그를 의미
    #CSS_SELECTOR : CSS문법을 이용해서 HTML요소를 찾는 방법
    #Selenium에서 가장 많이 쓰는 방식 중 하나
    next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')

    if not next_buttons:
        break

    #다음페이지로 이동 클릭
    next_buttons[0].click()

    current_page += 1
print("최종 수집 개수 :", len(results))


driver.quit()