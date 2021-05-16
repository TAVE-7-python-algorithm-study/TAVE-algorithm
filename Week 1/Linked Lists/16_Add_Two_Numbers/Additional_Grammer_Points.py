# 문법1: 숫자형 리스트를 단일 값으로 병합하기
## if a = [1,2,3,4,5]일 경우, 병합 결과는 '123456'

# 1) 풀이 1에서 사용한 방식: join()과 for-loop 사용
resultStr = int(''.join(str(e) for e in a))

# 2) map()을 이용해 숫자형 리스트를 단일 값으로 병합하기
resultStr = int(''.join(map(str, a)))

# => 위 두 방법 모두 숫자형을 문자형으로 바꿔 병합한 후 다시 숫자형으로 변환하는 방법임!

# 3) functools와 reduce(), lambda 함수를 이용하여, 숫자형 리스트를 숫자형으로 바로 변경하기
# functools: '함수를 다루는 함수'
# reduce(): 두 인수의 함수를 누적 적용하는 메소드
functools.reduce(lambda x, y: 10 * x + y, a, 0) # 값 x에 계속 10을 곱하면서 자릿수를 올리고, y를 더해 자릿수를 채워나가는 형식



# 문법2: 간결하고 우아하게 숫자형 리스트 연산하기

# 1) lambda 함수 이용하기
fuctools.reduce(lambda x, y : x+y, [1,2,3,4,5]) # 결과: 15

# 2) operator 모듈 활용하기
from operator import add, mul
functools.reduce(add, [1,2,3,4,5]) # 결과: 15
functools.reduce(mul, [1,2,3,4,5]) # 결과: 120
