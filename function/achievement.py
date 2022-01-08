import function.status as status
import function.觸發事件判定 as trig

"""
小筆記

1）當前面的觸發事件被觸發後，需要記下次數或布林值
2）製作成就畫面
"""



# 用於判斷，只跑一次

# achieveSex = False
# achieveVtuber = False
# achieveStocks = False
# achieveChristmas = False
# achieveBirth = False
# achieveMoney = False


def checkAchievement(data):
    achievement = data["status"].achievement
    achievement_queue = []

    """
    判斷成就程式，傳入相關成就觸發的條件
    """

    if achievement.number_of_sex == 8:
        achievement_queue.append("情場浪子")

    if achievement.being_Vtuber:
        achievement_queue.append("好油ㄛpeko")

    if achievement.stocks_surfing == 3:
        achievement_queue.append("超級絕命韭菜")

    if achievement.christmas:
        achievement_queue.append("傳說挑戰者")

    if achievement.birth:
        achievement_queue.append("送子鳥之禮")

    if data["status"].money >= 0:
        achievement_queue.append("金錢管理大師")

    return achievement_queue


class Achievement():

    def __init__(self):
        self.number_of_sex = 0
        self.being_Vtuber = False
        self.stocks_surfing = 0:
        self.christmas = False
        self.birth = False

# achievement = Achievement()

# checkAchievement(trig.achieve(), status.stocks_surfing, status.money)
