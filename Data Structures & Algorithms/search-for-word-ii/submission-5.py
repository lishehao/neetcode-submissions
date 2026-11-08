
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board[0])
        m = len(board)

        root = {}

        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]

            node["#"] = word

        output = []

        def dfs(node, x, y):
            if not (0 <= x < n and 0 <= y < m):
                return

            char = board[y][x]

            if char == "#" or char not in node:
                return

            # 移动到当前字符对应的 Trie 节点
            nextNode = node[char]

            # 如果这里是单词结尾，记录并去重
            if "#" in nextNode:
                output.append(nextNode.pop("#"))

            # 标记当前格子已经使用
            board[y][x] = "#"

            dfs(nextNode, x-1, y)
            dfs(nextNode, x+1, y)
            dfs(nextNode, x, y-1)
            dfs(nextNode, x, y+1)

            board[y][x] = char

        for x in range(n):
            for y in range(m):
                dfs(root, x, y)

        return output
