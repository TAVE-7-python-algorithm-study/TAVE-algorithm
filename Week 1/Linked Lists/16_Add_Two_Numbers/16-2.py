# 8장 연결 리스트 - 16번 두 수의 덧셈 (난이도 2)

# 풀이 2.전가산기 구현
# 각 자리 수를 추출해 더하기 위해 자료형을 변환해야 했던 풀이1과 달리,
# 전가산기와 유사한 연산을 통해 간편하게 두 수의 합을 구할 수 있음!!

# 연결 리스트의 노드를 생성하는 클래스 (단일 연결 리스트 정의)
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


# 두 개의 값을 더해서, 가산 결과가 두 자릿수가 될 경우, 
# 몫은 자리 올림수로 설정해 다음번 연산에 사용하고, 나머지를 값으로 사용
# 이 값을 연결 리스트로 변환
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)
    carry = 0     # 이전 연산의 자리 올림 수

    while l1 or l2 or carry:
        sum = 0

        # 두 입력값의 합을 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
    
        # 몫(자리 올림수)과 나머지(값) 계산
        # divmod(a//b, a%b): 몫과 나머지로 구성된 튜플을 반환 -> 십진 연산이므로 a%b = 10!
        carry, val = divmod(sum+carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next
