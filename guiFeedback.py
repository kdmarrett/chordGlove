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

HardwareInterface = HardwareInterface()
subject = 'Karl'
DictFilesPath = '/home/kdmarrett/git/chordGlove/DictFiles'
skipTraining = 0
# PathToSubject ?

class Section:
    global subject
    global sectionBackground
    global letters
    global DictFilesPath
    global HardwareInterface
    global FINGERS

    def __init__(self):
        self.pastChord = 0
        self.ValidInput = ValidInput()
        self.letterComplete = False
        self.sectionComplete = False
        self.letterIndex = 0
        self.currentLetter = letters[letterIndex]  # always space
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

    # def drawFingerCircles(self, currentList):
    #     global sectionBackground
    #     circleList = [pyglet.sprite.Sprite(resources.whiteCircle, batch=sectionBackground) for i in range(FINGERS)]
    #     circularSteps = pi / (FINGERS - 1)
    #     arcRadiusX = int(round(min(window.width, window.height) / 2))
    #     arcRadiusY = int(round(window.height / 4))
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
    #     # add to batch
    #     # circle.draw()

class trainSection(Section):
    def __init__(self):
        # Section.__init__()
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]  #check this for bugs
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        self.ValidInput = ValidInput()
        self.currentLetter = letters[letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)

    def tic(self):
        self.currentHardware()
        self.correctChord = learnSection.finalLetterDict[letters[self.letterIndex]]  #check this for bugs
        if self.letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not self.letterComplete:
                self.letterComplete = self.onlineFeedback()
            else:
                learnSection.finalLetterDict[currentLetter] = currentChord
                self.letterComplete = False
                letterIndex += 1
                ValidInput = ValidInput()  # recreate instance
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        Section.drawText(self.currentLetter)  # writes letter text to background buffer
        # Section.drawFingerCircles(self.currentList)
        # update baseline in ValidInput
        ValidInput.setBaseline(self.correctChord)
        return ValidInput.tic()

class learnSection(Section):
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
        self.currentLetter = letters[letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        sel.currentList = HardwareInterface.chordToList(currentChord)

    def tic(self):
        self.currentHardware()
        if letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not letterComplete:
                self.letterComplete = onlineFeedback()
            else:
                if isUniqueChord(self.currentChord):
                    self.finalLetterDict[currentLetter] = currentChord
                    self.letterComplete = False
                    letterIndex += 1
                    ValidInput = ValidInput()  # recreate instance
                else:
                    self.letterComplete = False
                    Section.drawText("Please choose a unique finger combination")
        else: 
            letters = self.finalLetterDict.keys()
            FileOutput.writeFile(self.finalLetterDict, DictFilesPath)
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        Section.drawText(Section, self.currentLetter)  # writes letter text to background buffer
        # Section.drawFingerCircles(Section, self.currentList)
        ValidInput.setBaseline(self.pastChord)  # update baseline in ValidInput
        return ValidInput.tic()

    def isUniqueChord(self, chord):
        return chord in self.finalLetterDict.values()


class testSection(Section):

    def __init__(self):
        # Section.__init__()
        correctChord = learnSection.finalLetterDict[letters[letterIndex]]
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]  #check this for bugs
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        self.letterIndex = 0
        self.sectionComplete = False
        self.letterComplete = False
        self.ValidInput = ValidInput()
        self.currentLetter = letters[letterIndex]  # always space
        self.currentChord = 0
        self.currentList = []

    def currentHardware(self):
        self.currentChord = HardwareInterface.getChord()
        self.currentList = HardwareInterface.chordToList(self.currentChord)

    def tic(self):
        self.currentHardware()
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        if letterIndex > len(letters):
            self.sectionComplete = True
        if not self.sectionComplete:
            if not letterComplete:
                self.letterComplete = onlineFeedback()
            else:
                learnSection.finalLetterDict[currentLetter] = currentChord
                self.letterComplete = False
                letterIndex += 1
                ValidInput = ValidInput()  # recreate instance
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        Section.drawText(Section, self.currentLetter)  # writes letter text to background buffer
        # Section.drawFingerCircles(Section, self.currentList)
        # update baseline in ValidInput
        ValidInput.setBaseline(self.correctChord)
        return ValidInput.tic()

class ValidInput():

    def __init__(self):
        self.stableInput = False
        self.totalStabilityTime = 0
        self.currentChord = 0
        self.currentList = []
        self.timeNoChange = 0
        self.baselineInput = 0  # sets to null

    def tic(self):
        Section.currentHardware()
        if currentChord == baselineinput:
            if timeNoChange > LOCK_TIME:
                stableInput = True
            else:
                timeNoChange += TIME_SAMPLE
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
# initiate batch needs to be global
sectionBackground = pyglet.graphics.Batch()
# args of dt must be defined here

def update(dt):
    if not skipTraining:
        testSection.tic()
    trainSection.tic()
    testSection.tic()
    GLOBAL_TIME = GLOBAL_TIME + dt

@window.event
def on_draw():
    global sectionBackground
    window.clear()
    sectionBackground.draw()
    # for i in range(FINGERS):
    #     circleList[i].draw()

pyglet.clock.schedule_interval(update, TIME_SAMPLE)
pyglet.app.run()
