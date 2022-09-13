class Area:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def rec(self):
        result = self.width * self.height
        return result
    def tri(self):
        result = self.width*self.height*(1/2)
        return result
    def circle(self):
        result = self.width * self.width * 3.14
        return result

area = Area(10,20)
print(area.rec())
print(area.tri())
print(area.circle())