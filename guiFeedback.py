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
import pdb

# CLASS CONSTANTS
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
defaultLetterDict = {'A': 8, 'B':16, 'C':24, 'D':12, 'E':14, 'F':5, 'G':1, 'H':27, 
    'I':4, 'J':20, 'K':28, 'L':29, 'M':10, 'N':11, 'O':2, 'P':13, 'Q':23, 'R':18, 
    'S':30, 'T':6, 'U':9, 'V':3, 'W':15, 'X':26, 'Y':7, 'Z':21, 
    '.':17, ',':22, '?':19, 'Spaces':31, "Delete":25}
letters = defaultLetterDict.keys()
sectionBackground = pyglet.graphics.Batch()
circleList = [ pyglet.sprite.Sprite(resources.whiteCircle, batch = sectionBackground) for i in range(FINGERS)]

HardwareInterface = HardwareInterface()
subject = 'Karl'
DictFilesPath = '/home/kdmarrett/git/chordGlove/DictFiles'
skipTraining = False
GLOBAL_TIME = 0
# text = 'hello'
# PathToSubject ?

def drawText(text, size):
    global sectionBackground
    # global label
    # print text + 'space'
    label = pyglet.text.Label(text, font_name='Times New Roman', font_size=size,
                              x=window.width / 2, y=window.height / 2, anchor_x='center', anchor_y='center', batch=sectionBackground)

# def drawFingerCircles(currentList):
#     global FINGERS
#     global sectionBackground
#     global circleList
#     circularSteps = pi / (FINGERS - 1)
#     arcRadiusX = int(round(min(window.width, window.height) / 2))
#     arcRadiusY = int(round( window.height / 4))
#     # print "new circle"
#     # circle = pyglet.sprite.Sprite(img = resources.whiteCircle, x = 50, y = 50, batch = sectionBackground)
#     for i in range(FINGERS):
#         phi = pi - circularSteps * i
#         x = x_center + arcRadiusX * cos(phi)
#         y = y_center + arcRadiusY * sin(phi)
#         if currentList[i] == 0:  # if off color is white
#             color = (255, 255, 255)
#         else:  # else turn red
#             color = (255, 0, 0)
#         # circleList[i] = pyglet.sprite.Sprite(resources.whiteCircle, x, y, batch = sectionBackground)
#         circleList[i].scale = .17
#         circleList[i].color = color
#         circleList[i].position = (x, y)
#         # print "x=" + str(x)+ "y=" + str(y)
#         # print "x_center" + str(x_center) 
#         # print "y_center"+ str(y_center)
#         # circle = pyglet.sprite.Sprite(resources.whiteCircle, x, y, color)
#     #     # add to batch
#     #     # circle.draw()

def drawFingerCircles(currentList):
    global sectionBackground
    global circleList
    # circleList = [pyglet.sprite.Sprite(resources.whiteCircle, batch=sectionBackground) for i in range(FINGERS)]
    circularSteps = pi / (FINGERS - 1)
    arcRadiusX = int(round(min(window.width, window.height) / 2))
    arcRadiusY = int(round(window.height / 4))
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
    # add to batch
    # circle.draw()

class Section:
    global DictFilesPath
    global subject
    global sectionBackground
    global letters
    global HardwareInterface
    global FINGERS

    def __init__(self):
        self.pastChord = 0
        self.ValidInput = ValidInput()
        self.letterComplete = False
        self.sectionComplete = False
        self.letterIndex = 0
        self.currentLetter = letters[self.letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)
        # global currentChord
        # global currentList
        # self.ValidInput.currentChord = HardwareInterface.getChord()
        # sel.ValidInput.currentList = HardwareInterface.chordToList(currentChord)

    def drawText(self, text):
        global sectionBackground
        label = pyglet.text.Label(text, font_name='Times New Roman', font_size=36,
                                  x=window.width / 2, y=window.height / 2, anchor_x='center', anchor_y='center', batch=sectionBackground)


class learnSection(Section):
    global subject
    global sectionBackground
    global letters
    global HardwareInterface
    global FINGERS
    def __init__(self):
        # Section.__init__(self)  # extend Section init
        self.finalLetterDict = {}
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        # change baselineInput to pastChord
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        self.ValidInput = ValidInput()
        self.currentLetter = letters[self.letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []
        self.pastChord = 0

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)

    def tic(self):
        global letters
        self.currentHardware()
        self.ValidInput.setBaseline(self.pastChord)
        if self.letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not self.letterComplete:
                self.letterComplete = self.onlineFeedback()
            else:
                if self.isUniqueChord(self.currentChord):
                    self.finalLetterDict[currentLetter] = self.currentChord
                    self.letterComplete = False
                    self.letterIndex += 1
                    self.ValidInput = ValidInput()  # recreate instance
                else:
                    self.letterComplete = False
                    # drawText("Please choose a unique finger combination", 20)
        else: 
            letters = self.finalLetterDict.keys()
            FileOutput.writeFile(self.finalLetterDict, DictFilesPath)
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        # Section.drawText(Section, self.currentLetter)  # writes letter text to background buffer
        print self.currentLetter
        drawText(self.currentLetter, 36)  # writes letter text to background buffer
        drawFingerCircles(self.currentList)
        self.ValidInput.setBaseline(self.pastChord)  # update baseline in ValidInput
        HardwareInterface.setChord(self.currentChord)
        return self.ValidInput.tic()

    def isUniqueChord(self, chord):
        return chord in self.finalLetterDict.values()

