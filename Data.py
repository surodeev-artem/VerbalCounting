class Data:
    correctButton = 0
    maxScores = 100
    scores = 100
    tasks = []

    def getTask(self, taskId):
        return self.tasks[taskId]

    def setTask(self, taskId, task):
        self.tasks[taskId] = task
