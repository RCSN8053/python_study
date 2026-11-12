#pandas : 파이썬에서 데이터 분석과 데이터를 처리하기 위한 대표적인 라이브러리
#주로 표 형태의 데이터(엑셀,csv,데이터베이스 등)을 다루는 데 사용
#데이터 과학, 머신러닝, 금융분석, 통계 처리 등에서 매우 많이 사용됨
'''
Series: 인덱스를 가진 1차원 데이터
DataFrame : 행과 열로 구성된 표 형태의 데이터
- '열 이름' : [값들]
- 각 열에는 열 이름이 있음
- 각 행에는 자동으로 행번호(index)가 붙음
'''
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],

        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df) #전체 출력
print(df['Name']) #열 하나씩 출력
print(df['Age'])
print(df['Sex'])

#타입 출력
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
print(type(df['Name'])) #<class 'pandas.core.series.Series'>

#이름이 age인 series 생성
age = pd.Series([22,35,58], name='Age')
print(age)

#기본 통계 함수
print('max : 최댓값')
print('최대 나이 : ', df['Age'].max())
print('min : 최솟값')
print('최소 나이 : ', df['Age'].min())
print('mean : 평균값')
print('평균 나이 : ', df['Age'].mean())

print('요약 통계 정보 보기')
#describe : 숫자형 열에 대해 '요약 통계 정보 한번에 보기
print(df.describe())
'''
count   3.000000 데이터 개수
mean   38.333333 평균
std    18.230012 표준편차
min    22.000000 최솟값
25%    28.500000 1사분위수(Q1)
50%    35.000000 중앙값(median)
75%    46.500000 3사분위수 (q3)
max    58.000000 최댓값
'''
print('datafram의 요약 정보 보기')
#구조 보기
print(df.info())

print("\nDataFrame에서 특정 행을 선택하는 방법 2가지")
#iloc : 위치(Position)로 선택(0번째, 1번째 처럼 순서/번호 접근)
#loc : 라벨(Label)로 선택(index에붙어있는 이름으로 접근)
'''
iloc
iloc은 index의 값이 뭐든 상관없이 몇번째 줄이냐를 가져옴
'''
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])
'''
loc
loc은 index label로 접근
index를 '이름'으로 바꾸면(ex: Name열을 index로 지정)
df.index = ['사람1','사람2','사람3']
df,loc['사람1']로 접근
'''
print(df.loc[0])

#상위 하위 데이터 출력
print("\nhead(), tail()")
#head() : 위쪽 몇개의 행만 보여주는 함수
#tail() : 아래쪽 몇개의 행만 보여주는 함수
#기본값은 5개

print(df.head(1))
print(df.tail(1))

#열 수정
df['Survived'] = [0,1,1]
print(df)

#열 이름 바꾸기
df = df.rename(columns={'Sex' : "Gender"})
print(df)

#열 제거 axis=1 : 열 / axis=0 : 행
df = df.drop('Survived', axis=1)
print(df)

#결측치(NaN) 처리
#결측치란 값이 비어있는 상태
#pandas에서 보통 NaN(Not of Nuber)로 표시
#none를 넣어도 pandas에서는 자동으로 NaN으로 변환

print(df.isnull())
df2 = df.copy()
df2.loc[1,'Age'] = None
print(df2.isnull())

print(df2.dropna(axis=0)) #dropna() : 결측지가 있는 부분 제거
print(df2.fillna(0)) #fillna(i) : 결측치를 값으로 채우기
print(df2['Age'].fillna(df['Age'].mean)) # 결측치 평균값으로 채우기
print(df2.ffill())#바로 이전행의 값으로 채운다.foword
print(df2.bfill())#이후 행의 값으로 채운다.backward