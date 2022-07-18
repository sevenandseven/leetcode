class Solution:
    def longestWord(self, words):
        if words is None or len(words) == 0:
            return
            # 每一步都有终止符，证明每一步在字典中都有相对应的字符串
        # b没有终止符，所以它不是字典中存在的单词
        # # 字典树的开头
        root = Trie()
        for word in words:
            cur = root
            # 判断该字母是否在单词中
            for c in word:
                if c in cur.children:
                    cur = cur.children[c]
                else:
                    newNode = Trie()
                    cur.children[c] = newNode
                    cur = newNode
            cur.val = word
            cur.isEnd = True

        result = ''
        for word in words:
            cur = root
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                isWord = True
                for c in word:
                    cur = cur.children[c]
                    if not cur.isEnd:
                        isWord = False
                        break
                result = word if isWord else result
        return result


class Trie():
    def __init__(self):
        # 孩子节点一般用hashmap做，有一个结束标志isEnd
        # 并且要将该字符写出来存入到val中
        self.children = {}
        self.isEnd = False
        self.val = ""
s = Solution()

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

s.longestWord(words)
