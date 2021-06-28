# 48번 균형 이진 트리

# 풀이 1: 재귀 구조로 높이 차이 계산

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 높이 균형: 모든 노드의 subtrees 간에 높이 차가 '1 이하'인 트리, 트리가 높이 균형인지 아닌지 판단
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            # root일 경우 -1을 부여 -> 트리의 level을 판단하기 위함
            # root가 아닐 경우 0부터 시작!
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            # 높이 차이가 나는 경우 -1, 나지 않으면 높이 1 증가
            if left == -1 or right == -1 or abs(left+right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != = -1 
