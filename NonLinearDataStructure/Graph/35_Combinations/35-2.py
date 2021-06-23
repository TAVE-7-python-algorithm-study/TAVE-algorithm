# 35번 순열

# 풀이 2: itertools 모듈 사용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
