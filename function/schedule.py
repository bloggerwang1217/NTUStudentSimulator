import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import function.status as status
import function.check_event_trigger as check
import function.sound_effect as sound
import sys

if sys.platform == "darwin":
    f = tkFont.Font(size = 24)
    title_f = tkFont.Font(size = 48)
    week_f = tkFont.Font(size = 16)
    money_f = tk.font.Font(size = 30)
    abi_f = tk.font.Font(size = 24)
    text_f = tkFont.Font(size = 20)
    button_f = tkFont.Font(size = 24)
else:
    f = tkFont.Font(size = 16)
    title_f = tkFont.Font(size = 40)
    week_f = tkFont.Font(size = 8)
    money_f = tk.font.Font(size = 22)
    abi_f = tk.font.Font(size = 16)
    text_f = tkFont.Font(size = 12)
    button_f = tkFont.Font(size = 16)


class Schedule:

    def __init__(self, classes, picked, options):
        self.classes = classes
        self.picked = picked
        self.options = options
        self.result = {}


    def createWidgets(self, window, data):
        widgets = []
        clicked = []
        options = []
        class_time = list(self.classes.keys())
        # datatype of menu text and initial menu text
        for i in range(4):
            clicked.append([])
            options.append([])
            for j in range(5):
                clicked_item = tk.StringVar()
                clicked[i].append(clicked_item)
                clicked[i][j].set(self.picked[f"{j+1}-{i+1}"])
                if f"{j+1}-{i+1}" in class_time:
                    options[i].append([self.classes[f"{j+1}-{i+1}"]])
                else:
                    options[i].append(self.options)

        schedule = Image.open("figure/schedule.png")
        schedule = schedule.resize((916,480), Image.ANTIALIAS)
        schedule = ImageTk.PhotoImage(schedule)
        background = tk.Label(window, image = schedule)
        widgets.append(background)

        if sys.platform == "darwin":
            MonLabel = tk.Label(window, text = " ζζδΈ ", font = week_f, bg = "#3895b9", fg = "white")
            TueLabel = tk.Label(window, text = " ζζδΊ ", font = week_f, bg = "#3895b9", fg = "white")
            WedLabel = tk.Label(window, text = " ζζδΈ ", font = week_f, bg = "#3895b9", fg = "white")
            ThuLabel = tk.Label(window, text = " ζζε ", font = week_f, bg = "#3895b9", fg = "white")
            FriLabel = tk.Label(window, text = " ζζδΊ ", font = week_f, bg = "#3895b9", fg = "white")
            widgets.append(MonLabel)
            widgets.append(TueLabel)
            widgets.append(WedLabel)
            widgets.append(ThuLabel)
            widgets.append(FriLabel)

        MorningLabel = tk.Label(window, text = "ζ©δΈ", height = 1, width = 4, font = f, bg= "#eeefee")
        MonMorningList = tk.OptionMenu(window, clicked[0][0], *options[0][0])
        MonMorningList.config(bg = "#eeefee")
        TueMorningList = tk.OptionMenu(window, clicked[0][1], *options[0][1])
        TueMorningList.config(bg = "#eeefee")
        WedMorningList = tk.OptionMenu(window, clicked[0][2], *options[0][2])
        WedMorningList.config(bg = "#eeefee")
        ThuMorningList = tk.OptionMenu(window, clicked[0][3], *options[0][3])
        ThuMorningList.config(bg = "#eeefee")
        FriMorningList = tk.OptionMenu(window, clicked[0][4], *options[0][4])
        FriMorningList.config(bg = "#eeefee")
        widgets.append(MorningLabel)
        widgets.append(MonMorningList)
        widgets.append(TueMorningList)
        widgets.append(WedMorningList)
        widgets.append(ThuMorningList)
        widgets.append(FriMorningList)

        AfternoonLabel = tk.Label(window, text = "δΈε", height = 1, width = 4, font = f)
        MonAfternoonList = tk.OptionMenu(window, clicked[1][0], *options[1][0])
        TueAfternoonList = tk.OptionMenu(window, clicked[1][1], *options[1][1])
        WedAfternoonList = tk.OptionMenu(window, clicked[1][2], *options[1][2])
        ThuAfternoonList = tk.OptionMenu(window, clicked[1][3], *options[1][3])        
        FriAfternoonList = tk.OptionMenu(window, clicked[1][4], *options[1][4])
        widgets.append(AfternoonLabel)
        widgets.append(MonAfternoonList)
        widgets.append(TueAfternoonList)
        widgets.append(WedAfternoonList)
        widgets.append(ThuAfternoonList)
        widgets.append(FriAfternoonList)

        EveningLabel = tk.Label(window, text = "ζδΈ", height = 1, width = 4, font = f, bg= "#eeefee")
        MonEveningList = tk.OptionMenu(window, clicked[2][0], *options[2][0])
        MonEveningList.config(bg = "#eeefee")
        TueEveningList = tk.OptionMenu(window, clicked[2][1], *options[2][1])
        TueEveningList.config(bg = "#eeefee")
        WedEveningList = tk.OptionMenu(window, clicked[2][2], *options[2][2])
        WedEveningList.config(bg = "#eeefee")
        ThuEveningList = tk.OptionMenu(window, clicked[2][3], *options[2][3])
        ThuEveningList.config(bg = "#eeefee")
        FriEveningList = tk.OptionMenu(window, clicked[2][4], *options[2][4])
        FriEveningList.config(bg = "#eeefee")
        widgets.append(EveningLabel)
        widgets.append(MonEveningList)
        widgets.append(TueEveningList)
        widgets.append(WedEveningList)
        widgets.append(ThuEveningList)
        widgets.append(FriEveningList)

        MidnightLabel = tk.Label(window, text = "εε€", height = 1, width = 4, font = f)
        MonMidnightList = tk.OptionMenu(window, clicked[3][0], *options[3][0])
        TueMidnightList = tk.OptionMenu(window, clicked[3][1], *options[3][1])
        WedMidnightList = tk.OptionMenu(window, clicked[3][2], *options[3][2])
        ThuMidnightList = tk.OptionMenu(window, clicked[3][3], *options[3][3])
        FriMidnightList = tk.OptionMenu(window, clicked[3][4], *options[3][4])
        widgets.append(MidnightLabel)
        widgets.append(MonMidnightList)
        widgets.append(TueMidnightList)
        widgets.append(WedMidnightList)
        widgets.append(ThuMidnightList)
        widgets.append(FriMidnightList)

        FinishButton = tk.Button(window, text ="ε?ζ", height = 1, width = 4, font = f, command = lambda: [self.save(clicked, self.result, data, widgets, FinishButton, moneyLabel, abilityLabel), sound.play_button_sound()])

        title = tk.Label(window, text = "δ½ ηζιθ‘¨" ,font = title_f, bg = "#eeefee", fg = "#712322")
        subtitle1 = tk.Label(window, text = "#ζιζ²ζζΆε€±οΌ", font = f, bg = "#eeefee")
        subtitle2 = tk.Label(window, text = "  εͺζ―θ?ζδ½ εζ­‘ηζ¨£ε­", font = f, bg = "#eeefee")
        subtitle3 = tk.Label(window, text = f"#ιζ―δ½ ιεε­Έζ", font = f, bg = "#eeefee")
        widgets.append(title)
        widgets.append(subtitle1)
        widgets.append(subtitle2)
        widgets.append(subtitle3)

        schedule_time = data['previous_event']
        if schedule_time == "ζδΈ­θ":
            schedule_time = "η¬¬δΈζ¬‘ζθ‘η¨θ‘¨"

        subtitle4 = tk.Label(window, text = f"  {schedule_time[0:2]}εζ", font = f, bg = "#eeefee")
        widgets.append(subtitle4)

        background.image = schedule
        background.place(x=0, y=0)


        if sys.platform == "darwin":
            MonLabel.place(x=150, y=8)
            TueLabel.place(x=315, y=8)
            WedLabel.place(x=478, y=8)
            ThuLabel.place(x=642, y=8)
            FriLabel.place(x=807, y=8)

        MorningLabel.place(x=20, y=100)
        MonMorningList.place(x=155, y=100)
        TueMorningList.place(x=320, y=100)
        WedMorningList.place(x=480, y=100)
        ThuMorningList.place(x=640, y=100)
        FriMorningList.place(x=810, y=100)

        AfternoonLabel.place(x=20, y=210)
        MonAfternoonList.place(x=155, y=210)
        TueAfternoonList.place(x=320, y=210)
        WedAfternoonList.place(x=480, y=210)
        ThuAfternoonList.place(x=640, y=210)
        FriAfternoonList.place(x=810, y=210)

        EveningLabel.place(x=20, y=315)
        MonEveningList.place(x=155, y=315)
        TueEveningList.place(x=320, y=315)
        WedEveningList.place(x=480, y=315)
        ThuEveningList.place(x=640, y=315)
        FriEveningList.place(x=810, y=315)

        MidnightLabel.place(x=20, y=415)
        MonMidnightList.place(x=155, y=415)
        TueMidnightList.place(x=320, y=415)
        WedMidnightList.place(x=480, y=415)
        ThuMidnightList.place(x=640, y=415)
        FriMidnightList.place(x=810, y=415)

        FinishButton.place(x=810, y=500)
        title.place(x=975, y=25)
        subtitle1.place(x=975, y=100)
        subtitle2.place(x=975, y=140)
        subtitle3.place(x=975, y=180)
        subtitle4.place(x=975, y=220)

        moneyLabel = tk.Label(window, text = f"ι’εοΌ{data['status'].money}ε", font = money_f)
        moneyLabel.place(x = 1000, y = 640)

        abilityLabel = tk.Label(window, text = f"δ½ ηθ½εεΌ\nι­εοΌ{data['status'].charm}  ι«θ½οΌ{data['status'].fitness}  η€ΎδΊ€θ½εοΌ{data['status'].social}  ε₯εΊ·οΌ{data['status'].health}  ζΊζ§οΌ{data['status'].wisdom}", font = f)
        widgets.append(abilityLabel)
        abilityLabel.place(x = 50, y = 620)


    def save(self, clicked, result, data, used_widgets, FinishButton, moneyLabel, abilityLabel):
        FinishButton.destroy()

        for i in range(1, 6):
            for j in range(1, 5):
                result[f"{i}-{j}"] = clicked[j-1][i-1].get()
        data["status"].run_schedule(result)
        data["picked_schedule"] = result

        moneyLabel.destroy()
        moneyLabel = tk.Label(data["status"].display, text = f"ι’εοΌ{data['status'].money}ε", font = money_f)
        moneyLabel.place(x = 1000, y = 640)
        used_widgets.append(moneyLabel)

        abilityLabel.destroy()
        abilityLabel = tk.Label(data["status"].display, text = f"δ½ ηθ½εεΌ\nι­εοΌ{data['status'].charm}  ι«θ½οΌ{data['status'].fitness}  η€ΎδΊ€θ½εοΌ{data['status'].social}  ε₯εΊ·οΌ{data['status'].health}  ζΊζ§οΌ{data['status'].wisdom}", font = abi_f)
        abilityLabel.place(x = 50, y = 620)
        used_widgets.append(abilityLabel)

        if data["status"].cash_flow["εε‘"] < 0:
            you_drank_coffee(data["status"].display, data, -data["status"].cash_flow["εε‘"], used_widgets)
        else:
            show_cash_flow(data["status"].display, data, used_widgets)



