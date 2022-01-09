import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import function.read_file as read
import function.midterm_report as show_mid
import function.final_report as show_fi
import function.sound_effect as sound
import function.achievement as achievement
import random


class Status:

    def __init__(self, wisdom, charm, fitness, social, health, luck, course, window):
        self.wisdom = wisdom  # 存
        self.charm = charm  # 存
        self.fitness = fitness  # 存
        self.social = social  # 存
        self.health = health  # 存
        self.money = 40000  # 存
        self.san = 100  # 隨便設
        self.rest_time = 100  # 隨便設
        self.score = dict()
        self.display = window
        self.luck = luck  # 存
        self.love_progress = 100  # 存
        self.grade = 100  # 存
        self.yang_sheng = 100  # 存
        self.prestige = 100  # 存
        self.study_time = dict()
        self.course = course  # 存
        self.achievement = achievement.Achievement()

    # 每天獲得的san值(尚未加入累加機制，函式先隨便寫的)
    def san_reset(self):
        self.san = 50 + self.rest_time + self.fitness * 0.1 + self.health * 0.5
        self.rest_time = 0
        
    # 學期初發錢
    def allowance(self):
        self.money += 40000

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
            a = self.coffee_or_not(int(money_need))  # 讓使用者選擇是否喝咖啡
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

    def social_with_other(self):
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

    def midterm(self, class_dict, data):
        class_list = list(class_dict.values())
        for i in class_list:
            self.score[i] = scoring(self, i)
        show_mid.show_midterm_report(data["status"].display, data, self.score)


    def final_exam(self, class_dict, data):
        classtodiff = read.get_course_type_dic(data["status"].course)
        # 健康值轉養生
        self.yang_sheng = self.yang_sheng + self.health * 0.1
        # 結算學期成績
        class_list = list(class_dict.values())
        #計算被當科目
        class_fail = 0
        drop_out = False
        for i in class_list:
            self.score[i] = (scoring(self, i) + self.score[i]) / 2
            if self.score[i] >= 90:
                if classtodiff[i] == "硬課":
                    self.grade += 10
                if classtodiff[i] == "甜課":
                    self.grade += 7
                if classtodiff[i] == "涼課":
                    self.grade += 5
                if classtodiff[i] == "爽課":
                    self.grade += 2
            elif self.score[i] >= 70:
                if classtodiff[i] == "硬課":
                    self.grade += 7
                if classtodiff[i] == "甜課":
                    self.grade += 5
                if classtodiff[i] == "涼課":
                    self.grade += 3
            elif self.score[i] >= 60:
                if classtodiff[i] == "硬課":
                    self.grade += 3
                if classtodiff[i] == "甜課":
                    self.grade += 2
                if classtodiff[i] == "涼課":
                    self.grade += 1
            for j in self.course:
                if i in j:
                    j[2] -= 1
                    if self.score[i] >= 60:
                        j[3] += 1
                    else:
                        j[4] += 1
                        class_fail += 1
        if class_fail >= 2:
            drop_out = True
        score_final = self.score
        show_fi.show_final_report(data["status"].display, data, self.score)
        self.score.clear()
        return drop_out
    

    def coffee_or_not(self, money_need):
        ans = [""]
        # Top level window
        f = tkFont.Font(size=20)

         # Button Creation

        var1 = tk.IntVar()
        var2 = tk.IntVar()
        c1 = tk.Button(self.display, text="要", width=5, font=f, command=lambda: [save_input(True, ans, c1, c2, lbl, self.display), sound.play_button_sound()])
        c1.place(x=1005, y=300)
        c2 = tk.Button(self.display, text="不要", width=5, font=f, command=lambda: [save_input(False, ans, c1, c2, lbl, self.display), sound.play_button_sound()])
        c2.place(x=1130, y=300)

        # Cute Pic Creation

        coffee_pic = Image.open("figure/coffee.jpeg")
        coffee_pic = coffee_pic.resize((300, 219), Image.ANTIALIAS)
        coffee_pic = ImageTk.PhotoImage(coffee_pic)
        coffee = tk.Label(self.display, image=coffee_pic, bd=4, relief="raised")
        coffee.image = coffee_pic
        coffee.place(x=947, y=340)

        # Label Creation
        lbl = tk.Label(self.display, text=f"精力值不足\n是否消耗{int(money_need)}金錢來購買咖啡...", font=f, bg="#bebfbe", relief="raised")
        lbl.place(x=960, y=350)

        return ans[0]

