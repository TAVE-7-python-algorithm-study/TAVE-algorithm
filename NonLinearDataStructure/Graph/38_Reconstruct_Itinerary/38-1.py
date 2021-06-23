import collections
from typing import List
# 38번 일정 재구성

# 풀이 1: DFS로 일정 그래프 구성
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성하기
        graph = collections.defaultdict(list)
       # dictionary 형태로 그래프 구성, sorted() 함수를 이용해 중복 key 값 사전 순 정렬
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        
        # pop()으로 재귀 호출하며 모두 꺼내 결과 리스트에 역순으로 요소 담기
        # 이미 방문한 경로는 pop()이 수행되어 삭제되었으므로, 재방문 방지 가능
        def dfs(a):
            # 어휘 순으로 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        # 문제 조건 모든 일정은 'JFK'에서 출발
        dfs('JFK')
        # 결과가 역순으로 담겼으므로, 마지막에 결과를 출력할 때에는
        # 다시 뒤집어서 어휘 순으로 '맨 처음에 읽어들였던 값'이 리스트의 '맨 처음'으로 오도록 만듦
        return route[::-1]
