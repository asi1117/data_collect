import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(12, 8))
# plt.figure(figsize=(12, 8))

# 输入统计数据
# waters = ('SamsungGear', 'OculusRift', 'OculusRiftS', 'ViveCosmos', 'VivePro', 'VivePro2', 'ValueIndex', 'Pimax5kSeries', 'Pimax8KSeries', 'OculusGo', 'OculusQuest', 'OculusQuest2')
# buy_number_male = [0.82, 0.90, 0.84, 0.84, 0.82, 0.62, 0.88, 0.80, 0.66, 0.86, 0.94, 0.94]
# buy_number_female = [0.80, 0.86, 0.70, 0.56, 0.64, 0.62, 0.40, 0.71, 0.69, 0.80, 0.88, 0.89]
waters = ('SamsungGear', 'VivePro2', 'Pimax8KSeries', 'Pimax5kSeries',  'ViveCosmos', 'OculusRiftS',  'ValueIndex', 'VivePro', 'OculusRift', 'OculusGo', 'OculusQuest', 'OculusQuest2')
buy_number_male = [0.82, 0.62, 0.66, 0.80,  0.82, 0.84, 0.88, 0.88, 0.90, 0.86, 0.94, 0.94]
buy_number_female = [0.80, 0.62, 0.69, 0.71, 0.56, 0.70, 0.40,  0.80, 0.86, 0.80, 0.88, 0.89]

bar_width = 0.4  # 条形宽度
index_male = np.arange(len(waters))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='Amazon_Rating')
plt.bar(index_female, height=buy_number_female, width=bar_width, color='g', label='DRR_Rating')



plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, waters, rotation=25)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('percentage')  # 纵坐标轴标题
plt.title('recommendation')  # 图形标题

for i in range(1, 12):
    # if i == 0:
    #     clor = 'black'
    if i >= 9:
        clor = 'purple'
    else:
        clor = 'red'
    ax.get_xticklabels()[i].set_color(clor)
plt.savefig('recommend.jpg',dpi=500)
plt.show()
