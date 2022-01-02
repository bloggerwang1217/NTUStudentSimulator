import random
import function.show_event as show

status = "" 

# 觸發事件的判斷，每學期有些事件會更新一次，讓事件不會重複發生
study_freq, res_freq, acad_freq, sex_freq, OldExam_freq, First_Date_freq,\
Sugar_freq, preg_freq, Bike_tow_freq = True, True, True, True, True, True, True, True, True
def reset():
    study_freq, res_freq, acad_freq, sex_freq, OldExam_freq,\
    Sugar_freq, Bike_tow_freq = True, True, True, True, True, True, True


def Vtuber_or_Not():  # 推坑Vt
    global status
    if status.social < 40:
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
    if status.charm > 90 and sex_freq:
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
    global First_Date_freq, status
    if status.love_progress > 40 and First_Date_freq:
        First_Date_freq = False
        return True
    else:
        return False

def Marriage_or_not():  # 婚姻抉擇
    if status.love_progress >= 100:
        return True
    else:
        return False

def SugarDaddy():  # 不想努力了
    global Sugar_freq, status
    if status.charm > 100 and status.love_progress < 10 and Sugar_freq:
        Sugar_freq = False
        return True
    else:
        return False

def Pregnant():  # 懷孕
    global preg_freq, status
    prob = random.randrange(1, 101)
    if status.charm > 100 and status.luck < 5 and preg_freq and prob < 6:
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

def check_event(data):
    global status
    status = data["status"]

    outputList = []    
    TriIncident_List = ['觸發事件:推坑Vt', '觸發事件:參加讀書會', '觸發事件:參加研究專案', '觸發事件:翹課打ㄆ', '觸發事件:獲得考古題', '觸發事件:第一次約會', '觸發事件:婚姻抉擇', '觸發事件:不想努力了', '觸發事件:懷孕', '觸發事件:腳踏車被拖吊']
    Yes_or_Not_List = [Vtuber_or_Not(), Study_or_not(), Research_or_not(), Sex_or_not(), OldExam_or_not(), First_Date(), Marriage_or_not(), SugarDaddy(), Pregnant(), Bike_tow()]
    for i in range(10):
        if Yes_or_Not_List[i] == True:
            outputList.append(TriIncident_List[i])

    if data["time"] == "大一上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('必然事件:健康檢查')
        # 有必然事件就加入
    if data["time"] == "大一上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大一上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大一上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大一上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    if data["time"] == "大一下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大一下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('必然事件:社團')
        outputList.append('第二次排行程表')
    if data["time"] == "大一下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大一下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('必然事件:舞會')
        outputList.append('第一次排行程表')
    if data["time"] == "大一下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大一下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()
        
    if data["time"] == "大二上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大二上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('必然事件:比賽')
    if data["time"] == "大二上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    if data["time"] == "大二下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大二下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大二下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大二下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
        outputList.append('必然事件:聯誼')
    if data["time"] == "大二下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    if data["time"] == "大三上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
    if data["time"] == "大三上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('必然事件:實習')
        outputList.append('期末考')
        reset()

    if data["time"] == "大三下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('必然事件:打疫苗')
        outputList.append('第二次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大三下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    if data["time"] == "大四上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大四上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    if data["time"] == "大四下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
    if data["time"] == "大四下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        reset()

    print(outputList)
    show.process_event(data, outputList)
