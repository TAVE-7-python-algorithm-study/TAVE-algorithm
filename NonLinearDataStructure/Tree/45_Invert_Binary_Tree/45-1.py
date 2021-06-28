# 45번 이진 트리 반전

# 풀이 1: 파이썬다운 방식

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 재귀를 통해 왼쪽 자식 노드와 오른쪽 자식 노드를 swap
        if root:
            root.left, root.right = self.invertTree(root.right), self.inverTree(root.left)
            return root
        return None
