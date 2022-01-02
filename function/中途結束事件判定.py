import random
import function.show_event as show

status = "" 

To_New_World_freq, Too_Stupid_freq = True, True

def blow_wind():  # 樓頂吹風
    global status
    if status.social<= 0 or status.wisdom <= 0 or status.fitness <= 0 or status.charm <= 0 or status.health <= 0:
        return True


def To_New_World():  # 轉生異世界
    global status
    prob = random.randrange(1, 101)
    if status.luck < 5 and prob < 2 and To_New_World_freq:
        return True
    elif status.luck < 5 and prob > 1 and To_New_World_freq:  # 一學期只會判定一次
        To_New_World_freq = False


def Me_First():  # 明明是我先來的
    global status
    if status.charm > 90 and love_progress < 40:
        return True


def Too_Stupid():  # 被二一
    global pass_or_not, status
    if pass_or_not:  # 暫定
        return True


def Broke():  # 破產
    global status
    if status.Money <= -50000:
        return True


def Wealth_Freedom():  # 財富自由
    global status
    if status.Money >= 1000000:
        return True


def IntoDust():  # 火化
    global status
    if status.health <= 0:
        return True

    
def check_event(data):
    global status
    status = data["status"]
    
    outputList = []
    Incident_List = ['中途結束事件：樓頂吹風', '中途結束事件：轉生異世界', '中途結束事件：明明是我先來的', '中途結束事件：被二一', '中途結束事件：破產', '中途結束事件：財富自由', '中途結束事件：火化']
    Mid_End = [blow_wind(), To_New_World(), Me_First(), Too_Stupid(), Broke(), Wealth_Freedom(), IntoDust()]
    for i in range(7):
        if Mid_End[i] = True:
            outputList.append(Incident_List[i])
            
    if len(outputList) > 1:
        prob = random.randrange(0, len(outputList))
        outputList = outputList[prob]
        
    if data["time"] == "大一上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('必然事件:健康檢查')
        # 有必然事件就加入
    if data["time"] == "大一上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大一上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大一上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大一上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        To_New_World_freq, Too_Stupid_freq = True, True

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
        To_New_World_freq, Too_Stupid_freq = True, True
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
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大二上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大二上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('必然事件:比賽')
    if data["time"] == "大二上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        To_New_World_freq, Too_Stupid_freq = True, True

    if data["time"] == "大二下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大二下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大二下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
        To_New_World_freq, Too_Stupid_freq = True, True
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
        To_New_World_freq, Too_Stupid_freq = True, True

    if data["time"] == "大三上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大三上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        To_New_World_freq, Too_Stupid_freq = True, True
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
        To_New_World_freq, Too_Stupid_freq = True, True

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
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大三下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大三下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        To_New_World_freq, Too_Stupid_freq = True, True

    if data["time"] == "大四上"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大四上"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四上"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        To_New_World_freq, Too_Stupid_freq = True, True

    if data["time"] == "大四下"  and data["previous_event"] == "期末考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期中考"
        outputList.append('期中考')
        To_New_World_freq, Too_Stupid_freq = True, True
    if data["time"] == "大四下"  and data["previous_event"] == "期中考":
        data["previous_event"] == "第一次排行程表"
        outputList.append('第一次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第一次排行程表":
        data["previous_event"] == "第二次排行程表"
        outputList.append('第二次排行程表')
    if data["time"] == "大四下"  and data["previous_event"] == "第二次排行程表":
        data["previous_event"] == "期末考"
        outputList.append('期末考')
        
    print(outputList)
    process_event(data, outputList)  # 一旦觸發中途結束，將直接結束遊戲
