import function.read_file as read
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image

def show_necessary_event(data, name):
    pass


def show_trigger_event(data, name):
    pass


def show_summer_event(data, name):
    event_list = ["實習", "當兵", "打工", "服務學習", "陪另一半", "耍廢", "唸書", "規律作息", "高報酬", "中報酬", "低報酬"]
    background = tk.Canvas(data["status"].display, width = 1280, height = 720, bg = "gray")

    reference = []

    background_image = Image.open(f"figure/event/summer_event/{name}.jpg")
    background_image = background_image.resize((1280, 720), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)
    background.create_image(0,0, anchor=tk.NW, image=background_image)
    reference.append(background_image)

    # peep = Image.open(f"figure/event/summer_event/peep.png")
    # peep = ImageTk.PhotoImage(peep)
    # background.create_image(0,0, anchor=tk.NW, image=peep)
    # reference.append(peep)

    text_box = Image.open(f"figure/text_box.png")
    text_box = text_box.resize((1180, 220), Image.ANTIALIAS)
    text_box = ImageTk.PhotoImage(text_box)
    background.create_image(50, 450, anchor=tk.NW, image=text_box)
    reference.append(text_box)

    background.image = reference

    background.create_rectangle(50, 450, 1230, 670, width = 5)

    # 傳入句子多長要換行和讀檔名稱
    read_data = read.read_event("暑假事件.txt")

    f = tk.font.Font(size = 30)

    text = []

    for i in range(len(read_data)): 
        if read_data[i] == name:
            index = i
            while True:
                if name == "低報酬":
                    text.append(read_data[index])
                    if index == len(read_data)-1:
                        break
                    index += 1
                else:
                    if read_data[index] == event_list[event_list.index(name)+1]:
                        break
                    else:
                        text.append(read_data[index])
                    index += 1
            break


    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: press_continue(background, nextButton, status, text))
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 670 - nextButton.winfo_reqheight() * 2)
    
    widget_now, next_line = show_widgets(background, nextButton, text, text[0], 0)
    status = [widget_now, next_line]


def show_ending_event(data, name):
    pass


def show_widgets(background, nextButton, text, text_now, index):
    f = tk.font.Font(size = 28)
    special_status = ["u", "v", "c", "1", "2", "3"]
    if text_now[0] in special_status:
        pass
    else:
        if len(text_now) > 32:
            text_now = read.rearrange(32, text_now)
        widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = text_now, anchor = "center", fill = "white", font = f)
    background.pack()
    if index + 1 == len(text):
        background.destroy()
        nextButton.destroy()
        ans = False



        # 在這裡呼叫更新能力值、評分值的函數




    else:
        ans = index + 1
    return widget, ans

def press_continue(background, nextButton, status, text):
    background.delete(status[0])

    status[0], status[1] = show_widgets(background, nextButton, text, text[status[1]], status[1])



