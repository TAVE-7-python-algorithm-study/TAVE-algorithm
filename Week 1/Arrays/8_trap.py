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


# 풀이2. 스택 쌓기
def trap(height: List[int]) -> int:
    stack = []
    volume = 0

    # 막대 기둥 높이만큼 스택에 쌓아 나가다가, 
    # 막대 기둥 간에 높이 차가 발생하면, 스택에 저장해둔 높이를 하나씩 꺼내서
    # 이전 막대 기둥과의 높이 차이만큼 volume에 더해주기
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]: # 변곡점을 만나는 경우
            top = stack.pop()                          # 스택에서 저장해둔 높이를 꺼낸다

            if not len(stack):
                break

        distance = i - stack[-1] - 1                  # 이전 막대 기둥과의 차이만큼 물 높이 처리하기
        waters = min(height[i], height[stack[-1]]) - height[top]
        volume += distance * waters
    stack.append(i)
    return volume


def main():
    ls = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(ls))
