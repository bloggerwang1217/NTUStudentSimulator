import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.init_ability as init_abi
import function.graph_ability_figure as graph_abi
import function.schedule as sch
import function.status as status
import function.read_file as read
import function.sound_effect as sound

title_f = tk.font.Font(size = 36)
subtitle_f = tk.font.Font(size = 32)
f = tk.font.Font(size = 20)


def show_midterm_report(window, data, grades):
    sound.play_background_music("night")
    desk = Image.open("figure/desk_texture.jpeg")
    desk = desk.resize((1280, 720), Image.ANTIALIAS)
    desk = ImageTk.PhotoImage(desk)
    background = tk.Label(window, image = desk)
    background.image = desk
    background.pack()

    white = Image.open("figure/white.png")
    white = white.resize((960, 690), Image.ANTIALIAS)
    white = ImageTk.PhotoImage(white)
    small_bg = tk.Label(window, image = white, highlightthickness=2, highlightbackground="black")
    small_bg.image = white
    small_bg.place(x = 640-small_bg.winfo_reqwidth()/2, y = 10)

    # 傳入句子多長要換行和讀檔名稱
    read_data = read.read_file(41, "midterm.txt")
    read_data.insert(0, f"受文者：{data['name']}")
    read_data.insert(0, "期中成績單")

    text = []
    for i in range(len(read_data)): 
        if i == 0:
            text.append(tk.Label(window, text = read_data[i],fg = "black", font = title_f))
        elif i == 1:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = subtitle_f))
        else:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))

        if i == 0:
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 25)
        elif i == 1:
            text[i].place(x = 220, y = 100)
        else:
            text[i].place(x = 220, y = 100 + text[i].winfo_reqheight() * i)

    flip_button = tk.Button(window, text = "翻面", font = f, command = lambda: [press_flip_button(window, data, text, background, small_bg, grades), sound.play_button_sound()])
    flip_button.place(x = 1000, y = 625)

    text.append(flip_button)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除

    
def press_flip_button(window, data, used_widgets, widget1, widget2, grades):
    for widget in used_widgets:
        widget.destroy()

    text = []
    show_grades = []

    show_grades.append("你的成績如下：")
    for item in grades.keys():
        show_grades.append(f"{item}:{grades[item]}分\n")
    for i in range(len(show_grades)): 
        if i == 0:
            text.append(tk.Label(window, text = show_grades[i],fg = "black", font = title_f))
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 30)
        else:
            text.append(tk.Label(window, text = show_grades[i],fg = "black", font = f))
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 200 + text[i].winfo_reqheight() * i)

    check_ability_button = tk.Button(window, text = "你發現信封裡還有其他東西...", font = f, command = lambda: [press_check_ability_button(window, data, text, widget1, widget2), sound.play_button_sound()])
    check_ability_button.place(x = 800, y = 600)

    text.append(check_ability_button)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除


def press_check_ability_button(window, data, used_widgets, widget1, widget2):
    for widget in used_widgets:
        widget.destroy()

    read_data = ["各項能力檢驗量表"]
    read_data.append("經過了一段時間，下面是你各項能力值的分佈")

    text = []
    for i in range(len(read_data)): 
        if i == 0:
            text.append(tk.Label(window, text = read_data[i],fg = "black", font = title_f))
        elif i == 1:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))

        if i == 0:
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 25)
        elif i == 1:
            text[i].place(x = 220, y = 100)


    # 貼上初始化能力值的圖
    time = graph_abi.abi_illu(data["status"].wisdom, data["status"].charm, data["status"].fitness, data["status"].social, data["status"].health)
    data["ability_graph"].append(time)
    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    ability = tk.Label(window, image = ability_graph)
    ability.image = ability_graph
    ability.place(x = 640 - widget2.winfo_reqwidth()/2.3, y = 140)
    

    nextbutton = tk.Button(window, text = "開始排行程表囉！", font = f, command = lambda: [press_go_picking_button(window, data, text), sound.play_button_sound()])
    nextbutton.place(x = 850, y = 620)

    text.append(widget1)
    text.append(widget2)
    text.append(nextbutton)
    text.append(ability)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除

def press_go_picking_button(window, data, used_widgets):
    for widget in used_widgets:
        widget.destroy()
    data["previous_event"] = "第三次排行程表"
    sch.get_new_schedule(window, data["picked_course"], data, False)