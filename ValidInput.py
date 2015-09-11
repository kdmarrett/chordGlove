# from SectionControl import Section
# import SectionControl
import Section, testSection, trainSection, learnSection

class ValidInput():

    def __init__(self):
        self.stableInput = False
        self.totalStabilityTime = 0
        self.currentChord = 0
        self.currentList = []
        self.timeNoChange = 0
        self.baselineInput = 0  # sets to null

    def tic(self):
        Section.Section.currentHardware()
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

