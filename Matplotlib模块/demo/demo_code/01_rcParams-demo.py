import matplotlib.font_manager
import matplotlib.pyplot as plt

plt.rcParams['savefig.dpi'] = 100
plt.rcParams['figure.dpi'] = 100
"""
默认的像素：[6,4]，分辨率为72，图片尺寸为 432 x 288
指定dpi=200，图片尺寸为 1200 x 800
指定dpi=300，图片尺寸为 1800 x 1200
设置figsize可以在不改变分辨率情况下改变比例

"""
myfont = matplotlib.font_manager.FontProperties(family='SimHei')
#这种方法不推荐，会改变所有的字体
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
plt.plot([1, 2, 3], [4, 3, -1])
plt.xlabel('横坐标', fontproperties=myfont)
plt.ylabel('纵坐标', fontproperties=myfont)

plt.show()


