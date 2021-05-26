# 풀이 1: 슬라이딩 윈도우와 투 포인터로 사이즈 조절
class Solution:
    def lengthOfLonestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for index, char in enumerate(s):
            # 중복되는 문자일 경우 start pointer 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 비교를 통한 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index-start+1)

            # 현재 문자의 위치 갱신
            used[char] = index

        return max_length
