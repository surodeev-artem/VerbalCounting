from tkinter import *


class UI:
    buttons = []

    root = None
    score = None
    task = None

    def createRoot(self):
        self.root = Tk()

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
            self.buttons.append(Button(text="1", width=btnWidth, height=btnHeight)
                                .grid(row=i[0], column=i[1], padx=btnPadX, pady=btnPadY))

    def renderWindow(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.geometry("800x600")
        self.root.title("Счет в уме")
        self.root.resizable(False, False)
        self.root.mainloop()