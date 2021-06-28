from typing import List

# 57번 팰린드롬 페어

# 풀이 2. 트라이 구현

# 트라이 선언
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
        
# 트라이 구현
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        # 팰린드롬 여부를 판단하는 메소드
        def is_palindrome(word):
            return word[::] == word[::-1]
        
        # 단어 삽입 메소드
        def insert(self, index, word) -> None:
            node = self.root
            # 팰린드롬을 판단해야 하므로 뒤집어서 삽입하기
            for i, char in enumerate(reversed(word)):
                if self.is_palindrome(word[0:len(word)-i]):
                    node.palindrome_word_ids.append(index)
                node = node.children[char]
            node.word_id = index # 각각의 단어가 끝나는 지점에 index 값 부여
                
            
        # 판별 로직에 따라 결과를 출력하는 메소드
        def search(self, index, word) -> List[List[int]]:
            result = []
            node = self.root
            
            while word:
                # 판별 로직 3: 탐색 중간에 word_id가 있고, 나머지 문자가 팰린드롬인 경우
                if node.word_id >= 0:
                    if self.is_palindrome(word):
                        result.append([index, node.word_id])
                if not word[0] in node.children:
                    return result
                node = node.children[word[0]]
                word = word[1:]
                
            # 판별 로직 1: 끝까지 탐색했을 때 word_id가 있는 경우
            if node.word_id >= 0 and node.word_id != index:
                result.append([index, node.word_id])
                
            # 판별 로직 2: 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
            for palindrome_word_id in node.palindrome_word_ids:
                result.append([index, palindrome_word_id])
                    
            return result
        
        
# 팰린드롬 페어들을 모아 반환하는 클래스
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        
        for i, word in enumerate(words): # 단어들 삽입
            trie.insert(i, word)
            
        results = []
        
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
            
        return results
        
        # time complexity: O(n)
