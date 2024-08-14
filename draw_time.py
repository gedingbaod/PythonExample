# -*-coding:utf-8-*-
import PyQt5
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

# 假设有一组时间数据，以小时为单位
# 这里随机生成一些数据作为示例
np.random.seed(0)
time_data_hours = np.random.randint(0, 24, 100)  # 随机生成0-23小时的数据

# 将小时转换为30分钟单位
time_data_30min = time_data_hours * 2 + np.random.choice([0, 1], size=len(time_data_hours))


plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 绘制时间数据的分布情况
plt.figure(figsize=(10, 6))
plt.hist(time_data_30min, bins=range(0, 49), edgecolor='black', align='left')
plt.title('时间数据（30分钟单位）分布情况')
plt.xlabel('时间（30分钟单位）')
plt.ylabel('频数')
plt.xticks(range(0, 49, 2))  # 设置x轴刻度，每2个刻度表示1小时
plt.grid(axis='y')
# plt.draw()
plt.show()
# plt.savefig('test.png')
