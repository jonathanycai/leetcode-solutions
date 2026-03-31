class Node:
    def __init__(self):
        self.endWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.start = Node()

    def addWord(self, word: str) -> None:
        curr = self.start

        for s in word:
            if s not in curr.children:
                curr.children[s] = Node()
            curr = curr.children[s]
        
        curr.endWord = True
    
    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                curr = curr.children[c]
            return curr.endWord
            
        return dfs(0, self.start)

