class MyHashSet:

    def __init__(self):
        self.hashset = [0] * 10000001

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        self.hashset[key] = 0

    def contains(self, key: int) -> bool:
        return self.hashset[key]

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key = 2
obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)