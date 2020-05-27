import win32gui as gui
import win32api as api
import win32process as p
import psutil
import time
import datetime
from pywinauto import Desktop
import json
import pathlib

active_window = ""
data = {}
process_name = ""
process_pid = ""
time_started = ""
time_ended = ""
time_stamp = ""

data = {
    "process_name":"",
    "process_pid":"",
    "time_stamp":"",
    "time_started":"",
    "time_ended":"",
    "time_spent":"",
}

while True:
    new_window =  p.GetWindowThreadProcessId(gui.GetForegroundWindow())

    if new_window != active_window:
        active_window = new_window
        
        if time_started != "":

            if process_pid == data["process_pid"]:
                pass

            else:
                time_ended = time.time()
                time_spent = time_ended - time_started
                
                data = {
                    "process_name":process_name,
                    "process_pid":process_pid,
                    "time_stamp":time_stamp,
                    "time_started":time_started,
                    "time_ended":time_ended,
                    "time_spent":time_spent,
                }

                print(data)

                with open(pathlib.Path(__file__).parent / "data.json", "a+") as f:
                    json.dump(data, f, indent=4)
                    f.write(",")
                    f.write("\n")
                
                time_started = time_ended
                time_stamp = time.ctime()

        else:
            time_stamp = time.ctime()
            time_started = time.time()

        for process in psutil.process_iter():
            if any(x == process.pid for x in new_window):
                if process.pid == 0:
                    pass
                else:
                    process_name = process.name()
                    process_pid = process.pid

#Author: Tiemo Timtschenko