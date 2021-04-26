from tkinter import *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

import Timer
from Task import *


class UI:
    def __init__(self, logic):
        self._buttonsText = []
        self._buttons = []
        self._root = Tk()
        self.logic = logic
        self.scores = StringVar()
        self.scores.set("Текущий счет: " + str(self.logic.getScores()))
        self._score = Label(textvariable=self.scores, font=("Arial", 25), bg="#FFFEF0").grid(row=0, column=1, pady=20)
        self.maxScores = StringVar()
        self.maxScores.set("Максимальный счет: " + str(self.logic.getMaxScores()))
        self._maxScore = Label(textvariable=self.maxScores, font=("Arial", 15), bg="#FFFEF0").grid(row=0, column=2, pady=20)

    def initComponents(self):
        self.createButtons()
        self.setTasks()
        self.renderWindow()
=======


class UI:
    buttons = []
>>>>>>> parent of a19504e (Version 1.0)

    root = None
    score = None
    task = None

    def createRoot(self):
        self.root = Tk()

=======


class UI:
    buttons = []

    root = None
    score = None
    task = None

    def createRoot(self):
        self.root = Tk()

>>>>>>> parent of a19504e (Version 1.0)
=======


class UI:
    buttons = []

    root = None
    score = None
    task = None

    def createRoot(self):
        self.root = Tk()

>>>>>>> parent of a19504e (Version 1.0)
    def createLabels(self):
        self.score = Label(text="Очки: 666").grid(row=0, column=2, pady=20)
        self.task = Label(text="123123").grid(row=0, column=1, pady=20)

    def createButtons(self):
        buttonCoords = [[1, 0], [1, 2], [2, 1], [3, 0], [3, 2]]

        btnPadX = 10
        btnPadY = 5
        btnWidth = 15
        btnHeight = 5

        for i in buttonCoords:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            btn = Button(textvariable=self._buttonsText[len(self._buttons)], width=btnWidth, height=btnHeight,
                         bg="#746096", fg="#FFFEF0",
                         font=("Arial", 15), activebackground="#CCBFE3",
                         command=lambda btnId=len(self._buttons):self.isCorrectAnswer(btnId))
            btn.grid(row=i[0], column=i[1], padx=btnPadX, pady=btnPadY)
            self._buttons.append(btn)

    def isCorrectAnswer(self, btnId):
        self.logic.btnClicked(btnId)
        self.scores.set("Текущий счет: " + str(self.logic.getScores()))
        self.maxScores.set("Максимальный счет: " + str(self.logic.getMaxScores()))
        self.setTasks()

    def setTasks(self):
        self.logic.createTasks()
        tasks = self.logic.getTasks()

        for i in range(len(self._buttonsText)):
            sign = tasks[i].sign
            if sign == 0:
                handledSign = "+"
            elif sign == 1:
                handledSign = "-"
            elif sign == 2:
                handledSign = "*"
            else:
                handledSign = "/"
            task = str(tasks[i].firstNum) + " " + handledSign + " " + str(tasks[i].secondNum) + " = " + str(tasks[i].answer)
            self._buttonsText[i].set(task)
=======
            self.buttons.append(Button(text="1", width=btnWidth, height=btnHeight)
                                .grid(row=i[0], column=i[1], padx=btnPadX, pady=btnPadY))
>>>>>>> parent of a19504e (Version 1.0)

    def onClosing(self):
        Timer.Timer.appIsOpen = False
        self._root.destroy()

    def renderWindow(self):
<<<<<<< HEAD
        self._root.config(bg="#FFFEF0")
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(2, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(3, weight=1)
        self._root.geometry("800x600")
        self._root.title("Счет в уме")
        self._root.resizable(False, False)
        self._root.protocol("WM_DELETE_WINDOW", lambda: self.onClosing())
        self._root.mainloop()
=======
=======
            self.buttons.append(Button(text="1", width=btnWidth, height=btnHeight)
                                .grid(row=i[0], column=i[1], padx=btnPadX, pady=btnPadY))

    def renderWindow(self):
>>>>>>> parent of a19504e (Version 1.0)
=======
            self.buttons.append(Button(text="1", width=btnWidth, height=btnHeight)
                                .grid(row=i[0], column=i[1], padx=btnPadX, pady=btnPadY))

    def renderWindow(self):
>>>>>>> parent of a19504e (Version 1.0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.geometry("800x600")
        self.root.title("Счет в уме")
        self.root.resizable(False, False)
<<<<<<< HEAD
<<<<<<< HEAD
        self.root.mainloop()
>>>>>>> parent of a19504e (Version 1.0)
=======
        self.root.mainloop()
>>>>>>> parent of a19504e (Version 1.0)
=======
        self.root.mainloop()
>>>>>>> parent of a19504e (Version 1.0)
