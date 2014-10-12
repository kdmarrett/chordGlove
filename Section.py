# from ValidInput import ValidInput
import ValidInput
from HardwareInterface import HardwareInterface

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
        sel.currentList = HardwareInterface.chordToList(currentChord)
        # global currentChord
        # global currentList
        # self.ValidInput.currentChord = HardwareInterface.getChord()
        # sel.ValidInput.currentList = HardwareInterface.chordToList(currentChord)

    def drawText(self, text):
        global sectionBackground
        label = pyglet.text.Label(text, font_name='Times New Roman', font_size=36,
                                  x=window.width / 2, y=window.height / 2, anchor_x='center', anchor_y='center', batch=sectionBackground)

    def drawFingerCircles(self, currentList):
        global sectionBackground
        circleList = [pyglet.sprite.Sprite(resources.whiteCircle, batch=sectionBackground) for i in range(FINGERS)]
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