def save_input(yn, ans, c1, c2, ori_lbl, window):
    c1.destroy()
    c2.destroy()
    ori_lbl.destroy()
    if ans == True:
        lbl = tk.Label(window, text=f"你喝了咖啡，超勇的好不好", font=f, bg="#bebfbe", relief="raised")
        lbl.place(x=960, y=300)
    else:
        lbl = tk.Label(window, text=f"你沒喝咖啡，那天直接不支倒地睡死", font=f, bg="#bebfbe", relief="raised")
        lbl.place(x=960, y=300)
    ans[0] = yn

 # 判讀並執行行程表中"一項"行程的函式
def act_check(status, i):
    classtodiff = read.get_course_type_dic(status.course)
    if i in list(classtodiff.keys()):
        i = classtodiff[i]
    elif i[1::] in list(classtodiff.keys()):
        i_name = i[1::]
        i = "讀" + classtodiff[i_name]
    if i == "甜課":
        status.class_sweet()
        return
    elif i == "涼課":
        status.class_easy()
        return
    elif i == "硬課":
        status.class_hard()
        return
    elif i == "爽課":
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
    elif i == "讀爽課":
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
        status.social_with_other()
        return
    elif i == "休息":
        status.rest()
    return

def scoring(status, classname):
    classtodiff = read.get_course_type_dic(status.course)
    coefficient = {"甜課": 0.08, "涼課": 0.12, "硬課": 0.04}
    status.study_time.setdefault(classname, 0)
    if classtodiff[classname] == "爽課":
        point = 90 + random.randint(0, 10)
        return int(point)
    else:
        point = status.wisdom * status.study_time[classname] * coefficient[
            classtodiff[classname]] + 0.2 * status.luck + random.randint(-10, 10)
        if point >= 100:
            point = 100
        return int(point)



