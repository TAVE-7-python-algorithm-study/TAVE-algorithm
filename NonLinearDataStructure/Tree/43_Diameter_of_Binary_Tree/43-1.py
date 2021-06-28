# 43번 이진 트리의 직경

# 풀이 1: 상태값 누적 트리 BFS

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 가장 긴 경로를 찾는 방법: 리프 노드까지 탐색한 다음, 부모로 거슬러 올라가며
#                         각각의 거리를 계산해 상태값을 업데이트, 누적하기
class Solution:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            # External nodes do not store items - place holder 생성, -1 값 부여
            if not node:
                return -1
            
            # 재귀 호출을 통해 왼쪽, 오른쪽의 각 리프 노드까지 DFS로 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로 탐색
            # 왼쪽/오른쪽 자식 노드의 리프 노드에서 현재 노드까지의 거리 + 2
            self.longest = mex(self.longest, left+right+2)
            
            # 현재 상태값를 반환하여 업데이트
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
    
