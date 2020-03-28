import win32gui as gui
import win32api as api
import win32process as p
import psutil
import time
import datetime
from pywinauto import Desktop

active_window = ""


while True:
    new_window =  p.GetWindowThreadProcessId(gui.GetForegroundWindow())

    if new_window != active_window:

        active_window = new_window
        started = time.time()

        for process in psutil.process_iter():
            if any(x == process.pid for x in new_window):
                if process.pid == 0:
                    pass
                else:
                    print(process.name()," - ", process.pid ," - ", started)
                    print()


#Author: Tiemo Timtschenko