class trainSection(Section):
    global subject
    global sectionBackground
    global letters
    global HardwareInterface
    global FINGERS
    def __init__(self):
        # Section.__init__()
        if len(learnSection.finalLetterDict) == 0:
            self.finalLetterDict = defaultLetterDict
        else:
            self.finalLetterDict = learnSection.finalLetterDict
        self.letterIndex = 0
        self.correctChord = self.finalLetterDict[letters[self.letterIndex]]  #check this for bugs
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        self.sectionComplete = False
        self.letterComplete = False
        self.ValidInput = ValidInput()
        self.currentLetter = letters[self.letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)

    def tic(self):
        self.currentHardware()
        self.correctChord = self.finalLetterDict[letters[self.letterIndex]]  #check this for bugs
        if self.letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not self.letterComplete:
                self.letterComplete = self.onlineFeedback()
            else:
                self.finalLetterDict[currentLetter] = self.currentChord
                self.letterComplete = False
                self.letterIndex += 1
                self.ValidInput = ValidInput()  # recreate instance
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        Section.drawText(self.currentLetter)  # writes letter text to background buffer
        # Section.drawFingerCircles(self.currentList)
        # update baseline in ValidInput
        self.ValidInput.setBaseline(self.correctChord)
        return self.ValidInput.tic()


class testSection(Section):
    global subject
    global sectionBackground
    global letters
    global HardwareInterface
    global FINGERS

    def __init__(self):
        # Section.__init__()
        if len(learnSection.finalLetterDict) == 0:
            self.finalLetterDict = defaultLetterDict
        else:
            self.finalLetterDict = learnSection.finalLetterDict
        self.letterIndex = 0
        correctChord = self.finalLetterDict[letters[self.letterIndex]]
        self.sectionComplete = False
        self.letterComplete = False
        self.correctChord = self.finalLetterDict[letters[self.letterIndex]]  #check this for bugs
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        self.ValidInput = ValidInput()
        self.currentLetter = letters[self.letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)

    def tic(self):
        self.currentHardware()
        self.correctChord = self.finalLetterDict[letters[self.letterIndex]]
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        if self.letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not self.letterComplete:
                self.letterComplete = self.onlineFeedback()
            else:
                self.finalLetterDict[currentLetter] = self.currentChord
                self.letterComplete = False
                self.letterIndex += 1
                self.ValidInput = ValidInput()  # recreate instance
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        Section.drawText(self.currentLetter)  # writes letter text to background buffer
        # Section.drawFingerCircles(Section, self.currentList)
        # update baseline in ValidInput
        self.ValidInput.setBaseline(self.correctChord)
        return self.ValidInput.tic()

class ValidInput:
    global subject
    global sectionBackground
    global letters
    global HardwareInterface
    global FINGERS
    global TIME_SAMPLE
    global LOCK_TIME

    def __init__(self):
        self.stableInput = False
        self.totalStabilityTime = 0
        self.currentChord = 0
        self.currentList = []
        self.timeNoChange = 0
        self.baselineInput = 0  # sets to null

    def tic(self):
        Section.currentHardware()
        if self.currentChord == self.baselineInput:
            if self.timeNoChange > LOCK_TIME:
                self.stableInput = True
            else:
                self.timeNoChange += TIME_SAMPLE
        else:
            timeNoChange = 0
        return self.stableInput

    def setBaseline(self, chord):
        self.baselineInput = chord


# MAIN
Section = Section()
learnSection = learnSection()
if skipTraining:
    learnSection.finalLetterDict = defaultLetterDict
trainSection = trainSection()
testSection = testSection()
# label = pyglet.text.Label(text, font_name='Times New Roman', font_size=36,
                          # x=window.width / 2, y=window.height / 2, anchor_x='center', anchor_y='center', batch=sectionBackground)
# initiate batch needs to be global
# args of dt must be defined here

def update(dt):
    global GLOBAL_TIME
    # if not skipTraining:
    #     testSection.tic()
    learnSection.tic()
    trainSection.tic()
    testSection.tic()
    GLOBAL_TIME = GLOBAL_TIME + dt

@window.event
def on_draw():
    # global sectionBackground
    # # global label
    # global circleList
    # window.clear()
    # sectionBackground.draw()
    # # label.draw()
    # # for i in range(FINGERS):
    # #     circleList[i].draw()
    # window.clear()
    # sectionBackground.draw()
    # for i in range(FINGERS):
    #     circleList[i].draw()
    global sectionBackground
    global circleList
    window.clear()
    sectionBackground.draw()
    for i in range(FINGERS):
        circleList[i].draw()

pyglet.clock.schedule_interval(update, TIME_SAMPLE)
pyglet.app.run()
