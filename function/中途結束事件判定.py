import random

class ability():
    pass
abi = ability()
abi.wisdom = 99
abi.social_skill = 75
abi.love_progress = 42
abi.luck = 15
abi.charm = 70
abi.Money = 0
abi.health = 5
pass_or_not = True




To_New_World_freq, Too_Stupid_freq = True, True

def blow_wind():  # 樓頂吹風
    global abi
    if abi.social_skill <= 0 or abi.wisdom <= 0: # 這裡需要參考所有的值，故暫定
        return True


def To_New_World():  # 轉生異世界
    global abi
    prob = random.randrange(1, 101)
    if abi.luck < 5 and prob < 2 and To_New_World_freq:
        return True
    elif abi.luck < 5 and prob >1 and To_New_World_freq:
        To_New_World_freq = False


def Me_First():  # 明明是我先來的
    global abi
    if abi.charm > 90 and love_progress < 40:
        return True


def Too_Stupid():  # 被二一
    global pass_or_not
    if pass_or_not:
        return True


def Broke():  # 破產
    global abi
    if abi.Money <= 0:  # 尚未決定
        return True


def Wealth_Freedom():  # 財富自由
    global abi
    if abi.Money >= 100000:  # 尚未決定
        return True


def IntoDust():  # 火化
    global abi
    if abi.health <= 0:
        return True



print(blow_wind(), To_New_World(), Me_First(), Too_Stupid(),
      Broke(), Wealth_Freedom(), IntoDust())

