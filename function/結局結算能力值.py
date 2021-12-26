import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
from datetime import datetime
from time import strftime, gmtime
import os

path = os.getcwd()

title_f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 20)
f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 12)

# plt.rcParams['font.family'] = 'MingLiU'  # 要顯示中文有點複雜
# plt.rcParams['axes.unicode_minus'] = False

class abi():
    pass
ability = abi()
ability.wisdom = 40
ability.charm = 70
ability.fitness = 80
ability.social_skill = 90
ability.health = 50


def abi_illu(abi):
    results = [{"智慧": ability.wisdom, "魅力": ability.charm, 
                "體能": ability.fitness, "社交能力": ability.social_skill,
                "健康": ability.health}]
    data_length = 5
    # 將極座標根據資料長度進行等分
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = ["智慧" + ':' + str(ability.wisdom),
              "魅力" + ':' + str(ability.charm),
              "體能" + ':' + str(ability.fitness),
              "社交能力" + ':' + str(ability.social_skill),
              "健康" + ':' + str(ability.health)]
    print(labels)
    score = [[v for v in result.values()] for result in results]
    print(score)
    # 使雷達圖資料封閉
    score_a = np.concatenate((score[0], [score[0][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 設定圖形的大小
    fig = plt.figure(figsize=(6, 6), dpi=100)
    # 新建一個子圖
    ax = plt.subplot(111, polar=True)
    # 繪製雷達圖
    ax.plot(angles, score_a, color='g')
    # 設定雷達圖中每一項的標籤顯示
    ax.set_thetagrids(angles*180/np.pi, labels, font = f)
    # 設定雷達圖的0度起始位置
    ax.set_theta_zero_location('N')
    # 設定雷達圖的座標刻度範圍
    ax.set_rlim(0, 100)
    # 設定雷達圖的座標值顯示角度，相對於起始角度的偏移量
    ax.set_rlabel_position(270)
    ax.set_title("能力值", font = title_f)
    # plt.legend(["你"], loc='best')
    ax.spines['polar'].set_visible(False)
    now = str(datetime.now())
    plt.savefig(r'C:\Users\周匯森\Desktop\000.png')  # 這裡會選擇存檔路徑與檔名
    plt.show()

"""
now_time = strftime('%Y-%m-%d_%H-%M-%S', gmtime())
fig = plt.figure()
fig.savefig(str(now_time) + '.png')
"""

abi_illu(ability)
