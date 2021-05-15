# 7장 배열 - 12번 주식을 사고팔기 가장 좋은 시점 (난이도 1)
import sys
from typing import List

# 풀이1. 브루트 포스로 계산
# 브루트 포스: 무차별 대입 검색 -> Time out Error
def maxProfit(prices: List[int]) -> int:
    max_price = 0
    # enumerate(): list/tuple/string의 인덱스와 원소에 동시에 접근하며 for-loop 반복 가능
    for index, price in enumerate(prices): 
        for j in range(index, len(prieces)):
            max_price = max(prices[j] - price, max_price)
    return max_price
    
def main() :
  ls = [7,1,5,3,6,4]
  print(maxProfit(ls))
