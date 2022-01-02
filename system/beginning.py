import tkinter as tk
from tkinter import font 
from PIL import ImageTk, Image
import function.read_file as read
import function.初始能力值設定 as init_abi
import function.結算能力值圖片產生 as graph_abi
import function.course_selection as cs
import function.status as status
import function.sound_effect as sound

def press_start_game(start_scene, start_button, name_list, window, data):

    sound.play_button_sound()
    sound.play_background_music("閱讀信封場景")

    start_scene.destroy()
    start_button.destroy()
    name_list.destroy()
    beginning_story(window, data)


def start_game(window, data):

    sound.play_background_music("封面背景音樂")

    f = tk.font.Font(size = 28)

    beginning = Image.open("figure/beginning.png")
    beginning = beginning.resize((1280, 720), Image.ANTIALIAS)
    beginning = ImageTk.PhotoImage(beginning)

    start_scene = tk.Label(window, image = beginning)
    start_scene.image = beginning
    start_scene.pack(fill = "both")

    name_list = tk.Label(window, text = "製作者：王敏行、劉健榮、羅士軒、陳利煌、周匯森、何峻德", font = f)
    name_list.place(x = 640-name_list.winfo_reqwidth()/2, y = 660)

    start_button = tk.Button(window, text = "開始遊戲",width = 7, font = f, command = lambda: press_start_game(start_scene, start_button, name_list, window, data))
    start_button.place(x = 640-start_button.winfo_reqwidth()/2, y = 300)


def beginning_story(window, data):

    f = tk.font.Font(size = 42)

    # window.configure(bg="white")
    night = Image.open("figure/night.png")
    # night = night.resize((1280, 720), Image.ANTIALIAS) 
    night = ImageTk.PhotoImage(night)
    background = tk.Label(window, image = night)
    background.image = night
    background.pack()

    back_room_button = tk.Button(window, text = "回書房開信", font = f, relief = "solid", command = lambda: press_back_room_button(window, background, back_room_button, data))
    back_room_button.place(x = 880, y = 500)


def press_back_room_button(window, background, back_room_button, data):

    sound.play_button_sound()

    background.destroy()
    back_room_button.destroy()
    input_basic_data(window, data)


def input_basic_data(window, data):

    f = tk.font.Font(size = 32)
    check_f = tk.font.Font(size = 16)

    widgets = []

    desk = Image.open("figure/desk_texture.jpeg")
    desk = desk.resize((1280, 720), Image.ANTIALIAS)
    desk = ImageTk.PhotoImage(desk)
    back_ground = tk.Label(window, image = desk)
    back_ground.image = desk
    back_ground.pack()
    widgets.append(back_ground)

    letter_of_admission = Image.open("figure/letter_of_admission.png")
    letter_of_admission = letter_of_admission.resize((829, 600), Image.ANTIALIAS)
    letter_of_admission = ImageTk.PhotoImage(letter_of_admission)
    letter = tk.Label(window, image = letter_of_admission)
    letter.image = letter_of_admission
    letter.place(x = 490-letter.winfo_reqwidth()/2, y = 470-letter.winfo_reqwidth()/2)
    widgets.append(letter)

    # TextBox Creation
    description = tk.Label(window, text = "姓名輸入（無法顯示注音，但仍可方向鍵選字）")
    description.place(x = 450-description.winfo_reqwidth()/2, y = 265)
    widgets.append(description)

    inputtxt = tk.Text(window,
                       height = 1,
                       width = 10,
                       font = f)
    inputtxt.config(highlightthickness=2, highlightbackground="black")
    inputtxt.place(x = 450-inputtxt.winfo_reqwidth()/2, y = 290)
    widgets.append(inputtxt)

    after_imputtxt = tk.Label(window, text = "同學       收", font = f)
    after_imputtxt.place(x = 510+after_imputtxt.winfo_reqwidth()/2, y = 290)
    widgets.append(after_imputtxt)

    white = Image.open("figure/white.png")
    white = white.resize((200, 280), Image.ANTIALIAS)
    white = ImageTk.PhotoImage(white)
    small_bg = tk.Label(window, image = white, highlightthickness=2, highlightbackground="black")
    small_bg.image = white
    small_bg.place(x = 975, y = 200)
    widgets.append(small_bg)

    confirmation = tk.Label(window, text = "資料確認", font = f)
    confirmation.place(x = 975+small_bg.winfo_reqwidth()/2-confirmation.winfo_reqwidth()/2, y = 225)
    widgets.append(confirmation)

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text="男性",font = check_f, variable=var1, onvalue=1, offvalue=0, command = sound.play_button_sound)
    c1.place(x = 1000, y = 290)
    c2 = tk.Checkbutton(window, text='女性',font = check_f, variable=var2, onvalue=1, offvalue=0, command = sound.play_button_sound)
    c2.place(x = 1100, y = 290)
    widgets.append(c1)
    widgets.append(c2)

    # Label Creation
    lbl = tk.Label(window)
    lbl.place(x = 992, y = 363)
    widgets.append(lbl)

    # Button Creation
    endButton = tk.Button(window,
            text = "結束",
            font = check_f, 
            command = lambda : [end_input(window, data, widgets), sound.play_button_sound()])
    widgets.append(endButton)

    printButton = tk.Button(window,
                            text = "確認",
                            font = check_f, 
                            command = lambda: [save_input(data, var1, var2, inputtxt, lbl, window, endButton, check_f, small_bg.winfo_reqwidth()), sound.play_button_sound()])
    printButton.place(x = 975+small_bg.winfo_reqwidth()/2-printButton.winfo_reqwidth()/2, y = 330)
    widgets.append(printButton)


