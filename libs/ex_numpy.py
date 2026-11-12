#Numpy : 파이썬에서 수학과 데이터 분석을 쉽게 할 수 있도록 도와주는 라이브러리
#ndArray : 숫자를 여러 차원으로 저장할 수 있는 배열
#Numpy로 할 수 있는 것들
    # - 숫자 묶음 생성
    # - 평균, 합계, 최댓값
    # - 배열
    # - 2차원 표(행렬)
#빠른 수치 연산
#다차원 배열 ㅣ원
#배열 단위 연산
#통계 계산
#데이터 분석 활용
import numpy as np

#일반 리스트
print("일반 리스트")
a = [1,2,3]
b = [1,2,3]
print(a+b)

#numpy 리스트
print("numpy 리스트")
a = np.array([1,2,3])
b = np.array([1,2,3])
print(a+b)

#1차원 ndarray 생성(숫자가 한 줄로 있는 배열)
arr1 = np.array([1,2,3,4]) #<class 'numpy.ndarray'>
arr_list = [1,2,3,4] #<class 'list'>

#다차원 ndarray 생성
arr2 = np.array([[1,2,3,4],[5,6,7,8]]) #2차원
arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])#3차원
print("2차원 배열 :\n",arr2)
print("3차원 배열 :\n",arr3)

#numpy 간단 계산
a = np.array([1,2,3,4])
print("\nnumpy 계산")
print(a+2)
print(a*2)
print(a**2)

arr3 = np.array([[[0.1,0.2,0.3,0.4],[1,2,3,4]],
                 [[5,6,7,8],[9,10,11,12]]])

print('\nndim은 현제 배열이 몇차원인지 말함')
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print('\nshape은 배열의 형태(배열 구조를 튜플로 보여줌)')
#(총 개수, 행 개수, 열 개수)
print(arr1.shape) #(4,) 4
print(arr2.shape) #(2, 4) 8
print(arr3.shape) #(2, 2, 4) 16

print('\nsize는 배열 요소의 총 개수를 알려줌')
print(arr1.size) #4
print(arr2.size) #8
print(arr3.size) #16

print('\ndtype는 배열 요소의 타입을 알려줌')
print(arr1.dtype) 
print(arr2.dtype) 
print(arr3.dtype) 

print('\nitemsize는 배열 원소 하나가 차지하는 메모리 크기')
print(arr1.itemsize) 
print(arr2.itemsize) 
print(arr3.itemsize) 

print('\ndata는 배열의 실제 데이터가 저장된 메모리 버퍼(buffer 주소)')
print(arr2.data) 
print(arr3.data)

print("\nndArray T : 전치 행렬(행/열을 서로 바꾸는것)")
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.T)
print("flatten() : 1차원으로 펼치기)")
print(arr.flatten())
flat = arr.flatten() #수정도 가능함 <class 'numpy.ndarray'>
flat[0] = 1
print(flat)

print("\nrehape : 원본과 size가 같아야함")
arr_reshape = arr.reshape(2,3) #2행과 3열 반환
print(arr_reshape)

print("\nndarray.sum() : 합계 구하기")
#axis : 어느 축을 기준으로 계산할 것인가?
#axis=0 : 열(세로) 방향 합
#axis=1 : 행(가로축) 방향합
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

print("\nndarray.max : 최댓값 구하기")
print("ndarray.min : 최솟값 구하기")
#axis : 어느 축을 기준으로 계산할 것인가?
#axis=0 : 열(세로) 방향 합
#axis=1 : 행(가로축) 방향합
print(arr.max())
print(arr.min())
print(arr.max(axis=0))
print(arr.min(axis=0))
print(arr.max(axis=1))
print(arr.min(axis=1))

print("\nnp.zeoros(shape) : shape모양으로 배열을 만들고 모든 원소를 0으로 채움")
print(np.zeros((3,4)))
print("\nnp.ones(shape) : shape모양으로 배열을 만들고 모든 원소를 1로 채움")
print(np.ones((2,3,4)))
print("\nnp.full(shape, full_value) : shape모양으로 배열을 만들고 모든 원소를 full_value로 채움")
print(np.full((2,3),4))
#_like 계열 : 다른 배열을 보고 똑같이 따라 만듬
#기존 배열의 shape을 가져와 새 배열 생성
#장점
#shape를 매번 적을 필요가 없다(실수가 줄어듬)
#기본적으로 dtype도 원본을 따라감
print("\n_like 출력")
print(np.zeros_like(arr2))
print(np.ones_like(arr2))
print(np.full_like(arr2, 2))

print("\nnp.random")
#np.random 모듈은 다양한 난수 생성 기능 제공
#머신러닝, 시뮬레이션, 데이터 생성, 테스트 데이터 제작 등에 사용
'''
randint(시작값, 끝값, 사이즈)
지정 범위 안에서 정수 난수 생성
    - 시작값 이상 끝값 미만(끝값 포함 X)
    - size는 생성할 배열의 shape
'''
print(np.random.randint(-100,100,[2,3]))
'''
seed(숫자)
난수 생성의 초기 상태 고정
같은 seed를 주면 항상 같은 난수 결과가 나옴
'''
np.random.seed(1)
print(np.random.randint(-10,10,[2,3]))
np.random.seed(1)
print(np.random.randint(-10,10,[2,3]))#시드가 같아서 같은 값이 나옴

print("\nIndexing, Slicing, funcy")
print("1차원")
print(arr1[0])#인덱싱
print(arr1[:-1])#슬라이싱
print(arr1[[0,2]])#펜시
print("2차원")
print(arr2[1,0])#인덱싱
print(arr2[1,:-1])#슬라이싱
print(arr2[[0,1], [0,2]])#펜시
print(arr2[:, [0,2]])#펜시+인덱싱+슬라이싱