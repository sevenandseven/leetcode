class Circle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(self, x, y):
        self.x = x
        self.y = y

c = Circle(10, 20)   # init
print(c.x, c.y)
c(100, 200)          # 调用instance()触发__call__
print(c.x, c.y)

