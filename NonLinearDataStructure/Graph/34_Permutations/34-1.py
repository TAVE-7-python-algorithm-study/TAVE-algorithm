from typing import List
# 34번 순열

# 풀이 1: DFS를 활용한 순열 생성
# 순열: 모든 가능한 경우를 그래프 형태로 나열한 결과
# 팩토리얼, 순열의 계산 방식은 순열의 상태 전달을 그래프로 언결하였을 때, 레벨에 따른 자식 노드의 수와 동일함

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드에 도달하였을 경우, 조합 결과를 추가
            # 그래프에서 자식 노드의 수가 0인 경우를 생각하면 됨
            if len(elements) == 0:
                # prev_element의 참조가 아닌, 결과 값을 추가해야 하므로 prev_element가 아닌 prev_element[:]를 append해야 함
                # prev_element에 조합 결과를 누적하여 추가
                results.append(prev_element[:])
                
            # 재귀 호출하여 순열을 계속 생성
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                next_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
                
        def(nums)
        return prev_elements
