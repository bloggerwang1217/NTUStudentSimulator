import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import function.read_file as read
import function.midterm_report as show_mid
import function.final_report as show_fi
import function.sound_effect as sound
import function.achievement as achievement
import function.show_event as show
import random


class Status:

    def __init__(self, wisdom, charm, fitness, social, health, luck, course, window):
        self.wisdom = wisdom  
        self.charm = charm  
        self.fitness = fitness  
        self.social = social  
        self.health = health  
        self.money = 0
        self.san = 100  
        self.rest_time = 100  
        self.score = dict()
        self.display = window
        self.luck = luck  
        self.love_progress = 100  
        self.grade = 100  
        self.yang_sheng = 100  
        self.prestige = 100  
        self.study_time = dict()
        self.course = course  
        self.achievement = achievement.Achievement()
        self.time = 0
        self.freq = True, True, True, True, True, True, True, True, True, True
        self.cash_flow = {"學費":0, "伙食費":0, "急診":0, "咖啡":0, "健身":0, "約會":0, "社交":0, "打工":0, "月伙食費":0, "零用錢":0, "書卷獎":0, "健康檢查":0, "投資虛擬貨幣":0, "投資ETF":0, "投資債券":0, "結婚":0, "腳踏車贖金":0, "和女友約會支出":0, "育兒基金":0, "暑假打工":0}

    # 每天獲得的san值(尚未加入累加機制，函式先隨便寫的)
    def san_reset(self):
        self.san = 50 + self.rest_time + self.fitness * 0.1 + self.health * 0.5
        self.rest_time = 0


    # 學期初發錢
    def allowance(self):
        self.money += 40000
        self.money -= 25000


    # 跑一週的行程(更新數值的部分，若需要可加入觸發事件判斷)
    def run_schedule(self, schedule):
        money_spent = 0
        Mon = ["1-1", "1-2", "1-3", "1-4"]
        Tue = ["2-1", "2-2", "2-3", "2-4"]
        Wed = ["3-1", "3-2", "3-3", "3-4"]
        Thr = ["4-1", "4-2", "4-3", "4-4"]
        Fri = ["5-1", "5-2", "5-3", "5-4"]
        self.san_reset()
        for i in Mon:
            money_spent += act_check(self, schedule[i])
        self.san_reset()
        for i in Tue:
            money_spent += act_check(self, schedule[i])
        self.san_reset()
        for i in Wed:
            money_spent += act_check(self, schedule[i])
        self.san_reset()
        for i in Thr:
            money_spent += act_check(self, schedule[i])
        self.san_reset()
        for i in Fri:
            money_spent += act_check(self, schedule[i])

        self.health = int(self.health)
        self.cash_flow["咖啡"] = -money_spent

        self.money -= 4000
        self.cash_flow["月伙食費"] -= 4000


    # 在進行每一次事件前判斷精力值是否足夠並詢問要不要喝咖啡及之後處理得函式
    def check_san(self, san_require):
        money_need = 0
        if self.san < san_require:
            money_need = (san_require - self.san) * 5

            self.money -= int(money_need)
            self.san += san_require
            self.health -= (san_require * 0.1)

        if int(money_need) > 0:
            return int(money_need)
        else:
            return 0


    # 甜課得函式
    def class_sweet(self):
        self.san -= 10
        self.wisdom += (2+random.randrange(0, 3))
        self.charm -= 1
        self.social += 0
        self.fitness -= 1

        return self.check_san(10)


    def class_easy(self):
        self.san -= 5
        self.wisdom += (2+random.randrange(-2, 3))
        self.charm -= 1
        self.social += 1
        self.fitness -= 1

        return self.check_san(5)


    def class_hard(self):
        self.san -= 30
        self.wisdom += (2+random.randrange(0, 5))
        self.charm -= 1
        self.social -= 1
        self.fitness -= 2

        return self.check_san(30)


    def class_waste(self):
        self.san -= 0
        self.wisdom -= 1
        self.charm -= 0
        self.social += 2

        return self.check_san(0)


    def workout(self):
        self.money -= 30
        self.cash_flow["健身"] -= 30
        self.san -= 25
        self.wisdom -= 0
        self.charm += 1
        self.fitness += (4+random.randrange(0, 7))
        self.health += (2+random.randrange(0, 3))

        return self.check_san(25)


    def part_time(self):
        self.san -= 20
        self.wisdom -= 2
        self.fitness += 1
        self.social += 4
        self.health -= 2
        self.money += 1200
        self.cash_flow["打工"] += 1200

        return self.check_san(20)


    def go_dating(self):
        self.san -= 30
        self.wisdom -= 3
        self.charm += (2+random.randrange(0, 5))
        self.social -= 2
        self.health -= 5
        self.money -= 1111
        self.cash_flow["約會"] -= 1111

        return self.check_san(30)


    def social_with_other(self):
        self.san -= 20
        self.wisdom -= 3
        self.charm += 3
        self.social += (2+random.randrange(0, 5))
        self.health -= 4
        self.fitness -= 3
        self.money -= 100
        self.cash_flow["社交"] -= 100

        return self.check_san(-20)


    def rest(self):
        self.rest_time += 1
        self.wisdom -= 1
        self.charm -= 1
        self.social -= 2
        self.health += 5

        return 0


    def midterm(self, class_dict, data):
        class_list = list(class_dict.values())
        for i in class_list:
            self.score[i] = scoring(self, i)
        self.time += 1
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
                    if self.score[i] >= 60:
                        j[3] += 1
                    else:
                        j[4] += 1
                        class_fail += 1
        self.time += 1

        score_final = self.score.copy()
        show_fi.show_final_report(data["status"].display, data, score_final)
        self.score.clear()



 # 判讀並執行行程表中"一項"行程的函式
