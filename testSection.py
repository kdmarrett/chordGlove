import Section
# import learnSection

class testSection(Section):

    def __init__(self):
        Section.__init__(self)
        correctChord = learnSection.finalLetterDict[letters[letterIndex]]

    def tic(self):
        currentHardware()
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]
        self.correctList = HardwareInterface.chordToList(self.correctChord)
        if letterIndex > len(letters):
            sectionComplete = True
        if not sectionComplete:
            if not letterComplete:
                self.letterComplete = onlineFeedback()
            else:
                learnSection.finalLetterDict[currentLetter] = currentChord
                self.letterComplete = False
                letterIndex += 1
                ValidInput = ValidInput()  # recreate instance
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        drawText(self.currentLetter)  # writes letter text to background buffer
        drawFingerCircles(self.currentList)
        # update baseline in ValidInput
        ValidInput.setBaseline(self.correctChord)
        return ValidInput.tic()

