# Пример многопоточности Python для печати текущей даты.
# 1. Определите подкласс, используя класс Thread.
# 2. Создайте подкласс и запустите поток.

import threading
import time


class Timer(threading.Thread):
    appIsOpen = True

    def __init__(self, name, counter, data, logic):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.data = data
        self.logic = logic

    def run(self):
        timing = time.time()
        while self.appIsOpen:
            if time.time() - timing > 1.0:
                timing = time.time()
                self.data.timeLeft -= 1
                if self.data.timeLeft:

                    self.data.timeLeft = 10

