import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.結算能力值圖片產生 as graph_abi
import function.結算評分值圖片產生 as graph_sco
import function.status as status
import function.sound_effect as sound
import function.achievement as achievement
import os

time = ""
achievement_pics = []

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
    f = tk.font.Font(size = 30)

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
    f = tk.font.Font(size = 30)
    sound.play_button_sound()
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
    
    f = tk.font.Font(size = 30)
    if len(queue) == 1:
        sound.play_achievement_music(queue[-1])
        qq = Image.open(f"figure/成就/{queue[-1]}.jpg")
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
    else:
        qq = Image.open(f"figure/成就/{queue[-1]}.jpg")
        qq = qq.resize((1280, 720), Image.ANTIALIAS)
        qq = ImageTk.PhotoImage(qq)
        achievement = tk.Label(window, image = qq)
        achievement.image = qq
        achievement.pack()
        achievement_pics.append(achievement)
        queue.pop()
        next_achi_button.place(x = 1000, y = 640)


def press_end_button(window, data, used_widget):
    f = tk.font.Font(size = 30)
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
    try:
        for name in data["ability_graph"]:
            os.remove(f"{path}/figure/ability/{name}.png")
        os.remove(f"{path}/figure/ability/finalpix.png")
    except:
        pass