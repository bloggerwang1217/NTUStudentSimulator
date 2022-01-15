import function.read_file as read
import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image
import function.status as status
import function.schedule as sch
import function.sound_effect as sound
import function.course_selection as cs
import system.ending as ending


reach_event_type, reach_name = "", ""

def process_event(data, events):
    data["event_processing"] = []
    data["event_processing"].clear()
    for i in range(len(events)):
        try:
            data["event_processing"].append(events[i].split(":"))
        except:
            data["event_processing"].append([events[i]])
    if data["event_processing"][0][0] == "第一次排行程表" or data["event_processing"][0][0] == "第二次排行程表" or data["event_processing"][0][0] == "第三次排行程表" or data["event_processing"][0][0] == "第四次排行程表":
        sch.get_new_schedule(data["status"].display, data["picked_course"], data, False)
    elif data["event_processing"][0][0] == "期中考":
        data["status"].midterm(data["picked_course"], data)
    elif data["event_processing"][0][0] == "期末考":
        data["status"].final_exam(data["picked_course"], data)
    else:
        show_event(data, data["event_processing"][0][0], data["event_processing"][0][1])


def show_event(data, event_type, name):
    global reach_event_type, reach_name
    reach_event_type, reach_name = event_type, name

    f = tk.font.Font(size = 30)

    data["choose_result"] = []

    background = tk.Canvas(data["status"].display, width = 1280, height = 720)

    reference = []

    sound.play_event_background_music(event_type, name)
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

    background.image = reference

    # 傳入事件類別與事件名稱
    text = read.read_event(event_type, name)

    # 處理主人公名稱
    if (event_type == "必然事件" and name == "聯誼") or (event_type == "中途結束事件" and name == "明明是我先來的") or (event_type == "中途結束事件" and name == "轉生異世界") or (event_type == "必然事件" and name == "系隊"):
        for i in range(len(text)):
            if "{}" in text[i]:
                text[i] = f"{data['name']}".join(text[i].split("{}"))

    # 處理成就
    if name == "虛擬貨幣":
        data["status"].achievement.stocks_surfing += 1
    elif name == "翹課打ㄆ":
        data["status"].achievement.number_of_sex += 1
    elif name == "懷孕":
        data["status"].achievement.birth = True

    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: [press_continue(data, background, nextButton, reference, text_status, text, text_widget, image_widget), sound.play_button_sound()])
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 670 - nextButton.winfo_reqheight() * 2)
    
    image_widget = []
    text_widget, next_line = show_widgets(data, background, nextButton, reference, text, text[0], 0, 0, image_widget)
    text_status = [text_widget, next_line]  # [文字工具, 指標]


def show_widgets(data, background, nextButton, reference, text, text_now, index, text_widget, image_widget):
    global reach_name

    f = tk.font.Font(size = 28)
    special_status = ["u", "v", "c", "d"]
    if text_now[0] in special_status:
        if text_now[0] == "v":
            text_widget = call_status_v(background, reference, text_now, image_widget)
        elif text_now[0] == "u":
            text_widget = call_status_u(background, reference, text_now, image_widget)
        elif text_now[0] == "c":
            text_widget = call_status_c(data, background, text, index, reference, text_widget, image_widget)
            nextButton.destroy()
        elif text_now[0] == "d":
            special_situation(data, reach_event_type, reach_name, text, index)
            text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = "...", anchor = "center", fill = "white", font = f)
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

        # 更新能力值、評分值+呼叫下個事件
        
        if data["event_processing"][0][0] == "中途結束事件" or data["event_processing"][0][0] == "破關":
            ending.show_ending_graph(data["status"].display, data)
        elif data["event_processing"][0][0] == "暑假事件":
            status.event_adjust(data["status"], reach_name, data["choose_result"])
            cs.course_selection(data["status"].display, data)
        else:
            end = status.event_adjust(data["status"], reach_name, data["choose_result"])
            if end == "阿姨":
                process_event(data, ["中途結束事件:阿姨結束"])
            data["event_processing"].remove(data["event_processing"][0])
            if len(data["event_processing"]) == 1:
                if data["event_processing"][0][0] == "第二次排行程表" or data["event_processing"][0][0] == "第三次排行程表" or data["event_processing"][0][0] == "第四次排行程表":
                    process_event(data, data["event_processing"][0])
                elif data["event_processing"][0][0] == "期中考":
                    data["status"].midterm(data["picked_course"], data)
                elif data["event_processing"][0][0] == "期末考":
                    data["status"].final_exam(data["picked_course"], data)
            else:
                show_event(data, data["event_processing"][0][0], data["event_processing"][0][1])

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
    name_f = tk.font.Font(size = 30)
    f = tk.font.Font(size = 28)
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

    c = background.create_text(1130 - len(name), 425, text = f"-{name}-", anchor = "center", fill = "white", font = name_f)
    image_widget.append(c)

    if len(line) > 32:  # 自己說話時的斷行長度
        line = read.rearrange(32, line)
    text_widget = background.create_text(background.winfo_reqwidth()/2, 3 * background.winfo_reqheight()/4, text = line, anchor = "center", fill = "white", font = f)
    return text_widget


