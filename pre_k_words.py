import heapq


class Solution:
    def topKFrequent(self, words, k: int):
        mapping = {}
        for word in words:
            if word not in mapping:
                mapping[word] = 0
            mapping[word] += 1
        # 生成一个哈希表，保存每个词及其出现的频数
        print(mapping)
        # 生成最小堆
        heap = []
        for key, value in mapping.items():
            # 将元素添加到最小堆中
            heapq.heappush(heap, Node(key, value))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while len(heap) > 0:
            temp = heapq.heappop(heap)
            print(temp.key, "", temp.value)
            result.append(temp.key)

        # 翻转最小堆结果
        result.reverse()
        return result


# 创建一个包含key和value的node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, nxt):
        return self.key > nxt.key if self.value == nxt.value else self.value < nxt.value

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
s = Solution()
s.topKFrequent(words, k)