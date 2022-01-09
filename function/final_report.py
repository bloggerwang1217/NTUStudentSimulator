import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.初始能力值設定 as init_abi
import function.結算能力值圖片產生 as graph_abi
import function.暑假事件選擇 as summer
import function.status as status
import function.read_file as read
import function.sound_effect as sound
import function.show_event as show

def show_final_report(window, data, grades):
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

    title_f = tk.font.Font(size = 36)
    subtitle_f = tk.font.Font(size = 32)
    f = tk.font.Font(size = 20)

    # 傳入句子多長要換行和讀檔名稱
    read_data = read.read_file(41, "midterm.txt")
    read_data.insert(0, f"受文者：{data['name']}")
    read_data.insert(0, "學期成績單")

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
    
    f = tk.font.Font(size = 32)

    text = []
    show_grades = []
    for item in grades.keys():
        show_grades.append(f"{item}:{grades[item]}分\n")
    for i in range(len(show_grades)): 
        text.append(tk.Label(window, text = show_grades[i],fg = "black", font = f))

        if i == 0:
            text[i].place(x = 180, y = 30)
        else:
            text[i].place(x = 180, y = 30 + text[i].winfo_reqheight() * i)

    check_ability_button = tk.Button(window, text = "你發現信封裡還有其他東西...", font = f, command = lambda: [press_check_ability_button(window, data, text, widget1, widget2), sound.play_button_sound()])
    check_ability_button.place(x = 800, y = 620)

    text.append(check_ability_button)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除


def press_check_ability_button(window, data, used_widgets, widget1, widget2):
    for widget in used_widgets:
        widget.destroy()
    
    title_f = tk.font.Font(size = 36)
    f = tk.font.Font(size = 20)

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
    
    time_list = ["大一上", "大一下", "大二上", "大二下","大三上", "大三下","大四上","大四下"]
    if data["time"] == "大四下":
        nextbutton = tk.Button(window, text = "歡樂畢業！", font = f, command = lambda: [press_next_button(window, data, text), sound.play_button_sound()])
        data["time"] = "畢業"
    else:
        data["time"] = time_list[time_list.index(data["time"])+1]
        nextbutton = tk.Button(window, text = "進入暑假", font = f, command = lambda: [press_next_button(window, data, text), sound.play_button_sound()])
    nextbutton.place(x = 850, y = 620)

    text.append(widget1)
    text.append(widget2)
    text.append(nextbutton)
    text.append(ability)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除

def press_next_button(window, data, used_widgets):
    time_list = ["大一上", "大一下", "大二上", "大二下","大三上", "大三下","大四上","大四下"]
    sound.enter_game_button_sound()
    for widget in used_widgets:
        widget.destroy()

    if data["time"] == "大四下":
        f = tk.font.Font(size = 30)
        reference = []

        background = tk.Canvas(data["status"].display, width = 1280, height = 720)

        desk = Image.open("figure/desk_texture.jpeg")
        desk = desk.resize((1280, 720), Image.ANTIALIAS)
        desk = ImageTk.PhotoImage(desk)
        background.create_image(0,0, anchor=tk.NW, image=desk)
        reference.append(desk)

        diploma = Image.open("figure/diploma.jpeg")
        diploma = diploma.resize((960, 680), Image.ANTIALIAS)
        diploma = ImageTk.PhotoImage(diploma)
        background.create_image(640 - 480, 10, anchor=tk.NW, image=diploma)
        reference.append(diploma)

        background.create_text(640 - 320, 250, anchor=tk.NW, text = f"學生：{data['name']}", font = f)


        background.image = reference
        background.pack()


        graduateButton = tk.Button(window, text = "最後的最後...", font = f, command = lambda: [press_graduate_button(window, data, background, graduateButton), sound.play_button_sound()])
        graduateButton.place(x = 640 + 320 - graduateButton.winfo_reqwidth(), y = 250)

        
    else:
        time = time_list[time_list.index(data["time"]+1)]
        summer.choose_summer_event(data)


def press_graduate_button(window, data, background, graduateButton):
    background.destroy()
    graduateButton.destroy()
    show.show_event(data, "破關", "正常結局")