def save_input(data, var1, var2, inputtxt, lbl, frame, endButton, check_f, length):
    sex = ""
    if (var1.get() + var2.get() == 1) and inputtxt.get(1.0, "end-1c") != "":        
        if (var1.get() == 1) and (var2.get() == 0):
            sex = "男性"
        elif (var1.get() == 0) & (var2.get() == 1):
            sex =  "女性"
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = f"您的名字是\n「{inp}」\n{sex}\n不想重新輸入請按結束", font=check_f)
        endButton.place(x = 975+length/2-endButton.winfo_reqwidth()/2, y = 450)

    else:
        if inputtxt.get(1.0, "end-1c") == "":
            lbl.config(text = f"          請輸入姓名", font=check_f)
            endButton.place_forget() 
        else:
            inp = inputtxt.get(1.0, "end-1c")
            lbl.config(text = f"您的名字是\n「{inp}」\n請苟選一個最認同的性別", font=check_f)
            endButton.place_forget()
    data["sex"] = sex
    data["name"] = inp


def end_input(window, data, widgets):

    for widget in widgets:
        widget.destroy()
    read_letter(window, data)


def read_letter(window, data):

    # sound.play_button_sound()

    desk = Image.open("figure/desk_texture.jpeg")
    desk = desk.resize((1280, 720), Image.ANTIALIAS)
    desk = ImageTk.PhotoImage(desk)
    background = tk.Label(window, image = desk)
    background.image = desk
    background.pack()

    white = Image.open("figure/white.png")
    white = white.resize((960, 690), Image.ANTIALIAS)
    white = ImageTk.PhotoImage(white)
    small_bg = tk.Label(window, image = white, highlightthickness=2, highlightbackground="black")
    small_bg.image = white
    small_bg.place(x = 640-small_bg.winfo_reqwidth()/2, y = 10)

    title_f = tk.font.Font(size = 36)
    subtitle_f = tk.font.Font(size = 32)
    f = tk.font.Font(size = 20)

    # 傳入句子多長要換行和讀檔名稱
    read_data = read.read_file(41, "beginning1.txt")
    read_data.insert(0, f"受文者：{data['name']}")
    read_data.insert(0, "國立臺灣大學學士班新生入學通知書")

    text = []
    for i in range(len(read_data)): 
        if i == 0:
            text.append(tk.Label(window, text = read_data[i],fg = "black", font = title_f))
        elif i == 1:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = subtitle_f))
        else:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))

        if i == 0:
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 25)
        elif i == 1:
            text[i].place(x = 220, y = 100)
        else:
            text[i].place(x = 220, y = 100 + text[i].winfo_reqheight() * i)

    flip_button = tk.Button(window, text = "翻面", font = f, command = lambda: press_flip_button(window, data, text, background, small_bg))
    flip_button.place(x = 1000, y = 625)

    text.append(flip_button)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除

    
def press_flip_button(window, data, used_widgets, widget1, widget2):

    sound.play_button_sound()

    for widget in used_widgets:
        widget.destroy()
    
    f = tk.font.Font(size = 20)

    read_data = read.read_file(45, "beginning2.txt")

    text = []
    for i in range(len(read_data)): 
        if i == 0:
            text.append(tk.Label(window, text = read_data[i],fg = "black", font = f))
        elif i == 1:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))
        else:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))

        if i == 0:
            text[i].place(x = 180, y = 30)
        else:
            text[i].place(x = 180, y = 30 + text[i].winfo_reqheight() * i)

    check_ability_button = tk.Button(window, text = "你發現信封裡還有其他東西...", font = f, command = lambda: press_check_ability_button(window, data, text, widget1, widget2))
    check_ability_button.place(x = 800, y = 620)

    text.append(check_ability_button)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除


def press_check_ability_button(window, data, used_widgets, widget1, widget2):

    sound.play_button_sound()

    for widget in used_widgets:
        widget.destroy()
    
    title_f = tk.font.Font(size = 36)
    f = tk.font.Font(size = 20)

    read_data = ["各項能力檢驗量表"]
    read_data.append("下面是你各項能力值的分佈，你有四年的時間好好培養，期待你的表現")

    text = []
    for i in range(len(read_data)): 
        if i == 0:
            text.append(tk.Label(window, text = read_data[i],fg = "black", font = title_f))
        elif i == 1:
            text.append(tk.Label(window, text = read_data[i].strip("\n"),fg = "black", font = f))

        if i == 0:
            text[i].place(x = 640 - text[i].winfo_reqwidth()/2, y = 25)
        elif i == 1:
            text[i].place(x = 220, y = 100)


    # 在這邊初始化status，並且貼上初始化能力值的圖
    wisdom, charm, fitness, social, health, luck = init_abi.ininial_set()
    data["status"] = status.Status(wisdom, charm, fitness, social, health, luck, read.read_course(), window)
    time = graph_abi.abi_illu(wisdom, charm, fitness, social, health)
    ability_graph = Image.open(f"figure/ability/{time}.png")
    ability_graph = ImageTk.PhotoImage(ability_graph)
    ability = tk.Label(window, image = ability_graph)
    ability.image = ability_graph
    ability.place(x = 640 - widget2.winfo_reqwidth()/2.3, y = 140)
    

    go_course_selecting_button = tk.Button(window, text = "進入選課系統選課囉！", font = f, command = lambda: press_go_course_selecting_button(window, data, text))
    go_course_selecting_button.place(x = 850, y = 620)

    text.append(widget1)
    text.append(widget2)
    text.append(go_course_selecting_button)
    text.append(ability)
    # 現在text裡有目前所有要清掉的widgets，按按鈕後一次清除

def press_go_course_selecting_button(window, data, used_widgets):
    sound.enter_game_button_sound()

    sound.play_background_music("正式遊戲背景音樂")

    for widget in used_widgets:
        widget.destroy()
    cs.course_selection(window, data)

