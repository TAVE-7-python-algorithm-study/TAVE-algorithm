# 7장 배열 - 8번 빗물 트래핑 (난이도 3)
from typing import List

# 풀이1. 투 포인터를 최대로 이동시키기
def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0 # 채울 수 있는 물의 높이
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right: # 좌우 기둥 최대 높이 찾기
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 가장 높은 쪽을 향해 투 포인터를 이동시키며, 물 높이 volume을 더해가기
        if left_max <= right_max:
            volume += left_max - height[left] # 최대 기둥 높이와 현재 기둥 높이의 차만큼 더하기
            left += 1 # 왼쪽에서 오른쪽으로 1칸 전진
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
    
def main():
    ls = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(ls))
