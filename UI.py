import tkinter.messagebox
from tkinter import *
import tkinter.ttk as ttk

BTN_BG_COLOR = "#746096"
ACTIVE_BTN_BG_COLOR = "#CCBFE3"
APP_BG_COLOR = "#FFFEF0"


class UI:
    def __init__(self, logic):
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

        self.countdown()
        self.create_buttons()
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

        self._remaining_time_progress_bar.step(-10 / 3)  # Уменьшение на 1 секунду
        self._root.after(1000, self.countdown)

    # Создает кнопки для задач
    def create_buttons(self):
        button_coords = [[1, 0], [1, 2], [2, 1], [3, 0], [3, 2]]

        btn_pad_x = 10
        btn_pad_y = 5
        btn_width = 15
        btn_height = 5

        for button_id, coords in enumerate(button_coords):
            task = StringVar()
            btn = Button(textvariable=task, width=btn_width, height=btn_height,
                         bg=BTN_BG_COLOR, fg=APP_BG_COLOR,
                         font=("Arial", 15), activebackground=ACTIVE_BTN_BG_COLOR,
                         command=(lambda btn_id=button_id: self.handle_btn_click(btn_id)))
            btn.grid(row=coords[0], column=coords[1], padx=btn_pad_x, pady=btn_pad_y)
            self._tasks.append(task)

    # Обрабатывает нажатие на кнопку с задачей
    def handle_btn_click(self, btnId):
        self._logic.btn_clicked(btnId)
        self.new_round(self._logic.get_score(), self._logic.get_max_scores())

    # Начинает новый раунд игры
    def new_round(self, score, max_score):
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
        self._root.rowconfigure(3, weight=1)
        self._root.geometry("800x600")
        self._root.title("Счет в уме")
        self._root.resizable(False, False)
