import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
from datetime import datetime
from time import strftime, gmtime
import os
import function.status as status

path = os.getcwd()

title_f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 20)
f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 12)




def score_illu(ability):
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
