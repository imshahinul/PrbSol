class WordTree:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordTreeEx:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return WordTree()

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            if key[level] not in pCrawl.children:
                pCrawl.children[key[level]] = self.getNode()
            pCrawl = pCrawl.children[key[level]]
        pCrawl.isEndOfWord = True

    def rm(self, wtn, key):
        if key[0] in wtn.children:
            if len(key) == 1:
                wtn.children[key[0]].isEndOfWord = False
                if len(wtn.children[key[0]].children) == 0:
                    del wtn.children[key[0]]
            else:
                wtn.children[key[0]] = self.rm(wtn.children[key[0]], key[1:])
                if len(wtn.children[key[0]].children) == 0 and wtn.children[key[0]].isEndOfWord == False:
                    del wtn.children[key[0]]
        return wtn

    def remove(self, key):
        pCrawl = self.root
        self.root = self.rm(pCrawl, key)

    def printx(self, wtn, le=0):
        for k in wtn.children:
            if wtn.children[k].isEndOfWord:
                print(k.upper(), end="")
            else:
                print(k, end="")
            self.printx(wtn.children[k], le + 1)
        if len(wtn.children):
            print()
            print(" " * (le - 1), end="")


class Solution:
    def dfs(self, word, i, j, path, board, wtn, le=0):
        if word[-1] not in wtn.children:
            return []
        out = []

        if wtn.children[word[-1]].isEndOfWord:
            out.append(word)
            self.t.remove(word)

        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            next_cell = (i + d[0], j + d[1])
            if 0 <= next_cell[0] < m and 0 <= next_cell[1] < n:
                if word[-1] in wtn.children and board[next_cell[0]][next_cell[1]] in wtn.children[
                    word[-1]].children and next_cell not in path:  # valid cell:
                    next_word = word + board[next_cell[0]][next_cell[1]]  # make

                    path.add(next_cell)
                    out += self.dfs(next_word, next_cell[0], next_cell[1], path, board, wtn.children[word[-1]], le + 1)
                    path.remove(next_cell)
        return out

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.t = WordTreeEx()

        # Construct trie
        for key in words:
            self.t.insert(key)

        m = len(board)
        n = len(board[0])
        out = []
        for i in range(m):
            for j in range(n):
                out += (
                    self.dfs(board[i][j], i, j, set([(i, j)]), board,
                             self.t.root, le=0))
        return set(out)