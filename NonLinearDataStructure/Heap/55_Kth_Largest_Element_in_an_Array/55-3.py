import heapq
from typing import List

# 55번 배열의 K번째 큰 요소

# 풀이 3. heapq 모듈의 nlargest 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
