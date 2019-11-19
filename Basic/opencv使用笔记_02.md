---
style: ocean
---
## opencv使用笔记（六）（图像的形态学转换）

- 形态学一般是使用**`二值图像`**，进行**`边界提取，骨架提取，孔洞填充，角点提取，图像重建`**等等。常用的形态学操作时**`腐蚀`**与`膨胀`，在他们的基础上演变出一些变体，包括**`开运算`**、**`闭运算`**、**`梯度`**等等。形态学一般是对**二值图像**进行的操作。
- 下面贴几个比较好的介绍图像形态学方面的博客 
  **图像处理基本算法-形态学** 
  **图像的形态学处理**

###（一）腐蚀

**`关于腐蚀就是将图像的边界腐蚀掉，或者说使得图像整体上看起来变瘦了。`**它的操作原理就是**卷积核沿着图像滑动，** **如果与卷积核对应的原图像的所有像素值都是1，那么中心元素保持原来的值，否则就变为0**。这对于去除白噪声很有用，也可以用于断开两个连载一起的物体。

一个例子如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,1)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(erosion,'gray')

```

![这里写图片描述](http://img.blog.csdn.net/20150712155018421)

### （二）膨胀

膨胀原理与腐蚀相同，**只不过膨胀的时候与卷积核对应的原图像的像素值只要有一个为1，那么中心元素就是1。这么做带来的变化就是图像膨胀了，或者说图像`变胖`了。**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
erosion = cv2.dilate(img,kernel,1)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(erosion,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150712155250367)

### （三）开运算

先进行腐蚀再进行膨胀的运算就是开运算，**腐蚀可以让那些在图像外面的小点点去掉**，然后把主图像膨胀回去，实现去除图像外噪声。这里为了测试，将图像改一改，内外都加点白点试试：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man1.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
erosion = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(erosion,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150712155329721)

可以看到，外面的白点去点了，但是图像里面的白点似乎还在，多多少少影响着图形。

### （四）闭运算

**先进行膨胀再进行腐蚀的运算就是闭运算，膨胀可以让那些`在图像里面的小点点`去掉，然后把主图像腐蚀回去，实现去除图像内噪声。**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man1.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
erosion = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(erosion,'gray')
12345678910
```

![这里写图片描述](http://img.blog.csdn.net/20150712155422479)

###(五)形态学梯度

膨胀与腐蚀的组合使用，使得结果看上去是提取了物体的轮廓一样。

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
closing= cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(closing,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150712155551435)

### （六）礼帽

**原始图像与其进行开运算后的图像进行一个差。**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
closing= cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(closing,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150712155621552)

### （七）黑帽

**原始图像与其进行闭运算后的图像进行一个差。**

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('man.jpg',0) #直接读为灰度图像

kernel = np.ones((5,5),np.uint8)
closing= cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(closing,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150712155647664) 
从运算上讲是这样的，但是这个图下礼帽与黑帽的结果并不是很明显。

##opencv使用笔记（七）（图像梯度与边缘检测）

梯度简单来说就是求导，在图像上表现出来的就是**提取图像的边缘**（不管是横向的、纵向的、斜方向的等等），所需要的无非也是一个**`核模板`**，模板的不同结果也不同。所以可以看到，所有的这些个算子函数，归结到底都可以用函数**`cv2.filter2D()`**来表示，不同的方法给予不同的核模板，然后演化为不同的算子而已。并且这只是这类滤波函数的一个用途，曾经写过一个关于matlab下滤波函数**`imfilter()`**的扩展应用（等同于opencv的**`cv2.filter2D`**函数）：

**图像滤波函数imfilter函数的应用及其扩展**

就是很多复杂的计算都是可以通过这个滤波函数组合实现，这样的话速度快。

### （一）关于Sobel算子与Scharr算子

**`Sobel`**算子是高斯平滑与微分操作的结合体，所以其抗噪能力很强，用途较多。一般的**`sobel`**算子包括x与y两个方向，算子模板为： 
$$
sobel_x=\begin{bmatrix}
-1&0 &1\\
-1&0&2\\
-1&0&1
\end{bmatrix}\\
sobel_y=\begin{bmatrix}
-1&-2 &-1\\
0&0&0\\
1&2&1
\end{bmatrix}\\
$$
在opencv函数中，还可以设置卷积核(ksize)的大小，如果ksize=-1,就演变为3*3的Scharr算子，模板无非变了个数字： 
$$
scharr_x=\begin{bmatrix}
-3&0 &3\\
-10&0&10\\
-3&0&3
\end{bmatrix}\\
scharr_y=\begin{bmatrix}
-1&-10&-3\\
0&0&0\\
3&10&3
\end{bmatrix}
$$
### (二)关于拉普拉斯(Laplacian)算子

**要注意uint8出现截断，需要把图片转为64位** **`img1 = np.float64(img)#转化为浮点型的`**或者用**`cv2.CV_64F`**

拉普拉斯算子可以实现图像的二阶倒数的定义，至于二阶倒数有什么意义，可以看这位博主的详细介绍：

**OpenCV-Python教程（7、Laplacian算子）**

其核模板为： 
$$
scharr_x=\begin{bmatrix}
0&1 &0\\
1&-4&1\\
0&1&0
\end{bmatrix}
$$


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)#默认ksize=3
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelxy = cv2.Sobel(img,cv2.CV_64F,1,1)
laplacian = cv2.Laplacian(img,cv2.CV_64F)#默认ksize=3
#人工生成一个高斯核，去和函数生成的比较
kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)#
img1 = np.float64(img)#转化为浮点型的
img_filter = cv2.filter2D(img1,-1,kernel)
sobelxy1 = cv2.Sobel(img1,-1,1,1)

plt.subplot(221),plt.imshow(sobelx,'gray')
plt.subplot(222),plt.imshow(sobely,'gray')
plt.subplot(223),plt.imshow(sobelxy,'gray')
plt.subplot(224),plt.imshow(laplacian,'gray')

