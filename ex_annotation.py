#이 변수나 함수는 이런 타입이다. 라고 설명해주는 표시
#가독성 향상용

#변수 어노테이션

#기본 변수
age = 30

#어노테이션 추가
#변수이름 : 자료형 = 값
age: int = 30

print(age)

#함수 어노테이션

def add(a: int, b: int) -> int:
    return a+b

print(add(1,2))

#리스트, 딕셔너리 어노테이션

#리스트 안에 int가 들어간다는 의미
nums = list[int] = [1,2,3]

#딕셔너리 저장타입 지정
person: dict[str, int] = {
    'age' : 30,
    'height' : 170
}