# 事件數值調整
def event_adjust(status, event_name, choice):
    if event_name =="健康檢查":
        if choice[0] == 1:
            status.health += 50
            status.money -= 500
            return
        else:
            status.health -= 50
        return
    elif event_name == "Elite":
        status.wisdom += 25
        if choice[0] == 1:
            status.wisdom += 50
            status.health -= 25
        else:
            status.social -= 25
        if choice[1] == 1:
            status.health -= 25
            status.prestige += 25
        else:
            status.health += 15
            status.prestige -= 15
        return
    elif event_name == "系隊":
        status.health += 25
        if choice[0] == 1:
            status.prestige += 25
            status.charm += 50
            return
        else:
            status.prestige -= 25
        return
    elif event_name == "系學會":
        status.prestige += 25
        if choice[0] == 1:
            status.health -= 50
            status.prestige += 15
            if status.wisdom >= 85:
                status.prestige += 25
                return
            else:
                status.prestige -= 10
                return
        else:
            status.prestige -= 10
        return
    elif event_name == "比賽":
        if choice[0] == 1:
            status.wisdom += 75
            status.prestige += 15
            return
        else:
            status.fitness += 75
            status.prestige += 15
            return
    elif event_name == "聯誼":
        if choice[0] == 1:
            if choice[1] == 1:
                status.love_progress += 50
                status.social += 15
                return
            else:
                status.social += 15
                return
        else:
            if choice[1] == 1:
                if status.charm >= 90:
                    status.social += 50
                    return
                else:
                    status.social += 25
                    return
            else:
                if choice[2] == 1:
                    if choice[3] == 1:
                        status.love_progress += 50
                        status.social += 15
                        return
                    else:
                        status.social += 15
                        return
        return
    elif event_name == "舞會1-男":
        if choice[0] == 1:
            if choice[1] == 1:
                if choice[2] == 1:
                    status.charm += 25
                    return
                else:
                    status.charm -= 25
                    status.prestige -= 25
                    return
        else:
            if choice[1] == 1:
                status.charm += 15
                if choice[2] == 1:
                    status.charm += 25
                    return
                return
            else:
                if choice[1] == 2:
                    if choice[2] == 1:
                        status.prestige += 25
                        status.charm += 25
                        if choice[3] == 1:
                            status.charm += 25
                            return
                        return
                    else:
                        status.prestige += 25
                        status.charm -= 15
                        return
                if choice[1] == 3:
                    status.prestige -= 25
                    status.charm += 25
                    return
    elif event_name == "舞會2-男":
        if choice[0] == 1:
            status.prestige += 25
            status.health -= 50
            return 
    elif event_name == "打疫苗":
        if choice[0] == 1 and status.luck >=75:
            status.health += 75
            return
        elif status.luck >= 35:
            status.health += 75
        return
    elif event_name == "實習":
        if choice[0] == 1:
            if choice[1] == 1:
                if status.luck >= 95:
                    status.prestige += 40
                    status.wisdom += 40
                    return 
            else:
                status.prestige += 25
                status.wisdom += 25
                return 
        else:
            status.prestige += 25
            status.wisdom += 25
        return 
    elif event_name == "當兵":
        if choice[0] == 1:
            status.fitness += 50
            return
        else:
            status.fitness += 100
        return
    elif event_name == "耍廢":
        status.social -= 25
        status.fitness -= 25
        return
    elif event_name == "念書":
        status.wisdom += 75
        return
    elif event_name == "規律作息":
        status.health += 100
        status.yang_sheng += 25
        return
    elif event_name == "虛擬貨幣":
        if status.luck >= 95:
            status.money += 400000
            self.stocks_surfing += 1
            return
        else:
            status.money += 10000
            self.stocks_surfing += 1
        return
    elif event_name == "ETF":
        status.money += 100000
        self.stocks_surfing += 1
        return
    elif event_name == "債券":
        status.money += 10000
        self.stocks_surfing += 1
        return
    elif event_name == "陪另一半":
        status.love_progress += 50
        return
    elif event_name =="服務學習":
        status.social += 50
        status.prestige += 25
        status.charm += 25
    elif event_name == "翹課打ㄆ":
        if choice[0] == 1:
            status.prestige = 0
            status.charm -= 25
            return
        else:
            status.charm += 25
            return
    elif event_name == "學長姊送考古題":
        if choice[0] == 1:
            status.charm -= 5
            return
        elif choice[0] == 2:
            status.charm += 25
            status.wisdom += 45
            return
        else:
            status.charm -= 25
            status.social -= 25
            return
    elif event_name == "推坑V":
        if choice[0] == 1 and choice[1] == 1:
            status.social += 25
            status.prestige += 25
            return
        elif choice[0] == 2:
            status.prestige -= 25
    elif event_name == "婚姻抉擇":
        if choice[0] == 2:
            status.love_progress = 1000000
            status.money -= 50000
            return
    elif event_name == "讀書會":
        if choice[0] == 1:
            status.prestige -= 25
            status.yang_sheng += 50
            return
        else:
            status.yang_sheng -= 50
            status.wisdom += 100
            status.grade += 25
            return
    elif event_name == "研究專案":
        if choice[0] == 1:
            status.grade += 100
            status.prestige += 25
            return
        else:
            status.grade = 30
            return
    elif event_name == "不想努力了":
        if choice[0] == 1:
            return "阿姨"
    elif event_name == "車被拖吊":
        status.money -= 300
        return
    elif event_name == "第一次約會":
        if choice[0] == 1:
            if choice[1] == 1:
                status.charm -= 50
                status.love_progress -= 50
                return
            else:
                if choice[2] == 1:
                    status.money -= 1000
                    status.love_progress += 50
                    return
                else:
                    status.love_progress -= 25
                    return
        elif choice[0] == 2:
            status.money -= 1000
            if choice[1] == 1:
                status.charm -= 25
                return
            else:
                status.love_progress += 100
                return
        else:
            status.money -= 1000
            if choice[1] == 1:
                status.charm -= 50
                status.love_progress -= 50
                return
            else:
                status.charm += 50
                status.love_progress += 50
    return