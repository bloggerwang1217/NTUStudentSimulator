import random


To_New_World_freq, Too_Stupid_freq = True, True

def blow_wind():  # 樓頂吹風
    if status.social_skill <= 0 or status.wisdom <= 0 or status.fitness <= 0 or status.charm <= 0 or status.health <= 0:
        return True


def To_New_World():  # 轉生異世界
    prob = random.randrange(1, 101)
    if status.luck < 5 and prob < 2 and To_New_World_freq:
        return True
    elif status.luck < 5 and prob > 1 and To_New_World_freq:  # 一學期只會判定一次
        To_New_World_freq = False


def Me_First():  # 明明是我先來的
    if status.charm > 90 and love_progress < 40:
        return True


def Too_Stupid():  # 被二一
    global pass_or_not
    if pass_or_not:
        return True


def Broke():  # 破產
    if status.Money <= -50000:
        return True


def Wealth_Freedom():  # 財富自由
    if status.Money >= 1000000:
        return True


def IntoDust():  # 火化
    if status.health <= 0:
        return True


outputList = []
Incident_List = ['樓頂吹風', '轉生異世界', '明明是我先來的', '被二一', '破產', '財富自由', '火化']
Mid_End = [blow_wind(), To_New_World(), Me_First(), Too_Stupid(), Broke(), Wealth_Freedom(), IntoDust()]
for i in range(7):
    if Mid_End[i] = True:
        outputList.append(Incident_List[i])
 
if outputList != []:
    for i in outputList:
        show_MidEnd_events(data, i)
else:
    pass

