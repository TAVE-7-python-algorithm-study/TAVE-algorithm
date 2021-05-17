# 9장 스택, 큐 - 24번 스택을 이용한 큐 구현 (난이도 1)

# 풀이1. 스택 2개 사용
# pop()의 경우, stack의 맨 뒤 item(가장 최근에 push된 요소)을 꺼내야 함
# 다음 수행에서도 또 다시 맨 뒤의 item을 꺼내게 되고, 이는 무한반복 문제로 이어짐
# 따라서, 스택의 연산만으로 큐를 구현하기 위해서는 2개의 스택이 필요함

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def peek(self):
        # output이 없을 경우, 모두 재입력하기
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    # pop()과 peek()는 같은 요소를 반환하기 때문에, peek()를 호출하고 여기에 반환값을 재입력함
    def pop(self):
        self.peek()
        return self.output.pop()

    def empty(self):
        return self.input == [] and self.output == []
