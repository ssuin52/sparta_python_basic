class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
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

try:
    cal = FourCal(4, 0)
    print(cal.add())
    print(cal.minus())
    print(cal.mul())
    print(cal.div())
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자가 아닙니다.")




