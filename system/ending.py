import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.graph_ability_figure as graph_abi
import function.graph_score_figure as graph_sco
import function.status as status
import function.sound_effect as sound
import function.achievement as achievement
import os, sys

time = ""
achievement_pics = []

if sys.platform == "darwin":
    f1 = tk.font.Font(size = 16)
    f2 = tk.font.Font(size = 32)
    f = tk.font.Font(size = 30)
else:
    f1 = tk.font.Font(size = 8)
    f2 = tk.font.Font(size = 16)
    f = tk.font.Font(size = 22)


def show_ending_graph(window, data):
    global time

    background = tk.Canvas(data["status"].display, width = 1280, height = 720)
    reference = []

    night = Image.open("figure/end_night.png")
    night = ImageTk.PhotoImage(night)
    reference.append(night)

    background.create_image(0,-150, anchor=tk.NW, image=night)

    name = graph_sco.score_illu(data["status"].love_progress, data["status"].grade, data["status"].yang_sheng, data["status"].prestige)
    score_graph = Image.open(f"figure/ability/{name}.png")
    score_graph = ImageTk.PhotoImage(score_graph)
    reference.append(score_graph)
    background.create_image(2 * 1280 / 3 + 270 + 100, 360 - 300, anchor=tk.NE, image=score_graph)

    time = graph_abi.abi_illu(data["status"].wisdom, data["status"].charm, data["status"].fitness, data["status"].social, data["status"].health)
    data["ability_graph"].append(time)
    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    reference.append(ability_graph)
    background.create_image(1280 / 3 + 270 - 100, 360 - 300, anchor=tk.NE, image=ability_graph)

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
    pic_list = data["ability_graph"]
    reference.pop()

    if pic_list.index(time) == len(pic_list) - 1:
        time = pic_list[0]
    else:
        time = pic_list[pic_list.index(time)+1]

    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    reference.append(ability_graph)
    background.create_image(1280 / 3 + 270 - 100, 360 - 300, anchor=tk.NE, image=ability_graph)
    background.image = reference
    background.pack()        


def press_next_button(window, data, background, repeatButton, nextButton):
    background.destroy()
    repeatButton.destroy()
    nextButton.destroy()
    achievement_queue = achievement.checkAchievement(data)
    if len(achievement_queue) == 0:
        qq = Image.open("figure/oily.jpeg")
        qq = ImageTk.PhotoImage(qq)
        no_achievement = tk.Label(window, image = qq)
        no_achievement.image = qq
        no_achievement.pack()

        endButton = tk.Button(window,
                    text = "好吧QQ",
                    font = f, 
                    command = lambda: [press_end_button(window, data, [no_achievement, endButton]), sound.play_button_sound()])
        endButton.place(x = 1000, y = 640)
    else:
        next_achi_button = tk.Button(window,
            text = "下一個成就",
            font = f, 
            command = lambda: [show_achievement(window, data, achievement_queue, next_achi_button), sound.play_button_sound()])
        show_achievement(window, data, achievement_queue, next_achi_button)


def show_achievement(window, data, queue, next_achi_button):
    global achievement_pics
    name = {"情場浪子":"love_master", "好油ㄛpeko":"oh_oily_peko", "超級絕命韭菜":"garlic_chive", "傳說挑戰者":"christmas_challenger", "送子鳥之禮":"storks", "金錢管理大師":"money_manager"}
    
    if len(queue) == 1:
        next_achi_button.destroy()

        sound.play_achievement_music(name[queue[-1]])

        qq = Image.open(f"figure/achievement/{name[queue[-1]]}.jpg")
        qq = qq.resize((1280, 720), Image.ANTIALIAS)
        qq = ImageTk.PhotoImage(qq)
        achievement = tk.Label(window, image = qq)
        achievement.image = qq
        achievement_pics.append(achievement)
        achievement.pack()

        endButton = tk.Button(window,
            text = "沒成就囉",
            font = f, 
            command = lambda: [press_end_button(window, data, achievement_pics), sound.play_button_sound()])
        endButton.place(x = 1000, y = 640)
        achievement_pics.append(endButton)
        achievement_pics.append(next_achi_button)
    else:
        next_achi_button.destroy()

        sound.play_achievement_music(name[queue[-1]])

        qq = Image.open(f"figure/achievement/{name[queue[-1]]}.jpg")
        qq = qq.resize((1280, 720), Image.ANTIALIAS)
        qq = ImageTk.PhotoImage(qq)
        achievement = tk.Label(window, image = qq)
        achievement.image = qq
        achievement_pics.append(achievement)
        achievement.pack()
        
        queue.pop()

        next_achi_button = tk.Button(window,
            text = "下一個成就",
            font = f, 
            command = lambda: [show_achievement(window, data, queue, next_achi_button), sound.play_button_sound()])
        next_achi_button.place(x = 1000, y = 640)


def press_end_button(window, data, used_widget):
    for widget in used_widget:
        widget.destroy()

    ending = Image.open("figure/ending.jpeg")
    ending = ending.resize((1280, 720), Image.ANTIALIAS)
    ending = ImageTk.PhotoImage(ending)

    end_scene = tk.Label(window, image = ending)
    end_scene.image = ending
    end_scene.pack(fill = "both")

    end_button = tk.Button(window, text = "結束",width = 7, font = f, command = lambda: [press_end_game(window), sound.play_button_sound()])
    end_button.place(x = 640-end_button.winfo_reqwidth()/2, y = 300)


def press_end_game(window):
    window.quit()
    path = os.getcwd()
    os.remove(f"{path}/figure/ability/finalpix.png")