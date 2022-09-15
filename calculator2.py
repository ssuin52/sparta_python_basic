class FourCal():
    def set_number(self, first, second):
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
        try:
            return self.first / self.second
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
while True:
    try:
        first, second = map(int, input().split())
        break
    except ValueError:
        print("숫자를 입력하세요")

cal = FourCal()
cal.set_number(first, second)
print(cal.add())
print(cal.minus())
print(cal.mul())
print(cal.div())




