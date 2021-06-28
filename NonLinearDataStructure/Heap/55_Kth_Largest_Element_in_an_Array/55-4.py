from typing import List
# 55번 배열의 K번째 큰 요소

# 풀이 4. 정렬을 이용한 풀이
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
