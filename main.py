import Data
from Logic import Logic
from UiThread import UiThread
from Timer import Timer
import UI


def startThreads():
    timer = Timer("Timer", 1, data, logic)
    uiThread = UiThread("UI", 2, logic, timer, ui)
    timer.start()
    uiThread.start()
    timer.join()
    uiThread.join()

data = Data.Data()
logic = Logic(data)
logic.getMaxScoresFromFile()
ui = UI.UI(logic)
startThreads()
