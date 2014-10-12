import Section
# import learnSection

class trainSection(Section):
    def __init__(self):
        Section.__init__(self)
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]  #check this for bugs
        self.correctList = HardwareInterface.chordToList(self.correctChord)

    def tic(self):
        currentHardware()
        self.correctChord = learnSection.finalLetterDict[letters[letterIndex]]  #check this for bugs
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


