class MyList(object):
    def __init__(self, values=None):
        self.values = values or []
    def __setitem__(self, key, value):
        # 添加元素
        self.values[key] = value
    def __getitem__(self, key):
        # 获取元素
        return self.values[key]
    def __delitem__(self, key):
        # 删除元素
        del self.values[key]
    def __len__(self):
        # 自定义的list元素的个数
        return len(self.values)
    def __iter__(self):
        # 可迭代
        return self
    def __next__(self):
        # 迭代具体细节
        # 如果__iter__返回self则必须实现此方法
        if self._index >= len(self.values):
            raise StopIteration
        value = self.values[self._index]
        self._index += 1
        return value
    def __contains__(self, key):
        # 元素是否在自定义list中
        return key in self.values
    def __reversed__(self):
        # 反转
        return list(reversed(self.values))


# 初始化list
my_list = MyList([1, 2, 3, 4])
print(my_list[0])                                 # getitem
my_list[1] = 20                                   # setitem
print(1 in my_list)                              # contains
print(len(my_list))                               # len
print(i for i in my_list)                         # iter
del my_list[0]                                    # del
reversed_list = reversed(my_list)                 # reversed
print(i for i in reversed_list)                   # iter



