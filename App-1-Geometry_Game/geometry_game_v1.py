import turtle
from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self,canvas ):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1 .y)
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.right(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.right(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.right(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.right(90)



class GuiPoint(Point):
    def draw(self,canvas,size=5,color='black'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)

# Create rectangle object
gui_rectangle = GuiRectangle(Point(randint(0, 300), randint(0, 300)),
                             Point(randint(10, 300), randint(10, 300)))



# Print rectangle coordinates
print("Rectangle Coordinates: ",
      gui_rectangle.point1.x, ",",
      gui_rectangle.point1.y, "and",
      gui_rectangle.point2.x, ",",
      gui_rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(gui_rectangle))
print("Your area was off by: ", gui_rectangle.area() - user_area)

my_turtle = turtle.Turtle()

gui_rectangle.draw(my_turtle)
user_point.draw(my_turtle)
turtle.done()  # The Canvas stays after compiling