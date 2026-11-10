
# a = 10
# b = 20
# print(str(a)+str(b))

# a = '1'
# b = '2'
# print(int(a)+int(b))

# a = '1.1'
# b = '2.2'
# c = round(float(a)+float(b),1)
# print(c)

# a = '1.1'
# b = '2.2'
# a = int(float(a))
# b = int(float(b))
# print(a+b)

# a = ord(input())
# a += 1
# print(chr(a))

# l = input().strip().split(',')
# print(l)

# a, b =input().split()
# a= float(a)
# b= float(b)
# print(format(a/b,".3f"))

# a,b,c = map(int, input().strip().split(','))
# print(a+b+c)

# c = int(input(),16)
# for i in range(1,16):
#     print(f"{format(c,'X')}*{format(i,'X')}={format(c*i,'X')}")

# r, g, b = input().split()
# r = int(r)
# g = int(g)
# b = int(b)
# a=0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(f"{i} {j} {k}")
#             a += 1
# print (a)

def print_dan(dan):
    print("== {}단 ==".format(dan))
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan * i))
        i += 1

print_dan(2)

h, b, c, s = input().split()
b = b//8
a = h*b*c*s

