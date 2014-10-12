import Section
import FileOutput

class learnSection(Section.Section):
    def __init__(self):
        Section.__init__(self)  # extend Section init
        self.finalLetterDict = {}
        # change baselineInput to pastChord

    def tic(self):
        currentHardware()
        if letterIndex > len(letters):
            sectionComplete = True
        if not sectionComplete:
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
                    drawText("Please choose a unique finger combination")
        else: 
            letters = self.finalLetterDict.keys()
            FileOutput.writeFile(self.finalLetterDict, DictFilesPath)
        self.pastChord = self.currentChord

    def onlineFeedback(self):
        drawText(self.currentLetter)  # writes letter text to background buffer
        drawFingerCircles(self.currentList)
        ValidInput.setBaseline(self.pastChord)  # update baseline in ValidInput
        return ValidInput.tic()

    def isUniqueChord(self, chord):
        return chord in self.finalLetterDict.values()

