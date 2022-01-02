import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.read_file as read
import function.初始能力值設定 as init_abi
import function.結算能力值圖片產生 as graph_abi
import function.結算評分值圖片產生 as graph_sco
import function.status as status
import function.sound_effect as sound

time = ""

def show_ending_graph(window, data):
    global time

    f1 = tk.font.Font(size = 16)
    f2 = tk.font.Font(size = 32)
    background = tk.Canvas(data["status"].display, width = 1280, height = 720)
    reference = []

    night = Image.open("figure/end_night.png")
    night = ImageTk.PhotoImage(night)
    reference.append(night)

    background.create_image(0,-150, anchor=tk.NW, image=night)

    # name = graph_abi.score_illu(data["status"].love_progress, data["status"].grade, data["status"].yang_sheng, data["status"].prestige)
    name = graph_sco.score_illu(40, 50, 60, 70)
    score_graph = Image.open(f"figure/ability/{name}.png")
    score_graph = ImageTk.PhotoImage(score_graph)
    reference.append(score_graph)
    background.create_image(2 * 1280 / 3 + 270 + 120, 360 - 240, anchor=tk.NE, image=score_graph)

    # time = graph_abi.abi_illu(data["status"].wisdom, data["status"].charm, data["status"].fitness, data["status"].social, data["status"].health)
    time = "5"
    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    reference.append(ability_graph)
    background.create_image(1280 / 3 + 270 - 120, 360 - 240, anchor=tk.NE, image=ability_graph)

    background.image = reference
    background.pack()

    repeatButton = tk.Button(window,
                        text = "重複點擊看你的能力值變化",
                        font = f1, 
                        command = lambda: [press_repeat_button(data, background, reference), sound.play_button_sound()])
    repeatButton.place(x = 1280 / 3 + 200, y = 640)
    
    nextButton = tk.Button(window,
                        text = "前往成就",
                        font = f2, 
                        command = lambda: [press_next_button(window, data, background, repeatButton, nextButton), sound.play_button_sound()])
    nextButton.place(x = 1280 / 3 + 475, y = 630)

def press_repeat_button(data, background, reference):
    global time
    pic_list = ["1", "2", "3" , "4", "5"]
    reference.pop()

    if pic_list.index(time) == len(pic_list) - 1:
        time = pic_list[0]
    else:
        time = pic_list[pic_list.index(time)+1]

    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    reference.append(ability_graph)
    background.create_image(1280 / 3 + 270 - 120, 360 - 240, anchor=tk.NE, image=ability_graph)
    background.image = reference
    background.pack()        


def press_next_button(window, data, background, repeatButton, nextButton):

    sound.play_button_sound()

    background.destroy()
    repeatButton.destroy()
    nextButton.destroy()





def run_achievement():
    pass

