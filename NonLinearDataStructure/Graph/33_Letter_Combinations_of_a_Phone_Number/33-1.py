# 33번 전화 번호 문자 조합

# 풀이 1: 모든 조합 탐색
# 가능한 경우의 수를 모두 조합하는 형태로 전체를 탐색한 후, 백트래킹하면서 결과를 조합
class Solution:
    def letterCombinations(selfself, digits: str) -> List[str]:
        # digits: 입력값
        # 자릿수가 동일할 때까지 재귀 호출을 반복하다, 끝까지 탐색하면 결과를 추가하고 리턴
        # 모든 경우의 수를 DFS로 탐색하고, 백트래킹으로 결과를 조합하며 리턴
        def dfs(index, path):
            # index: 현재 탐색 위치, path: 가능한 조합 case
            # 끝까지 탐색하면 '백 트래킹'!
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값의 자릿수만큼 반복
            for i in range(index, len(digits)):
                # 입력값 숫자에 해당하는 모든 문자열을 차례로 반복해서 탐색
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)

        # 예외 처리
        if not digits:
            return []

        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wyxz"}
        result = []
        dfs(0, "")

        return result
