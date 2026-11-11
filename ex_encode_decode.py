#유니코드/인코딩

print(ord("A")) #문자를 유니코드로 출력
print(chr(65)) #유니코드를 문자로 변환

#인코딩
#encode : 문자열을 바이트(byte)로 바꾸는 작업
#파일 저장이나 네트워크 전송시 사용됨
text = "파이썬"
encoded = text.encode('utf-8')
print(encoded)
print(type(encoded))

#디코드
#decode : 인코딩의 반대과정 / 문자열로 다시 복원하는 과정
decoded = encoded.decode('utf-8')
print(decoded)
print(type(decoded))

#인코딩이 맞지 않으면 오류가 발생할 수 있음
try:
    wrong = encoded.decode('cp949')
    print(wrong)
except UnicodeDecodeError:
    print("인코딩 방법이 다름")