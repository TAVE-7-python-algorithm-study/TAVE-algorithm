# 풀이 1: Counter를 이용한 음수 순 추출

# 요소의 값을 key로 하는 해시 테이블에 빈도 수를 저장한 후, 
# 우선순위 큐를 이용해 상위 k번만큼 추출하여 k번 이상 등장하는 요소 추출하기
import collections
import heapq
from typing import List

class Solution:
    # key: 빈도수, value: freqs의 key(=숫자) -> heap은 key 순서대로 내림차순으로 정렬되기 때문
    # 파이썬의 heapq 모듈에서는 최소 힙만 지원하므로, key를 음수로 저장
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums) # 숫자가 key로, 빈도 수가 value로, 딕셔너리로 저장됨
        freqs_heap = []

        # heap에 key와 value를 치환하고, value 값을 음수로 변환하여 key로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

            topk = list()
            # 가장 작은 음수부터 k번만큼 추출하여 k번 이상 등장하는 요소를 추출
            for _ in range(k):
                topk.append(heapq.heapop(freqs_heap)[1])

            return topk
