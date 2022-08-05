class Square:
    def __init__(self, x=0, y=0, side=0, color=0):
        self.side = side
        self.color = color
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0, color=0):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.width, self.y: self.y + self.height] = self.color
