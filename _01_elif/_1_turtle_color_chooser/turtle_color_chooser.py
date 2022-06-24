import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    bob = turtle.Turtle()

    c = simpledialog.askstring(title='...', prompt='what color do you want to use')
    if c == 'blue':
        bob.pencolor('blue')
    elif c == 'red':
        bob.pencolor('red')
    elif c == 'green':
        bob.pencolor('green')
    elif c == 'yellow':
        bob.pencolor('yellow')
    elif c == 'cyan':
        bob.pencolor('cyan')
    elif c == 'pink':
        bob.pencolor('pink')
    elif c == 'magenta':
        bob.pencolor('magenta')
    elif c == 'black':
        bob.pencolor('black')
    elif c == 'white':
        bob.pencolor('white')
    else:
        bob.pencolor(get_random_color())
        for i in range(4):
            bob.width(10)
            bob.forward(100)
            bob.right(90)

    #     TODO 2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
