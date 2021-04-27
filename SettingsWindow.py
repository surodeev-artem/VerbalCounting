from tkinter import *


class SettingsWindow(Toplevel):
    def change(self):
        self._logic.change_difficult(self._difficult.get())
        self.destroy()

    def __init__(self, parent, logic):
        super().__init__(parent)
        self._logic = logic
        self._difficult = IntVar()
        self._difficult.set(self._logic.get_difficult())
        Label(self, text="Выберите сложность").grid(row=0, column=0, padx=15, pady=15)
        Radiobutton(self, text="Легкая", variable=self._difficult, value=0).grid(row=1, column=0, padx=15, pady=15)
        Radiobutton(self, text="Средняя", variable=self._difficult, value=1).grid(row=2, column=0, padx=15, pady=15)
        Radiobutton(self, text="Тяжелая", variable=self._difficult, value=2).grid(row=3, column=0, padx=15, pady=15)
        Button(self, text="Изменить", command=self.change).grid(row=4, column=0, padx=15, pady=15)
        super().title("Найтройки")
