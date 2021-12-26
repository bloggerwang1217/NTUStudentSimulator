import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot

class abi():
    pass
ability = abi()
ability.love_progress = 40
ability.grade = 70
ability.yang_sheng = 80
ability.prestige = 90



def score_illu(ability):
    plt.rcParams['font.family'] = 'MingLiU'  # 要顯示中文有點複雜
    plt.rcParams['axes.unicode_minus'] = False
    point_table = ['愛情進度', '學業成績', '養生', '聲望']
    points = [ability.love_progress,
              ability.grade,
              ability.yang_sheng,
              ability.prestige]  # 我隨便預設的值，應該要讀入結尾數值
    # 圖形長與寬可以再討論
    x = np.arange(len(point_table))
    plt.bar(x, points, color=['red', 'green', 'blue', 'yellow'])
    plt.xticks(x, point_table)
    plt.xlabel('評分值')
    plt.ylabel('分數')
    plt.savefig(r'C:\Users\周匯森\Desktop\00.png')  # 這裡會選擇存檔路徑與檔名
    plt.show()
    
score_illu(ability)
