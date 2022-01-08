import function.status as status
import function.觸發事件判定 as trig

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
achieveMoney = False


def checkAchievement(number_of_sex, being_Vtuber, christmas, birth, stocks, moneyman):

    """
    判斷成就程式，傳入相關成就觸發的條件
    """
    global achieveSex
    global achieveVtuber
    global achieveStocks
    global achieveChristmas
    global achieveBirth
    global achieveMoney

    if number_of_sex == 8 and achieveSex == False:
        achieveSex = True
        achievement.loveMaster()

    if being_Vtuber and achieveVtuber == False:
        achieveVtuber = True
        achievement.peko()

    if status.stocks_surfing == 3 and achieveStocks == False:
        achieveStocks = True
        achievement.superChieves()

    if christmas and achieveChristmas == False:
        achieveChristmas = True
        achievement.legendChallenger()

    if birth and achieveBirth == False:
        achieveBirth = True
        achievement.giftBirth()

    if status.money >= 0:
        achieveMoney = True
        achievement.MoneyMan()

class Achievement():

    """
    成就程式（被觸發）
    """

    def loveMaster(self):  # 情場浪子
        print('唷，恭喜你達成「情場浪子」成就！')
        return


    def peko(self):  # 好油ㄛpeko
        print('唷，恭喜你達成「好油ㄛpeko」成就！')
        return


    def superChieves(self):  # 超級絕命韭菜
        print('唷，恭喜你達成「超級絕命韭菜」成就！')
        return


    def legendChallenger(self):  # 傳說挑戰者
        print('唷，恭喜你達成「傳說挑戰者」成就！')
        return


    def giftBirth(self):  # 送子鳥之禮
        print('唷，恭喜你達成「送子鳥之禮」成就！')
        return
    
    def MoneyMan(self):  # 金錢管理大師
        print('待安排')
        return

achievement = Achievement()

checkAchievement(trig.achieve(), status.stocks_surfing, status.money)
