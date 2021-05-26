# 풀이 1: 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0

        # S의 빈도수 계산
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                frequs[char] += 1

        # J의 빈도수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]
        return count
