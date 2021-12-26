import tkinter as tk
import tkinter.font as tkFont
import random

classtodiff = {"個經原": "甜課"}


class Status:

    def __init__(self, wisdom, charm, fitness, social, health, san, luck, rest_time, classes, window):
        self.wisdom = wisdom
        self.charm = charm
        self.fitness = fitness
        self.social = social
        self.health = health
        self.money = 40000
        self.san = san
        self.rest_time = rest_time
        self.score = dict()
        self.display = window
        self.luck = luck
        self.love_progress = 0
        self.grade = 0
        self.yang_sheng = 0
        self.prestige = 0
        self.study_time = dict()
        self.classes = classes

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
        if self.check_san(10):
            return None
        self.san -= 10
        self.wisdom += 5
        self.charm -= 1
        self.social += 2
        self.fitness -= 1

    def class_easy(self):
        if self.check_san(5):
            return None
        self.san -= 5
        self.wisdom += 2
        self.charm -= 1
        self.social += 1
        self.fitness -= 1

    def class_hard(self):
        if self.check_san(30):
            return None
        self.san -= 30
        self.wisdom += 10
        self.charm -= 1
        self.social -= 1
        self.fitness -= 2

    def class_waste(self):
        if self.check_san(0):
            return None
        self.san -= 0
        self.wisdom -= 1
        self.charm -= -1
        self.social += 3

    def workout(self):
        if self.check_san(25):
            return None
        self.money -= 30
        self.san -= 25
        self.wisdom -= 3
        self.charm += 4
        self.fitness += 10
        self.health += 3

    def part_time(self):
        if self.check_san(20):
            return None
        self.san -= 20
        self.wisdom -= 2
        self.fitness += 1
        self.social += 4
        self.health -= 2
        self.money += 1200

    def go_dating(self):
        if self.check_san(30):
            return None
        self.san -= 30
        self.wisdom -= 4
        self.charm += 10
        self.social -= 2
        self.health -= 5
        self.money -= 1111

    def social(self):
        if self.check_san(-20):
            return None
        self.san -= 20
        self.wisdom -= 5
        self.charm += 3
        self.social += 10
        self.health -= 4
        self.fitness -= 3
        self.money -= 100

    def rest(self):
        self.rest_time += 1
        self.wisdom -= 1
        self.charm -= 1
        self.social -= 2
        self.health += 5

    def midterm(self, class_dict):
        class_list = list(class_dict.values())
        for i in class_list:
            self.score[i] = scoring(self, i)
        return


    def final_exam(self, class_dict):
        class_list = list(class_dict.values())
        for i in class_list:
            self.score[i] = (scoring(self, i) + self.score[i]) / 2
        score_final = self.score
        self.score.clear()
        return  score_final
    

    def coffee_or_not(status, money_need):
        ans = [""]
        # Top level window
        f = tkFont.Font(size=20)

        # Label Creation
        lbl = tk.Label(window, text=f"精力值不足\n是否消耗{money_need}金錢來購買咖啡...", font=f, bg="#bebfbe", relief="raised")
        lbl.place(x=960, y=225)

         # Button Creation

        var1 = tk.IntVar()
        var2 = tk.IntVar()
        c1 = tk.Button(status.display, text="要", width=5, font=f, command=lambda: save_input(True, ans))
        c1.place(x=1005, y=300)
        c2 = tk.Button(status.display, text="不要", width=5, font=f, command=lambda: save_input(False, ans))
        c2.place(x=1130, y=300)

        # Cute Pic Creation

        coffee_pic = Image.open("figure/coffee.jpeg")
        coffee_pic = coffee_pic.resize((300, 219), Image.ANTIALIAS)
        coffee_pic = ImageTk.PhotoImage(coffee_pic)
        coffee = tk.Label(window, image=coffee_pic, bd=4, relief="raised")
        coffee.image = coffee_pic
        coffee.place(x=947, y=340)

        return ans[0]

def save_input(yn, ans):
    ans[0] = yn

 # 判讀並執行行程表中"一項"行程的函式
def act_check(status, i):
    if i in list(classtodiff.keys()):
        i = classtodiff[i]
    elif i[2:] in list(classtodiff.keys()):
        i_name = i
        i = "讀" + classtodiff[i]
    if i == "甜課":
        status.class_sweet()
        return
    elif i == "涼課":
        status.class_easy()
        return
    elif i == "硬課":
        status.class_hard()
        return
    elif i == "廢課":
        status.class_waste()
        return
    elif i == "讀甜課":
        status.class_sweet()
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return
    elif i == "讀涼課":
        status.class_easy()
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return
    elif i == "讀硬課":
        status.class_hard()
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return
    elif i == "讀廢課":
        status.class_waste()
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return
    elif i == "健身":
        status.workout()
        return
    elif i == "打工":
        status.part_time()
        return
    elif i == "約會":
        status.go_dating()
        return
    elif i == "社交":
        status.social()
        return
    elif i == "休息":
        status.rest()
    return

def scoring(status, classname):
    coefficient = {"甜課" : 0.001, "涼課" : 0.003, "硬課" : 0.0002}
    point = status.wisdom * status.study_time[classname] * coefficient[classtodiff[classname]] + 0.2 * status.luck + random.randint(-10, 10)
    return int(point)


