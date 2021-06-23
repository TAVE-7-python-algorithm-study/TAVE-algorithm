# 35번 순열

# 풀이 1: DFS로 k개의 조합 생성
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            # elements: 자기 자신뿐 아니라 앞의 모든 요소를 배제한 요소들의 조합
            
            # k가 0이 되면 결과에 append
            if k == 0:
                results.append(elements[:])
                return
            
            # for문을 이용한 재귀 호출
            # 재귀호출 시 parameter로 넘겨주는 값은, 자신 이전의 모든 값을 그대로 넘겨줌
            # 이렇게 하면 k가 0이 될 때까지 남아 있는 값끼리 나머지 조합을 수행하게 됨
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([], 1, k)
        return results
