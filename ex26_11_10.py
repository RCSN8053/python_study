# import random

#소수 확인
def is_prime_number(num):
    n = 1
    s = 0
    is_prime = False

    while(n <= num):
        if num%n == 0:
            s+=1
        n += 1

    if s == 2:
        is_prime = True
    else:
        is_prime = False

    print(f"{num} 은 소수입니까? : {is_prime}")
    return is_prime

# a = [2, 1, 5, 6, 7]
# b = []

# b.append(2)
# b.append(1)
# b.append(5)
# b.append(6)
# # b.append(7)

# c = ['월','화','수','목','금']
# c += ['토','일']
# i=0
# while(i < len(c)):
#     print(c[i])
#     i += 1

# d = [2,1,'오',6,7]
# d[d.index('오')] = 5

# i=0
# n=0
# while(i < len(c)):
#     if c[i] == '화':
#         print("화가 있음")
#         print(f"화는 {n} 번쨰 있음")
#     i+=1
#     n+=1
# if '화' in c:
#     print("화가 있음")
# else:
#     print("화가 없음")
# n = c.index('화')
# print(n)


# c = ['월','화','수','목','금']
# del c[-1]
# print(c)

# c = ['월','화','수','목','금']
# del c[c.index('금')]
# print(c)

# c = ['월','화','수','목','금']
# c.remove('금')
# print(c)

#딕셔너리
#1월 부터 12월까지 마지막날 넣기

# a = {"1월":31, "2월": 28, "3월":31, "4월":30, "5월":31, "6월":30, "7월":31, "8월":31, "9월":30, "10월":31, "11월":30, "12월":31}
# b = {}
# for i in range(12):
#     m = str(i+1) + "월"
#     end_day = 31
#     if i == 2:
#         end_day = 28
#     elif i in [4,6,9,11]:
#         end_day == 30
#     b[m] = end_day
# print(a)
# print(b)

#슬라이싱

# s = "안녕하세요"
# print(len(s))
# print(s[:2])
# print(s[1:2])
# print(s[:4])
# print(s[3:])
# print(s[3:len(s)])

# i = 0
# while(i<len(s)):
#     print(s[i])
#     i += 1
# for c in s:
#     print(c)

# i = len(s)
# while (i>0):
#     print(s[i-1])
#     i -= 1

# s = "a안b녕c하d세e요f"
# print(s[1::2])

#예외처리

# try:
#     num = int("ABC")
#     print(num)
# except ValueError:
#     print("숫자를 변환할 수 었습니다.")

# print("프로그램 종료")

#클래스

# class person:
#     def __init__(self, name, age, hobby):
#         self.Hello = "안녕하세요"
#         self.name = name
#         self.age = age
#         self.hobby = hobby

#     def hi(self):
#         print(f"{self.Hello} 저는 {self.name} 이고 {self.age}살 입니다. 취미는 {self.hobby}입니다.")

#     def hello(self):
#         print("Hello")

# a = person("진",22,"운동")
# a.hello()
# a.hi()
# print(f"이름 : {a.name}")
# print(f"나이 : {a.age}")
# print(f"취미 : {a.hobby}")

# class person_:
#     pass

# jin = person_()
# jin.name = "진"
# print(jin.name)

#클래스 내부에서만 사용가능한 attribute
#__를 넣으면 외부에서 조작할 수 없기 때문에 밑에와 같이 내부에서 우회를 할 수 있게 제작해야함

# class Person_pri:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.__weight = weight

#     def diet(self, loss_weight):
#         self.__weight -= loss_weight
#         print(self.__weight)

# a = Person_pri("Jin", 20 , 80)
# a.diet(10)

#클래스 속성
# class person_2:
#     folder = [] #클래스 속성
#     def add_files(self, file):
#         self.folder.append(file)

# jin = person_2()
# jin.add_files('txt')
# print(jin.folder)

# kim = person_2()
# kim.add_files('img')
# print(kim.folder)

