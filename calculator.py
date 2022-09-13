class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

cal = FourCal(4, 2)


print(cal.add())
print(cal.minus())
print(cal.mul())
print(cal.div())

