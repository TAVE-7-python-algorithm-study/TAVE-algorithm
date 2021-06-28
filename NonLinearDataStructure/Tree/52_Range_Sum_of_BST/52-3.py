# 52번 이진 탐색 트리(BST) 합의 범위

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 풀이 3. 반복 구조 DFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택을 이용하여 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum
