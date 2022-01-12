import function.status as status
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib import font_manager as fm
from time import strftime, gmtime
from datetime import datetime


path = os.getcwd()

title_f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 20)
f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf", size = 12)


def abi_illu(wisdom, charm, fitness, social, health):
    results = [{"智慧": wisdom, "魅力": charm, 
                "體能": fitness, "社交能力": social,
                "健康": int(health)}]
    data_length = 5
    # 將極座標根據資料長度進行等分
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = ["智慧" + ':' + str(wisdom),
              "魅力" + ':' + str(charm),
              "體能" + ':' + str(fitness),
              "社交能力" + ':' + str(social),
              "健康" + ':' + str(int(health))]

    score = [[v for v in result.values()] for result in results]
    for i in range(5):
        if score[0][i] <= 0:
            score[0][i] = 1

    # 使雷達圖資料封閉
    score_a = np.concatenate((score[0], [score[0][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 設定圖形的大小
    fig = plt.figure(figsize=(6, 6), dpi=90)
    # 新建一個子圖
    ax = plt.subplot(111, polar=True)
    # 繪製雷達圖
    ax.plot(angles, score_a, color='g')
    # 設定雷達圖中每一項的標籤顯示
    ax.set_thetagrids(angles*180/np.pi, labels, font = f)
    # 設定雷達圖的0度起始位置
    ax.set_theta_zero_location('N')
    # 設定雷達圖的座標刻度範圍
    ax.set_rlim(0, max(wisdom, charm, fitness, social, int(health))+20)
    # 設定雷達圖的座標值顯示角度，相對於起始角度的偏移量
    ax.set_rlabel_position(270)
    ax.set_title("能力值", font = title_f)
    now = str(datetime.now()).split(".")[0]
    now = now.split(" ")
    name = "_".join(now[0].split("-")) + "_" + "_".join(now[1].split(":"))
    ax.spines['polar'].set_visible(False)
    plt.savefig(f"figure/ability/{name}.png")  # 這裡會選擇存檔路徑與檔名
    return name