def you_drank_coffee(window, data, money_need, widgets):
    # Cute Pic Creation

    coffee_pic = Image.open("figure/coffee.jpeg")
    coffee_pic = coffee_pic.resize((300, 219), Image.ANTIALIAS)
    coffee_pic = ImageTk.PhotoImage(coffee_pic)
    coffee = tk.Label(window, image=coffee_pic, bd=4, relief="raised")
    coffee.image = coffee_pic
    coffee.place(x=947, y=340)
    widgets.append(coffee)

    # Label Creation
    lbl = tk.Label(window, text=f"η²ΎεεΌδΈθΆ³\nδ½ θ±δΊ{money_need}εθ³Όθ²·εε‘...", font=text_f, bg="#bebfbe", relief="raised")
    lbl.place(x=950+coffee.winfo_reqwidth()/2-lbl.winfo_reqwidth()/2, y=275)
    widgets.append(lbl)

    show_cash_flow(data["status"].display, data, widgets)


def show_cash_flow(window, data, widgets):
    revenueLabel = tk.Label(window, text = f"ζΆε₯-ζε·₯:{data['status'].cash_flow['ζε·₯']}ε", font = text_f)
    expenseLabel = tk.Label(window, text = f"ζ―εΊ-ε₯θΊ«:{-data['status'].cash_flow['ε₯θΊ«']}εγη΄ζ:{-data['status'].cash_flow['η΄ζ']}εγη€ΎδΊ€:{-data['status'].cash_flow['η€ΎδΊ€']}εγζδΌι£θ²»:{-data['status'].cash_flow['ζδΌι£θ²»']}ε", font = text_f)
    revenueLabel.place(x = 50, y = 550)
    expenseLabel.place(x = 50, y = 575)
    widgets.append(revenueLabel)
    widgets.append(expenseLabel)

    for key in ["εε‘", "ε₯θΊ«", "η΄ζ", "η€ΎδΊ€", "ζε·₯", "ζδΌι£θ²»"]:
        data["status"].cash_flow[key] = 0

    # Button Creation

    continueButton = tk.Button(window, text="ηΉΌηΊ", width=5, font=button_f, command=lambda: [destroy_widgets(widgets), sound.play_button_sound(), check.check_event(data)])
    continueButton.place(x=810, y=640)
    widgets.append(continueButton)


