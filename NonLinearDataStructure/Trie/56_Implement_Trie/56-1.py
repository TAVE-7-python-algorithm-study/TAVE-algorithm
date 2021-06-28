import collections
# 56번 트라이 구현

# 풀이 1. 딕셔너리를 이용해 간결한 트라이 구현

# 트라이의 노드 정의
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
        # 단어 삽입 메소드
        def insert(self, word: str) -> None:
            node = self.root
            for char in word:
                node = node.children[char]
            node.word = True # 마지막 철자에 도달하면 (단어의 끝 철자에 도달하면) True로 변환
            
        # 단어의 존재 여부를 판별하는 메소드
        def search(self, word: str) -> bool:
            # word의 초기 상태: True
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.word
        
        # 해당 문자열로 시작하는 단어가 존재하는지 여부를 판별
        def startsWith(self, prefix: str) -> bool:
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True
