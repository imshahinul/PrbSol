class WordTree():
    def __init__(self):
        self.children = collections.defaultdict(WordTree)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = WordTree()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        out = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", out)
        return out

    def dfs(self, board, node, i, j, path, out):
        if node.isWord:
            out.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        ch = board[i][j]
        node = node.children.get(ch)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + ch, out)
        self.dfs(board, node, i - 1, j, path + ch, out)
        self.dfs(board, node, i, j - 1, path + ch, out)
        self.dfs(board, node, i, j + 1, path + ch, out)
        board[i][j] = ch