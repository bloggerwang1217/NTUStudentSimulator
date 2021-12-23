import tkinter as tk
from PIL import ImageTk, Image

def press_start_game(start_scene, start_button, name_list, window):
    start_scene.destroy()
    start_button.destroy()
    name_list.destroy()
    beginning_story(window)


def start_game(window):

    f = tk.font.Font(size = 28)

    beginning = Image.open("figure/beginning.png")
    beginning = beginning.resize((1280, 720), Image.ANTIALIAS)
    beginning = ImageTk.PhotoImage(beginning)

    start_scene = tk.Label(window, image = beginning)
    start_scene.image = beginning
    start_scene.pack(fill = "both")

    name_list = tk.Label(window, text = "製作者：王敏行、劉健榮、羅士軒、陳利煌、周匯森、何峻德", font = f)
    name_list.place(x = 240, y = 660)

    start_button = tk.Button(window, text = "開始遊戲",width = 7, font = f, command = lambda: press_start_game(start_scene, start_button, name_list, window))
    start_button.place(x = 560, y = 300)




def beginning_story(window):
    f = tk.font.Font(size = 48, family = "lihsianti")

    window.configure(bg="white")

    text = [0, 1]  # 加入開場說明文字或圖片
    text[0] = tk.Label(window, text = "你終於進入了理想中的大學\n台大\n帶著既期待又怕受傷害的心情\n你準備迎向這四年未知的生活...", font = f)
    text[1] = tk.Label(window, text = "我為什麼在這裡", font = f)
    text[0].place(x = 300, y = 100)

    index = [0]
    next_button = tk.Button(window, text = "下一頁",width = 6, font = f, command = lambda: press_next_button(window, text, next_button, index))
    next_button.place(x = 1000, y = 500)

    
def press_next_button(window, text, next_button, index):
    f = tk.font.Font(size = 32)
    if index[0] == len(text)-1:
        text[index[0]].destroy()
        next_button.destroy()
        # 呼叫輸入姓名函式
        return
    text[index[0]].destroy()
    text[index[0]+1].place(x = 300, y = 100)
    index[0] += 1
