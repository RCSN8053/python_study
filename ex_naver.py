import requests as req
from bs4 import BeautifulSoup

response = req.get('https://news.naver.com/')
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.select('.cnf_news_item')
print(content[0].text)
