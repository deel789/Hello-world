import numpy as np

a = np.array(2)
b = np.arange(1,20,0.5)

print(a)
print(type(a))
print(type(b[0]))
for k, v in enumerate(b):
    print(k, v)


'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：778463939
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(3, 4)
v2 = Vector(5, 6)
M = v1 + v2
print(M)
