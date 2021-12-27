import system.beginning as bg
import tkinter as tk
import function.schedule as sch
import function.status as status
import function.read_file as rf
import function.course_selection as cs

window = tk.Tk()
window.geometry("1280x720")
window.resizable(0, 0)
window.title("為美好的台大生活獻上祝福")

data = {}
bg.start_game(window, data)

# 排時間表
# selected_course = {"1-1":"A課", "2-2":"B課", "4-3":"C課"}
# data["picked_schedule"] = {'1-1': 'A課', '1-2': '讀A課', '1-3': '社交', '1-4': '健身', '2-1': '社交', '2-2': 'B課', '2-3': '讀A課', '2-4': '休息', '3-1': '讀A課', '3-2': '讀B課', '3-3': '讀A課', '3-4': '休息', '4-1': '讀A課', '4-2': '健身', '4-3': 'C課', '4-4': '社交', '5-1': '休息', '5-2': '約會', '5-3': '社交', '5-4': '休息'}
# sch.get_new_schedule(window, selected_course, data)

window.mainloop()