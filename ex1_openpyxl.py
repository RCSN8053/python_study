from openpyxl import *
from openpyxl.styles import PatternFill
from openpyxl.chart import BarChart, Reference

w2 = load_workbook('test.xlsx')

new_ws = w2.create_sheet()
new_ws.title = 'scores'

color = PatternFill(fill_type='solid',fgColor='FFFF00')

# new_ws['A1'] = '이름'
# new_ws['B1'] = '국어'
# new_ws['C1'] = '수학'

new_ws.append(['이름', '점수'])
new_ws.append(['홍길동', 90])
new_ws.append(['홍길순', 80])
new_ws.append(['홍길자', 70])

for cell in new_ws[1]:
    cell.fill = color

chart = BarChart()

data = Reference(new_ws, min_col=2, min_row=1, max_row=5)

chart.add_data(data, titles_from_data= True)

new_ws.add_chart(chart, 'E5')

w2.save('test.xlsx')