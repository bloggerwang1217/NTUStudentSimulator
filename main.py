import system.beginning as bg
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import function.schedule as sch
import function.status as status
import function.read_file as read
import function.course_selection as cs
import function.show_event as show
import function.初始能力值設定 as init_abi
import function.結算能力值圖片產生 as graph_abi
import function.結算評分值圖片產生 as graph_sco
import function.暑假事件選擇 as cse
import system.ending as ending

window = tk.Tk()
window.geometry("1280x720")
window.resizable(0, 0)
window.title("為美好的台大生活獻上祝福")

data = {}
bg.start_game(window, data)

# 初始化測試
# wisdom, charm, fitness, social, health, luck = init_abi.ininial_set()
# data["status"] = status.Status(wisdom, charm, fitness, social, health, luck, read.read_course(), window)

# show.process_event(data, ["觸發事件:推坑Vt"])
# show.process_event(data, ["必然事件:聯誼"])
# semester.start_semester(window, data, "大一下", selected_course)
# data["status"].yang_sheng = 100
# data["status"].prestige = 50
# data["status"].grade = 50
# data["status"].love_progress = 50
# data["ability_graph"] = []
# ending.show_ending_graph(window, data)

window.mainloop()