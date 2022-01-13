import random
import function.status as status001
import function.show_event as show

status = ""
VtAchievement = False
DateAchievement = False

# 觸發事件的判斷，每學期有些事件會更新一次，讓事件不會重複發生
study_freq, res_freq, sex_freq, OldExam_freq, First_Date_freq, To_New_World_freq,\
Sugar_freq, preg_freq, Bike_tow_freq, Vt_freq = True, True, True, True, True, True, True, True, True, True


def reset():  # 重置事件頻率
    study_freq, res_freq, sex_freq, OldExam_freq, Sugar_freq, Bike_tow_freq, To_New_World_freq = True, True, True, True, True, True, True

    
def blow_wind():  # 樓頂吹風
    global status
    if status.wisdom <= 0 or status.charm <= 0:
        return True


def Leave_school():  # 轉學
    global status
    if status.social<= 0:
        return True

    
def To_New_World():  # 轉生異世界
    global status, To_New_World_freq
    prob = random.randrange(1, 101)
    if status.luck < 6 and prob < 2 and To_New_World_freq:
        return True
    elif status.luck > 6 and prob >= 2 and To_New_World_freq:  # 一學期只會判定一次
        To_New_World_freq = False


def Me_First():  # 明明是我先來的
    global status
    if status.charm > 300 and status.love_progress < 40:
        return True


def Broke():  # 破產
    global status
    if status.money <= -50000:
        return True


def Wealth_Freedom():  # 財富自由
    global status
    if status.money >= 1000000:
        return True


def IntoDust():  # 火化
    global status
    if status.health <= 0 or status.fitness <= 0:
        return True


def Vtuber_or_Not():  # 推坑Vt
    global status, Vt_freq, VtAchievement
    if status.social < 40 and Vt_freq:
        VtAchievement = True
        Vt_freq = False
        return True
    else:
        return False


def Study_or_not():  # 參加讀書會
    global study_freq, status
    if status.wisdom > 85 and status.wisdom <  100 and\
       status.social > 70 and study_freq:
        study_freq = False
        return True
    else:
        return False


def Research_or_not():  # 參加研究專案
    global res_freq, status
    if status.wisdom > 100 and status.wisdom < 115 and\
       status.social > 70 and res_freq:
        res_freq = False
        return True
    else:
        return False

    
def Sex_or_not():  # 翹課打ㄆ
    global sex_freq, status
    if status.charm > 200 and sex_freq:
        sex_freq = False
        return True
    else:
        return False


def OldExam_or_not():  # 獲得考古題
    global OldExam_freq, status
    if status.social > 80 and OldExam_freq:
        OldExam_freq = False
        return True
    else:
        return False


def First_Date():  # 第一次約會
    global First_Date_freq, status, DateAchievement 
    if status.love_progress > 140 and First_Date_freq:
        First_Date_freq = False
        DateAchievement = True
        return True
    else:
        return False


def Marriage_or_not():  # 婚姻抉擇
    global status
    if status.love_progress >= 350:
        return True
    else:
        return False


def SugarDaddy():  # 不想努力了
    global Sugar_freq, status
    if status.charm > 500 and status.love_progress < 110 and Sugar_freq:
        Sugar_freq = False
        return True
    else:
        return False


def Pregnant():  # 懷孕
    global preg_freq, status
    prob = random.randrange(1, 101)
    if status.charm > 500 and status.luck < 5 and preg_freq and prob < 6:
        preg_freq = False
        return True
    else:
        return False


def Bike_tow():  # 腳踏車被拖吊
    global Bike_tow_freq, status
    prob = random.randrange(1, 101)
    if status.luck < 20 and Bike_tow_freq and prob < 81:
        Bike_tow_freq = False
        return True
    else:
        return False

status001.status.freq = study_freq, res_freq, sex_freq, OldExam_freq, First_Date_freq, To_New_World_freq, Sugar_freq, preg_freq, Bike_tow_freq, Vt_freq

