import turtle
from prime import isprime


WIDTH, HEIGHT = 500, 500
WHITE = '#ffffff'
BLACK = '#111111'

LINE = False
SIZE = 5


def init(line=False, size=5):
    '''
    Initialize turtle window.

    Parameters
    ----------
    line : bool
        Add spiral line.
    size : int
        Size of the spiral/circles.
    '''

    global LINE, SIZE
    LINE = line

    SIZE = size
    if size < 1:
        SIZE = 1
    elif size >= 30:
        SIZE = 30


def mainloop():
    if not LINE:
        cursor.penup()
    else:
        cursor.pendown()

    number = 1
    steps = 1
    steps_taken = 0
    direction_changes = 0

    running = True
    while running:
        screen.update()

        if paused:
            continue

        if steps * SIZE >= WIDTH and cursor.heading() == 90:
            _pause()

        cursor.forward(SIZE)
        steps_taken += 1

        number += 1
        if isprime(number):
            cursor.dot(SIZE, WHITE)

        if steps / steps_taken == 1:
            cursor.left(90)
            steps_taken = 0
            direction_changes += 1

            if direction_changes == 2:
                direction_changes = 0
                steps += 1


def _pause():
    global paused
    paused = True if not paused else False


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Ulam Spiral')
screen.bgcolor(BLACK)
screen.tracer(0, 0)

screen.listen()
screen.onkeypress(screen.bye, 'q')
screen.onkeypress(_pause, 'p')

cursor = turtle.Turtle()
cursor.color(WHITE)
cursor.hideturtle()
cursor.speed(3)

paused = False


if __name__ == '__main__':
    try: mainloop()
    except Exception: pass
