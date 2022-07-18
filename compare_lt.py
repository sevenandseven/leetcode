class Person(object):
    def __init__(self, uid, name, salary):
        self.uid = uid
        self.name = name
        self.salary = salary

    # 比较函数
    def __cmp__(self, other):
        if self.uid == other.uid:
            return 0
        if self.uid > other.uid:
            return 1
        else:
            return -1

    def __eq__(self, other):
        # 对象==判断
        return self.uid == other.uid

    def __ne__(self, other):
        # 对象!= 判断
        return self.uid != other.uid

    def __lt__(self, other):
        # 对象
        return len(self.name)

    def __gt__(self, other):
        # 对象>判断，根据salary
        return self.salary > other.salary

p1 = Person(1, 'zhkfae', 1000)
p2 = Person(1, 'zhkfae', 1000)
p3 = Person(1, 'eaiejre', 3000)

print(p1 == p2)

