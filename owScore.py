from tkinter import Label
import os
class OwScore:
    def __init__(self):
        self.direction = os.path.expanduser(r'~\Documents')

        f = open(self.direction, "r+")
        fileString = f.read()
        if fileString == '':
            self.wins = 0
            self.looses = 0
            self.draws = 0
            f.write(f'W:{self.wins}  L:{self.looses}  D:{self.draws}')
        else:
            fileIndividualLetter = fileString.split("  ", 2)
            stringArray = list()
            for onePart in fileIndividualLetter:
                tempStringWithNumber = onePart.split(":")
                stringArray.append(tempStringWithNumber)

            self.wins = int(stringArray[0][1])
            self.looses = int(stringArray[1][1])
            self.draws = int(stringArray[2][1])
        f.close()

    def update_file(self):
        f = open(self.direction, "r+")
        stringToFile = 'W:{wins}  L:{looses}  D:{draws}'.format(wins=self.wins, looses=self.looses, draws = self.draws)
        f.truncate(0)
        f.write(stringToFile)
        f.close()

    def update_string(self):
        testString = 'Wins: {wins}\nLooses: {looses}\nDraws: {draws}'.format(wins=self.wins, looses=self.looses, draws = self.draws)
        self.update_file()
        return testString

    def update_label(self, lbl:Label):
        testString = self.update_string()
        lbl.configure(text=testString)

    def get_test_string(self):
        return 'Wins: {wins}\nLooses: {looses}\nDraws: {draws}'.format(wins=self.wins, looses=self.looses, draws = self.draws)

    def winsPlus(self, lbl:Label):
        self.wins += 1
        self.update_label(lbl)

    def winsLess(self, lbl:Label):
        self.wins = 0 if self.wins == 0 else self.wins - 1
        self.update_label(lbl)

    def loosesPlus(self, lbl:Label):
        self.looses += 1
        self.update_label(lbl)

    def loosesLess(self, lbl:Label):
        self.looses = 0 if self.looses == 0 else self.looses - 1
        self.update_label(lbl)

    def drawPlus(self, lbl:Label):
        self.draws += 1
        self.update_label(lbl)

    def drawLess(self, lbl:Label):
        self.draws = 0 if self.draws == 0 else self.draws - 1
        self.update_label(lbl)

    def reset(self, lbl:Label):
        self.wins = 0
        self.looses = 0
        self.draws = 0
        self.update_label(lbl)