def call_status_v(background, reference, text_now, image_widget):
    name_f = tk.font.Font(size = 30)
    f = tk.font.Font(size = 28)
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

    peep = Image.open(f"figure/event/人物/{name}.png")
    peep = peep.resize((500, 500), Image.ANTIALIAS)
    peep = ImageTk.PhotoImage(peep)
    c = background.create_image(-100,235, anchor=tk.NW, image=peep)
    reference.append(peep)

    d = background.create_text(385, 425, text = f"-{name}-", anchor = "center", fill = "white", font = f)
    image_widget.append(c)
    image_widget.append(d)

    if len(line) > 20:  # 有npc時的斷行長度
        line = read.rearrange(20, line)
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
        button1 = tk.Button(data["status"].display, text = f"{text_now[0]}", relief = "raise", font = button_f, command = lambda: [choose(data, choose_button, 1, output1, background, reference, text_widget, index, text, image_widget), sound.play_button_sound()])
        button2 = tk.Button(data["status"].display, text = f"{text_now[1]}", relief = "raise", font = button_f, command = lambda: [choose(data, choose_button, 2, output2, background, reference, text_widget, index, text, image_widget), sound.play_button_sound()])
        choose_button.append(button1)
        choose_button.append(button2)
        button1.place(x = 1280 / 3 - button1.winfo_reqwidth()/2, y = 320 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 3 - button2.winfo_reqwidth()/2, y = 320 - button2.winfo_reqheight()/2)

    elif len(text_now) == 3:
        output1 = meme_processor(text_now[0])
        output2 = meme_processor(text_now[1])
        output3 = meme_processor(text_now[2])
        button1 = tk.Button(data["status"].display, text = f"{text_now[0]}", relief = "raise", font = button_f, command = lambda: [choose(data, choose_button, 1, output1, background, reference, text_widget, index, text, image_widget), sound.play_button_sound()])
        button2 = tk.Button(data["status"].display, text = f"{text_now[1]}", relief = "raise", font = button_f, command = lambda: [choose(data, choose_button, 2, output2, background, reference, text_widget, index, text, image_widget), sound.play_button_sound()])
        button3 = tk.Button(data["status"].display, text = f"{text_now[2]}", relief = "raise", font = button_f, command = lambda: [choose(data, choose_button, 3, output3, background, reference, text_widget, index, text, image_widget), sound.play_button_sound()])
        choose_button.append(button1)
        choose_button.append(button2)
        choose_button.append(button3)
        button1.place(x = 1280 / 4 - button1.winfo_reqwidth()/2, y = 320 - button1.winfo_reqheight()/2)
        button2.place(x = 2 * 1280 / 4 - button2.winfo_reqwidth()/2, y = 320 - button2.winfo_reqheight()/2)
        button3.place(x = 3 * 1280 / 4 - button3.winfo_reqwidth()/2, y = 320 - button3.winfo_reqheight()/2)

    return text_widget


def choose(data, choose_button, chosen, name, background, reference, text_widget, index, text, image_widget):
    f = tk.font.Font(size = 30)
    data["choose_result"].append(chosen)
    background.delete(text_widget)
    
    nextButton = tk.Button(data["status"].display, text = "繼續", relief = "raise", font = f, command = lambda: [press_continue(data, background, nextButton, reference, text_status, text, text_widget, image_widget), sound.play_button_sound()])
    nextButton.place(x = 1230 - nextButton.winfo_reqwidth() * 2, y = 670 - nextButton.winfo_reqheight() * 2)
    for button in choose_button:
        button.destroy()

    shrinker(data, text, index, name)

    text_widget, next_line = show_widgets(data, background, nextButton, reference, text, text[index+1], index+1, text_widget, image_widget)
    text_status = [text_widget, next_line]  # [文字工具, 指標]