def act_check(status, i):
    classtodiff = read.get_course_type_dic(status.course)
    if i in list(classtodiff.keys()):
        i = classtodiff[i]
    elif i[1::] in list(classtodiff.keys()):
        i_name = i[1::]
        i = "讀" + classtodiff[i_name]
    if i == "甜課":
        return status.class_sweet()
        
    elif i == "涼課":
        return status.class_easy()
        
    elif i == "硬課":
        return status.class_hard()
        
    elif i == "爽課":
        return status.class_waste()
        
    elif i == "讀甜課":
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return status.class_sweet()

    elif i == "讀涼課":
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return status.class_easy()

    elif i == "讀硬課":
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return status.class_hard()

    elif i == "讀爽課":
        status.study_time[i_name] = status.study_time.setdefault(i_name, 0) + 1
        return status.class_waste()

    elif i == "健身":
        return status.workout()

    elif i == "打工":
        return status.part_time()

    elif i == "約會":
        return status.go_dating()

    elif i == "社交":
        return status.social_with_other()

    elif i == "休息":
        return status.rest()


def scoring(status, classname):
    classtodiff = read.get_course_type_dic(status.course)
    coefficient = {"甜課": 0.08 / (1.2 ** (status.time/2)), "涼課": 0.12 / (1.2 ** (status.time/2)), "硬課": 0.04 / (1.2 ** (status.time/2))}
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
            status.cash_flow["健康檢查"] -= 500
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
    elif event_name == "打工":
        status.money += 50000
        status.cash_flow["暑假打工"] += 50000
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
    elif event_name == "唸書":
        status.wisdom += 75
        return
    elif event_name == "規律作息":
        status.health += 100
        status.yang_sheng += 25
        return
    elif event_name == "虛擬貨幣":
        if status.luck >= 95:
            status.money += 400000
            status.cash_flow["投資虛擬貨幣"] += 400000
            return
        else:
            status.money += 10000
            status.cash_flow["投資虛擬貨幣"] += 10000
        return
    elif event_name == "ETF":
        status.money += 100000
        status.cash_flow["投資ETF"] += 100000
        return
    elif event_name == "債券":
        status.money += 10000
        status.cash_flow["投資債券"] += 10000
        return
    elif event_name == "陪另一半":
        status.love_progress += 50
        return
    elif event_name == "服務學習":
        status.social += 50
        status.prestige += 25
        status.charm += 25
    elif event_name == "懷孕":
        status.money -= 50000
        status.cash_flow["育兒基金"] -= 50000
    elif event_name == "翹課打ㄆ":
        if choice[0] == 1:
            status.prestige = 0
            status.charm -= 25
            return
        else:
            status.charm += 25
            return
    elif event_name == "獲得考古題":
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
    elif event_name == "推坑Vt":
        if choice[0] == 1 and choice[1] == 1:
            status.social += 25
            status.prestige += 25
            return
        elif choice[0] == 2:
            status.prestige -= 25
    elif event_name == "婚姻抉擇":
        if choice[0] == 1:
            status.love_progress = 1000
            status.money -= 50000
            status.cash_flow["結婚"] -= 50000
            return
    elif event_name == "參加讀書會":
        if choice[0] == 1:
            status.prestige -= 25
            status.yang_sheng += 50
            return
        else:
            status.yang_sheng -= 50
            status.wisdom += 100
            status.grade += 25
            return
    elif event_name == "參加研究專案":
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
    elif event_name == "腳踏車被拖吊":
        status.money -= 300
        status.cash_flow["腳踏車贖金"] -= 300
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
                    status.cash_flow["和女友約會支出"] -= 300
                    status.love_progress += 50
                    return
                else:
                    status.love_progress -= 25
                    return
        elif choice[0] == 2:
            status.money -= 1000
            status.cash_flow["和女友約會支出"] -= 1000
            if choice[1] == 1:
                status.charm -= 25
                return
            else:
                status.love_progress += 100
                return
        else:
            status.money -= 1000
            status.cash_flow["和女友約會支出"] -= 1000
            if choice[1] == 1:
                status.charm -= 50
                status.love_progress -= 50
                return
            else:
                status.charm += 50
                status.love_progress += 50
    return
