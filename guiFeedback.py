# chordGlove
# guiFeedback

import pyglet
import time  # time.sleep(60)
from pyglet.gl import *
from math import pi, sin, cos
# import HardwareInterface

# SAMPLE_RATE = 9600
TIME_SAMPLE = .01
FINGERS = 5
LOCK_TIME = 2  # in seconds
window = pyglet.window.Window()

letters = ('Space', 'Pause', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z', '.', 'Backspace')


def drawText(text):
    label = pyglet.text.Label(text, font_name='Times New Roman', font_size=36,
                              x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
    label.draw()


@window.event
def on_draw():
    window.clear()

def drawFingerCircles():
    radius = 30
    # for
    circle(100, 100, radius).draw()

def circle(x, y, radius):
    """
    We want a pixel perfect circle.
    """
    iterations = int(2 * radius * pi)
    s = sin(2 * pi / iterations)
    c = cos(2 * pi / iterations)

    dx, dy = radius, 0

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations + 1 - 10):
        glVertex2f(x + dx, y + dy)
        dx, dy = (dx * c - dy * s), (dy * c + dx * s)
    glEnd()

def learnChords():
    ''' First section that learns and saves user input for each letter'''
    letterBins = dict()
    for letter in letters:
        drawText(letter)
        lockLetter(letter)

def lockLetter(letter):
    global currentChord
    global pastChord
    global timeNoChange
    locked = False
    while not locked:
        currentChord = 31 # hack for developing before HI completion
        # currentChord = HardwareInterface.getChord()
        # currentList = HardwareInterface.chordToList(currentChord)
        # draw the state of the fingers
        # HardwareInterface.setChord(currentChord)  # Stimulate currently active
        pastChord = currentChord
        if timeNoChange >= LOCK_TIME:
            locked = True

    # set the current letter to the chord int
    letterBins[letter] = currentChord

def update(dt):
    global currentChord
    global pastChord
    global timeNoChange
    if currentChord == pastChord:
        timeNoChange += dt
    else:
        timeNoChange = 0

# main
currentChord, pastChord, timeNoChange = 0, 0, 0.0 # hack initialize to 0
pyglet.clock.schedule_interval(update, TIME_SAMPLE) # args of dt must be defined here
pyglet.app.run()
learnChords()
drawFingerCircles()
# finger = pyglet.sprite.Sprite(resources.player, x=400, y=0)

