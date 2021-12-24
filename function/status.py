import tkinter as tk
import tkinter.font as tkFont

# 玩家除了評分值之外的數值都存在"status"名稱的Class(Status)裡面
class Status:


    def __init__(self, wisdom, charm, fitness, social, health, money, san, luck, rest_time, score, window):
        self.wisdom = wisdom
        self.charm = charm
        self.fitness = fitness
        self.social = social
        self.health = health
        self.money = money
        self.san = san
        self.rest_time = rest_time
        self.score = score
        self.display = window
        self.luck = luck

    # 每天獲得的san值(尚未加入累加機制，函式先隨便寫的)
    def san_reset(self):
        self.san = 50 + self.rest_time + self.fitness * 0.1 + self.health * 0.5
        self.rest_time = 0

    # 跑一週的行程(更新數值的部分，若需要可加入觸發事件判斷)
    def run_schedule(self, schedule):
        Mon = ["1-1", "1-2", "1-3", "1-4"]
        Tue = ["2-1", "2-2", "2-3", "2-4"]
        Wed = ["3-1", "3-2", "3-3", "3-4"]
        Thr = ["4-1", "4-2", "4-3", "4-4"]
        Fri = ["5-1", "5-2", "5-3", "5-4"]
        self.san_reset()
        for i in Mon:
            act_check(self, schedule[i])
        self.san_reset()
        for i in Tue:
            act_check(self, schedule[i])
        self.san_reset()
        for i in Wed:
            act_check(self, schedule[i])
        self.san_reset()
        for i in Thr:
            act_check(self, schedule[i])
        self.san_reset()
        for i in Fri:
            act_check(self, schedule[i])
        return

    # 在進行每一次事件前判斷精力值是否足夠並詢問要不要喝咖啡及之後處理得函式
    def check_san(self, san_require):
        if self.san < san_require:
            money_need = (san_require - self.san) * 5
            a = self.coffee_or_not(self, money_need)  # 讓使用者選擇是否喝咖啡
            if a:
                self.money -= money_need
                self.san += san_require
                self.health -= (san_require * 0.1)
                return False
            else:
                return True
        else:
            return False

    # 甜課得函式
    def class_sweet(self):
        if self.check_san(5):
            return None
        self.sam -= 5
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1


    def class_easy(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def class_hard(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def class_waste(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def workout(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def part_time(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def go_dating(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def social(self):
        if self.check_san(3):
            return None
        self.san -= 3
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1

    def rest(self):
        self.rest_time += 1
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.health -= 1
        
        
    def midterm(self, class_type_a, class_type_b, class_type_c):
        self.score[a] = self.wisdom * 0.5 + self.san * 0.1 - (100 - self.luck) * 0.8
        
        
        

def coffee_or_not(status, money_need):
    ans = [""]
    # Top level window
    f = tkFont.Font(size = 20)

    # Label Creation
    lbl = tk.Label(window, text = f"精力值不足\n是否消耗{money_need}金錢來購買咖啡...", font = f, bg = "#bebfbe", relief = "raised")
    lbl.place(x = 960, y = 225)


    # Button Creation

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Button(status.display, text = "要",width = 5, font = f, command = lambda: save_input(True, ans))
    c1.place(x = 1005, y = 300)
    c2 = tk.Button(status.display, text = "不要",width = 5, font = f, command = lambda: save_input(False, ans))
    c2.place(x = 1130, y = 300)


    # Cute Pic Creation

    coffee_pic = Image.open("figure/coffee.jpeg")
    coffee_pic = coffee_pic.resize((300,219), Image.ANTIALIAS)
    coffee_pic = ImageTk.PhotoImage(coffee_pic)
    coffee = tk.Label(window, image = coffee_pic, bd =4, relief ="raised")
    coffee.image = coffee_pic
    coffee.place(x = 947, y = 340)

    return ans[0]


def save_input(yn, ans):
    ans[0] = yn 

# 判讀並執行行程表中"一項"行程的函式
def act_check(status, i):
    if i == "甜課":
        status.class_sweet()
        return
    elif i == "":
        status.class_easy()
        return
    elif i == "":
        status.class_hard()
        return
    elif i == "":
        status.class_waste()
        return
    elif i == "":
        status.workout()
        return
    elif i == "":
        status.part_time()
        return
    elif i == "":
        status.go_dating()
        return
    elif i == "":
        status.social()
        return
    elif i == "":
        status.rest()
    return
