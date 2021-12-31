import function.read_file as read
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image


def process_event(data, events):
    data["event_processing"] = []
    for i in range(len(events)):
        try:
            data["event_processing"].append(events[i].split(":"))
        except:
            data["event_processing"].append(events[i])
    if data["event_processing"] != "排行程表":
        show_event(data, data["event_processing"][0][0], data["event_processing"][0][1])


def show_necessary_event(data, name):
    pass


def show_trigger_event(data, name):
    pass


def show_event(data, event_type, name):
    f = tk.font.Font(size = 30)

    data["choose_result"] = []

    background = tk.Canvas(data["status"].display, width = 1280, height = 720)

    reference = []

    background_image = Image.open(f"figure/event/{event_type}/{name}.jpg")
    background_image = background_image.resize((1280, 720), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)
    background.create_image(0,0, anchor=tk.NW, image=background_image)
    reference.append(background_image)

    text_box = Image.open(f"figure/text_box.png")
    text_box = text_box.resize((1180, 220), Image.ANTIALIAS)
    text_box = ImageTk.PhotoImage(text_box)
    background.create_image(50, 450, anchor=tk.NW, image=text_box)
    reference.append(text_box)
    background.create_rectangle(50, 450, 1230, 670, width = 5)

    # peep = Image.open(f"figure/event/summer_event/peep.png")
    # peep = peep.resize((400, 500), Image.ANTIALIAS)
    # peep = ImageTk.PhotoImage(peep, format="gif -index 2")
    # background.create_image(-20,235, anchor=tk.NW, image=peep)
    # reference.append(peep)

    # background.create_rectangle(350 - 50, 425 - 23, 350 + 50, 425 + 23, fill = "gray")
    # background.create_rectangle(350 - 50, 425 - 23, 350 + 50, 425 + 23, width = 5)
    # background.create_text(350, 425, text = "-長官-", anchor = "center", fill = "white", font = f)
    

    background.image = reference



    # 傳入事件類別與事件名稱
    text = read.read_event(event_type, name)

    # 處理特殊情況
    if event_type == "暑假事件" and name == "高報酬":
        for i in range(len(text)):
            if text[i][0] == "c":
                special_situation(data, event_type, name)
                text.pop(i)
                break

    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: press_continue(data, background, nextButton, reference, text_status, text, text_widget, image_widget))
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 670 - nextButton.winfo_reqheight() * 2)
    
    image_widget = []
    text_widget, next_line = show_widgets(data, background, nextButton, reference, text, text[0], 0, 0, image_widget)
    text_status = [text_widget, next_line]  # [文字工具, 指標]


def show_ending_event(data, name):
    pass


def show_widgets(data, background, nextButton, reference, text, text_now, index, text_widget, image_widget):
    f = tk.font.Font(size = 28)
    special_status = ["u", "v", "c", "1", "2", "3"]
    if text_now[0] in special_status:
        if text_now[0] == "v":
            text_widget = call_status_v(background, reference, text_now, image_widget)
        elif text_now[0] == "u":
            text_widget = call_status_u(background, reference, text_now, image_widget)
        elif text_now[0] == "c":
            text_widget = call_status_c(data, background, text, index, reference, text_widget, image_widget)
            nextButton.destroy()
        else:
            while text_now[0] != str(data["choose_result"][-1]):
                index += 1
                text_now = text[index]
                if index == len(text)-1:
                    break

    else:
        if len(text_now) > 34:  # 正常的斷行長度
            text_now = read.rearrange(32, text_now)
        text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = text_now, anchor = "center", fill = "white", font = f)
    background.image = reference
    background.pack()
    if index+1 == len(text):
        background.destroy()
        nextButton.destroy()
        index = False



        # 在這裡呼叫更新能力值、評分值的函數




    else:
        index += 1
    return text_widget, index


def press_continue(data, background, nextButton, reference, text_status, text, text_widget, image_widget):
    background.delete(text_status[0])
    for i in range(len(image_widget)):
        background.delete(image_widget[i])
    image_widget.clear()
    try:
        text_status[0], text_status[1] = show_widgets(data, background, nextButton, reference, text, text[text_status[1]], text_status[1], text_status[0], image_widget)
    except:
        text_status[0], text_status[1] = show_widgets(data, background, nextButton, reference, text, text[text_status[1]-1], text_status[1], text_status[0], image_widget)


def call_status_u(background, reference, text_now, image_widget):
    f = tk.font.Font(size = 30)
    name = "你"
    line = text_now.split(text_now[1])[1]

    name_box = Image.open(f"figure/text_box.png")
    name_box = name_box.resize((200 + 2*len(name), 46), Image.ANTIALIAS)
    name_box = ImageTk.PhotoImage(name_box)
    a = background.create_image(1230, 402, anchor=tk.NE, image=name_box)
    reference.append(name_box)
    b = background.create_rectangle(1030 - 2*len(name), 425 - 23, 1230, 425 + 23, width = 5)
    image_widget.append(a)
    image_widget.append(b)
    # background.create_rectangle(0, 425 - 23, 350 + 50, 425 + 23, fill = "gray")
    # background.create_rectangle(350 - 50, 425 - 23, 350 + 50, 425 + 23, width = 5)

    # peep = Image.open(f"figure/event/summer_event/peep.png")
    # peep = peep.resize((500, 500), Image.ANTIALIAS)
    # peep = ImageTk.PhotoImage(peep, format="gif -index 2")
    # c = background.create_image(-100,235, anchor=tk.NW, image=peep)
    # reference.append(peep)

    d = background.create_text(1130 - len(name), 425, text = f"-{name}-", anchor = "center", fill = "white", font = f)
    # image_widget.append(c)
    image_widget.append(d)

    if len(line) > 30:  # 有npc時的斷行長度
        line = read.rearrange(32, line)
    text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = line, anchor = "center", fill = "white", font = f)
    return text_widget


