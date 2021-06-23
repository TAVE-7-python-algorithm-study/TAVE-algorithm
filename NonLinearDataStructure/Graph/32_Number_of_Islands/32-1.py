from typing import List
# 32번 섬의 개수

# 풀이 1. DFS로 그래프 탐색
# 동서남북이 모두 연결된 그래프로 가정하고, 네 방향 각각에 DFS 재귀를 이용해 탐색을 마치면 1을 증가시키는 형태로 육지의 개수 파악 가능
class Solution:
    # 해당 위치에서 탐색할 수 있는 모든 육지를 dfs로 탐색하였으므로 카운트 +1
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs 재귀를 이용한 탐색
        def dfs(i, j):
            # 종료 조건: 육지가 아닌 경우
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return

            # 이미 방문한 곳은 1이 아닌 값으로 마킹
            grid[i][j] = '0'

            # 동서남북 탐색
            # 중첩 함수를 이용한 재귀 호출
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
