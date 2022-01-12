import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import function.status as status
import function.觸發事件判定 as check
import function.sound_effect as sound


class Schedule:

    def __init__(self, classes, picked, options):
        self.classes = classes
        self.picked = picked
        self.options = options
        self.result = {}


    def createWidgets(self, window, data):
        widgets = []
        f = tkFont.Font(size = 24)
        title_f = tkFont.Font(size = 48)
        week_f = tkFont.Font(size = 16)

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

        # self.imageNTU = ImageTk.PhotoImage(file = "figure/ntu.png")
        # self.NTUButton = tk.Button(window, image = self.imageNTU)
        MonLabel = tk.Label(window, text = " 星期一 ", font = week_f, bg = "#3895b9", fg = "white")
        TueLabel = tk.Label(window, text = " 星期二 ", font = week_f, bg = "#3895b9", fg = "white")
        WedLabel = tk.Label(window, text = " 星期三 ", font = week_f, bg = "#3895b9", fg = "white")
        ThuLabel = tk.Label(window, text = " 星期四 ", font = week_f, bg = "#3895b9", fg = "white")
        FriLabel = tk.Label(window, text = " 星期五 ", font = week_f, bg = "#3895b9", fg = "white")
        widgets.append(MonLabel)
        widgets.append(TueLabel)
        widgets.append(WedLabel)
        widgets.append(ThuLabel)
        widgets.append(FriLabel)

        MorningLabel = tk.Label(window, text = "早上", height = 1, width = 4, font = f, bg= "#eeefee")
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

        AfternoonLabel = tk.Label(window, text = "下午", height = 1, width = 4, font = f)
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

        EveningLabel = tk.Label(window, text = "晚上", height = 1, width = 4, font = f, bg= "#eeefee")
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

        MidnightLabel = tk.Label(window, text = "半夜", height = 1, width = 4, font = f)
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

        FinishButton = tk.Button(window, text ="完成", height = 1, width = 4, font = f, command = lambda: [self.save(clicked, self.result, data, widgets, FinishButton, moneyLabel), sound.play_button_sound()])

        title = tk.Label(window, text = "你的時間表" ,font = title_f, bg = "#eeefee", fg = "#712322")
        subtitle1 = tk.Label(window, text = "#時間沒有消失，", font = f, bg = "#eeefee")
        subtitle2 = tk.Label(window, text = "  只是變成你喜歡的樣子", font = f, bg = "#eeefee")
        subtitle3 = tk.Label(window, text = f"#這是你這個學期", font = f, bg = "#eeefee")
        widgets.append(title)
        widgets.append(subtitle1)
        widgets.append(subtitle2)
        widgets.append(subtitle3)

        schedule_time = data['previous_event']
        if schedule_time == "期中考":
            schedule_time = "第三次排行程表"

        subtitle4 = tk.Label(window, text = f"  {schedule_time}", font = f, bg = "#eeefee")
        widgets.append(subtitle4)

        background.image = schedule
        background.place(x=0, y=0)


        # NTUButton.place(x=20, y=50)
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

        money_f = tk.font.Font(size = 30)
        moneyLabel = tk.Label(window, text = f"錢包：{data['status'].money}元", font = money_f)
        moneyLabel.place(x = 1000, y = 640)

        abilityLabel = tk.Label(window, text = f"你的能力值\n魅力：{data['status'].charm}  體能：{data['status'].fitness}  社交能力：{data['status'].social}  健康：{data['status'].health}  智慧：{data['status'].wisdom}", font = f)
        widgets.append(abilityLabel)
        abilityLabel.place(x = 50, y = 600)

    def save(self, clicked, result, data, used_widgets, FinishButton, moneyLabel):
        FinishButton.destroy()

        for i in range(1, 6):
            for j in range(1, 5):
                result[f"{i}-{j}"] = clicked[j-1][i-1].get()
        money_spent = data["status"].run_schedule(result)
        data["picked_schedule"] = result
        if money_spent > 0:
            moneyLabel.destroy()
            money_f = tk.font.Font(size = 30)
            moneyLabel = tk.Label(data["status"].display, text = f"錢包：{data['status'].money}元", font = money_f)
            moneyLabel.place(x = 1000, y = 640)
            used_widgets.append(moneyLabel)
            you_drank_coffee(data["status"].display, data, money_spent, used_widgets)
        else:
            used_widgets.append(moneyLabel)
            for widget in used_widgets:
                widget.destroy()
            check.check_event(data)

        
def get_new_schedule(window, selected_class, data, is_new_semester):
    sound.play_background_music("正式遊戲背景音樂")
    # 傳入格式
    # selected_class = {"1-1":"A課", "2-2":"B課", "4-3":"C課"}
    selected_class_list = list(selected_class.items())

    options = [
        f"讀{selected_class_list[0][1]}",
        f"讀{selected_class_list[1][1]}",
        f"讀{selected_class_list[2][1]}",
        "健身",
        "打工",
        "約會",
        "社交",
        "休息",
    ]

    if is_new_semester:
        data["picked_schedule"] = {'1-1': '休息', '1-2': '休息', '1-3': '休息', '1-4': '休息', '2-1': '休息', '2-2': '休息', '2-3': '休息', '2-4': '休息', '3-1': '休息', '3-2': '休息', '3-3': '休息', '3-4': '休息', '4-1': '休息', '4-2': '休息', '4-3': '休息', '4-4': '休息', '5-1': '休息', '5-2': '休息', '5-3': '休息', '5-4': '休息'}
        data["picked_schedule"][selected_class_list[0][0]] = selected_class_list[0][1]
        data["picked_schedule"][selected_class_list[1][0]] = selected_class_list[1][1]
        data["picked_schedule"][selected_class_list[2][0]] = selected_class_list[2][1]

    window.configure(background="#eeefee")
    sch = Schedule(selected_class, data["picked_schedule"], options)
    sch.createWidgets(window, data)


def you_drank_coffee(window, data, money_need, widgets):
    f = tkFont.Font(size=20)
    button_f = tkFont.Font(size=24)

    # Button Creation

    continueButton = tk.Button(window, text="繼續", width=5, font=button_f, command=lambda: [destroy_widgets(widgets), sound.play_button_sound(), check.check_event(data)])
    continueButton.place(x=1070, y=300)
    widgets.append(continueButton)

    # Cute Pic Creation

    coffee_pic = Image.open("figure/coffee.jpeg")
    coffee_pic = coffee_pic.resize((300, 219), Image.ANTIALIAS)
    coffee_pic = ImageTk.PhotoImage(coffee_pic)
    coffee = tk.Label(window, image=coffee_pic, bd=4, relief="raised")
    coffee.image = coffee_pic
    coffee.place(x=947, y=340)
    widgets.append(coffee)

    # Label Creation
    lbl = tk.Label(window, text=f"精力值不足\n你花了{money_need}元購買咖啡...", font=f, bg="#bebfbe", relief="raised")
    lbl.place(x=960, y=350)
    widgets.append(lbl)


def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()