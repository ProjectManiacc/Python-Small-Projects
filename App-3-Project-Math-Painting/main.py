from figures import Square, Rectangle
from canvas import Canvas
import webcolors

canvas = Canvas()
canvas.width = int(input("Provide a width for a canvas: "))
canvas.height = int(input("Provide a height for a canvas: "))
user_canvas_color = ""
while user_canvas_color == "":
    user_canvas_color = input("Provide a color for a canvas (black or white): ")

    if user_canvas_color == "white":
        canvas.color = [255, 255, 255]
    elif user_canvas_color == "black":
        canvas.color = [0, 0, 0]
    else:
        print("Please choose black or white")

canvas.create_matrix()

game_on = True

while game_on:
    figure = input("What would you like to draw? (circle,square,rectangle): ")

    if figure == "square":

        square = Square()
        square.x = int(input("Provide x coordinate: "))
        square.y = int(input("Provide y coordinate: "))
        square.side = int(input("Provide a side length: "))

        color_as_word = input("Provide square color: ")
        color_triplet = webcolors.name_to_rgb(color_as_word)
        square.color = [color_triplet.red, color_triplet.green, color_triplet.blue]
        square.draw(canvas)

    elif figure == "rectangle":
        rectangle = Rectangle()
        rectangle.x = int(input("Provide x coordinate: "))
        rectangle.y = int(input("Provide y coordinate: "))
        rectangle.width = int(input("Provide a width length: "))
        rectangle.height = int(input("Provide a height length: "))

        color_as_word = input("Provide square color: ")
        color_triplet = webcolors.name_to_rgb(color_as_word)

        rectangle.color = [color_triplet.red, color_triplet.green, color_triplet.blue]
        rectangle.draw(canvas)
    else:
        print("Please choose correct figure")

    drawing_choice = input("Type 'quit' if you would like to quit ")
    if drawing_choice.lower() == 'quit':
        game_on = False

canvas.make("canvas.png")
