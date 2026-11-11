import openpyxl
from openpyxl import *

# print(openpyxl.__version__)

w1 = Workbook() #새 엑셀파일 제작
ws = w1.active # 만들어진 엑셀 파일에서 기본 시트를 선택
w1.save('test.xlsx')#지금 만든 엑셀 파일을 실제로 저장

#기존에 저장된 엑셀 불러오기
w2 = load_workbook('test.xlsx')
ws2 = w2.active

ws2['A1'] = 'hello' #A1 셀에 값 입력
ws2['C3'] = 'bye'

a = 'python'
for row in ws2['D5':'F8']:
    for cell in row:
        cell.value = a

w2.save('test.xlsx')