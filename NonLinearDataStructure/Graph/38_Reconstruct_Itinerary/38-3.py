import collections
from typing import List
# 38번 일정 재구성

# 풀이 23: 일정 그래프 반복
# 재귀가 아닌, 동일한 구조를 스택을 이용한 반복으로 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 사전 순서대로 그래프 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        # 스택을 구성할 경우, 사전순으로 앞에 오지만, 도착지가 없는 여행지의 경우 막히게 됨
        # 따라서 반복을 통해 한번 더 풀어낼 수 있도록 별도의 변수가 필요하기 때문에 route와 stack 두개의 변수를 이용함
        # route: 최종 결과 리스트
        # stack: 현재 탐색 경로, 'JFK'에서 출발
        route, stack = [], ['JFK']
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
        
        # 다시 뒤집어 어휘 순 결과로 반환
        return route[::-1]
