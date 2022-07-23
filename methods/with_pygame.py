import sys
import os
from prime import isprime

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
import pygame


WIDTH, HEIGHT = 500, 500
FPS = 120
BLACK = '#111111'
WHITE = '#ffffff'

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
    if size < 2:
        SIZE = 2
    elif size >= 30:
        SIZE = 30


def mainloop():
    screen.fill(BLACK)
    clock = pygame.time.Clock()

    while 1:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('p'):
                    _pause()
                if event.key == ord('q'):
                    sys.exit()

        if not paused:
            _update()


def _pause():
    global paused
    paused = True if not paused else False


def _update():
    global number, steps, steps_taken, direction_changes, dir_index
    global x, y

    direction = directions[dir_index]
    match direction:
        case 'up' if steps * SIZE >= WIDTH - SIZE:
            return

        case 'right':
            next_x, next_y = x + SIZE, y
        case 'up':
            next_x, next_y = x, y - SIZE
        case 'left':
            next_x, next_y = x - SIZE, y
        case 'down':
            next_x, next_y = x, y + SIZE

    if LINE:
        pygame.draw.line(screen, WHITE, (x, y), (next_x, next_y))
    x, y = next_x, next_y
    steps_taken += 1

    if steps_taken == steps:
        dir_index = dir_index + 1 if dir_index < 3 else 0

        steps_taken = 0
        direction_changes += 1

        if direction_changes == 2:
            steps += 1
            direction_changes = 0

    number += 1
    if isprime(number):
        pygame.draw.circle(screen, WHITE, (x, y), SIZE//2)

    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ulam Spiral')

x, y = WIDTH//2, HEIGHT//2

number = 1
steps = 1
steps_taken = 0
direction_changes = 0
directions = ['right', 'up', 'left', 'down']
dir_index = 0

paused = False


if __name__ == '__main__':
    mainloop()
