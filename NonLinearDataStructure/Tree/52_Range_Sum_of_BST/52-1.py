# 52번 이진 탐색 트리(BST) 합의 범위

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 풀이 1. 재귀 구조 DFS로 브루트 포스 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
               self.rangeSumBST(root.left, L, R) + \
               self.rangeSumBST(root.right, L, R)
