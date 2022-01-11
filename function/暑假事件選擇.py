import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import function.show_event as show
import function.sound_effect as sound

def choose_summer_event(data):
    f = tk.font.Font(size = 28)

    background = tk.Canvas(data["status"].display, width = 1280, height = 720)

    beach = Image.open("figure/summer_vacation.jpeg")
    beach = beach.resize((1280, 720), Image.ANTIALIAS)
    beach = ImageTk.PhotoImage(beach)
    background.create_image(0,0, anchor=tk.NW, image=beach)
    background.image = beach

    text = background.create_text(640, 2 * 320 / 3, text = f"學期結束後，身為一個大學生兩個月的暑假應該如何分配是很重要的。\n不過這也是人生中，所剩無幾的暑假了，大學畢業後，哪會有暑假能夠休息。\n來吧，做出你的選擇。（註：選在家宅會出現細項）", anchor = "center", fill = "white", font = f)

    background.pack(fill = "both")

    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: [press_continue(data, background, nextButton, text), sound.play_button_sound()])
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 320 - nextButton.winfo_reqheight()/2)

def press_continue(data, background, nextButton, text):
    f = tk.font.Font(size = 28)
    background.delete(text)
    nextButton.destroy()

    choose_button = []
    button1 = tk.Button(data["status"].display, text = "當兵", relief = "raise", font = f, command = lambda: [choose(data, background, choose_button, "當兵"), sound.play_button_sound()])
    button2 = tk.Button(data["status"].display, text = "打工", relief = "raise", font = f, command = lambda: [choose(data, background, choose_button, "打工"), sound.play_button_sound()])
    button3 = tk.Button(data["status"].display, text = "服務學習", relief = "raise", font = f, command = lambda: [choose(data, background, choose_button, "服務學習"), sound.play_button_sound()])
    button4 = tk.Button(data["status"].display, text = "陪另一半", relief = "raise", font = f, command = lambda: [choose(data, background, choose_button, "陪另一半"), sound.play_button_sound()])
    button5 = tk.Button(data["status"].display, text = "在家宅", relief = "raise", font = f, command = lambda: [choose(data, background, choose_button, "在家宅"), sound.play_button_sound()])
    
    choose_button.append(button1)
    choose_button.append(button2)
    choose_button.append(button3)
    choose_button.append(button4)
    choose_button.append(button5)

    button1.place(x = 1 * 1280 / 6 - button1.winfo_reqwidth()/2, y = 320/1.5 - button1.winfo_reqheight()/2)
    button2.place(x = 2 * 1280 / 6 - button2.winfo_reqwidth()/2, y = 320/1.5 - button2.winfo_reqheight()/2)
    button3.place(x = 3 * 1280 / 6 - button3.winfo_reqwidth()/2, y = 320/1.5 - button3.winfo_reqheight()/2)
    button4.place(x = 4 * 1280 / 6 - button4.winfo_reqwidth()/2, y = 320/1.5 - button1.winfo_reqheight()/2)
    button5.place(x = 5 * 1280 / 6 - button5.winfo_reqwidth()/2, y = 320/1.5 - button1.winfo_reqheight()/2)


def choose(data, background, used_button , chosen):
    f = tk.font.Font(size = 28)
    for button in used_button:
        button.destroy()
    if chosen != "在家宅":
        background.destroy()
        show.process_event(data, [[f"暑假事件:{chosen}"]])
    else:
        choose_button = []

        button1 = tk.Button(data["status"].display, text = "耍廢", relief = "raise", font = f, command = lambda: [home_choose(data, background, choose_button, "耍廢"), sound.play_button_sound()])
        button2 = tk.Button(data["status"].display, text = "唸書", relief = "raise", font = f, command = lambda: [home_choose(data, background, choose_button, "唸書"), sound.play_button_sound()])
        button3 = tk.Button(data["status"].display, text = "規律作息", relief = "raise", font = f, command = lambda: [home_choose(data, background, choose_button, "規律作息"), sound.play_button_sound()])
        button4 = tk.Button(data["status"].display, text = "投資", relief = "raise", font = f, command = lambda: [home_choose(data, background, choose_button, "投資"), sound.play_button_sound()])

        choose_button.append(button1)
        choose_button.append(button2)
        choose_button.append(button3)
        choose_button.append(button4)

        button1.place(x = 1 * 1280 / 5 - button1.winfo_reqwidth()/2, y = 320/1.5 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 5 - button2.winfo_reqwidth()/2, y = 320/1.5 - button2.winfo_reqheight()/2)
        button3.place(x = 3 * 1280 / 5 - button3.winfo_reqwidth()/2, y = 320/1.5 - button3.winfo_reqheight()/2)
        button4.place(x = 4 * 1280 / 5 - button4.winfo_reqwidth()/2, y = 320/1.5 - button3.winfo_reqheight()/2)


def home_choose(data, background, used_button , chosen):
    f = tk.font.Font(size = 28)
    for button in used_button:
        button.destroy()
    if chosen != "投資":
        background.destroy()
        show.process_event(data, [[f"暑假事件:{chosen}"]])
    else:
        choose_button = []

        button1 = tk.Button(data["status"].display, text = "虛擬貨幣", relief = "raise", font = f, command = lambda: [stock_choose(data, background, choose_button, "虛擬貨幣"), sound.play_button_sound()])
        button2 = tk.Button(data["status"].display, text = "ETF", relief = "raise", font = f, command = lambda: [stock_choose(data, background, choose_button, "ETF"), sound.play_button_sound()])
        button3 = tk.Button(data["status"].display, text = "債券", relief = "raise", font = f, command = lambda: [stock_choose(data, background, choose_button, "債券"), sound.play_button_sound()])

        choose_button.append(button1)
        choose_button.append(button2)
        choose_button.append(button3)

        button1.place(x = 1 * 1280 / 4 - button1.winfo_reqwidth()/2, y = 320/1.5 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 4 - button2.winfo_reqwidth()/2, y = 320/1.5 - button2.winfo_reqheight()/2)
        button3.place(x = 3 * 1280 / 4 - button3.winfo_reqwidth()/2, y = 320/1.5 - button3.winfo_reqheight()/2)


def stock_choose(data, background, used_button , chosen):
    f = tk.font.Font(size = 28)
    for button in used_button:
        button.destroy()
    background.destroy()
    show.process_event(data, [[f"暑假事件:{chosen}"]])