def call_status_v(background, reference, text_now, image_widget):
    f = tk.font.Font(size = 30)
    name = text_now.split(text_now[1])[1]
    line = text_now.split(text_now[1])[2]

    name_box = Image.open(f"figure/text_box.png")
    name_box = name_box.resize((400+ 2*len(name), 46), Image.ANTIALIAS)
    name_box = ImageTk.PhotoImage(name_box)
    a = background.create_image(50, 402, anchor=tk.NW, image=name_box)
    reference.append(name_box)
    b = background.create_rectangle(50, 425 - 23, 450+ 2*len(name), 425 + 23, width = 5)
    image_widget.append(a)
    image_widget.append(b)
    # background.create_rectangle(0, 425 - 23, 350 + 50, 425 + 23, fill = "gray")
    # background.create_rectangle(350 - 50, 425 - 23, 350 + 50, 425 + 23, width = 5)

    peep = Image.open(f"figure/event/人物/{name}.png")
    peep = peep.resize((500, 500), Image.ANTIALIAS)
    peep = ImageTk.PhotoImage(peep)
    c = background.create_image(-100,235, anchor=tk.NW, image=peep)
    reference.append(peep)

    d = background.create_text(385, 425, text = f"-{name}-", anchor = "center", fill = "white", font = f)
    image_widget.append(c)
    image_widget.append(d)

    if len(line) > 32:  # 有npc時的斷行長度
        line = read.rearrange(32, line)
    text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = line.strip("「」"), anchor = "center", fill = "white", font = f)
    return text_widget


def call_status_c(data, background, text, index, reference, text_widget, image_widget):
    f = tk.font.Font(size = 28)
    button_f = tk.font.Font(size = 36)
    line = text[index-1]

    if len(line) > 32:  # 正常的斷行長度
        line = read.rearrange(32, line)
    text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = line.strip("「」"), anchor = "center", fill = "white", font = f)

    text_now = text[index][2::].split(text[index][1])
    choose_button = []

    if len(text_now) == 2:
        output1 = meme_processor(text_now[0])
        output2 = meme_processor(text_now[1])
        button1 = tk.Button(data["status"].display, text = f"{text_now[0]}", relief = "raise", font = button_f, command = lambda: choose(data, choose_button, 1, output1, background, reference, text_widget, index, text, image_widget))
        button2 = tk.Button(data["status"].display, text = f"{text_now[1]}", relief = "raise", font = button_f, command = lambda: choose(data, choose_button, 2, output2, background, reference, text_widget, index, text, image_widget))
        choose_button.append(button1)
        choose_button.append(button2)
        button1.place(x = 1280 / 3 - button1.winfo_reqwidth()/2, y = 320 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 3 - button2.winfo_reqwidth()/2, y = 320 - button2.winfo_reqheight()/2)

    if len(text_now) == 3:
        output1 = meme_processor(text_now[0])
        output2 = meme_processor(text_now[1])
        output3 = meme_processor(text_now[0])
        button1 = tk.Button(data["status"].display, text = f"{text_now[0]}", relief = "raise", font = button_f, command = lambda: choose(data, choose_button, 1, output1, background, reference, text_widget, index, text, image_widget))
        button2 = tk.Button(data["status"].display, text = f"{text_now[1]}", relief = "raise", font = button_f, command = lambda: choose(data, choose_button, 2, output2, background, reference, text_widget, index, text, image_widget))
        button2 = tk.Button(data["status"].display, text = f"{text_now[2]}", relief = "raise", font = button_f, command = lambda: choose(data, choose_button, 3, output2, background, reference, text_widget, index, text, image_widget))
        choose_button.append(button1)
        choose_button.append(button2)
        choose_button.append(button3)
        button1.place(x = 1280 / 4 - button1.winfo_reqwidth()/2, y = 320 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 4 - button2.winfo_reqwidth()/2, y = 320 - button2.winfo_reqheight()/2)
        button3.place(x = 3 * 1280 / 4 - button2.winfo_reqwidth()/2, y = 320 - button2.winfo_reqheight()/2)

    return text_widget


def choose(data, choose_button, chosen, name, background, reference, text_widget, index, text, image_widget):
    f = tk.font.Font(size = 30)
    data["choose_result"].append(chosen)
    background.delete(text_widget)
    text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = name, anchor = "center", fill = "white", font = f)
    print(data["choose_result"])
    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: press_continue(data, background, nextButton, reference, text_status, text, text_widget, image_widget))
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 670 - nextButton.winfo_reqheight() * 2)
    for button in choose_button:
        button.destroy()
    text_widget, next_line = show_widgets(data, background, nextButton, reference, text, text[index+1], index+1, text_widget, image_widget)
    text_status = [text_widget, next_line]  # [文字工具, 指標]


def meme_processor(line):
    special_meme_translation = {"不要":"不要啦，哪次要"}
    if line in special_meme_translation:
        line = special_meme_translation[line]
    else:
        line = f"{line}啦，哪次不{line}"
    return line


def special_situation(data, event_type, name):
    if event_type == "暑假事件" and name == "高報酬":
        i = 2  # 按照主辦方的機率分配
        data["choose_result"].append(i)