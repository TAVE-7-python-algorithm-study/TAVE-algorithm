import collections
# 42번 이진 트리의 최대 깊이

# 풀이 1: 반복 구조로 BFS 풀이

# 이진 트리 노드를 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS 풀이는 '큐'를 이용해 풀이하므로, 큐를 선언
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 데크 자료형을 이용하면 이중 연결리스트로 구성되므로 큐/스택 연산을 자유롭게 활용 가능
        # 양방향 모두 O(1)에 추출 가능
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            # 큐 연산을 이용해 추출한 노드를 임의의 루트 노드로 지정하여,
            # 이 노드의 자식 노드를 재귀 반복 구조로 큐에 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # depth == BFS 반복 횟수
        return depth
      
# input: [3, 9, 20, null, null, 15, 7]
# depth 1: queue에 [3]
# depth 2: queue에 [9, 20]
# depth 3: queue에 [15,7]이 삽입되어 처리됨
