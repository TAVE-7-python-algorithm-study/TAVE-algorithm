import collections
# 45번 이진 트리 반전

# 풀이 2: 반복 구조로 BFS

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# BFS 풀이를 위해 queue를 정의
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            # 부모 노드부터 시작해 내려가며 swap 진행
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
            
        return root
