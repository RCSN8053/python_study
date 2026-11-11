#정규표현식

#문자열에서 특정한 규칙이나 패턴을 가진 데이터를 추출, 검색, 치환하기 위한 표현방식

import re

#일반 검색
text = "내 혈압은 120mmHg 입니다."
print('120' in text)

#정규표현식 검색
pattern = r'\d+' #\d+ 는 숫자 한개이상의 패턴 확인
reult = re.findall(pattern, text)#패턴과 같은 문자를 모두 추출
print(reult)

sample = 'abc123xyz456'

print(re.findall(r'\d+', sample))#숫자 찾기
print(re.findall(r'[a-z]+', sample))#영어 찾기
# + 가 붙으면 1개이상 붙은것을 한번에 추출
# * 가 붙으면 0개이상
# ? 가 붙으면 0개 또는 1개
# 아무것도 없으면 하나씩 추출

data = '이메일은 test123@gmail.com 입니다.'
email_pattern = r'\w+@\w+.\w+'
print(re.findall(email_pattern, data))
#\w : 문자 또는 숫자
# .같은 문자도 \를 사용해야함

# re.search()

#문자열 치환
text2 = "가격은 12000원입니다."
print(re.sub(r'\d+','',text2))

#정규식/일반 일처리 비교
text3 = "몸무게 60kg , 키 170cm"
print(text3.split(','))
print(re.findall(r'\d+', text3))


#정규식은
#크롤링 데이터에서 숫자만 추출할때
#단위 제거
#특정 형식 데이터 찾기 ex) 이메일, 날짜
#불필요한 특수 문자 제거
#할때 사용함