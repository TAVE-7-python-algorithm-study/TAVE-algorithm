# 풀이2. 저점과 현재 값과의 차이 계산
# 문제 핵심 -> 주식 그래프의 저점과 고점 찾기!
def maxProfit(prices: List[int]) -> int:
    profit = 0               # 수익의 초깃값은 시스템의 가장 작은 값으로 설정! (최대 수익을 찾아야 함)
    min_price = sys.maxsize  # 저점의 초깃값은 시스템의 가장 큰 값으로 설정!

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price) # (현재 시점 - 저점)
    return profit

def main() :
  ls = [7,1,5,3,6,4]
  print(maxProfit(ls))
