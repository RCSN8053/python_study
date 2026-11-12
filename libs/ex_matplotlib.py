#Matplotlib = 데이터를 표현할 수 있게 해주는 파이썬 라이브러리
#figure : 큰 도화지
#subplots : 도화지 원에 나눠진 작은 칸들
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


#기본 스타일 적용
plt.style.use('default')

#y값만 전달, x는 자동으로 채워짐
plt.plot([2,4,6,8])

#x랑 y값 직접 설정
x = [2,4,6,8]
y = [1,3,5,7]
plt.plot(x,y)
# plt.show()

fig = plt.figure()
#(행 개수, 열개수, 위치값)
fig.add_subplot(1,2,1)
fig.add_subplot(2,2,2)
# plt.show()

# plt.close('all')
fig = plt.figure()
a1 = fig.add_subplot(1,2,1)
a2 = fig.add_subplot(1,2,2)

x = range(0,10)
y = range(5, 15)
a1.plot(x, y, 'c*')

x = range(0,50)
y = range(0, 50)
a2.plot(x, y, 'mp')

# plt.show()

# ggplot 특징
# - 배경에 격자가 있음

plt.style.use('ggplot')
a = fig.add_subplot(111)

x = [3,4]
y = [1,2]
labels = ['english','math']
colors = ['red','blue']

a.bar(x, y, tick_label=labels, color=colors)#세로막대
# a.barh(x, y, tick_label=labels, color = colors)#가로막대
plt.show()
