"""
小筆記

1）當前面的觸發事件被觸發後，需要記下次數或布林值
2）製作成就畫面
"""


# 用於判斷，只跑一次

achieveSex = False
achieveVtuber = False
achieveStocks = False
achieveChristmas = False
achieveBirth = False


def checkAchievement(number_of_sex, being_Vtuber, stocks, christmas, birth):

    """
    判斷成就程式，傳入相關成就觸發的條件
    """
    global achieveSex
    global achieveVtuber
    global achieveStocks
    global achieveChristmas
    global achieveBirth

    if number_of_sex == 8 and achieveSex == False:
        achieveSex = True
        achievement.loveMaster()

    if being_Vtuber is True and achieveVtuber == False:
        achieveVtuber = True
        achievement.peko()

    if stocks is True and achieveStocks == False:
        achieveStocks = True
        achievement.superChieves()

    if christmas is True and achieveChristmas == False:
        achieveChristmas = True
        achievement.legendChallenger()

    if birth is True and achieveBirth == False:
        achieveBirth = True
        achievement.giftBirth()


class Achievement():

    """
    成就程式（被處罰）
    """

    def loveMaster(self):  # 情場浪子
        print('唷，恭喜你達成“情場浪子”成就！')
        return


    def peko(self):  # 好油ㄛpeko
        print('唷，恭喜你達成“好油ㄛpeko”成就！')
        return


    def superChieves(self):  # 超級絕命韭菜
        print('唷，恭喜你達成“超級絕命韭菜”成就！')
        return


    def legendChallenger(self):  # 傳說挑戰者
        print('唷，恭喜你達成“傳說挑戰者”成就！')
        return


    def giftBirth(self):  # 送子鳥之禮
        print('唷，恭喜你達成“送子鳥之禮”成就！')
        return

achievement = Achievement()

# 測試
checkAchievement(3, True, False, False, False)
checkAchievement(3, True, False, False, False)
checkAchievement(8, True, False, False, False)
checkAchievement(8, True, False, True, False)
checkAchievement(8, True, False, True, False)
checkAchievement(8, True, False, True, True)
checkAchievement(8, True, True, True, True)
checkAchievement(8, True, True, True, True)
