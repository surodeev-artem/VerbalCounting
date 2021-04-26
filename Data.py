class Data:
    correctButton = 0
    maxScores = 100
    scores = 100
    tasks = []
    time = 30

    def __init__(self):
        self.timeReset()

    def timeReset(self):
        self.time = 30
