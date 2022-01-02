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




def score_illu(love_progress, grade, yang_sheng, prestige):
    global status
    status = data["status"]

    
    point_table = [{'愛情進度':love_progress, '學業成績':grade, 
                    '養生':yang_sheng, '聲望':prestige}]
    points = [status.love_progress,
              status.grade,
              status.yang_sheng,
              status.prestige]  # 應該要讀入結尾數值
    # 圖形長與寬可以再討論
    x = np.arange(len(point_table))
    plt.bar(x, points, color=['red', 'green', 'blue', 'yellow'])
    plt.xticks(x, point_table)
    plt.xlabel('評分值')
    plt.ylabel('分數')
    plt.savefig(figure/ability/finalpix.png)  # 這裡會選擇存檔路徑與檔名
    return 'finalpix'
    
