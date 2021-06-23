import collections
from typing import List

# 39번 코스 스케줄

# 풀이 1: DFS로 순환 구조 판별
# 입력값으로 주어진 n개의 코스들이 순환구조가 '아니어야'함

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # x와 y의 관계 -> y를 끝내기 위해서는 x를 끝내야 함
        for x, y in prerequisites:
            graph[x].append(y)
            
        # 방문한 노드를 traced 변수에 저장, 중복 방문할 경우 순환 구조로 간주
        # traced는 중복 값을 갖지 않으므로 집합 자료형인 set()로 선언
        traced = set()
        
        def dfs(i):
            # 순환구조일 경우 return False
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y): # 순환 구조일 경우
                    return False
            # 해당 노드를 이용한 모든 탐색이 종료된 이후에는 방문 내역을 삭제하기
            traced.remove(i)
            
            return True
        
        # 순환구조 판별하기
        for x in list(graph):
            if not dfs(x):
                return False
        return True
