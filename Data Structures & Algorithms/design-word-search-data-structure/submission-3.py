class Node:

    def __init__(self):
        self.endWord = False
        self.neighbours = {}

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.neighbours:
                curr.neighbours[c] = Node()
            curr = curr.neighbours[c]
        
        curr.endWord = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            curr = node

            for j in range(i, len(word)):
                
                if word[j] == '.':
                    for n in curr.neighbours.values():
                        if dfs(j + 1, n):
                            return True
                    return False
                else:
                    if word[j] not in curr.neighbours:
                        return False
                curr = curr.neighbours[word[j]]
            return curr.endWord
        
        return dfs(0, self.head)
                    