plt.figure()
plt.imshow(img_filter,'gray')
```

![这里写图片描述](http://img.blog.csdn.net/20150712165425613) 
![这里写图片描述](http://img.blog.csdn.net/20150712165438843) 
上述一个很重要的问题需要明白的就是，在滤波函数第二个参数，当我们使用-1表示输出图像与输入图像的数据类型一致时，如果原始图像是**`uint8型`**的，那么在经过算子计算以后，得到的图像可能会有**`负值`**，如果与原图像数据类型一致，那么**负值就会被截断变成0或者255**，使得结果错误，那么针对这种问题有两种方式改变（上述程序中都有）：**一种就是改变输出图像的数据类型**（第二个参数**`cv2.CV_64F`**），**另一种就是改变原始图像的数据类型**（此时第二个参数可以为-1，与原始图像一致）。 
上述程序从结果上也说明使用函数**`cv2.filter2D`**也能达到相同的效果。

### （三）Canny边缘检测算子

关于canny边缘检测算子，细究的话还算比较的复杂，给出一个介绍比较详细的博客吧：

**canny算子**

**`cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges`**

- **mage** – 8-bit input image.
- **edges** – output edge map; single channels 8-bit image, which has the same size as `image` .
- **threshold1** – first threshold for the hysteresis procedure.
- **threshold2** – second threshold for the hysteresis procedure.
- **apertureSize** – aperture size for the [`Sobel()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html#void Sobel(InputArray src, OutputArray dst, int ddepth, int dx, int dy, int ksize, double scale, double delta, int borderType)) operator.
- **L2gradient** – a flag, indicating whether a more accurate ![L_2](https://docs.opencv.org/3.0-beta/_images/math/c80021c104dcee49fc0f685e54711978dff03111.png) norm ![=\sqrt{(dI/dx)^2 + (dI/dy)^2}](https://docs.opencv.org/3.0-beta/_images/math/be14865ba11769377900576b01b30a683f84d091.png)should be used to calculate the image gradient magnitude ( `L2gradient=true` ), or whether the default ![L_1](https://docs.opencv.org/3.0-beta/_images/math/99a8045a334a911a88e1d2e3805e17bd1d254c39.png) norm ![=|dI/dx|+|dI/dy|](https://docs.opencv.org/3.0-beta/_images/math/50098b0fb8a0251ddd4ef15f5b037f7c61dccdb7.png) is enough ( `L2gradient=false` ).

那么opencv中的函数也非常简单，直接**`cv2.Canny()`**，这个函数需要五个参数，**`原始图像`**，两个范围控制值**`minVal`**和**`maxVal`**（见上述原理介绍）,第四个参数用于规定核模板的大小（默认3），最后一个是true与false（默认）的选择，有一点不同，不太重要，可以试着那个好用那个。

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0)
edges = cv2.Canny(img,100,200)#其他的默认
plt.subplot(121),plt.imshow(img,'gray')
plt.subplot(122),plt.imshow(edges,'gray')
```

![这里写图片描述](http://img.blog.csdn.net/20150712165622371)

## opencv使用笔记（八）（图像金字塔）

图像金字塔操作的将是**`图像的像素问题`**（图像变清晰了还是模糊了）（本质上有点像图像的放大与缩小一样(前面介绍过的cv2.resize()函数)）。**图像金字塔是视觉运用中广泛采用的一项技术。**

一般来说我们操作的图像是具有固定分辨率的，但是有些情况下，我们需要对同一图像的不同分辨率的子图像进行处理（尤其是在我们需要提取图像特征的时候）。这个时候我们**需要创建一组新的图像**，这些图像是**具有不同分辨率的原始图像**，那么我们把这组图像讲座图像金字塔。我们把**最大的图像放在底部，最小的放在底部**，看起来就像金字塔。如下所示： 
![这里写图片描述](http://img.blog.csdn.net/20150713211739903) 

### 图像金字塔

- 一个图像金字塔是一系列图像的集合 - 所有图像来源于同一张原始图像 - 通过梯次向下采样获得，直到达到某个终止条件才停止采样。

- 有两种类型的图像金字塔常常出现在文献和应用中:

  - **高斯金字塔(Gaussian pyramid):** 用来向下采样
  - **拉普拉斯金字塔(Laplacian pyramid):** 用来从金字塔低层图像重建上层未采样图像

- 在这篇文档中我们将使用 *高斯金字塔* 。

  #### 高斯金字塔

  - 想想金字塔为一层一层的图像，层级越高，图像越小。

  - 每一层都按从下到上的次序编号， 层级 ![(i+1)](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/03c724ff4c149a75e0dabfe498b5d54a13097ee8.png) (表示为 ![G_{i+1}](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/04bc90f6ab9ae2b72301c8f8c5272d8aa1a97351.png) 尺寸小于层级 ![i](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/34857b3ba74ce5cd8607f3ebd23e9015908ada71.png) (![G_{i}](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/1e35910309fd7fd1668d4b8cb49a996a544b2907.png)))。

  - 为了获取层级为 ![(i+1)](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/03c724ff4c149a75e0dabfe498b5d54a13097ee8.png) 的金字塔图像，我们采用如下方法:

    - 将 ![G_{i}](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/1e35910309fd7fd1668d4b8cb49a996a544b2907.png) 与高斯内核卷积:

      ![\frac{1}{16} \begin{bmatrix} 1 & 4 & 6 & 4 & 1  \\ 4 & 16 & 24 & 16 & 4  \\ 6 & 24 & 36 & 24 & 6  \\ 4 & 16 & 24 & 16 & 4  \\ 1 & 4 & 6 & 4 & 1 \end{bmatrix}](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/1a445c5612efa84c0ae80b4c334e45076fe1687b.png)

    - 将所有偶数行和列去除。

  - 显而易见，**`结果图像只有原图的四分之一`**。通过对输入图像 ![G_{0}](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/210fc2aadea2cfd3ab3f7a5ffc2d674fdc17bf38.png) (原始图像) 不停迭代以上步骤就会得到整个金字塔。

  - 以上过程描述了对图像的向下采样，如果将图像变大呢?:

    - 首先，将图像在每个方向扩大为原来的两倍，新增的行和列以0填充(![0](http://www.opencv.org.cn/opencvdoc/2.3.2/html/_images/math/bc1f9d9bf8a1b606a4188b5ce9a2af1809e27a89.png))
    - 使用先前同样的内核(乘以4)与放大后的图像卷积，获得 “新增像素” 的近似值。

  - 这两个步骤(向下和向上采样) 分别通过OpenCV函数 **`pyrUp`**和 **`pyrDown`**实现, 我们将会在下面的示例中演示如何使用这两个函数。

  `Note:我们向下采样缩小图像的时候, 我们实际上 *丢失* 了一些信息。`

**图像金字塔**的一个比较明显的应用就是**图像匹配中的sift算法**。找了一个介绍好的文章，感兴趣的可以看下：

**图像匹配算法研究之sift算法**

图像金字塔主要有两类：**`高斯金字塔`**和**`拉普拉斯金字塔`**。 
高斯金字塔的**`顶部`**是通过将**底部图像的连续行与列去掉得到的**。**每一层图像中的像素值等于下一层图像中对应位置5个像素的高斯加权平均值**。这样操作一个M\*N的图像就变成了$$ (\frac{M}{2})*(\frac{N}{2}) $$的图像，图像的面积就变为原来的**`1/4*`**，连续进行这样的操作，就会得到一些列的金字塔的图像。Opencv中可以通过函数**`cv2.pyrDown()`**和**`cv2.pyrUp()`**来构建金字塔。函数**`cv2.pyrDown()`**是从一个高分辨率图像变成低分辨率图像的。**`cv2.pyrDown()`**函数接受3个参数：

**`cv2.pyrDown(src[, dst[, dstsize[, borderType]]]) → dst`**

- **src** – input image.
- **dst** – output image; it has the specified size and the same type as `src`.
- **dstsize** – size of the output image.
- **borderType** – Pixel extrapolation method (BORDER_CONSTANT don’t supported). See`borderInterpolate` for details.

By default, **size of the output image** is computed as `Size((src.cols+1)/2, (src.rows+1)/2)`, but in any case, the following conditions should be satisfied:

![\begin{array}{l}| \texttt{dstsize.width} *2-src.cols| \leq  2  \\ | \texttt{dstsize.height} *2-src.rows| \leq  2 \end{array}](https://docs.opencv.org/3.0-beta/_images/math/b03379470ebe836184e7109946e128802a32a588.png)

The function performs the downsampling step of the Gaussian pyramid construction. First, it convolves the source image with the kernel:

![\frac{1}{256} \begin{bmatrix} 1 & 4 & 6 & 4 & 1  \\ 4 & 16 & 24 & 16 & 4  \\ 6 & 24 & 36 & 24 & 6  \\ 4 & 16 & 24 & 16 & 4  \\ 1 & 4 & 6 & 4 & 1 \end{bmatrix}](https://docs.opencv.org/3.0-beta/_images/math/9c3bdf1fb1ce550df9322554b0848bc7959176fa.png)

Then, it downsamples the image by rejecting even rows and columns.

**默认情况下直接输入需要操作的图像就可以，他会把图像按缩小1/4的来处理**。如：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
img1 = cv2.pyrDown(img)
plt.subplot(121),plt.imshow(img,'gray')
plt.subplot(122),plt.imshow(img1,'gray')
12345678
```

