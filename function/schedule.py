import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

class Schedule(tk.Frame):

    def __init__(self, classes, picked, options):
        tk.Frame.__init__(self)
        self.grid()
        self.classes = classes
        self.picked = picked
        self.options = options
        self.result = {}



    def createWidgets(self):
        f = tkFont.Font(size = 32, family = "lihsianti")
        small_f = tkFont.Font(size = 24, family = "lihsianti")

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

        self.imageNTU = ImageTk.PhotoImage(file = "function/ntu.png")
        self.NTUButton = tk.Button(self, image = self.imageNTU)
        self.MonLabel = tk.Label(self, text = "週一", height = 1, width = 4, font = f)
        self.TueLabel = tk.Label(self, text = "週二", height = 1, width = 4, font = f)
        self.WedLabel = tk.Label(self, text = "週三", height = 1, width = 4, font = f)
        self.ThuLabel = tk.Label(self, text = "週四", height = 1, width = 4, font = f)
        self.FriLabel = tk.Label(self, text = "週五", height = 1, width = 4, font = f)

        self.MorningLabel = tk.Label(self, text = "早上", height = 1, width = 4, font = f)
        self.MonMorningList = tk.OptionMenu(self, clicked[0][0], *options[0][0])
        self.TueMorningList = tk.OptionMenu(self, clicked[0][1], *options[0][1])
        self.WedMorningList = tk.OptionMenu(self, clicked[0][2], *options[0][2])
        self.ThuMorningList = tk.OptionMenu(self, clicked[0][3], *options[0][3])
        self.FriMorningList = tk.OptionMenu(self, clicked[0][4], *options[0][4])

        self.AfternoonLabel = tk.Label(self, text = "下午", height = 1, width = 4, font = f)
        self.MonAfternoonList = tk.OptionMenu(self, clicked[1][0], *options[1][0])
        self.TueAfternoonList = tk.OptionMenu(self, clicked[1][1], *options[1][1])
        self.WedAfternoonList = tk.OptionMenu(self, clicked[1][2], *options[1][2])
        self.ThuAfternoonList = tk.OptionMenu(self, clicked[1][3], *options[1][3])        
        self.FriAfternoonList = tk.OptionMenu(self, clicked[1][4], *options[1][4])

        self.EveningLabel = tk.Label(self, text = "晚上", height = 1, width = 4, font = f)
        self.MonEveningList = tk.OptionMenu(self, clicked[2][0], *options[2][0])
        self.TueEveningList = tk.OptionMenu(self, clicked[2][1], *options[2][1])
        self.WedEveningList = tk.OptionMenu(self, clicked[2][2], *options[2][2])
        self.ThuEveningList = tk.OptionMenu(self, clicked[2][3], *options[2][3])
        self.FriEveningList = tk.OptionMenu(self, clicked[2][4], *options[2][4])

        self.MidnightLabel = tk.Label(self, text = "半夜", height = 1, width = 4, font = f)
        self.MonMidnightList = tk.OptionMenu(self, clicked[3][0], *options[3][0])
        self.TueMidnightList = tk.OptionMenu(self, clicked[3][1], *options[3][1])
        self.WedMidnightList = tk.OptionMenu(self, clicked[3][2], *options[3][2])
        self.ThuMidnightList = tk.OptionMenu(self, clicked[3][3], *options[3][3])
        self.FriMidnightList = tk.OptionMenu(self, clicked[3][4], *options[3][4])

        self.FinishButton = tk.Button(self, text ="完成", height = 1, width = 4, font = small_f, command = lambda: self.save(clicked, self.result))


        self.NTUButton.grid(row = 0, column = 0, sticky = tk.NE + tk.SW)
        self.MonLabel.grid(row = 0, column = 1)
        self.TueLabel.grid(row = 0, column = 2)
        self.WedLabel.grid(row = 0, column = 3)
        self.ThuLabel.grid(row = 0, column = 4)
        self.FriLabel.grid(row = 0, column = 5)

        self.MorningLabel.grid(row = 1, column = 0)
        self.MonMorningList.grid(row = 1, column = 1)
        self.TueMorningList.grid(row = 1, column = 2)
        self.WedMorningList.grid(row = 1, column = 3)
        self.ThuMorningList.grid(row = 1, column = 4)
        self.FriMorningList.grid(row = 1, column = 5)

        self.AfternoonLabel.grid(row = 2, column = 0)
        self.MonAfternoonList.grid(row = 2, column = 1)
        self.TueAfternoonList.grid(row = 2, column = 2)
        self.WedAfternoonList.grid(row = 2, column = 3)
        self.ThuAfternoonList.grid(row = 2, column = 4)
        self.FriAfternoonList.grid(row = 2, column = 5)

        self.EveningLabel.grid(row = 3, column = 0)
        self.MonEveningList.grid(row = 3, column = 1)
        self.TueEveningList.grid(row = 3, column = 2)
        self.WedEveningList.grid(row = 3, column = 3)
        self.ThuEveningList.grid(row = 3, column = 4)
        self.FriEveningList.grid(row = 3, column = 5)

        self.MidnightLabel.grid(row = 4, column = 0)
        self.MonMidnightList.grid(row = 4, column = 1)
        self.TueMidnightList.grid(row = 4, column = 2)
        self.WedMidnightList.grid(row = 4, column = 3)
        self.ThuMidnightList.grid(row = 4, column = 4)
        self.FriMidnightList.grid(row = 4, column = 5)

        self.FinishButton.grid(row = 5, column = 5)


    def save(self, clicked, result):
        for i in range(1, 6):
            for j in range(1, 5):
                result[f"{i}-{j}"] = clicked[j-1][i-1].get()
        self.quit()


        
def get_new_schedule(selected_class, previous_picked):
    # # 傳入
    # selected_class = {"1-1":"A課", "2-2":"B課", "4-3":"C課"}
    selected_class_list = list(selected_class.items())

    # # 傳入
    # previous_picked = {'1-1': 'A課', '1-2': '讀A課', '1-3': '社交', '1-4': '健身', '2-1': '社交', '2-2': 'B課', '2-3': '讀A課', '2-4': '休息', '3-1': '讀A課', '3-2': '讀B課', '3-3': '讀A課', '3-4': '休息', '4-1': '讀A課', '4-2': '健身', '4-3': 'C課', '4-4': '社交', '5-1': '休息', '5-2': '約會', '5-3': '社交', '5-4': '休息'}

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

    sch = Schedule(selected_class, previous_picked, options)
    sch.createWidgets()
    sch.master.title("行程表")
    sch.mainloop()

    # 回傳
    return(sch.result)
