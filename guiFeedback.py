# chordGlove
# guiFeedback

import pyglet
import time  # time.sleep(60)
from pyglet.gl import *
from math import pi, sin, cos
import resources
import serial
from FileOutput import FileOutput
from HardwareInterface import HardwareInterface
# from ValidInput import *
import ValidInput
import Section, testSection, trainSection, learnSection

# CLASS CONSTANTS
# SAMPLE_RATE = 9600
TIME_SAMPLE = .01
GLOBAL_TIME = 0
FINGERS = 5
LOCK_TIME = 30  # in seconds
letterIndex = 0
window = pyglet.window.Window()
x_center = window.width / 2
y_center = window.height / 2
# x_center = window.width // 2
# y_center = window.height // 2
defaultLetterDict = {'A': 8, 'B':16, 'C':24, 'D':12, 'E':14, 'F':5, 'G':1, 'H':27, 
    'I':4, 'J':20, 'K':28, 'L':29, 'M':10, 'N':11, 'O':2, 'P':13, 'Q':23, 'R':18, 
    'S':30, 'T':6, 'U':9, 'V':3, 'W':15, 'X':26, 'Y':7, 'Z':21, 
    '.':17, ',':22, '?':19, ' ':31, "Delete":25}
letters = defaultLetterDict.keys()

subject = 'Karl'
DictFilesPath = '/home/kdmarrett/git/chordGlove/DictFiles'
skipTraining = 1
# PathToSubject ?

# MAIN
learnSection = learnSection()
if skipTraining:
    learnSection.finalLetterDict = defaultLetterDict
trainSection = trainSection()
testSection = testSection()
HardwareInterface = HardwareInterface()
# initiate batch needs to be global
sectionBackground = pyglet.graphics.Batch()
# args of dt must be defined here
pyglet.clock.schedule_interval(update, TIME_SAMPLE)

def update(dt):
    if not skipTraining:
        testSection.tic()
    trainSection.tic()
    testSection.tic()
    GLOBAL_TIME = GLOBAL_TIME + dt

@window.event
def on_draw():
    global sectionBackground
    global circleList
    window.clear()
    sectionBackground.draw()
    for i in range(FINGERS):
        circleList[i].draw()

pyglet.app.run()
