import tkinter as tk
from PIL import ImageTk, Image

def press_start_game(start_scene, start_button, name_list, window, data):
    start_scene.destroy()
    start_button.destroy()
    name_list.destroy()
    beginning_story(window, data)


def start_game(window, data):

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
    f = tk.font.Font(size = 48, family = "lihsianti")

    window.configure(bg="white")

    text = [0, 1]  # 加入開場說明文字或圖片
    text[0] = tk.Label(window, text = "你終於進入了理想中的大學\n台大\n帶著既期待又怕受傷害的心情\n你準備迎向這四年未知的生活...", font = f)
    text[1] = tk.Label(window, text = "我為什麼在這裡", font = f)
    text[0].place(x = 300, y = 100)

    index = [0]
    next_button = tk.Button(window, text = "下一頁",width = 6, font = f, command = lambda: press_next_button(window, text, next_button, index, data))
    next_button.place(x = 1000, y = 500)

    
def press_next_button(window, text, next_button, index, data):
    f = tk.font.Font(size = 32)
    if index[0] == len(text)-1:
        text[index[0]].destroy()
        next_button.destroy()
        # 呼叫輸入姓名函式
        input_basic_data(window, data)
        return
    text[index[0]].destroy()
    text[index[0]+1].place(x = 300, y = 100)
    index[0] += 1


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
    confirmation.place(x = 1013, y = 225)
    widgets.append(confirmation)

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text="男性",font = check_f, variable=var1, onvalue=1, offvalue=0)
    c1.place(x = 1000, y = 290)
    c2 = tk.Checkbutton(window, text='女性',font = check_f, variable=var2, onvalue=1, offvalue=0)
    c2.place(x = 1100, y = 290)
    widgets.append(c1)
    widgets.append(c2)

    # Label Creation
    lbl = tk.Label(window)
    lbl.place(x = 987, y = 365)
    widgets.append(lbl)

    # Button Creation
    endButton = tk.Button(window,
            text = "結束",
            font = check_f, 
            command = lambda :end_input(window, data, widgets))
    widgets.append(endButton)

    printButton = tk.Button(window,
                            text = "確認",
                            font = check_f, 
                            command = lambda: save_input(data, var1, var2, inputtxt, lbl, window, endButton, check_f))
    printButton.place(x = 1057, y = 330)
    widgets.append(printButton)

def save_input(data, var1, var2, inputtxt, lbl, frame, endButton, check_f):
    sex = ""
    if (var1.get() + var2.get() == 1) and inputtxt.get(1.0, "end-1c") != "":        
        if (var1.get() == 1) and (var2.get() == 0):
            sex = "男性"
        elif (var1.get() == 0) & (var2.get() == 1):
            sex =  "女性"
        inp = inputtxt.get(1.0, "end-1c")
        lbl.config(text = f"  您的名字是「{inp}」\n{sex}\n  不想重新輸入請按結束", font=check_f)
        endButton.place(x = 1057, y = 430)

    else:
        if inputtxt.get(1.0, "end-1c") == "":
            lbl.config(text = f"           請輸入姓名", font=check_f)
            endButton.place_forget() 
        else:
            inp = inputtxt.get(1.0, "end-1c")
            lbl.config(text = f" 您的名字是「{inp}」\n請苟選一個最認同的性別", font=check_f)
            endButton.place_forget()
    data["sex"] = sex
    data["name"] = inp


def end_input(window, data, widgets):
    for widget in widgets:
        widget.destroy()
    print(data)
    # 呼叫選課