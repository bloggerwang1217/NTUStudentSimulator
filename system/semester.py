import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.status as status
import function.schedule as schedule
import function.sound_effect as sound


def start_semester(window, data, picked, time):
    sound.play_background_music("封面背景音樂")
    title_f = tk.font.Font(size = 36)
    data["time"] = time
    data["previous_event"] = "第一次排行程表"

    background = tk.Canvas(window, width = 1280, height = 720)
    start_semester = Image.open(f"figure/semester/{time}.jpeg")
    start_semester = start_semester.resize((1280, 720), Image.ANTIALIAS)
    start_semester = ImageTk.PhotoImage(start_semester)
    background.create_image(0,0, anchor=tk.NW, image=start_semester)
    background.image = start_semester

    background.pack(fill = "both")
    print(data["status"])
    startButton = tk.Button(data["status"].display, text = "開始學期!", relief = "raise", font = title_f, command = lambda: [press_start(data, background, startButton, picked), sound.enter_game_button_sound()])
    startButton.place(x = 640 - startButton.winfo_reqwidth()/2, y = 2 *360/3)


def press_start(data, background, startButton, picked):
    background.destroy()
    startButton.destroy()
    schedule.get_new_schedule(data["status"].display, picked, data, True)