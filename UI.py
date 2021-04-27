import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk

from SettingsWindow import SettingsWindow

BTN_BG_COLOR = "#746096"
ACTIVE_BTN_BG_COLOR = "#CCBFE3"
APP_BG_COLOR = "#FFFEF0"
BTN_PAD_X = 10
BTN_PAD_Y = 5
BTN_WIDTH = 15
BTN_HEIGHT = 5


class UI:
    def __init__(self, logic):
        self._buttons = []
        self._tasks = []
        self._root = Tk()
        self._logic = logic

        self._current_score = StringVar()
        self._score_label = Label(textvariable=self._current_score, font=("Arial", 25), bg=APP_BG_COLOR) \
            .grid(row=0, column=1, pady=20)
        self.set_score(self._logic.get_score())

        self._max_score = StringVar()
        self._max_score_label = Label(textvariable=self._max_score, font=("Arial", 15), bg=APP_BG_COLOR) \
            .grid(row=0, column=2, pady=20)
        self.set_max_score(self._logic.get_max_scores())

        self._remaining_time_progress_bar = ttk.Progressbar(length=100, mode="determinate")
        self._remaining_time_progress_bar.grid(row=0, column=0, pady=20)
        self.reset_remaining_time()

        self._settings_btn = Button(text="Настройки", width=9, height=2,
                                    bg=BTN_BG_COLOR, fg=APP_BG_COLOR,
                                    font=("Arial", 15), activebackground=ACTIVE_BTN_BG_COLOR,
                                    command=(lambda: SettingsWindow(self._root, self._logic).grab_set()))
        self._settings_btn.grid(row=4, column=2, padx=BTN_PAD_X, pady=BTN_PAD_Y)

        self.countdown()
        self.create_tasks_buttons()
        self.set_tasks()
        self.set_window_config()

        self._root.mainloop()

    # Сбрасывает прогресс оставшегося времени
    def reset_remaining_time(self):
        self._remaining_time_progress_bar['value'] = 100

    # Отсчитывает время до окончания раунда
    def countdown(self):
        time = self._remaining_time_progress_bar['value']
        if time <= 0:  # Время вышло
            self._logic.time_is_up()
            self.new_round(self._logic.get_score(), self._logic.get_max_scores())

        self._remaining_time_progress_bar.step(-10 / (3 - self._logic.get_difficult()))  # Уменьшение времени
        self._root.after(1000, self.countdown)

    # Создает кнопки для задач
    def create_tasks_buttons(self):
        button_coords = [[1, 0], [1, 2], [2, 1], [3, 0], [3, 2]]

        for button_id, coords in enumerate(button_coords):
            task = StringVar()
            btn = Button(textvariable=task, width=BTN_WIDTH, height=BTN_HEIGHT,
                         bg=BTN_BG_COLOR, fg=APP_BG_COLOR,
                         font=("Arial", 15), activebackground=ACTIVE_BTN_BG_COLOR,
                         command=(lambda btn_id=button_id: self.handle_btn_click(btn_id)))
            btn.grid(row=coords[0], column=coords[1], padx=BTN_PAD_X, pady=BTN_PAD_Y)
            self._buttons.append(btn)
            self._tasks.append(task)

    # Обрабатывает нажатие на кнопку с задачей
    def handle_btn_click(self, btnId):
        self._buttons[self._logic.get_correct_answer()].config(bg="#0F0")  # Делает правильную кнопку зеленой
        isCorrect = self._logic.btn_clicked(btnId)
        if not isCorrect:
            self._buttons[btnId].config(bg="#F00")  # Делает правильную кнопку красной
        self._root.after(1000, lambda score=self._logic.get_score(), max_scores=self._logic.get_max_scores(): self.new_round(score, max_scores))

    # Начинает новый раунд игры
    def new_round(self, score, max_score):
        # Возвращает цвет кнопкам
        for btn in self._buttons:
            btn.config(bg=BTN_BG_COLOR)

        self.reset_remaining_time()
        self.set_max_score(max_score)
        self.set_score(score)
        self.set_tasks()

        if self._logic.get_score() < 0:
            messageBox = tkinter.messagebox.askquestion('Игра окончена', 'Вы хотите начать сначала?')
            if messageBox == 'yes':
                self._logic.reset_score_value()
                self.set_score(self._logic.get_score())
            else:
                self._root.destroy()

    # Устанавливает текущее количество очков в поле
    def set_score(self, score):
        self._current_score.set("Текущий счет: " + str(score))

    # Устанавливает количество максимальных очков в поле
    def set_max_score(self, max_score):
        self._max_score.set("Максимальный счет: " + str(max_score))

    # Устанавливает текст задач на кнопки
    def set_tasks(self):
        tasks = self._logic.create_tasks()
        for i, task in enumerate(tasks):
            handled_sign = self.handle_sign(task.sign)
            handled_task = str(task.firstNum) + " " + handled_sign + " " + str(task.secondNum) + " = " + str(task.answer)
            self._tasks[i].set(handled_task)

    # Возвращает знак выражения в текстовом формате
    def handle_sign(self, sign_id):
        if sign_id == 0:
            return "+"
        elif sign_id == 1:
            return "-"
        elif sign_id == 2:
            return "*"
        else:
            return "/"

    # Устанавливает настройки окна
    def set_window_config(self):
        self._root.config(bg=APP_BG_COLOR)
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(2, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(4, weight=1)
        self._root.geometry("800x600")
        self._root.title("Счет в уме")
        self._root.resizable(False, False)
