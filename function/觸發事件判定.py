import random

# 觸發事件的判斷，每學期有些事件會更新一次，讓事件不會重複發生
study_freq, res_freq, acad_freq, sex_freq, OldExam_freq, First_Date_freq,\
Sugar_freq, preg_freq, Bike_tow_freq = True, True, True, True, True, True, True, True, True


def Vtuber_or_Not():  # 推坑Vt
    if status.social_skill < 40:
        return True
    else:
        return False

def Study_or_not():  # 參加讀書會
    global study_freq
    if status.wisdom > 85 and status.wisdom <  100 and\
       status.social_skill > 70 and study_freq:
        study_freq = False
        return True
    else:
        return False

def Research_or_not():  # 參加研究專案
    global res_freq
    if status.wisdom > 100 and status.wisdom < 115 and\
       status.social_skill > 70 and res_freq:
        res_freq = False
        return True
    else:
        return False

#def Academic_or_not():  # 參加學術研討   # 已取消的項目
#    global acad_freq, abi
#    if abi.wisdom > 115 and abi.social_skill > 70 and acad_freq:
#        acad_freq = False
#        return True


def Sex_or_not():  # 翹課打ㄆ
    global sex_freq
    if status.charm > 90 and sex_freq:
        sex_freq = False
        return True
    else:
        return False

def OldExam_or_not():  # 獲得考古題
    global OldExam_freq
    if status.social_skill > 80 and OldExam_freq:
        OldExam_freq = False
        return True
    else:
        return False

def First_Date():  # 第一次約會
    global First_Date_freq
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
    global Sugar_freq
    if status.charm > 100 and status.love_progress < 10 and Sugar_freq:
        Sugar_freq = False
        return True
    else:
        return False

def Pregnant():  # 懷孕
    global preg_freq
    prob = random.randrange(1, 101)
    if status.charm > 100 and status.luck < 5 and preg_freq and prob < 6:
        preg_freq = False
        return True
    else:
        return False

def Bike_tow():  # 腳踏車被拖吊
    global Bike_tow_freq
    prob = random.randrange(1, 101)
    if status.luck < 20 and Bike_tow_freq and prob < 81:
        Bike_tow_freq = False
        return True
    else:
        return False

outputList = []    
TriIncident_List = ['Vt', 'Study', 'Research', 'Sex', 'Oldexam', 'First_D', 'Marriage', 'S_Daddy', 'Preg', 'Bike']
Yes_or_Not_List = [Vtuber_or_Not(), Study_or_not(), Research_or_not(), Sex_or_not(), OldExam_or_not(), First_Date(), Marriage_or_not(), SugarDaddy(), Pregnant(), Bike_tow()]
for i in range(10):
    if Yes_or_Not_List[i] == True:
        outputList.append(TriIncident_List[i])

for i in outputList:
    show_Trig_events(data, i)
