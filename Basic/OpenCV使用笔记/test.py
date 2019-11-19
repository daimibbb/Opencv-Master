import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/lena.jpg', 0) # 打开为灰度图像
plt.imshow(img, 'gray')
plt.xticks([]), plt.yticks([])       # 隐藏坐标线 
plt.show()