def check_event(data):
    global status
    status = data["status"]

    outputList01 = []
    outputList02 = []

    TriIncident_List = ['觸發事件:推坑Vt', '觸發事件:參加讀書會', '觸發事件:參加研究專案', '觸發事件:翹課打ㄆ', '觸發事件:獲得考古題', '觸發事件:第一次約會', 
                    '觸發事件:婚姻抉擇', '觸發事件:不想努力了', '觸發事件:懷孕', '觸發事件:腳踏車被拖吊']
    Incident_List = ['中途結束事件:樓頂吹風', '中途結束事件:轉生異世界', '中途結束事件:明明是我先來的', '中途結束事件:破產', 
                     '中途結束事件:財富自由', '中途結束事件:火化', '中途結束事件:轉學']
    Yes_or_Not = [Vtuber_or_Not(), Study_or_not(), Research_or_not(), Sex_or_not(), OldExam_or_not(), First_Date(), Marriage_or_not(), SugarDaddy(), Pregnant(), Bike_tow()]
    Mid_End = [blow_wind(), To_New_World(), Me_First(), Broke(), Wealth_Freedom(), IntoDust(), Leave_school()]
    for i in range(len(Incident_List)):
        if Mid_End[i] == True:
            outputList01.append(Incident_List[i])

    if len(outputList01) > 1:
        prob = random.randrange(0, len(outputList01))  # 若中途結束事件發生2種以上，隨機挑選其中一個
        outputList01 = outputList01[prob]
    
    for i in range(len(TriIncident_List)):
        if Yes_or_Not[i] == True:
            outputList02.append(TriIncident_List[i])
    
    outputList = outputList01 + outputList02
    
    if Pregnant() == True:
        birth =True
    
    if data["time"] == "大一上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('必然事件:健康檢查')
        outputList.append('第二次排行程表')
        if VtAchievement:
            status.achievement.being_Vtuber = True
        # 有必然事件就加入
    elif data["time"] == "大一上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('必然事件:系隊')
        outputList.append('期中考')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一上"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        if data["sex"] == "男性":
            outputList.append('必然事件:舞會1-男')
            outputList.append('必然事件:舞會2-男')
        outputList.append('第四次排行程表')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一上"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        if VtAchievement:
            status.achievement.being_Vtuber = True
        reset()

    elif data["time"] == "大一下"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('必然事件:系學會')
        outputList.append('第二次排行程表')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('期中考')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一下"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        if VtAchievement:
            status.achievement.being_Vtuber = True
    elif data["time"] == "大一下"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        if VtAchievement:
            status.achievement.being_Vtuber = True
        reset()
        
    elif data["time"] == "大二上"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
    elif data["time"] == "大二上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
    elif data["time"] == "大二上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('期中考')
    elif data["time"] == "大二上"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('必然事件:比賽')
        outputList.append('第四次排行程表')
    elif data["time"] == "大二上"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        reset()

    elif data["time"] == "大二下"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
    elif data["time"] == "大二下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
    elif data["time"] == "大二下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('期中考')
    elif data["time"] == "大二下"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        outputList.append('必然事件:聯誼')
    elif data["time"] == "大二下"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        reset()

    elif data["time"] == "大三上"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三上"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三上"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('必然事件:實習')
        outputList.append('期末考')
        if DateAchievement:
            status.achievement.christmas = True
        reset()

    elif data["time"] == "大三下"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
        outputList.append('必然事件:Elite')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('必然事件:打疫苗')
        outputList.append('期中考')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三下"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大三下"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        if DateAchievement:
            status.achievement.christmas = True
        reset()

    elif data["time"] == "大四上"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] = "期中考"
        outputList.append('期中考')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四上"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四上"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('必然事件:實習')
        outputList.append('期末考')
        if DateAchievement:
            status.achievement.christmas = True
        reset()

    elif data["time"] == "大四下"  and data["previous_event"] == "期末考":
        data["previous_event"] = "第一次排行程表"
        outputList.append('第一次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] = "第二次排行程表"
        outputList.append('第二次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四下"  and data["previous_event"] == "第二次排行程表":
        outputList.append('必然事件:打疫苗')
        data["previous_event"] = "期中考"
        outputList.append('期中考')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四下"  and data["previous_event"] == "第三次排行程表":
        data["previous_event"] = "第四次排行程表"
        outputList.append('第四次排行程表')
        if DateAchievement:
            status.achievement.christmas = True
    elif data["time"] == "大四下"  and data["previous_event"] == "第四次排行程表":
        data["previous_event"] = "期末考"
        outputList.append('期末考')
        if DateAchievement:
            status.achievement.christmas = True
        reset()

    show.process_event(data, outputList)
