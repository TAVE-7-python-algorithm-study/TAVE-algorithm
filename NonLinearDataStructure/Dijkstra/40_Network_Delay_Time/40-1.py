import collections
import heapq
from typing import List

# 40번 네트워크 딜레이 타임

# 풀이 1: 다익스트라 알고리즘 구현

# 2가지의 판별 조건
# 1) 모든 노드가 신호를 받는 데 걸리는 시간 (= 가장 오래 걸리는 노드까지의 최단 시간) 0> 다익스트라 알고리즘으로 추출 가능
# 2) 모든 노드에 도달할 수 있는지 여부 -> 모든 노드에 다익스트라 알고리즘 계산 값이 존재하는 가 유무로 판별 가능
# 우선 순위 큐를 최소 힙(Min Heap)으로 구현한 모듈이 heapq 모듈 사용
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Q: [(소요 시간, 정점)]
        Q = [(0, K)]
        # dist: 해당 정점과, 출발 지점 K에서부터 해당 정점까지 걸리는 시간 쌍으로 구성된 힙
        dist = collections.defaultdict(int)
        
        # 우선순위 큐의 '최솟값'을 기준으로 정점까지의 최단 경로를 삽입
        while Q:
            time, node = heapq.heappop(Q)
            # 만약, 이미 dist에 해당 node key 값이 존재한다면 그 값은 버리기
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    
        # 모든 노드가 최단 경로가 존재하는지 여부를 판별
        if len(dist) == N:
            return max(dist.values())
        
        return -1
