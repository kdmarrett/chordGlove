# chordGlove
# guiFeedback

import pyglet
import time  # time.sleep(60)
from pyglet.gl import *
from math import pi, sin, cos
import resources
from HardwareInterface import HardwareInterface


# make method for checking stable input

# SAMPLE_RATE = 9600
TIME_SAMPLE = .01
GLOBAL_TIME = 0
FINGERS = 5
LOCK_TIME = 3  # in seconds
letterIndex = 0
window = pyglet.window.Window()
x_center = window.width / 2
y_center = window.height / 2
# x_center = window.width // 2
# y_center = window.height // 2

letters = ('Space', 'Pause', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z', '.', 'Backspace')

def drawText(text):
    global sectionBackground
    label = pyglet.text.Label(text, font_name='Times New Roman', font_size=36,
                              x=window.width / 2, y=window.height / 2, anchor_x='center', anchor_y='center', batch = sectionBackground)

@window.event
def on_draw():
    global sectionBackground
    global circleList
    window.clear()
    sectionBackground.draw()
    for i in range(FINGERS):
        circleList[i].draw()

def drawFingerCircles(currentList):
    global FINGERS
    global sectionBackground
    global circleList
    circularSteps = pi / (FINGERS - 1)
    arcRadiusX = int(round(min(window.width, window.height) / 2))
    arcRadiusY = int(round( window.height / 4))
    # print "new circle"
    # circle = pyglet.sprite.Sprite(img = resources.whiteCircle, x = 50, y = 50, batch = sectionBackground)
    for i in range(FINGERS):
        phi = pi - circularSteps * i
        x = x_center + arcRadiusX * cos(phi)
        y = y_center + arcRadiusY * sin(phi)
        if currentList[i] == 0:  # if off color is white
            color = (255, 255, 255)
        else:  # else turn red
            color = (255, 0, 0)
        # circleList[i] = pyglet.sprite.Sprite(resources.whiteCircle, x, y, batch = sectionBackground)
        circleList[i].scale = .17
        circleList[i].color = color
        circleList[i].position = (x, y)
        # print "x=" + str(x)+ "y=" + str(y)
        # print "x_center" + str(x_center) 
        # print "y_center"+ str(y_center)
        # circle = pyglet.sprite.Sprite(resources.whiteCircle, x, y, color)
    #     # add to batch
    #     # circle.draw()

def sectionMain():
    ''' First section that learns and saves user input for each letter'''
    global letters
    global letterDict
    global letterIndex
    complete = False
    if letterIndex < len(letters):
        if not completeSection1:
            lockLetter(letters[letterIndex])
        else:
            checkCorrect()
    else:
        complete = True
    return complete

def checkCorrect(letter):
    global correctChord
    global correctList
    global currentChord
    global currentList
    correctChord = letterDict[letter]
    correctList = HardwareInterface.chordToList(correctChord)
    currentHardware()

def lockLetter(letter):
    global currentChord
    global pastChord
    global timeNoChange
    global sectionBackground
    global letterIndex
    global stableInput
    if stableInput:
        # set the current letter to the chord int
        letterDict[letter] = currentChord
        letterIndex += 1
        stableInput = False
        timeNoChange = 0
        sectionBackground = pyglet.graphics.Batch()  # initiate batch
    else:
        currentHardware()
        drawText(letter)
        drawFingerCircles(currentList)
        # sectionBackground.draw()
        # draw the state of the fingers
        HardwareInterface.setChord(currentChord)  # Stimulate currently active
        # drawText(timeNoChange)  for debugging

def currentHardware():
    global currentChord
    global currentList
    currentChord = HardwareInterface.getChord()
    currentList = HardwareInterface.chordToList(currentChord)

def update(dt):
    global currentChord
    global pastChord
    global timeNoChange
    global time
    global GLOBAL_TIME
    global completeSection1
    global stableInput
    if not completeSection1:
        completeSection1 = sectionMain()
        if currentChord == pastChord:
            timeNoChange = timeNoChange + dt
            # print timeNoChange
        else:
            timeNoChange = 0
        if timeNoChange >= LOCK_TIME:
            stableInput = True
            # print stableInput
        pastChord = currentChord
    elif not completeSection2:
        completeSection2 = sectionMain()
        if currentChord == correctChord:
            timeNoChange = timeNoChange + dt
            # print timeNoChange
        else:
            timeNoChange = 0
        if timeNoChange >= LOCK_TIME:
            stableInput = True
            # print stableInput
        pastChord = currentChord
    elif not completeSection3:
        completeSection3 = sectionMain()
        if currentChord == correctChord:
            timeNoChange = timeNoChange + dt
            # print timeNoChange
        else:
            timeNoChange = 0
        if timeNoChange >= LOCK_TIME:
            stableInput = True
            # print stableInput
        pastChord = currentChord
    else:
        pass # end current program
    GLOBAL_TIME = GLOBAL_TIME + dt

# main
completeSection1 = False
completeSection2 = False
completeSection3 = False
sectionBackground = pyglet.graphics.Batch()  # initiate batch
currentChord, pastChord, timeNoChange = 0, 0, 0.0 # hack initialize to 0
stableInput = False
pyglet.clock.schedule_interval(update, TIME_SAMPLE) # args of dt must be defined here
HardwareInterface = HardwareInterface()
letterDict= dict()
# circle = pyglet.sprite.Sprite(img = resources.whiteCircle, x = 50, y = 50, batch = sectionBackground)
# circle.visible = False
circleList = [ pyglet.sprite.Sprite(resources.whiteCircle, batch = sectionBackground) for i in range(FINGERS)]
pyglet.app.run()