# 9장 스택, 큐 - 유효한 괄호 (난이도 1)

# 풀이1. 스택 일치 여부 판별
def isValid(self, s: str) -> bool:
    stack = []
    # 알맞은 괄호를 짝지은 매핑 테이블 생성
    # 스택에서 pop()한 결과가 매핑 대상이므로, 반대의 순서로 매핑해야 함
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }

    # 예외 처리 및 일치 여부 판별 
    for char in s:
        if char not in table:
            stack.append(char)
            
        # 예외 처리
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0 # 만약 유효한 괄호였다면 stack의 모든 요소가 pop()됐을것이므로, True 반환
