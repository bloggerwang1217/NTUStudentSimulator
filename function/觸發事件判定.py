import random

class ability():
    pass
abi = ability()
abi.wisdom = 99
abi.social_skill = 75
abi.love_progress = 42
abi.luck = 15
abi.charm = 70



# 觸發事件的判斷，每學期有些事件會更新一次，讓事件不會重複發生
study_freq, res_freq, acad_freq, sex_freq, OldExam_freq, First_Date_freq,\
Sugar_freq, preg_freq, Bike_tow_freq = True, True, True, True, True, True, True, True, True


def Vtuber_or_Not():  # 推坑Vt
    global abi
    if abi.social_skill < 40:
        return True


def Study_or_not():  # 參加讀書會
    global study_freq, abi
    if abi.wisdom > 85 and abi.wisdom <  100 and\
       abi.social_skill > 70 and study_freq:
        study_freq = False
        abi.wisdom = 101  # 可以拔除，測試用
        return True


def Research_or_not():  # 參加研究專案
    global res_freq, abi
    if abi.wisdom > 100 and abi.wisdom < 115 and\
       abi.social_skill > 70 and res_freq:
        res_freq = False
        abi.wisdom = 116  # 可以拔除，測試用
        return True


def Academic_or_not():  # 參加學術研討
    global acad_freq, abi
    if abi.wisdom > 115 and abi.social_skill > 70 and acad_freq:
        acad_freq = False
        return True


def Sex_or_not():  # 翹課打ㄆ
    global sex_freq, abi
    if abi.charm > 90 and sex_freq:
        sex_freq = False
        return True


def OldExam_or_not():  # 獲得考古題
    global OldExam_freq, abi
    if abi.social_skill > 80 and OldExam_freq:
        OldExam_freq = False
        return True


def First_Date():  # 第一次約會
    global First_Date_freq, abi
    if abi.love_progress > 40 and First_Date_freq:
        First_Date_freq = False
        return True


def Marriage_or_not():  # 婚姻抉擇
    global abi
    if abi.love_progress >= 100:
        return True


def SugarDaddy():  # 不想努力了
    global Sugar_freq, abi
    if abi.charm > 100 and love_progress < 10 and Sugar_freq:
        Sugar_freq = False
        return True


def Pregnant():  # 懷孕
    global preg_freq, abi
    prob = random.randrange(1, 101)
    if abi.charm > 100 and abi.luck < 5 and\
        preg_freq and prob < 6:
        preg_freq = False
        return True


def Bike_tow():  # 腳踏車被拖吊
    global Bike_tow_freq, abi
    prob = random.randrange(1, 101)
    if abi.luck < 20 and Bike_tow_freq and prob < 81:
        Bike_tow_freq = False
        return prob  # 這裡回傳機率，若小於80即被拖吊



for i in range(10):  # 測試十次
    print(Vtuber_or_Not(), Academic_or_not(), Research_or_not(), Study_or_not(),
          Sex_or_not(), OldExam_or_not(), First_Date(), 
          Marriage_or_not(), SugarDaddy(), Pregnant(), Bike_tow())
