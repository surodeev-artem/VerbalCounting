import Data
import random
import json
from Task import Task


class Logic:
    def __init__(self):
        self.data = Data.Data()

    # Генерирует массив задач
    def create_tasks(self):
        self.data.tasks.clear()
        correctBtn = random.randint(0, 4)
        self.data.correct_button = correctBtn
        for i in range(5):
            shouldCorrect = i == correctBtn
            self.data.tasks.append(self.create_task(shouldCorrect))
        return self.data.tasks

    # Рандомно генерирует задачу
    def create_task(self, isTrue):
        sign = random.randint(0, 3)
        if sign == 0 or sign == 1:
            maxNum = 70 + (30 * self.data.difficult)
        elif sign == 2:
            maxNum = 15 + (10 * self.data.difficult)
        else:
            maxNum = 50 + (20 * self.data.difficult)

        if sign == 3:  # Деление. Используем умножение делителя на частное для получения целых чисел
            secondNum = random.randint(1, maxNum)
            firstNum = secondNum * random.randint(1, 15 + (10 * self.data.difficult))
        else:
            firstNum = random.randint(1, maxNum)
            secondNum = random.randint(1, maxNum)

        if isTrue:
            answer = self.getCorrectAnswer(firstNum, sign, secondNum)
        else:
            answer = random.randint(1, 300)
        return Task(firstNum, sign, secondNum, answer)

    # Рассчитывает правильный ответ исходя из знака
    def getCorrectAnswer(self, firstNum, sign, secondNum):
        if sign == 0:
            return firstNum + secondNum
        elif sign == 1:
            return firstNum - secondNum
        elif sign == 2:
            return firstNum * secondNum
        else:
            return int(firstNum / secondNum)

    # Обрабатывает наажатия на кнопку
    def btn_clicked(self, btnId):
        if btnId == self.data.correct_button:
            self.data.scores += 20 + (10 * self.data.difficult)
            if self.data.scores > self.data.max_scores:
                self.change_max_scores_in_file()
                self.data.max_scores = self.data.scores
            return True
        else:
            self.data.scores -= 30 + (15 * self.data.difficult)
            return False

    # Получает текущее количество очков
    def get_score(self):
        return self.data.scores

    # Получает максимальное количество очков в переменной
    def get_max_scores(self):
        return self.data.max_scores

    # Изменяет сложность игры
    def change_difficult(self, difficult):
        self.data.difficult = difficult

    def get_difficult(self):
        return self.data.difficult

    # Возвращает id правильной кнопки
    def get_correct_answer(self):
        return self.data.correct_button

    # Изменяет максимальное количество очков в файле
    def change_max_scores_in_file(self):
        score = self.data.scores
        f = open("max.json", "w")
        json.dump({"max_scores": score}, f)
        f.close()

    # Получает максимальное количество очков из файла
    def get_max_scores_from_file(self):
        try:
            f = open("max.json", "r")
            self.data.max_scores = json.load(f)["max_scores"]
            print(json)
        except FileNotFoundError:
            f = open("max.json", "w")
            json.dump({"max_scores": 100}, f)
            f.close()
            self.data.max_scores = 100
            print(json)

    # Уменьшает текущее количество очков при окончании времени
    def time_is_up(self):
        self.data.scores -= 20 + (10 * self.data.difficult)

    # Сбрасывает значения текущего количества очков
    def reset_score_value(self):
        self.data.scores = 100
