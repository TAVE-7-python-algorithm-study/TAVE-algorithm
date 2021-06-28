import collections
from typing import List

# 49번 최소 높이 트리

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# 풀이 1: 단계별 리프 노드 제거
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 삽입으로 그래프 구성
        # 무방향 그래프이므로 트리의 부모/자식은 양쪽 노드 번갈아 삽입해도 가능함
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 리프 노드: 그래프에서 해당 키 값이 1개뿐인 노드
        # 리프 노드 목록 추출
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # root 노드만 남을 때까지 반복해서 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
              # 리프 노드, 이와 이웃한 노드 제거
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
