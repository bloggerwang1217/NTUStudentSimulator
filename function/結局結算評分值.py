import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Noto Sans TC'  # 要顯示中文有點複雜
plt.rcParams['axes.unicode_minus'] = False

point_table = ['愛情進度', '學業成績', '養生', '聲望']
points = [70,80,52,100]  # 我隨便預設的值，應該要讀入結尾數值


# 長與寬可以再討論
x = np.arange(len(point_table))
plt.bar(x, points, color=['red', 'green', 'blue', 'yellow'])
plt.xticks(x, point_table)
plt.xlabel('評分值')
plt.ylabel('分數')
plt.show()
