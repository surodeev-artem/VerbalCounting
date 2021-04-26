import Data
import random
import json
from Task import Task


class Logic:
    def __init__(self):
        self.data = Data.Data()

    def createTasks(self):
        self.data.tasks.clear()
        correctBtn = random.randint(0, 4)
        self.data.correctButton = correctBtn
        for i in range(5):
            self._createTask(i == correctBtn)

    def _createTask(self, isTrue):
        sign = random.randint(0, 3)
        if sign == 0 or sign == 1:
            maxNum = 100
        elif sign == 2:
            maxNum = 20
        else:
            maxNum = 50

        if sign != 3:
            firstNum = random.randint(1, maxNum)
            secondNum = random.randint(1, maxNum)
        else:
            secondNum = random.randint(1, maxNum)
            firstNum = secondNum * random.randint(1, 20)

        if isTrue:
            if sign == 0:
                answer = firstNum + secondNum
            elif sign == 1:
                answer = firstNum - secondNum
            elif sign == 2:
                answer = firstNum * secondNum
            else:
                answer = int(firstNum / secondNum)
        else:
            answer = random.randint(1, 300)
        task = Task(firstNum, sign, secondNum, answer)
        self.data.tasks.append(task)

    def getTasks(self):
        return self.data.tasks

    def btnClicked(self, btnId):
        self.resetTimer()
        if btnId == self.data.correctButton:
            self.data.scores += 20
            if self.data.scores > self.data.maxScores:
                self.changeMaxScores()
            return True
        else:
            self.data.scores -= 30
            return False

    def getScores(self):
        return self.data.scores

    def getMaxScoresFromFile(self):
        try:
            f = open("max.json", "r")
            self.data.maxScores = json.load(f)["max_scores"]
            print(json)
        except FileNotFoundError:
            f = open("max.json", "w")
            json.dump({"max_scores": 100}, f)
            f.close()
            self.data.maxScores = 100
            print(json)

    def getMaxScores(self):
        return self.data.maxScores

    def changeMaxScores(self):
        score = self.data.scores
        f = open("max.json", "w")
        json.dump({"max_scores": score}, f)
        f.close()
        self.data.maxScores = score

    def timeChange(self):
        self.data.time -= 1
        return self.getTime()

    def getTime(self):
        return self.data.time

    def timeIsUp(self):
        self.data.scores -= 20
        self.resetTimer()

    def resetTimer(self):
        self.data.timeReset()
