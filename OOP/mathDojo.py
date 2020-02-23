class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for y in nums:
            self.result += y
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for y in nums:
            self.result -= y
        return self

mj = MathDojo()
y = mj.add(2).add(2, 5, 1).add(4, 2, 5, 7, 8).subtract(3).subtract(4,2,15).subtract(10,4,5,11).result
print(y)

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)