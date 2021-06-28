# 51번 이진 탐색 트리(BST)를 더 큰 수 합계 트리로

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 풀이 1: 중위 순회로 노드 값 누적        
class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회를 통해 노드 값을 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root