![这里写图片描述](http://img.blog.csdn.net/20150713212121961) 
从坐标轴看大小，图像缩小了一倍。像素上可以看出变得更模糊。

**`cv2.pyrUp()`**函数与**`cv2.pyrDown()`**函数的功能相反，把金字塔上层的图像变到下一层来，也就是图像变大，但是有一点要注意的是，虽然变大了，但是**图像并不能恢复成以前的样子**，也就是分辨率上不能达到以前的那种效果（仅仅是变大了而已）。比如对一幅图先**`cv2.pyrDown()`**然后再**`cv2.pyrUp()`**变回来就可以是：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
img1 = cv2.pyrDown(img)
img2 = cv2.pyrUp(img1)
plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(132),plt.imshow(img1,'gray'),plt.title('down')
plt.subplot(133),plt.imshow(img2,'gray'),plt.title('up')
12345678910
```

![这里写图片描述](http://img.blog.csdn.net/20150713212207122)

可以看到经过金字塔**一上一下变换后，图像的大小不变，然而图像的清晰度变差了**（这也是可以理解的，好的可以变成坏的，但是坏的想变成好的那是不可能的）。

图像的拉普拉斯金字塔可以由图像的高斯金字塔得到，转换的公式为： 
$$
L_i=G_i−PyrUp(G_i+1)
$$
**拉普拉斯金字塔的图像看起来就像是边界图，经常被用在图像压缩中**。比如：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
img1 = cv2.pyrDown(img)#高斯金字塔
temp_img1 = cv2.pyrDown(img1)
temp = cv2.pyrUp(temp_img1)
img2 = img1 - temp #拉普拉斯金字塔
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(img1,'gray')
plt.subplot(133),plt.imshow(img2,'gray')
123456789101112
```

![这里写图片描述](http://img.blog.csdn.net/20150713212316291)

## opencv使用笔记（九）（图像直方图）

### (一）图像直方图

图像的构成是由`像素点`构成的，每个`像素点的值`代表着`该点的颜色`（灰度图或者彩色图）。所谓`直方图`就是对`图像的中的这些像素点的值`进行统计，得到`一个统一的整体的灰度概念`。直方图的好处就在于可以清晰了解图像的整体灰度分布，这对于后面依据直方图处理图像来说至关重要。

一般情况下直方图都是灰度图像，**直方图x轴是灰度值（一般0~255）**，**y轴就是图像中每一个灰度级对应的像素点的个数。**

那么如何获得图像的`直方图`？首先来了解绘制直方图需要的一些量：`灰度级`，正常情况下就是`0-255`共256个灰度级，从`最黑`一直到`最亮（白`）（也有可能统计其中的`某部分灰度范围`），那么每一个灰度级对应一个数来储存该灰度对应的点数目。也就是说直方图其实就是一个`1*m（灰度级）`的一个`数组`而已。但是有的时候我们不希望一个一个灰度的递增，比如现在我想15个灰度一起作为一个灰度级来花直方图，这个时候我们可能只需要1*(m/15)这样一个数组就够了。那么这里的`15`就是直方图的`间隔宽度`了。

**`cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) → hist`**

Opencv给我们提供的函数是**`cv2.calcHist()`**，该函数有5个参数：

- **image**-输入图像，传入时应该用中括号`[]`括起来
- **channels**：传入图像的通道，如果是灰度图像，那就不用说了，只有一个通道，值为`0`，如果是彩色图像（有`3个通道`），那么值为`0,1,2`,中选择一个，对应着`BGR`各个通道。这个值也得用`[]`传入。
- **mask**：掩膜图像。`如果统计整幅图，那么为none`。主要是如果要统计部分图的直方图，就得构造相应的炎掩膜来计算。Optional mask. If the matrix is not empty, it must be an **8-bit array of the same size as`images[i]`** . The non-zero mask elements mark the array elements counted in the histogram.
- **histSize**：灰度级的个数，需要`中括号`，比如`[256]`
- **ranges**:像素值的范围，通常`[0,256]`，有的图像如果不是0-256，比如说你来回各种变换导致像素值负值、很大，则需要调整后才可以。

除此之外，强大的numpy也有函数用于统计直方图的，通用的一个函数**`np.histogram`**,还有一个函数是**`np.bincount()`**（用于以为统计直方图，速度更快）。这三个方式的传入参数基本上差不多，不同的是opencv自带的需要中括号括起来。 
对于直方图的显示也是比较简单的，直接**`plt.plot()`**就可以。一个实例如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
#opencv方法读取-cv2.calcHist（速度最快）
#图像，通道[0]-灰度图，掩膜-无，灰度级，像素范围
hist_cv = cv2.calcHist([img],[0],None,[256],[0,256])
#numpy方法读取-np.histogram()
hist_np,bins = np.histogram(img.ravel(),256,[0,256])
#numpy的另一种方法读取-np.bincount()（速度=10倍法2）
hist_np2 = np.bincount(img.ravel(),minlength=256)
plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.plot(hist_cv)
plt.subplot(223),plt.plot(hist_np)
plt.subplot(224),plt.plot(hist_np2)
```

![这里写图片描述](http://img.blog.csdn.net/20150714174631743)

现在来考虑opencv的直方图函数中掩膜的使用，这个掩膜就是一个区域大小，表示你接下来的直方图统计就是这个区域的像素统计。一个例子如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('flower.jpg',0) #直接读为灰度图像
mask = np.zeros(img.shape[:2],np.uint8)
mask[100:200,100:200] = 255
masked_img = cv2.bitwise_and(img,img,mask=mask) 

#opencv方法读取-cv2.calcHist（速度最快）
#图像，通道[0]-灰度图，掩膜-无，灰度级，像素范围
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)1234567891011121314151617
```

![这里写图片描述](http://img.blog.csdn.net/20150714174707917)

### （二）直方图均衡化

图像的直方图是对图像对比度效果上的一种处理，旨在使得图像整体效果均匀，黑与白之间的各个像素级之间的点更均匀一点。 
直方图均衡化只要包括三个步骤：

1. 统计直方图中每个灰度级出现的次数；
2. 计算累计归一化直方图；
3. 重新计算像素点的像素值；

关于原理的详细部分给一个参考：

**直方图均衡化原理**

[百度百科的解释也很棒](http://baike.baidu.com/link?url=RUjahehgkTMDGKwAEyMsHyeMyWWTw9a0KUx2CzLbXtxdZyoF6zqDbJsfEffUQYAwvr7kD9p6cbOxJGYGk1nkZq) 

在opencv有专门函数对直方图进行均衡化使用的函数就是**`cv2.equalizeHist()`**.

**`cv2.equalizeHist(src[, dst]) → dst`**

he function equalizes the histogram of the input image using the following algorithm:

1. Calculate the histogram ![H](https://docs.opencv.org/3.0-beta/_images/math/662c239f3e7a5d3290da0913485987263a7c1ae7.png) for `src` .

2. Normalize the histogram so that the sum of histogram bins is 255.

3. Compute the integral of the histogram:

   ![H'_i =  \sum _{0  \le j < i} H(j)](https://docs.opencv.org/3.0-beta/_images/math/c16cbf978f4cdec23b6a21cc98918603290f9be4.png)

4. Transform the image using ![H'](https://docs.opencv.org/3.0-beta/_images/math/f8bb589a8e50b2008690bf998bd93bb212683009.png) as a look-up table: ![\texttt{dst}(x,y) = H'(\texttt{src}(x,y))](https://docs.opencv.org/3.0-beta/_images/math/010948a7f16acce12df1ea533d164f744f8b501a.png)

**`The algorithm normalizes the brightness and increases the contrast of the image`**.

一个实例如：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
res = cv2.equalizeHist(img)

plt.subplot(121),plt.imshow(img,'gray')
plt.subplot(122),plt.imshow(res,'gray')12345678
```

![这里写图片描述](http://img.blog.csdn.net/20150714174935230)

上述的直方图均衡化可以可能到是一种全局意义上的均衡化，但是有的时候这种操作并不是很好，会把某些不该调整的部分给调整了。Opencv中还有一种直方图均衡化，它是一种局部局部来的均衡化，也就是是说把整个图像分成许多小块（比如按10*10作为一个小块），那么对**每个小块进行均衡化**。这种方法主要对于图像直方图不是那么单一的（比如存在多峰情况）图像比较实用。Opencv中将这种方法称之为`CLAHE`，使用到的函数就是**`cv2.createCLAHE()`**，一个实例如下：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
clahe = cv2.createCLAHE(clipLimit=2,tileGridSize=(10,10))
cl1 = clahe.apply(img)

plt.subplot(121),plt.imshow(img,'gray')
plt.subplot(122),plt.imshow(cl1,'gray')123456789
```

![这里写图片描述](http://img.blog.csdn.net/20150714175021176) 
可以看到，相对于全局的直方图均衡化，这个局部的均衡化似乎得到的效果更自然一点。

## Python下opencv使用笔记（十）（图像频域滤波与傅里叶变换）

前面曾经介绍过**`空间域滤波`**，**`空间域滤波`**就是用**各种模板直接与图像进行卷积运算**，实现对图像的处理，这种方法直接对图像空间操作，操作简单，所以也是空间域滤波。

**`频域滤波`**说到底最终可能是和空间域滤波实现相同的功能，比如实**现图像的轮廓提取**，在空间域滤波中我们使用一个**`拉普拉斯模板`**就可以提取，而在频域内，我们使用一个**`高通滤波模板`**（因为轮廓在频域内属于**`高频信号`**），可以实现**`轮廓的提取`**，后面也会把**拉普拉斯模板频域化**，会发现**拉普拉斯其实在频域来讲就是一个高通滤波器**。

既然是频域滤波就涉及到把图像首先变到频域内，那么把**图像变到频域内的方法**就是**`傅里叶变换`**。关于傅里叶变换，感觉真是个伟大的发明，尤其是其在**`信号领域的应用`**，对于傅里叶变换的理解，要是刚接触这个东西，想要理解还真是非常的困难，除非你的数学功底特别好。这里推荐一个非常好的通俗易懂的博客**(待会再去o-_-)**：

[**傅里叶分析之掐死教程（完整版）**](https://zhuanlan.zhihu.com/wille/19763358)

傅里叶的原理表明，**任何连续测量的时序或信号，都可以表示为`不同频率`的`正弦波信号`的`无限叠加`。**利用傅立叶变换算法**直接测量原始信号，以`累加`方式来计算该信号中`不同正弦波信号的频率`、`振幅`和`相位`就可以表示原始信号。**这里借用上述博客的一个图：![这里写图片描述](http://img.blog.csdn.net/20150721100309770) 
这个图就是把时域图像（大概是`方波`）变成了**一系列的`正弦波`的`线性叠加`**，其等价关系可以表示为： 
$$
f(原始信号)=A_1sin(w_1x+ϕ_1)+A_2sin(w_2x+ϕ_2)+..
$$
那么$w_1$,$w_2$,...可以看成是频率的变化（一般认为就是从1,2,…n定死了），所有的$A$就是对应频率下的振幅，所有的

$ϕ$就是对应频率下的相位，那么对于任一个信号，如果都认为**`频率`**$w$是从**`1,2,3`**…一直增加的话，那么每个信号就只由一组**`振幅`**与一组**`ϕ`**来决定，他们的不同决定了最终信号的不同。

再来理解下什么是`振幅`，振幅就是**各个频率下的信号的决定程度有多大**，如果某个频率的振幅越大，那么**它对原始信号的的重要性越大**，像上图，**当然是w=1的时候振幅最大，说明它对总的信号影响最多**（`去掉w=1的信号，原始信号将严重变形`）。**越往后面，也就是越高频，振幅逐渐减小，那么他们的作用就越小**，而他们对于整体信号又有什么影响呢？既然越小，那就是**影响小，所以其实去掉，原始信号也基本上不变**，他们影响就在于**`对原始信号的细节上的表现`**，比如原始信号上的**`边边角角`**，偶尔有个**`小凸起凹槽`**什么的，这些小细节部分都是靠这些个影响不大的**`高频信号`**来表现出来的。深入推广一下，这就很好理解为什么图像的`高频信号`其实表现出来的就是**图像的边缘轮廓、噪声等等这些细节的东西了**，而`低频信号`，表现的却是图像上**整块整块灰度大概一样的区域**了（这些个区域又称为**`直流分量区域`**）。

再来理解下什么是**`相位`**，**相位表示其实表面对应频率下的正弦分量偏离原点的程度**，再借用下上述博客中的一个图，把分量示意图放大了： 
![这里写图片描述](http://img.blog.csdn.net/20150721100425608) 
上图看到，如果各个频率的分量相位都是0的话，那么每个正弦分量的最大值（在频率轴附近的那个最大值）都会落在频率轴为0上，然而上述图并不是这样。在说简单一点，比如原始信号上有个凹槽，正好是由某一频率的分量叠加出来的，那么如果这个**频率的相位变大一点或者变小一点的话**，带来的影响就会使得这个**凹槽向左或者向右移动一下**，也就是说，**相位的作用就是精确定位到信号上一点的位置的**。

好了，有了上述的概念，再来看看图像的`傅里叶变换`，上述举得例子是一维信号的傅里叶变换，并且信号是连续的，我们知道图像是`二维离散`的，连续与离散都可以用`傅里叶进行变换`，那么`二维信号`无非就是在`x方向`与`y方向`都进行一次`一维`的`傅里叶变换`得到，这么看来，可以想象，它的频率构成就是一个`网格矩阵`了，横轴从$w=1$到$n$，纵轴也是这样。所有图像的频率构成都认为是这样的，那么不同的就是`一幅图的振幅`与`相位`了（振幅与相位此时同样是一个网格矩阵），也就是说你在`opencv`或者`matlab`下对图像进行傅里叶变换后其实是可以得到图像的`振幅图`与`相位图`的，而想把图像从频域空间恢复到时域空间，必须要同时有图像的`振幅图`与`相位图`才可以，缺少一个就恢复的不完整（后面会实验看看）。 
下面看看二维傅里叶变换，一个图像为M*N的图像f(x,y)进过离散傅里叶变换得到$F(u,v)$，那么一般的公式为： 
$$
F(u,v)=\sum _{x=0}^{M−1}\sum _{y=0}^{N−1}f(x,y)e^{−j2π(ux/M+vy/N)}
$$
它的反变换就是 
$$
f(x,y)=\frac{1}{MN}\sum _{x=0}^{M−1}\sum _{y=0}^{N−1}F(u,v)e^{j2π(ux/M+vy/N)}
$$
反变换就可以实现将频域图像恢复到时域图像。对正变换分析，当u=v=0时，那么： 
$$
F(0,0)=\sum _{x=0}^{M−1}\sum _{y=0}^{N−1}f(x,y)=\bar{f}(x,y)
$$
看看这个式子发现它是什么？f(x,y)可是时域里面图像的灰度。很明显，这个东西其实是整个图像的灰度求平均了（这里说的都是灰度图像），当图像进行傅里叶变换以后，你去把F(0,0)与原始图像平均灰度去比较看看是不是一样的。那么F(0,0)在频域内称为直流分量，`其他的所有F称为交流分量`，直流分量可以看到是在0处获得的，所以很明显是存在于`低频分量`下的。

说了这么多，来上个实验看看到底什么是傅里叶变换吧。在python+opencv下想实现图像傅里叶变换有两种途径，一种采用numpy包可以实现，还有opencv自带的可以实现，其中numpy带的使用方便，直观易懂。

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到较小的范围（比如0-255）
s1 = np.log(np.abs(f))
s2 = np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(s1,'gray'),plt.title('original')
plt.subplot(122),plt.imshow(s2,'gray'),plt.title('center')
plt.show()
'''
计算2维离散傅里叶变换

该函数通过快速傅立叶变换（FFT）计算M t>维数组中任何轴上的n离散傅里叶变换。默认情况下，在输入数组的最后两个轴上计算变换，即2维FFT。
'''
'''将零频率分量移动到频谱的中心。

此函数为所有列出的轴交换半角空格（默认为全部）。注意，只有len(x)是偶数时，y[0]才是奈奎斯特分量。'''
```

![这里写图片描述](http://img.blog.csdn.net/20150721100654216) 
注意的是，上图其实并没有什么含义，显示出来的可以看成是**频域后图像的振幅信息，并没有相位信息**，图像的相位$ϕ=\frac{atan(实部)}{atan(虚部)}$，numpy包中自带一个**`angle`**函数可以直接根据复数的实部与虚部求出角度（默认出来的角度是弧度）。像上述程序出来的f与fshift都是复数，就可以直接**`angle`**函数一下，比如试试并把对应的相位图像显示出来：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到较小的范围（比如0-255）
ph_f = np.angle(f)
ph_fshift = np.angle(fshift)

plt.subplot(121),plt.imshow(ph_f,'gray'),plt.title('original')
plt.subplot(122),plt.imshow(ph_fshift,'gray'),plt.title('center')
```

![这里写图片描述](http://img.blog.csdn.net/20150721100817374) 
这就是图像上每个像素点对应的相位图，其实是毫无规律的，理解就是**`偏移的角度`**。

Ok再来说说程序中为什么要有一个**`np.fft.fftshift(f)`**中心化操作，整个图像是在傅里叶变换的一个周期内完成的，将其看成横纵两个方向的一维傅里叶变换，在每个方向上都会有高频信号和低频信号，那么**傅里叶变换将低频信号放在了边缘，高频信号放在了中间**，然**而一副图像，很明显的低频信号多而明显**，所以将**低频信号采用一种方法移到中间，在时域上就是对f乘以（-1）^(M+N)，换到频域里面就是位置的移到了。**

图像变换到频域后就可以进行操作了，目前接触到的频域操作似乎也就是一些滤波操作，如同空域里面的滤波操作一样，不过原理不一样了，后面再说说一些频域滤波方法。好了一旦操作完，得到的数据还是频域数据，那么如何将其变换到时域呢？这里就是**`傅里叶反变换`**了，公式表示就如同前面那样。这个频域变换到时域的操作就是逆向傅里叶变换再走一遍（比如先**反中心化，在逆变换**）。一个实例如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到0-255
s1 = np.log(np.abs(fshift))
plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')
plt.subplot(132),plt.imshow(s1,'gray'),plt.title('center')
# 逆变换
f1shift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f1shift)
#出来的是复数，无法显示
img_back = np.abs(img_back)
plt.subplot(133),plt.imshow(img_back,'gray'),plt.title('img back')
```

![这里写图片描述](http://img.blog.csdn.net/20150721100930951) 
可以看到恢复的一模一样。

我们说，**恢复一个频域图像需要图像的振幅以及相位**，而一个**复数也正好包含这些**，振幅就是实部虚部的平方和开方，相位就是$atan(\frac{实部}{虚部})$，前面说过。那么现在假设我们只用一副图像的振幅或者相位来将频域内图像恢复到时域会怎么样呢？下面给出只用振幅、只用相位以及两者在联合起来来恢复的程序：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#取绝对值：将复数变化成实数
#取对数的目的为了将数据变化到0-255
s1 = np.log(np.abs(fshift))
plt.subplot(221),plt.imshow(img,'gray'),plt.title('original')
plt.xticks([]),plt.yticks([])
#---------------------------------------------
# 逆变换--取绝对值就是振幅
f1shift = np.fft.ifftshift(np.abs(fshift))
img_back = np.fft.ifft2(f1shift)
#出来的是复数，无法显示
img_back = np.abs(img_back)
#调整大小范围便于显示
img_back = (img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))
plt.subplot(222),plt.imshow(img_back,'gray'),plt.title('only Amplitude')
plt.xticks([]),plt.yticks([])
#---------------------------------------------
# 逆变换--取相位
f2shift = np.fft.ifftshift(np.angle(fshift))
img_back = np.fft.ifft2(f2shift)
#出来的是复数，无法显示
img_back = np.abs(img_back)
#调整大小范围便于显示
img_back = (img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))
plt.subplot(223),plt.imshow(img_back,'gray'),plt.title('only phase')
plt.xticks([]),plt.yticks([])
#---------------------------------------------
# 逆变换--将两者合成看看
s1 = np.abs(fshift) #取振幅
s1_angle = np.angle(fshift) #取相位
s1_real = s1*np.cos(s1_angle) #取实部
s1_imag = s1*np.sin(s1_angle) #取虚部
s2 = np.zeros(img.shape,dtype=complex) 
s2.real = np.array(s1_real) #重新赋值给s2
s2.imag = np.array(s1_imag)

f2shift = np.fft.ifftshift(s2) #对新的进行逆变换
img_back = np.fft.ifft2(f2shift)
#出来的是复数，无法显示
img_back = np.abs(img_back)
#调整大小范围便于显示
img_back = (img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))
plt.subplot(224),plt.imshow(img_back,'gray'),plt.title('another way')
plt.xticks([]),plt.yticks([])
```

![这里写图片描述](http://img.blog.csdn.net/20150721101037877) 
可以看到，仅仅振幅的恢复图啥也不是，仅仅的相位图还有那么点意思，当然也是啥也不是。最后是把振幅与相位分别作为频域内复数的实部和虚部，得到的恢复图才与原来的一样。

基于此，我们来做一个有趣的实验，假设有两幅图像，将这两幅图像进行傅里叶变换到频域，然后把用一个图像的振幅做为振幅，用另一幅图像的相位作为相位生成一副新的图像，那么，这个图像会怎么样呢？你觉得生成的图像会更像取振幅的那副还是取相位的那副呢？来看看吧：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_flower = cv2.imread('flower.jpg',0) #直接读为灰度图像
img_man = cv2.imread('woman.jpg',0) #直接读为灰度图像
plt.subplot(221),plt.imshow(img_flower,'gray'),plt.title('origial1')
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(img_man,'gray'),plt.title('origial_2')
plt.xticks([]),plt.yticks([])
#--------------------------------
f1 = np.fft.fft2(img_flower)
f1shift = np.fft.fftshift(f1)
f1_A = np.abs(f1shift) #取振幅
f1_P = np.angle(f1shift) #取相位
#--------------------------------
f2 = np.fft.fft2(img_man)
f2shift = np.fft.fftshift(f2)
f2_A = np.abs(f2shift) #取振幅
f2_P = np.angle(f2shift) #取相位
#---图1的振幅--图2的相位--------------------
img_new1_f = np.zeros(img_flower.shape,dtype=complex) 
img1_real = f1_A*np.cos(f2_P) #取实部
img1_imag = f1_A*np.sin(f2_P) #取虚部
img_new1_f.real = np.array(img1_real) 
img_new1_f.imag = np.array(img1_imag) 
f3shift = np.fft.ifftshift(img_new1_f) #对新的进行逆变换
img_new1 = np.fft.ifft2(f3shift)
#出来的是复数，无法显示
img_new1 = np.abs(img_new1)
#调整大小范围便于显示
img_new1 = (img_new1-np.amin(img_new1))/(np.amax(img_new1)-np.amin(img_new1))
plt.subplot(223),plt.imshow(img_new1,'gray'),plt.title('another way')
plt.xticks([]),plt.yticks([])
#---图2的振幅--图1的相位--------------------
img_new2_f = np.zeros(img_flower.shape,dtype=complex) 
img2_real = f2_A*np.cos(f1_P) #取实部
img2_imag = f2_A*np.sin(f1_P) #取虚部
img_new2_f.real = np.array(img2_real) 
img_new2_f.imag = np.array(img2_imag) 
f4shift = np.fft.ifftshift(img_new2_f) #对新的进行逆变换
img_new2 = np.fft.ifft2(f4shift)
#出来的是复数，无法显示
img_new2 = np.abs(img_new2)
#调整大小范围便于显示
img_new2 = (img_new2-np.amin(img_new2))/(np.amax(img_new2)-np.amin(img_new2))
plt.subplot(224),plt.imshow(img_new2,'gray'),plt.title('another way')
plt.xticks([]),plt.yticks([])
```

![这里写图片描述](http://img.blog.csdn.net/20150721101129923) 
这就是合成的图像，是不是很有趣，图像3是图1的振幅加图2的相位，图像4是图1的相位加上图2的振幅。很明显的可以看到，**新图像占用谁的相位就越像谁**，为什么会这样？很简单，可以理解**振幅不过描述图像灰度的亮度**，占用**谁的振幅不过使得结果哪些部分偏亮或者暗而已**，而**`图像是个什么样子是由它的相位决定的`**。相位描述的是一个方向，方向正确了，那么最终的结果离你的目的就不远了。可想而知，方向对于一件事物是多么的重要，大自然的规律尚且如此，更别说做人做事了，找准并相信一个方向，慢慢的走下去吧，总有一天会看到成果的，哪怕你的振幅不对，走的慢一点，但是最终也能走的像模像样的，不会说到了人生的最后，回头一看，再来感叹哎呀这是什么玩意，那就很悲哀了。

好了，扯回来我们的问题，关于傅里叶变换下的图像恢复基本上就是这了。但是我们发现，似乎我们只说了开头（怎么变换）和结尾（怎么变回去），那么中间我们要做的东西才是傅里叶变换的目的—频域下的各种变化操作。

这里主要介绍**`频域下的滤波–低通滤波器`**，**`高通滤波器`**，**`带通带阻滤波器`**。

我们知道，图像在变换加移动中心后，**从中间到外面，频率上依次是从低频到高频的**，那么我们如果把中间规定一小部分去掉，**`是不是相对于把低频信号去掉了呢？这也就是相当于进行了高通滤波。`**这个滤波模板画出来可能就是这样的：

![这里写图片描述](http://img.blog.csdn.net/20150721101233451) 
黑色为0，白色为1，**把这个模板去和图像进过傅里叶变换的频域矩阵去与（相乘）一下就实现了高通滤波。**比如下面：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_man = cv2.imread('woman.jpg',0) #直接读为灰度图像
plt.subplot(121),plt.imshow(img_man,'gray'),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
rows,cols = img_man.shape
mask = np.ones(img_man.shape,np.uint8)
mask[rows/2-30:rows/2+30,cols/2-30:cols/2+30] = 0
#--------------------------------
f1 = np.fft.fft2(img_man)
f1shift = np.fft.fftshift(f1)
f1shift = f1shift*mask
f2shift = np.fft.ifftshift(f1shift) #对新的进行逆变换
img_new = np.fft.ifft2(f2shift)
#出来的是复数，无法显示
img_new = np.abs(img_new)
#调整大小范围便于显示
img_new = (img_new-np.amin(img_new))/(np.amax(img_new)-np.amin(img_new))
plt.subplot(122),plt.imshow(img_new,'gray'),plt.title('Highpass')
plt.xticks([]),plt.yticks([])
```

![这里写图片描述](http://img.blog.csdn.net/20150721101310909) 
可以看到，**高通滤波器有利于提取图像的轮廓**，这里我们从原理上分析一下为什么，**图像的轮廓或者边缘或者一些噪声处，灰度变化剧烈，那么在把它们经过傅里叶变换后，就会变成高频信号**（我们知道**`高频时捕捉细节`**的），所以在**把图像低频信号滤掉以后剩下的自然就是轮廓**了。

反过来我们来看看空间域滤波中的拉普拉斯模板，我们知道这个模板是这样的
$$
M=\begin{bmatrix}
0&-1&0\\
-1&4&-1\\
0&-1&0\\
\end{bmatrix}
$$
现在我们把这个模板进行傅里叶变换到频域看看：

```python
import numpy as np
import matplotlib.pyplot as plt

laplacian = np.array([[0,1,0],[1,-4,1],[0,1,0]])
f = np.fft.fft2(laplacian)
f1shift = np.fft.fftshift(f)
img = np.log(np.abs(f1shift))
plt.imshow(img,'gray')
```

![这里写图片描述](http://img.blog.csdn.net/20150721101401932) 
可以看到，这个模板的频域变换下**四周特别亮**，也就是是个**高通滤波器**。其它空间域下的模板都可以转到频域下来看看。

下面再来试试**`低通滤波器`**什么效果，构造个低通滤波器也很简单，**把上述模板中的1变成0,0变成1**，其实就是低通了：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_man = cv2.imread('woman.jpg',0) #直接读为灰度图像
plt.subplot(121),plt.imshow(img_man,'gray'),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
rows,cols = img_man.shape
mask = np.zeros(img_man.shape,np.uint8)
mask[rows/2-20:rows/2+20,cols/2-20:cols/2+20] = 1
#--------------------------------
f1 = np.fft.fft2(img_man)
f1shift = np.fft.fftshift(f1)
f1shift = f1shift*mask
f2shift = np.fft.ifftshift(f1shift) #对新的进行逆变换
img_new = np.fft.ifft2(f2shift)
#出来的是复数，无法显示
img_new = np.abs(img_new)
#调整大小范围便于显示
img_new = (img_new-np.amin(img_new))/(np.amax(img_new)-np.amin(img_new))
plt.subplot(122),plt.imshow(img_new,'gray'),plt.title('Highpass')
plt.xticks([]),plt.yticks([])1234567891011121314151617181920212223
```

![这里写图片描述](http://img.blog.csdn.net/20150721101454923) 
可以看到**低通滤波后图像除了轮廓模糊了外，基本上没什么变化**，图像的大部分信息基本上都保持了。从原理上来看，**图像的主要信息都集中在低频**上，所以低通滤波器的效果是这样也是可以理解的。上述的高通、低通滤波器的构造有0,1构成的理想滤波器，也是最简单的滤波器，还有一些其他的滤波器，比如说高斯滤波器，butterworth滤波器等等，下面是参考冈萨雷斯书上的图： 
![这里写图片描述](http://img.blog.csdn.net/20150721101518238)

还有就是把高通低通都结合一部分到一个模板上形成的**`带通滤波器`**，这在一些场合会很有用，还是以理想的带通滤波器实验下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_man = cv2.imread('woman.jpg',0) #直接读为灰度图像
plt.subplot(121),plt.imshow(img_man,'gray'),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
rows,cols = img_man.shape
mask1 = np.ones(img_man.shape,np.uint8)
mask1[rows/2-8:rows/2+8,cols/2-8:cols/2+8] = 0
mask2 = np.zeros(img_man.shape,np.uint8)
mask2[rows/2-80:rows/2+80,cols/2-80:cols/2+80] = 1
mask = mask1*mask2
#--------------------------------
f1 = np.fft.fft2(img_man)
f1shift = np.fft.fftshift(f1)
f1shift = f1shift*mask
f2shift = np.fft.ifftshift(f1shift) #对新的进行逆变换
img_new = np.fft.ifft2(f2shift)
#出来的是复数，无法显示
img_new = np.abs(img_new)
#调整大小范围便于显示
img_new = (img_new-np.amin(img_new))/(np.amax(img_new)-np.amin(img_new))
plt.subplot(122),plt.imshow(img_new,'gray')
plt.xticks([]),plt.yticks([])
```

![这里写图片描述](http://img.blog.csdn.net/20150721101603980)

这就是带通的效果，既可以保留一部分低频，也可以保留一部分高频，至于保留多少，怎么保留就视问题的不同而不同了。

当然频域滤波的应用绝不仅限于此，更多的应用还有待探索学习。



## opencv使用笔记（十一）（详解hough变换检测直线与圆）

在数字图像中，往往存在着一些特殊形状的几何图形，像检测马路边一条直线，检测人眼的圆形等等，有时我们需要把这些特定图形检测出来，**`hough`**变换就是这样一种检测的工具。

#### (一)原理

**`Hough变换`**的原理是将特定图形上的点变换到一组参数空间上，根据参数空间点的累计结果找到一个极大值对应的解，那么这个解就对应着要寻找的几何形状的参数（比如说直线，那么就会得到直线的斜率k与常熟b，圆就会得到圆心与半径等等）。

关于**`hough变换`**，核心以及难点就是关于就是有原始空间到参数空间的变换上。以直线检测为例，假设有一条直线**`L`**，原点到该直线的垂直距离为p，垂线与x轴夹角为θ，那么这条直线是唯一的，且直线的方程为 $ρ=xcosθ+ysinθ$ 如下图所示： 
![这里写图片描述](http://img.blog.csdn.net/20150723210916294) 
可以看到的是这条直线在极坐标系下只有一个$(ρ,θ)$与之对应，随便改变其中一个参数的大小，变换到空间域上的这个直线将会改变。好了，再回来看看这个空间域上的这条直线上的所有点吧，你会发现，这条直线上的所有点都可以是在极坐标为(ρ,θ)所表示的直线上的，为什么说是都可以在，因为其中随便的一个点也可以在其他的(ρ,θ)所表示的直线上，就比如上述的(x,y)吧，它可以再很多直线上，准确的说，在经过这个点的直线上，随便画两条如下： 
![这里写图片描述](http://img.blog.csdn.net/20150723210936248) 
可以看到，光是空间上的一个点在极坐标系下就可能在很多极坐标对所对应的直线上，具体有多少个极坐标对呢？那得看你的$θ$的步长了，我们可以看到θ无非是从$0-360$度$（0−2π）$变化，假设我们没$10$度一走取一个直线（这个点在这个直线上），那么我们走一圈是不是取了$36$条直线，也就对应$36$个极坐标对没错吧，那么这个极坐标对，画在坐标轴上是什么样子的呢？因为$θ$是从$0−2π$，并且一个点定了，如果一个θ也定了，你想想它对应的直线的$ρ$会怎么样，自然也是唯一的。那么这个点在极坐标下对应的$(ρ,θ)$出来一个周期可能就是这样的，以$θ$为x轴的话： 
![这里写图片描述](http://img.blog.csdn.net/20150723211003943) 
ok前面说的是单单这一个点对应的极坐标系下的参数对，那么如果每个点都这么找一圈呢？也就是每个点在参数空间上都对应一系列参数对吧，现在把它们画在同一个坐标系下会怎么样呢？为了方便，假设在这个直线上取3个点画一下： 
![这里写图片描述](http://img.blog.csdn.net/20150723211022936) 
那么可以看到，**首先对于每一个点，在极坐标下，会存在一个周期的曲线来表示通过这个点**，其次，**这三个极坐标曲线同时经过一个点**，要搞清楚的是，极坐标上每一个点对$(ρ,θ)$在空间坐标上都是对应一条直线的。好了，同时经过的这一个点有什么含义呢？它表示在空间坐标系下，有一条直线可以经过点1，经过点2，经过点3，这是什么意思？说明这三个点在一条直线上吧。**反过来再来看这个极坐标系下的曲线，那么我们只需要找到交点最多的点，把它返回到空间域就是这个需要找的直线了**。为什么是找相交最多的点，因为上面这只是三个点的曲线，当空间上很多点都画出来的时候，那么相交的点可能就不知上述看到的一个点了，可能有多个曲线相交点，但是有一点，势必是一条直线上的所有点汇成的交点是曲线相交次数最多的。

再来分析这个算法。可以看到**`hough变换`**就是参数映射变换。对每一个点都进行映射，并且每一个映射还不止一次，**(ρ,θ)都是存在步长的，像一个点映射成一个(ρ,θ)，以θ取步长为例，当θ取得步长大的时候，映射的(ρ,θ)对少些，反之则多**，但是我们又看到，映射后的点对是需要求交点的，上述画出来的曲线是连续的，然而实际上因为θ步长的存在，他不可能是连续的，像上上个图一样，是离散的。那么当θ步长取得比较大的时候，你还想有很多交点是不可能的，因为这个时候是离散的曲线然后再去相交，所以说θ步长不能太大，**理论上是越小效果越好，因为越小，越接近于连续曲线，也就越容易相交**，但是越小带来的问题就是需要非常多的内存，计算机不会有那么多内存给你的，并且越小，计算量越大，想想一个点就需要映射那么多次，每次映射是需要计算的，耗时的。那么再想想对于一副图像所有点都进行映射，随便假设一副100\*100的图像（很小吧），就有10000个点，对每个点假设就映射36组(ρ,θ)参数（此时角度的步长是10度了，10度，已经非常大的一个概念了），那么总共需要映射360000次，在考虑每次映射计算的时间吧。可想而知，hough是多么耗时耗力。所以必须对其进行改进。首先就是对图像进行改进，100\*100的图像，10000个点，是不是每个点都要计算？大可不必，**我们只需要在开始把图像进行一个轮廓提取，一般使用`canny算子`就可以，生成黑白二值图像，白的是轮廓，那么在映射的时候，只需要把轮廓上的点进行参数空间变换**，为什么提轮廓？想想无论检测图像中存在的直线呀圆呀，它们都是轮廓鲜明的。那么需要变换的点可能就从`10000`个点降到可能`1000`个点了，这也就是为什么看到许多`hough变换`提取形状时为什么要把`图像提取轮廓`，变成`二值图像`了。

继续算法，分析这么多，可想而知那么一个`hough变换`在算法设计上就可以如下步骤： 
（1）将参数空间(ρ,θ)量化，赋初值一个二维矩阵M，M(ρ,θ)就是一个累加器了。 
（2）然后对图像边界上的每一个点进行变换，变换到属于哪一组(ρ,θ)，就把该组(ρ,θ)对应的累加器数加1，这里的需要变换的点就是上面说的经过边缘提取以后的图像了。 
（3）当所有点处理完成后，就来分析得到的M(ρ,θ)，设置一个阈值T，认为当M(ρ,θ)>T，就认为存在一条有意义的直线存在。而对应的M(ρ,θ)就是这组直线的参数，至于T是多少，自己去式，试的比较合适为止。 
（4）有了M(ρ,θ)和点（x,y）计算出来这个直线就ok了。

说了这么多，这就是原理上`hough变换`的最底层原理，事实上完全可以自己写程序去实现这些，然而，也说过，`hough变换`是一个耗时耗力的算法，`自己写循环实现通常很慢，曾经用matlab写过这个`，也有实际的hough变换例子可以看看：

[**虹膜识别（三）：Hough变换检测内圆边缘**](http://blog.csdn.net/on2way/article/details/40790559)

#### (二)cv2.HoughLines

**`cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]) → lines`**

- **image** – 8-bit, single-channel binary source image. The image may be modified by the function.

  - **lines** – Output vector of lines. Each line is represented by a two-element vector$(\rho,\theta)$ $\rho$is the distance from the coordinate origin$(0,0)$ (top-left corner of the image) $\theta$ is the line rotation angle in radians$(0-vertical\ line,\pi/2-horizontal\ line)$

- **rho** – Distance resolution of the accumulator in pixels.

- **theta** – Angle resolution of the accumulator in radians.

- **threshold** – Accumulator threshold parameter. Only those lines are returned that get enough votes ( ![>\texttt{threshold}](https://docs.opencv.org/3.0-beta/_images/math/6104115b7991b520555581f27af6a3da5c991419.png) ).

- **srn** – For the multi-scale Hough transform, it is a divisor for the distance resolution `rho` . The coarse accumulator distance resolution is `rho` and the accurate accumulator resolution is`rho/srn` . If both `srn=0` and `stn=0` , the classical Hough transform is used. Otherwise, both these parameters should be positive.

- **stn** – For the multi-scale Hough transform, it is a divisor for the distance resolution `theta`.

- **min_theta** – For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 0 and max_theta.

- **max_theta** – For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between min_theta and CV_PI.

- method–

  One of the following Hough transform variants:

  - **CV_HOUGH_STANDARD** classical or standard Hough transform. Every line is represented by two floating-point numbers ![(\rho, \theta)](https://docs.opencv.org/3.0-beta/_images/math/9dade0b8c81764b99b163a1ac2ef198e74a32045.png) , where ![\rho](https://docs.opencv.org/3.0-beta/_images/math/2b6a0a1d67cf5985b52f3c718c5a9bc38c01e568.png) is a distance between (0,0) point and the line, and![\theta](https://docs.opencv.org/3.0-beta/_images/math/f324df69016bcdbbc6a6b842f7cdb42d6b305049.png) is the angle between x-axis and the normal to the line. Thus, the matrix must be (the created sequence will be) of `CV_32FC2` type
  - **CV_HOUGH_PROBABILISTIC** probabilistic Hough transform (more efficient in case if the picture contains a few long linear segments). It returns line segments rather than the whole line. Each segment is represented by starting and ending points, and the matrix must be (the created sequence will be) of the `CV_32SC4` type.
  - **CV_HOUGH_MULTI_SCALE** multi-scale variant of the classical Hough transform. The lines are encoded the same way as `CV_HOUGH_STANDARD`.

- param1–

  First method-dependent parameter:

  - For the classical Hough transform, it is not used (0).
  - For the probabilistic Hough transform, it is the minimum line length.
  - For the multi-scale Hough transform, it is `srn`.

- param2–

  Second method-dependent parameter:

  - For the classical Hough transform, it is not used (0).
  - For the probabilistic Hough transform, it is the maximum gap between line segments lying on the same line to treat them as a single line segment (that is, to join them).
  - For the multi-scale Hough transform, it is `stn`.

那么我们在实际中大可不必自己写，opencv已经集成了`hough变换`的函数，调用它的函数效率高，也很简单。 
Opencv中检测直线的函数有`cv2.HoughLines()`，`cv2.HoughLinesP()` 
函数`cv2.HoughLines()`返回值有三个（opencv 3.0），实际是个二维矩阵，表述的就是上述的`(ρ,θ)`，其中`ρ`的单位是像素长度（也就是直线到图像原点(0,0)点的距离），而`θ`的单位是弧度。这个函数有四个输入，第一个是`二值图像`，上述的`canny变换后的图像`，二三参数分别是`ρ和θ的精确度`，可以理解为`步长`。第四个参数为`阈值T`，认为当`累加器中的值高于T是才认为是一条直线`。自己画了个图实验一下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('line.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
#open to see how to use: cv2.Canny
#http://blog.csdn.net/on2way/article/details/46851451 
edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
#hough transform
lines = cv2.HoughLines(edges,1,np.pi/180,160)
lines1 = lines[:,0,:]#提取为为二维
for rho,theta in lines1[:]: 
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a*rho
  y0 = b*rho
  x1 = int(x0 + 1000*(-b))
  y1 = int(y0 + 1000*(a))
  x2 = int(x0 - 1000*(-b))
  y2 = int(y0 - 1000*(a)) 
  cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])
plt.show()
```

![这里写图片描述](http://img.blog.csdn.net/20150723211957273)

测试一个新的图，不停的改变 cv2.HoughLines最后一个阈值参数到合理的时候如下： 
![这里写图片描述](http://img.blog.csdn.net/20150723212036871) 
可以看到检测的还可以的。

#### (三)cv2.HoughLinesP()

**`cv2.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]) → lines`**

函数**`cv2.HoughLinesP()`**是一种概率直线检测，我们知道，原理上讲hough变换是一个耗时耗力的算法，尤其是每一个点计算，即使经过了canny转换了有的时候点的个数依然是庞大的，这个时候我们采取一种概率挑选机制，**不是所有的点都计算，而是随机的选取一些个点来计算**，相当于降采样了。这样的话我们的阈值设置上也要降低一些。在参数输入输出上，输入不过多了两个参数：**`minLineLengh`**(线的最短长度，比这个短的都被忽略)和**`MaxLineCap`**（两条直线之间的最大间隔，小于此值，认为是一条直线）。输出上也变了，不再是直线参数的，这个函数输出的**直接就是直线点的坐标位置**，**这样可以省去一系列for循环中的由参数空间到图像的实际坐标点的转换。**

- **image** – 8-bit, single-channel binary source image. The image may be modified by the function.
- **lines** – Output vector of lines. Each line is represented by a 4-element vector ![(x_1, y_1, x_2, y_2)](https://docs.opencv.org/3.0-beta/_images/math/fba9fafd757b09fb79bb1e3195225e4da1915881.png) , where ![(x_1,y_1)](https://docs.opencv.org/3.0-beta/_images/math/d7765429cb69b57687846d15872a6782137ffab3.png) and ![(x_2, y_2)](https://docs.opencv.org/3.0-beta/_images/math/ae2e7abf8c35578f2d86ddf13f088e5dd2c33905.png) are the ending points of each detected line segment.
- **rho** – Distance resolution of the accumulator in pixels.
- **theta** – Angle resolution of the accumulator in radians.
- **threshold** – Accumulator threshold parameter. Only those lines are returned that get enough votes ( ![>\texttt{threshold}](https://docs.opencv.org/3.0-beta/_images/math/6104115b7991b520555581f27af6a3da5c991419.png) ).
- **minLineLength** – Minimum line length. Line segments shorter than that are rejected.
- **maxLineGap** – Maximum allowed gap between points on the same line to link them.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('room.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
#open to see how to use: cv2.Canny
#http://blog.csdn.net/on2way/article/details/46851451 
edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
#hough transform
lines = cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength=60,maxLineGap=10)
lines1 = lines[:,0,:]#提取为二维
for x1,y1,x2,y2 in lines1[:]: 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])12345678910111213141516171819
```

![这里写图片描述](http://img.blog.csdn.net/20150723212118184) 
可以看到这个方法似乎更好些，速度还快，调参数得到较好的效果就ok了。

Ok说完了直线的检测，再来说说圆环的检测，我们知道圆的数学表示为： 
$$
(x−x_{center})^2+(y−y_{center})^2=r^2
$$
从而一个圆的确定需要三个参数，那么就需要三层循环来实现（比直线的多一层），从容把图像上的所有点映射到三维参数空间上。其他的就一样了，寻找参数空间累加器的最大（或者大于某一阈值）的值。那么理论上圆的检测将比直线更耗时，然而opencv对其进行了优化，用了一种**`霍夫梯度法`**，感兴趣去研究吧，我们只要知道它能**优化算法的效率**就可以了。关于函数参数输入输出： 

**`cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles`**

- **image** – 8-bit, single-channel, grayscale input image.
- **circles** – Output vector of found circles. Each vector is encoded as a 3-element floating-point vector $(x,y,radius)$
- **method** – Detection method to use. Currently, the only implemented method is`CV_HOUGH_GRADIENT` , which is basically *21HT* , described in [[Yuen90\]](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/feature_detection.html?highlight=cv2.houghlines#yuen90).
- **dp** – Inverse ratio of the accumulator resolution to the image resolution. For example, if `dp=1` , the accumulator has the same resolution as the input image. If `dp=2` , the accumulator has half as big width and height.
- **minDist** – Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
- **param1** – First method-specific parameter. In case of `CV_HOUGH_GRADIENT` , it is the higher threshold of the two passed to the [`Canny()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/feature_detection.html?highlight=cv2.houghlines#void Canny(InputArray image, OutputArray edges, double threshold1, double threshold2, int apertureSize, bool L2gradient)) edge detector (the lower one is twice smaller).
- **param2** – Second method-specific parameter. In case of `CV_HOUGH_GRADIENT` , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
- **minRadius** – Minimum circle radius.
- **maxRadius** – Maximum circle radius.

这个时候输入为灰度图像，同时最好规定检测的圆的最大最小半径，不能盲目的检测，否侧浪费时间空间。输出就是三个参数空间矩阵。 

来个实际点的人眼图像，把minRadius和maxRadius调到大圆范围检测如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('eye.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 

plt.subplot(121),plt.imshow(gray,'gray')
plt.xticks([]),plt.yticks([])
#hough transform
circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,
100,param1=100,param2=30,minRadius=200,maxRadius=300)
circles = circles1[0,:,:]#提取为二维
circles = np.uint16(np.around(circles))#四舍五入，取整
for i in circles[:]: 
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)#画圆
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)#画圆心

plt.subplot(122),plt.imshow(img)
plt.xticks([]),plt.yticks([])
```

![这里写图片描述](http://img.blog.csdn.net/20150723212337411)

把半径范围调小点，检测内圆：

![这里写图片描述](http://img.blog.csdn.net/20150723212357710) 
至此圆的检测就是这样

## opencv使用笔记（十二）（k均值算法之图像分割）

k均值（kmeans）聚类是一种最为简单的聚类方法，直接根据数据点之间的距离（**欧氏距离，几何距离**等等）来划分数据是属于哪一类的，当所有数据点所属的类别不在变化的时候，聚类也就完成了。详细原理可索引下面一个博客：

[**聚类分析笔记-K均值matlab算法（一）**](http://blog.csdn.net/on2way/article/details/41828323)

**关于kmeans再谈几点认识：**

1. 重要的一点：聚类数目的问题。**有的聚类、分类问题已经限制好了要聚类成几类，也就是聚类数目一定，那么这种聚类通常简单些，直接规定聚类数就好了**。而有的聚类问题不知道分成几类才好，这个时候怎么办？那么就需要找到一种**评价指标去评价聚类成多少类是最好的**。比如说当聚类完了以后，可以计算一下类间的中心点的距离以及类内所有数据之间的距离和等等，作为判断标准，像DBI分类评价指标就是建立在这种基础上的。还有一种分类：减聚类分类，这也是在不知道分类数的时候进行的分类。
2. 关于初始聚类中心的确定。Kmeans分类其实是具有收敛性的，所以**初始聚类中心对其影响并不是很大**，只要开始不相同就可以。因为在每次迭代完成以后，新的聚类中心是根据新划分类的所有点取平均而来的，所以不再受制于初始聚类中心。**只是说聚类中心会影响迭代的次数**，以当前计算机的速度，这点影响带来的耗时是可以不计的。
3. 关于迭代终止条件。迭代终止条件可以有很多种，但是核心就是如何判定分类基本上已经收敛了，或者非常接近最优解，收敛不动了。一般情况下，可以设定迭代次数作为终止条件，还可以设定所有聚类中心在上下两次迭代过程中不发生变化时认为收敛，或者前后两次迭代的类中心之间的距离差小于某一个小的常数时认为收敛

关于opencv下的kmean算法，函数为**`cv2.kmeans()`** 
函数的格式为：

**`cv2.kmeans(data, K, bestLabels, criteria, attempts, flags[, centers]) → retval, bestLabels, centers`**

(1)**data**: 分类数据，最好是**`np.float32`**的数据，每个特征放一列。之所以是**`np.float32`**原因是这种数据类型运算速度快，同样的数据下如果是uint型数据将会慢死你。 
(2) **K**: 分类数，
(3) **bestLabels**：预设的分类标签：没有的话 None 
(4) **criteria**：迭代停止的模式选择，这是一个含有三个元素的元组型数。格式为（type,max_iter,epsilon） 
其中，type又有两种选择： 

- > cv2.TERM_CRITERIA_EPS :精确度（误差）满足epsilon停止。 

- > cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter停止。 

- > cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER，两者合体，任意一个满足结束。 

- > attempts：重复试验kmeans算法次数，将会返回最好的一次结果 

  **flags**：初始类中心选择，两种方法 

- **KMEANS_RANDOM_CENTERS** Select random initial centers in each attempt.

- **KMEANS_PP_CENTERS** Use `kmeans++` center initialization by Arthur and Vassilvitskii [Arthur2007].

- **KMEANS_USE_INITIAL_LABELS** During the first (and possibly the only) attempt, use the user-supplied labels instead of computing them from the initial centers. For the second and further attempts, use the random or semi-random centers. Use one of `KMEANS_*_CENTERS` flag to specify the exact method.

下面使用这个函数对灰度图像进行分类。首先需要明白的一点是输入数据变换到一维。因为我们是对整个图像进行聚类，所以他们的灰度值都属于一个特征（维度）内的，而图像属于二维的，所以不能直接当data输入进去，需要将图像转化为一个长条或者长链的一维数据。我们说data结束数据，每一个特征放一列，灰度图像聚类的灰度值就是一个特征。若果说是彩色图像聚类，**那么这个时候需要分别把RGB三个通道转化为一维才行**。最后把分类结果以图像的形式显示出来的时候，需要把长条或者长链的标签再变回来才行。详细代码如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('woman.jpg',0)#image read be 'gray'
plt.subplot(121),plt.imshow(img,'gray'),plt.title('original')
plt.xticks([]),plt.yticks([])

#change img(2D) to 1D
img1 = img.reshape((img.shape[0]*img.shape[1],1))
img1 = np.float32(img1)

#define criteria = (type,max_iter,epsilon)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

#set flags: hou to choose the initial center
#---cv2.KMEANS_PP_CENTERS ; cv2.KMEANS_RANDOM_CENTERS
flags = cv2.KMEANS_RANDOM_CENTERS
# apply kmenas
compactness,labels,centers = cv2.kmeans(img1,4,None,criteria,10,flags)

img2 = labels.reshape((img.shape[0],img.shape[1]))
plt.subplot(122),plt.imshow(img2,'gray'),plt.title('kmeans')
plt.xticks([]),plt.yticks([])123456789101112131415161718192021222324
```

![这里写图片描述](http://img.blog.csdn.net/20150724114407461)

这就是设置分成4类的结果。