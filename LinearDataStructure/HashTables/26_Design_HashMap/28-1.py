# 개별체이닝 방식을 이용한 해시 테이블 구현
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode) # 존재하지 않는 키를 조회할 경우, 자동으로 디폴트를 생성

    # key, value를 해시맵에 삽입, 이미 존재하는 key인 경우 체이닝(연결 리스트)으로 업데이트
    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return 

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # key에 해당하는 value를 조회, 만약 key가 존재하지 않는다면 -1 반환
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 경우, 일치하는 key를 탐색
        p = self.table[index] 
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # key에 해당하는 key, value를 해시맵에서 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫번째 노드일 때 삭제 처리 (연결 리스트가 없는 유일한 값일 경우)
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트에서의 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
