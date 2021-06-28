import sys
# 53번 이진 탐색 트리(BST) 노드 간 최소 거리

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 풀이 1. 재귀 구조로 중위 순회
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
