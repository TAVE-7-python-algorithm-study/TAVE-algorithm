import heapq
from typing import List
# 55번 배열의 K번째 큰 요소

# 풀이 2. heapq 모듈의 heapify 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
