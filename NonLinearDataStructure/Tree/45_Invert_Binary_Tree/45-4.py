import collections
# 45번 이진 트리 반전

# 풀이 4: 반복 구조로 DFS 후위 순회

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# DFS 풀이를 위해 stack을 정의
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
        
            if node:
                stack.append(node.left)
                stack.append(node.right)
                
                # 후위 순회
                node.left, node.right = node.right, node.left
        
        return root