def shrinker(data, text, index, name):  #index:c出現的位置；若為數值判定，則為c出現前一個
    option_dict = {"1":{1:"1", 2:"2", 3:"3"}, "A":{1: "A", 2: "B", 3: "C"}, "a":{1: "a", 2:"b", 3:"c"}, "甲":{1: "甲", 2: "乙", 3:"丙"}, "子":{1: "子", 2: "丑", 3:"寅"}}
    option_type = text[index+1][0]
    temp_index = index + 1
    ans = option_dict[option_type][data["choose_result"][-1]]
    while True:
        if text[temp_index] == ans:
            text.pop(temp_index)
            text.insert(temp_index, name)
            temp_index += 1
            while len(text[temp_index]) != 1 or (len(text[temp_index]) == 1 and (not text[temp_index] in option_dict[option_type].values())):
                temp_index += 1
            for i in range(len(text)-1, temp_index-1, -1):
                text.pop(i)
            break
        elif text[temp_index] != ans and len(text[temp_index]) == 1 and text[temp_index] in option_dict[option_type].values():
            while text[temp_index] != ans:
                text.pop(temp_index)
            text.pop(temp_index)
            text.insert(temp_index, name)
            break
    try:
        if option_dict[option_type][3] in text:
            for i in range(len(text)-1, text.index(option_dict[option_type][3])-1, -1):
                text.pop(i)
    except:
        pass


def meme_processor(line):
    special_meme_translation = {"不要":"不要啦，哪次要", "有":"有啦，哪次沒有", "沒有":"沒有啦，哪次有", "不好":"不好啦，哪次好"}
    if line in special_meme_translation:
        line = special_meme_translation[line]
    else:
        line = f"{line}啦，哪次不{line}"
    return line


def special_situation(data, event_type, name, text, index):
    if event_type == "暑假事件" and name == "虛擬貨幣":
        for i in range(len(text)):
            if text[i][0] == "d":
                if data["status"].luck >= 95:
                    data["choose_result"].append(1)
                else:
                    data["choose_result"].append(2)

    elif event_type == "觸發事件" and name == "第一次約會":
            for i in range(len(text)):
                if text[i][0] == "d":
                    if data["choose_result"][-1] == 1:
                        if data["status"].charm >= 50:
                            data["choose_result"].append(1)
                        else:
                            data["choose_result"].append(2)
                    elif data["choose_result"][-1] == 2:
                        if data["status"].luck < 20:
                            data["choose_result"].append(1)
                        else:
                            data["choose_result"].append(2)
                    break
            if data["choose_result"][0] == 1:
                shrinker(data, text, index, "（這肯定很看你的魅力的）")
            elif data["choose_result"][0] == 2:
                shrinker(data, text, index, "（賭一把了）")
    elif event_type == "必然事件":
        if name == "實習":
            for i in range(len(text)):
                if text[i][0] == "d":
                    if data["status"].luck >= 95:
                        data["choose_result"].append(1)
                    else:
                        data["choose_result"].append(2)
            shrinker(data, text, index, "（賭一把了）")
        elif name == "聯誼":
            for i in range(len(text)):
                if text[i][0] == "d":
                    if data["status"].charm >= 90:
                        data["choose_result"].append(1)
                    else:
                        data["choose_result"].append(2)
                    break
            shrinker(data, text, index, "（同學們的反應就很看你的魅力的表現囉）")
        elif name == "系學會":
            for i in range(len(text)):
                if text[i][0] == "d":
                    if data["choose_result"][-1] == 1:
                        if data["status"].wisdom >= 85:
                            data["choose_result"].append(1)
                        else:
                            data["choose_result"].append(2)
            shrinker(data, text, index, "（看看你多精明吧）")
        elif name == "舞會1-男":
            for i in range(len(text)):
                if text[i][0] == "d":
                    if len(data["choose_result"]) == 0:
                        if data["status"].charm < 60:
                            data["choose_result"].append(1)
                        else:
                            data["choose_result"].append(2)
                        shrinker(data, text, index, "（邀不邀的到異性舞伴間看你的魅力了！）")
                    elif len(data["choose_result"]) == 2:
                        if data["choose_result"][-1] == 1 and data["choose_result"][-2] == 1:
                            if data["status"].charm >= 80 and data["status"].luck >= 20:
                                data["choose_result"].append(1)
                            else:
                                data["choose_result"].append(2)
                            shrinker(data, text, index, "（看你的魅力和運氣囉）")
                        elif data["choose_result"][-1] == 2 and data["choose_result"][-2] == 2:
                            if data["status"].charm >= 70 and data["status"].luck >= 20:
                                data["choose_result"].append(1)
                            else:
                                data["choose_result"].append(2)
                            shrinker(data, text, index, "（看你的魅力和運氣囉）")
                    break