# 7장 배열 - 8번 빗물 트래핑 (난이도 3)
from typing import List

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
