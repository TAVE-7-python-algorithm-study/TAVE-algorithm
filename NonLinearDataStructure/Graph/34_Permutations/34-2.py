# 34번 순열
# 풀이 2: itertools 모듈 사용

# itertools 모듈은 반복자 생성에 최적화된 효율적인 기능들을 제공함
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))
