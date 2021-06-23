from typing import List
# 37번 부분 집합

# 풀이 1: 트리의 모든 DFS 결과

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            # 탐색 결과 path를 추가하고, 현재 탐색 위치인 index를 1씩 늘려 나가기
            # 별도의 종료 조건 없이 탐색이 종료될 경우 재귀 호출 종료
            # 부분 집합은 모든 탐색 경로가 결과이므로, 매 반복마다 결과를 추가
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        
        dfs(0, [])
        return result
