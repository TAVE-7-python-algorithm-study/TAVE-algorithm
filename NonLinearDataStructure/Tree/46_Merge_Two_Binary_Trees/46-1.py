import collections
# 46번 두 이진 트리 병합

# 풀이 1: 재귀 탐색

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # root부터 시작해서 None이 return될 때까지 내려가며,
        # 각 트리의 왼쪽/오른쪽 자식 노드를 재귀 호출을 통해 병합한다.
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2
