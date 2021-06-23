from typing import List
# 36번 조합의 합 옵션 문제

# 순열의 합 탐색

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 숫자 집합 candidates의 요소의 순열 결과 중 target과 값이 같도록 만드는 숫자 집합들을 반환
        result = []
        
        def dfs(csum, index, path):
            # csum: 합을 갱신해 나가는 parameter, path: 현재까지의 탐색 경로
            # 종료 조건 1: csum<0, 목표 값을 초과한 경우
            # 종료 조건 2: csum=0, 목표 값과 일치하는 경우, 결과 리스트에 추가한 후 탐색 종료
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            # '맨처음'부터 자신의 하위 원소까지 나열한 결과(path+[candidates[i]])를 재귀 호출
            # csum에 candidates[i]를 빼서 합을 갱신
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], 0, path+[candidates[i]])
        
        dfs(target, 0, [])
        return result
