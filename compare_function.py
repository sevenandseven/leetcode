class Person(object):
    def __init__(self, uid):
        self.uid = uid

    # 比较函数
    def __cmp__(self, other):
        if self.uid == other.uid:
            return True
        if self.uid > other.uid:
            return 1
        else:
            return -1


p1 = Person(1)
p2 = Person(1)
print(p1 == p2)
