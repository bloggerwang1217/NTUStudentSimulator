import function.input as ip
import function.schedule as sch
import function.status as status
import function.beginning as bg
import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.geometry("1280x720")
window.title("為美好的台大生活獻上祝福")

bg.start_game(window)


# def start_game():
#     start_scene.destroy()
#     start_button.destroy()
#     bg.beginning_story(window)

# title_f = tk.font.Font(size = 84, family = "lihsianti")
# f = tk.font.Font(size = 32, family = "lihsianti")

# beginning = Image.open("figure/beginning.jpeg")
# beginning = beginning.resize((1280, 720), Image.ANTIALIAS)
# beginning = ImageTk.PhotoImage(beginning)

# start_scene = tk.Label(window, image = beginning)
# start_scene.pack()


# start_button = tk.Button(window, text = "開始遊戲",width = 10, font = f, command = start_game)
# start_button.place(x = 550, y = 300)


window.mainloop()

# data = ip.input_basic_data()
# name = data[0]
# sex = data[1]
# print(name, sex)

# selected_class = {"1-1":"A課", "2-2":"B課", "4-3":"C課"}
# previous_picked_schedule = {'1-1': 'A課', '1-2': '讀A課', '1-3': '社交', '1-4': '健身', '2-1': '社交', '2-2': 'B課', '2-3': '讀A課', '2-4': '休息', '3-1': '讀A課', '3-2': '讀B課', '3-3': '讀A課', '3-4': '休息', '4-1': '讀A課', '4-2': '健身', '4-3': 'C課', '4-4': '社交', '5-1': '休息', '5-2': '約會', '5-3': '社交', '5-4': '休息'}

# picked_schedule = sch.get_new_schedule(selected_class, previous_picked_schedule)

# print(picked_schedule)