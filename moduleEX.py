#수학 모듈
#수학 계산 기능을 제공하는 모듈
import math

#랜덤 모듈
import random

#날짜/시간 모듈
#날짜와 시간을 다루는 모듈
#현재 시간 확인, 날짜 계산에 사용
import datetime

#시간 제어 모듈
#시간 흐름을 제어 하는 모듈
#프로그램을 잠시 멈출때 사용
import time

#시스템 모듈
#파이썬 실행 환경을 다루는 모듈
import sys

#운영체제 모듈
#운영체제와 관련된 기능 제공
#파일/폴더 경로 처리에 사용
import os

#데이터 형식 모듈
#json형식으로 데이터를 변환
# - json : 데이터를 약속된 모양으로 적는 방식("key":"value")
#웹 API 저장에 사용
# - API : 프로그램끼리 대화하는 방법(규칙)
import json

#정규 표현식 모듈
#문자열 패턴 검사 모듈
#형식 확인(아이디,이메일)에 사용
import re

#csv 파일 모듈
#csv(엑셀) 파일을 읽고 쓰는 모듈
#데이터 저장/분석 기초에 사용
import csv

#자료 구조 모듈
#자료구조를 편하게 쓰도록 도와줌
#카운트, 큐, 딕셔너리 확장 기능 제공
from collections import Counter #카운터만

# import ex26_11_10 #모듈 전체 불러오기
# from ex26_11_10 import is_prime_number #모듈중 일부만 불러오기


# #16의 제곱근 출력
# print(math.sqrt(16))

# #2^3 출력
# print(math.pow(2,3))

# #랜덤 int 출력
# print(random.randint(1,10))

#현제 날짜시분초 출력
# print(datetime.datetime.now())

# time.sleep(3)#3초 정지
# print("3초 후 실행")

# print(sys.version)#현제 파이썬 버전 추력

# print(os.getcwd())#현재 작업중인 폴더 경로 출력

# data = {
#     'name' : 'jin',
#     'age' : 22
# }
# print(json.dumps(data))

# print(bool(re.match('hi', 'hipython')))#문자열에 hi 있는지 확인

# #CSV 파일에 한 줄 데이터를 저장
# with open('test.csv', 'w', newline='') as f:
#     csv.writer(f).writerow(['name','score'])

# print(Counter('apple')) #문자열 개수를 셈