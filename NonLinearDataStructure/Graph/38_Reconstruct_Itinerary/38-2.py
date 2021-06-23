import collections
from typing import List
# 38번 일정 재구성

# 풀이 2: 스택 연산으로 큐 연산 최적화 시도

# 매 반복마다 pop(0)에서 O(n) time이 걸리는 큐 연산을 스택을 이용해 최적화하기
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프를 구성할 때 '뒤집어서' 구성 -> 스택을 통한 연산을 위함
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        route = []
        
        def dfs(a):
            # 마지막 값을 읽어 어휘 순으로 방문
            # 이 역시 사전 역순으로 결과가 담기게 됨
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로 출력
        return route[::-1]
