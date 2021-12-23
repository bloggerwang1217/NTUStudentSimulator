import tkinter as tk
from PIL import ImageTk, Image 

def press_start_game(start_scene, start_button, window):
    start_scene.destroy()
    start_button.destroy()
    beginning_story(window)

def start_game(window):

    f = tk.font.Font(size = 32, family = "lihsianti")


    beginning = Image.open("figure/beginning.jpeg")
    beginning = beginning.resize((1280, 720), Image.ANTIALIAS)
    beginning = ImageTk.PhotoImage(beginning)

    start_scene = tk.Label(window, image = beginning)
    start_scene.pack(fill = "both")

    start_button = tk.Button(window, text = "開始遊戲",width = 10, font = f, command = lambda: press_start_game(start_scene, start_button, window))
    start_button.place(x = 550, y = 300)

def beginning_story(window):
    f = tk.font.Font(size = 48, family = "lihsianti")
    gray = 0
    window.configure(bg="white")

    text = tk.Label(window, text = "你終於進入了理想中的大學\n台大\n帶著既期待又怕受傷害的心情\n你準備迎向這四年未知的生活...", font = f)
    text.place(x = 300, y = 100)
