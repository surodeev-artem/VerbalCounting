import threading
from UI import UI

class UiThread(threading.Thread):
    def __init__(self, name, counter, logic, timerThread, ui):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.logic = logic
        self.timerThread = timerThread
        self.ui = ui

    def run(self):
        self.ui.initComponents()