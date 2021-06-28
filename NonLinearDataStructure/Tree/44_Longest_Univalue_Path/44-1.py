# 44번 가장 긴 동일 값의 경로

# 풀이 1: 상태 값 거리 계산 DFS

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 리프 노드까지 DFS로 탐색해 내려간 다음, 동일한 값이 나올 경우 거리를 누적하며 백트래킹하기
class Solution:
    result: int = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            # 리프 노드까지 dfs 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드의 값이 부모 노드의 값과 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            # 결과: 왼쪽, 오른쪽 노드 거리의 합이 최대일 때
            self.result = max(self.result, left+right)
            # 왼쪽/오른쪽 자식 노드의 상태 값 중 큰 값을 리턴하여 상태값 업데이트
            return max(left, right)
        
        dfs(root)
        return self.result