def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()


def get_new_schedule(window, selected_class, data, is_new_semester):
    sound.play_background_music("main_bgm")
    # ε³ε₯ζ ΌεΌ
    # selected_class = {"1-1":"Aθͺ²", "2-2":"Bθͺ²", "4-3":"Cθͺ²"}
    selected_class_list = list(selected_class.items())

    options = [
        f"θ?{selected_class_list[0][1]}",
        f"θ?{selected_class_list[1][1]}",
        f"θ?{selected_class_list[2][1]}",
        "ε₯θΊ«",
        "ζε·₯",
        "η΄ζ",
        "η€ΎδΊ€",
        "δΌζ―",
    ]

    if is_new_semester:
        data["picked_schedule"] = {'1-1': 'δΌζ―', '1-2': 'δΌζ―', '1-3': 'δΌζ―', '1-4': 'δΌζ―', '2-1': 'δΌζ―', '2-2': 'δΌζ―', '2-3': 'δΌζ―', '2-4': 'δΌζ―', '3-1': 'δΌζ―', '3-2': 'δΌζ―', '3-3': 'δΌζ―', '3-4': 'δΌζ―', '4-1': 'δΌζ―', '4-2': 'δΌζ―', '4-3': 'δΌζ―', '4-4': 'δΌζ―', '5-1': 'δΌζ―', '5-2': 'δΌζ―', '5-3': 'δΌζ―', '5-4': 'δΌζ―'}
        data["picked_schedule"][selected_class_list[0][0]] = selected_class_list[0][1]
        data["picked_schedule"][selected_class_list[1][0]] = selected_class_list[1][1]
        data["picked_schedule"][selected_class_list[2][0]] = selected_class_list[2][1]

    window.configure(background="#eeefee")
    sch = Schedule(selected_class, data["picked_schedule"], options)
    sch.createWidgets(window, data)