# 8장 연결 리스트 - 16번 두 수의 덧셈 (난이도 2)
from typing import List

# 풀이 1. 자료형 변환
# 연결 리스트를 문자열 리스트로 이어 붙인 다음, 숫자로 변환하여 계산한 후, 연결 리스트로 바꾸기

# 연결 리스트를 생성하는 클래스
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트를 연결 리스트로 변환 - 출력 결과가 역순이므로 연결 리스트를 역순으로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1)) # 연결 리스트를 역순의 리스트로 변환
        b = self.toList(self.reverseList(l2))

        # ''.join(list): list의 요소를 문자열로 합쳐 반환하는 함수
        # 리스트의 각 요소를 숫자로 변환해 계산하기
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        # 최종 계산 결과를 연결 리스트로 변환
        return self.toReversedLinkedList(str(resultStr))
