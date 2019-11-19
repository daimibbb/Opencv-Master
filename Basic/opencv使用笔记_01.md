---
typora-root-url: 图片库
typora-copy-images-to: 图片库
style: ocean
---

## opencv使用笔记（一）（图像简单读取、显示与储存）



从去年开始关注python这个软件，途中间间断断看与学过一些关于python的东西，感觉python确实是一个简单优美、容易上手的脚本编程语言，众多的第三方库使得python异常的强大，可以处理许多不同的问题，同时它的许多开源免费的库使得python的使用也是十分的广泛。在科学计算、数据处理与图像领域，自己曾经一直在使用matlab，感觉matlab也是一个语言优美、简单方便的编程语言，都说matlab与python在某些领域是非常相似的，确实是这样，就科学计算、数据处理上真是，matlab中许多科学计算的东西在python中基本上都有对应的库包包含进去，比如numpy，matplotlib等等，这些都是强大而又适用的，但是要说不同，那就是应用层面的了，matlab是一个商业性质的软件，正版软件也是异常的贵，个人感觉属于研究性领域的用的较多，在工作后好像一般都不怎么用这个（可能比较贵的缘故），但是总的来说matlab同样在计算领域是强大无比的。 

Opencv是一个开源的计算机视觉库，从开始研究图像方面，并没有真正接触过它，使用的都是matlab带的图像处理库，现在看来他们很多函数也是那么的神似。但是opencv毕竟是一个专业性的库包，里面的许多函数matlab并没有，并且从其使用面及推广程度上看，opencv确实也是那么强大。所以在图像领域了解opencv（无论是python版本的还是C++版本的）都是必要的，但是对于简单适用的学习者来说，了解了解python版的就足够了。

在读取图像之前，你得把你的做实验的图像事先放到工作目录下才行。读取函数是cv2.imread()，关于函数说明： 
cv2.imread(‘图像名称’，’可选参数’) 
可选参数决定读入图像的模式： 
**0：读入的为灰度图像**（即使图像为彩色的） 
**1：读入的图像为彩色的**（默认）； 
注意的是：即使图像在工作空间不存在，这个函数也不会报错，只不过读入的结果为none。好了，读入一个图像就是这样的： 

```python
import cv2 
img = cv2.imread('flower.jpg') 
```


当你的import cv2运行后没有错误了，那么就导入成功了。

### 储存图像

储存图像函数：cv2.imwrite(‘保存的图像名’，图像，‘参数’) 
正常的图像储存使用就是cv2.imwrite(‘保存的图像名’，图像），后面一个参数默认，保存的图像名还得带类型，比如jpg，bmp等等，OpenCV目前支持读取bmp、jpg、png、tiff等常用格式，第三个参数较复杂，还得分是jpg、bmp等等图像的类型不同而不同，其实就是决定了图像储存大小，清晰度的，默认的就很好， 
那么在得到一副图像想储存，比如就直接：```cv2.imwrite(‘good_gray.tif’,img)```

### 图像显示

Opencv自带显示图像函数，但是较为复杂而且个人感觉不稳定，这里在介绍一种显示方法，就是使用库包matplotlib（这个库包Ipython自带）来显示图像。 
首先是opencv自带函数显示，一般要显示一个图像，在图像有了之后，然后直接下面函数一起组合使用：

```python
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

函数`cv2.imshow`的第一个参数是`名字`，第二个是要`显示的图`。然而为了让图像在显示屏上停留才有了下面两句话一起使用。由于系统（32位与64位）的不一样，有的时候会出现显示不出来，个人感觉opencv本身c语言写的，存在着系统上的差异，而且这种显示方法无法保存图像、调整图像大小等等，这里介绍另一种常用且强大的显示图像方法，`使用matplotlib库包中的pyplot子包来显示`，这种显示方法不但稳定，`还可以调整大小`、保存显示的图像等等。那么一般它的使用方法如下：

```python
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('good.jpg',0);#打开为灰度图像
plt.imshow(img, 'gray') #必须规定为显示的为什么图像
plt.xticks([]),plt.yticks([]) #隐藏坐标线 
plt.show() #显示出来
```

## opencv使用笔记（二）（简单几何图像绘制）

简单几何图像一般包括点、直线、矩阵、圆、椭圆、多边形等等。首先认识一下opencv对像素点的定义。图像的一个像素点有1或者3个值，对灰度图像有一个灰度值，对彩色图像有3个值组成一个像素值，他们表现出不同的颜色。 
那么有了点才能组成各种多边形。

### （一）首先绘制直线

函数为：**`cv2.line（img,pt1,pt2,color,thickness=1,line_type=8 shift=0）`** 

- **img** – Image.

- **pt1** – First point of the line segment.

- **pt2** – Second point of the line segment.

- **color** – Line color.

- **thickness** – Line thickness.

- lineType–

  Type of the line:

  - **LINE_8** (or omitted) - 8-connected line.
  - **LINE_4** - 4-connected line.
  - **LINE_AA** - antialiased line.

- **shift** – Number of fractional bits in the point coordinates.  点坐标中位数的个数。

  有值的代表有默认值，不用给也行。可以看到这个函数主要接受参数为两个点的坐标，线的颜色（彩色图像的话颜色就是一个1*3的数组）如下：

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  img = np.zeros((512,512),np.uint8)+255#生成一个空灰度图像
  cv2.line(img,(0,0),(511,511),255,5)
  plt.imshow(img,'gray')
  ```

  ![line](E:\machine_learning\opencv\line.jpg)

  ​

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.line(img,(0,0),(511,511),(155,155,155),5)
plt.imshow(img,'brg')
```

![line_01](E:\machine_learning\opencv\line_01.jpg)

### （二）绘制矩形

函数：` cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → img`

需要确定的就是矩形的两个点（左上角与右下角），颜色，线的类型（不设置就默认）。 
比如：

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)+255#生成一个空彩色图像
cv2.rectangle(img,(20,20),(411,411),(55,255,155),5)
plt.imshow(img,'brg')
```

![rectangle](E:\machine_learning\opencv\rectangle.jpg)

### 三）绘制圆形

绘制圆形也很简单，只需要确定圆心与半径，

函数：**` cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) → img`** 
比如：

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.circle(img,(200,200),50,(55,255,155),1)#修改最后一个参数
plt.imshow(img,'brg')
```

![circle](E:\machine_learning\opencv\circle.jpg)

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.circle(img,(200,200),50,(55,255,155),8)#修改最后一个参数
plt.imshow(img,'brg')123456
```

### （四）绘制椭圆

椭圆比较复杂，涉及到长轴短轴，椭圆圆心

- **` ``cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) → img`**


- **` ``cv2.``ellipse`(img, box, color[, thickness[, lineType]]) → img  

  | Parameters: | **img** – Image                          |
  | ----------- | ---------------------------------------- |
  |             | **center** – Center of the ellipse.      |
  |             | **axes** – Half of the size of the ellipse main axes. |
  |             | **angle** – Ellipse rotation angle in degrees. |
  |             | **startAngle** – Starting angle of the elliptic arc in degrees. |
  |             | **endAngle** – Ending angle of the elliptic arc in degrees. |
  |             | **box** – Alternative ellipse representation via [`RotatedRect`](https://docs.opencv.org/3.0-beta/modules/core/doc/basic_structures.html#RotatedRect) or `CvBox2D`. This means that the function draws an ellipse inscribed in the rotated rectangle. |
  |             | **color** – Ellipse color.               |
  |             | **thickness** – Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that a filled ellipse sector is to be drawn. |
  |             | **lineType** – Type of the ellipse boundary. See the [`line()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/drawing_functions.html?highlight=cv2.rectangle#void line(InputOutputArray img, Point pt1, Point pt2, const Scalar& color, int thickness, int lineType, int shift)) description. |
  |             | **shift** – Number of fractional bits in the coordinates of the center and values of axes. |

![../../../_images/ellipse.png](https://docs.opencv.org/3.0-beta/_images/ellipse.png)

```python
mport cv2
import numpy as np
from matplotlib import pyplot as plt
img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
cv2.ellipse(img,(256,256),(150,100),0,0,180,250,-1)

# 注意最后一个参数-1，表示对图像进行填充，默认是不填充的，如果去掉，只有椭圆轮廓了

plt.imshow(img,'brg')
```

![ellips](E:\machine_learning\opencv\ellips.jpg)

## opencv使用笔记（三）（图像的几何变换）

- 写在之前 
  二维与三维图像的几何变换在计算机图形学上有重要的应用，包括现在的许多图像界面的切换、二维与三维游戏画面控制等等都涉及到图像几何变换，就比如说在三维游戏中，控制角色三维移动的时候，画面是要跟着移动的，那么怎么移动，怎么让上一时刻的画面移动到这一时刻，这都是根据了你的移动量，然后找到三维坐标之间的对应关系，用这一时刻的坐标替换到上一时刻的坐标像素值实现图像的切换。

- 图像的几何变换主要包括：**`平移、扩大与缩小、旋转、仿射、透视`**等等。图像变换是建立在矩阵运算基础上的，通过矩阵运算可以很快的找到对应关系。理解变换的原理需要理解变换的构造方法以及矩阵的运算方法，曾经写过matlab下的简单图像变换原理，里面有最基础的构造原理可以看看：

  [**matlab之原始处理图像几何变换**](http://blog.csdn.net/on2way/article/details/40460675)

  ### （一）图像的平移

  下面介绍的图像操作假设你已经知道了为什么需要用矩阵构造才能实现了（上面那个博客有介绍为什么）。那么关于偏移很简单，图像的平移，沿着x方向tx距离，y方向ty距离，那么需要构造移动矩阵： 
  $$
  M = \begin{bmatrix}
     1 & 0 & t_x\\
     0& 1 & t_y\\
    \end{bmatrix}
  $$
  通过numpy来产生这个矩阵，并将其赋值给仿射函数**`cv2.warpAffine()`.** 

  仿射函数**`cv2.warpAffine()`**接受三个参数，需要变换的原始图像，移动矩阵M 以及变换的图像大小（这个大小如果不和原始图像大小相同，那么函数会自动通过插值来调整像素间的关系）。 

  **`cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst`**




- **src** – input image.
- **dst** – output image that has the size `dsize` and the same type as `src` .
- **M** – ![2\times 3](https://docs.opencv.org/3.0-beta/_images/math/f335f976f482cd08e9c6c198204b18c1fc769882.png) transformation matrix.
- **dsize** – size of the output image.
- **flags** – combination of interpolation methods (see [`resize()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/geometric_transformations.html?highlight=cv2.war#void resize(InputArray src, OutputArray dst, Size dsize, double fx, double fy, int interpolation)) ) and the optional flag `WARP_INVERSE_MAP` that means that `M` is the inverse transformation ( ![\texttt{dst}\rightarrow\texttt{src}](https://docs.opencv.org/3.0-beta/_images/math/79358c8b893d7d0db75b629175a7eab3db5f192b.png) ).
- **borderMode** – pixel extrapolation method (see [`borderInterpolate()`](https://docs.opencv.org/3.0-beta/modules/core/doc/operations_on_arrays.html#int borderInterpolate(int p, int len, int borderType))); when`borderMode=BORDER_TRANSPARENT` , it means that the pixels in the destination image corresponding to the “outliers” in the source image are not modified by the function.
- **borderValue** – value used in case of a constant border; by default, it is 0.

The function `warpAffine` transforms the source image using the specified matrix:

![\texttt{dst} (x,y) =  \texttt{src} ( \texttt{M} _{11} x +  \texttt{M} _{12} y +  \texttt{M} _{13}, \texttt{M} _{21} x +  \texttt{M} _{22} y +  \texttt{M} _{23})](https://docs.opencv.org/3.0-beta/_images/math/189dfa6dbab9ff81eaeaa453b1a1e2313dcd3a26.png)

一个例子如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
H = np.float32([[1,0,100],[0,1,50]])
rows,cols = img.shape[:2]
res = cv2.warpAffine(img,H,(cols,rows)) #需要图像、变换矩阵、变换后的大小
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
plt.show()
```

![4](E:\machine_learning\opencv\4.png)



### （二）图像的扩大与缩小

图像的扩大与缩小有专门的一个函数，**`cv2.resize()`**，那么关于伸缩需要确定的就是缩放比例，可以是x与y方向相同倍数，也可以单独设置x与y的缩放比例。另外一个就是在缩放以后图像必然就会变化，这就又涉及到一个插值问题。那么这个函数中，缩放有几种不同的插值（**`interpolation`**）方法，在缩小时推荐**`cv2.INTER_ARER`**,扩大是推荐**`cv2.INTER_CUBIC`**和**`cv2.INTER_LINEAR`**。默认都是**`cv2.INTER_LINEAR`**，比如：

 **`cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst`** 

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
# 插值：interpolation
# None本应该是放图像大小的位置的，后面设置了缩放比例，
# 所有就不要了
res1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
# 直接规定缩放大小，这个时候就不需要缩放因子
height,width = img.shape[:2]
res2 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
plt.subplot(131)
plt.imshow(img)
plt.subplot(132)
plt.imshow(res1)
plt.subplot(133)
plt.imshow(res2)
plt.show()
```

![这里写图片描述](http://img.blog.csdn.net/20150708111354556)

通过坐标轴可以看到图像扩大了一倍，并且两种方法相同。

### （三）图像的旋转

图像的旋转矩阵一般为： 
$$
M=\begin{bmatrix}
cos(\theta)&-sin(\theta)\\
sin(\theta)&cos(\theta)
\end{bmatrix}
$$
但是单纯的这个矩阵是在原点处进行变换的，为了能够在任意位置进行旋转变换，opencv采用了另一种方式： 
$$
M=\begin{bmatrix}
\alpha&-\beta&(1-\alpha)center_x-\beta center_y\\
-\beta &alpha&\beta center_x +(1-\alpha)center_y\\
\end{bmatrix}
$$
where
$$
\alpha=scale.cos(angle)\\
\beta = scale.sin(angle)
$$
为了构造这个矩阵，opencv提供了一个函数： 

**`cv2.getRotationMatrix2D()`**，这个函数需要三个参数，**`旋转中心`**，**`旋转角度`**，**`旋转后图像的缩放比例`**，

**`cv2.getRotationMatrix2D(center, angle, scale) → retval`**

比如下例：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
rows,cols = img.shape[:2]

# 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# 第三个参数：变换后的图像大小
res = cv2.warpAffine(img,M,(rows,cols))

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
```

![5](E:\machine_learning\opencv\5.png)

### 四）图像的仿射

图像的**`旋转加上拉升`**就是图像仿射变换，仿射变化也是需要一个M矩阵就可以，但是由于仿射变换比较复杂，一般直接找很难找到这个矩阵，opencv提供了根据变换前后三个点的对应关系来自动求解M。这个函数是 
**`M=cv2.getAffineTransform(pos1,pos2)`**,其中两个位置就是变换前后的对应位置关系。输 出的就是仿射矩阵M。然后在使用函数**`cv2.warpAffine()`**。形象化的图如下（引用参考的） 

![这里写图片描述](http://img.blog.csdn.net/20150708111543898)

一个例子比如：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
rows,cols = img.shape[:2]
pts1 = np.float32([[50,50],[200,50],[50,200]])#需要源图像和变换后三个点的坐标
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
#第三个参数：变换后的图像大小
res = cv2.warpAffine(img,M,(rows,cols))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
```

![6](E:\machine_learning\opencv\6.png)

###  （ 五）图像的透射

透视需要的是一个3*3的矩阵，同理opencv在构造这个矩阵的时候还是采用一种点对应的关系来通过函数自己寻找的，因为我们自己很难计算出来。这个函数是**`M = cv2.getPerspectiveTransform(pts1,pts2)`**，

```python
Calculates a perspective transform from four pairs of the corresponding points
```

其中pts需要变换前后的4个点对应位置。得到M后在通过函数cv2.warpPerspective(img,M,(200,200))进行。形象化的图如下（引用参考的） 
![这里写图片描述](http://img.blog.csdn.net/20150708111655043) 

一个例子如下：

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')
rows,cols = img.shape[:2]
pts1 = np.float32([[56,65],[238,52],[28,237],[239,240]])
pts2 = np.float32([[0,0],[200,0],[0,200],[200,200]])
M = cv2.getPerspectiveTransform(pts1,pts2)
res = cv2.warpPerspective(img,M,(200,200))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)
```

![这里写图片描述](http://img.blog.csdn.net/20150708111728790)

## opencv使用笔记（四）（图像的阈值处理）

- 图像的阈值处理一般使得图像的像素值更单一、图像更简单。阈值可以分为全局性质的阈值，也可以分为局部性质的阈值，可以是单阈值的也可以是多阈值的。当然阈值越多是越复杂的。下面将介绍opencv下的三种阈值方法。

###  （ 一）简单阈值

简单阈值当然是最简单，选取一个全局阈值，然后就把整幅图像分成了非黑即白的二值图像了。函数为**`cv2.threshold()`** 
这个函数有四个参数，第一个原图像，第二个进行分类的阈值，第三个是高于（低于）阈值时赋予的新值，第四个是一个方法选择参数，常用的有： 
• **`cv2.THRESH_BINARY`**（黑白二值） 
• **`cv2.THRESH_BINARY_INV`**（黑白二值反转） 
• **`cv2.THRESH_TRUNC`** （得到的图像为多像素值） 
• **`cv2.THRESH_TOZERO`** 
• **`cv2.THRESH_TOZERO_INV`** 
该函数有两个返回值，第一个**`retVal`**（得到的阈值值（在后面一个方法中会用到）），第二个就是阈值化后的图像。 

 **threshold**

Applies a fixed-level threshold to each array element.

- **` cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst`**

**Parameters:**

- **src** – input array (single-channel, 8-bit or 32-bit floating point).  
- **dst** – output array of the same size and type as `src`.  
- **thresh** – threshold value.  
- **maxval** – maximum value to use with the `THRESH_BINARY` and `THRESH_BINARY_INV` thresholding types.
- **type** – thresholding type (see the details below).  

The function applies fixed-level thresholding to a single-channel array. The function is typically used to get a bi-level (binary) image out of a grayscale image ( [`compare()`](https://docs.opencv.org/3.0-beta/modules/core/doc/operations_on_arrays.html#void compare(InputArray src1, InputArray src2, OutputArray dst, int cmpop)) could be also used for this purpose) or **for removing a noise**, that is, **filtering out pixels with too small or too large values.** There are several types of thresholding supported by the function. They are determined by `type` :

> - **THRESH_BINARY**
>
>   > ![\texttt{dst} (x,y) =  \fork{\texttt{maxval}}{if $\texttt{src}(x,y) > \texttt{thresh}$}{0}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/21dfc802899546a3a9a51794d241330e6377f032.png)
>
> - **THRESH_BINARY_INV**
>
>   > ![\texttt{dst} (x,y) =  \fork{0}{if $\texttt{src}(x,y) > \texttt{thresh}$}{\texttt{maxval}}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/2858653b2a9f18e326acd861f4f23476f918e52b.png)
>
> - **THRESH_TRUNC**
>
>   > ![\texttt{dst} (x,y) =  \fork{\texttt{threshold}}{if $\texttt{src}(x,y) > \texttt{thresh}$}{\texttt{src}(x,y)}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/85cd5dfea2f25f50640e7555c4019829859ff661.png)
>
> - **THRESH_TOZERO**
>
>   > ![\texttt{dst} (x,y) =  \fork{\texttt{src}(x,y)}{if $\texttt{src}(x,y) > \texttt{thresh}$}{0}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/c42e93ea5c713fb2fca2605fa03ccbdf15a98d16.png)
>
> - **THRESH_TOZERO_INV**
>
>   > ![\texttt{dst} (x,y) =  \fork{0}{if $\texttt{src}(x,y) > \texttt{thresh}$}{\texttt{src}(x,y)}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/6729a7b61fa189e9ad1a365aa5eb9290b70b023e.png)

also, the special values `THRESH_OTSU` or `THRESH_TRIANGLE` may be combined with one of the above values. In these cases, the function determines the optimal threshold value using the Otsu’s or Triangle algorithm and uses it instead of the specified `thresh` . The function returns the computed threshold value. Currently, the **`Otsu’s`** and **`Triangle`** methods are implemented only for 8-bit images.

![../../../_images/threshold.png](https://docs.opencv.org/3.0-beta/_images/threshold.png)

一个实例如下：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
```

![8](E:\machine_learning\opencv\8.png)

可以看到这里把阈值设置成了127，对于BINARY方法，当图像中的灰度值大于127的重置像素值为255.

###  （二）自适应阈值：

前面看到简单阈值是一种全局性的阈值，只需要规定一个阈值值，整个图像都和这个阈值比较。而自适应阈值可以看成一种局部性的阈值，**`通过规定一个区域大小，比较这个点与区域大小里面像素点的平均值（或者其他特征）的大小关系来确定这个像素点是属于黑或者白`**（如果是二值情况）。使用的函数为：**`cv2.adaptiveThreshold（）`** 
该函数需要填6个参数：

- 第一个原始图像

- 第二个像素值上限

- 第三个自适应方法**`Adaptive Method`**: 
  — **`cv2.ADAPTIVE_THRESH_MEAN_C`** ：领域内均值 
  —**`cv2.ADAPTIVE_THRESH_GAUSSIAN_C`** ：领域内像素点加权和，权重为一个高斯窗口

- 第四个值的赋值方法：只有**`cv2.THRESH_BINARY`** 和**`cv2.THRESH_BINARY_INV`**

- 第五个Block size:规定领域大小（一个正方形的领域）

- 第六个常数C，**`阈值等于均值或者加权值减去这个常数`**（为0相当于阈值 就是求得领域内均值或者加权值） 
  这种方法理论上得到的效果更好，相当于在动态自适应的调整属于自己像素点的阈值，而不是整幅图像都用一个阈值。

  ## adaptiveThreshold

  Applies an adaptive threshold to an array.

   **`cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) → dst`** **Parameters:**  

  **src** – Source 8-bit single-channel image.

  **dst** – Destination image of the same size and the same type as `src` .  

  **maxValue** – Non-zero value assigned to the pixels for which the condition is satisfied. See the details below.  

  **adaptiveMethod** – Adaptive thresholding algorithm to use, `ADAPTIVE_THRESH_MEAN_C` or`ADAPTIVE_THRESH_GAUSSIAN_C` . See the details below.  

  **thresholdType** – Thresholding type that must be either `THRESH_BINARY` or `THRESH_BINARY_INV` **blockSize** – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.  

  **C** – **`Constant subtracted from the mean or weighted mean`** (see the details below). Normally, it is positive but may be zero or negative as well. 

  **The function transforms a `grayscale image to a binary image` according to the formulae:**

  > - **THRESH_BINARY**
  >
  >   > ![dst(x,y) =  \fork{\texttt{maxValue}}{if $src(x,y) > T(x,y)$}{0}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/7df8e198374f12e5e28ff32b34d49ecb2fbdddb4.png)
  >
  > - **THRESH_BINARY_INV**
  >
  >   > ![dst(x,y) =  \fork{0}{if $src(x,y) > T(x,y)$}{\texttt{maxValue}}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/59b5b25f1acebef583c96c77c49354b22f871560.png)

  where ![T(x,y)](https://docs.opencv.org/3.0-beta/_images/math/5e11673cd01013b82529c8316a1505243cea62ad.png) is a threshold calculated individually for each pixel.

  - For the method `ADAPTIVE_THRESH_MEAN_C` , the threshold value ![T(x,y)](https://docs.opencv.org/3.0-beta/_images/math/5e11673cd01013b82529c8316a1505243cea62ad.png) is a mean of the ![\texttt{blockSize} \times \texttt{blockSize}](https://docs.opencv.org/3.0-beta/_images/math/91b988f5a3acb7025e903a2b1bc6b7558e5970dd.png) neighborhood of ![(x, y)](https://docs.opencv.org/3.0-beta/_images/math/dee21a914bf9088bc0dfbd38a96c1f859c412ec7.png) minus `C` .
  - For the method `ADAPTIVE_THRESH_GAUSSIAN_C` , the threshold value ![T(x, y)](https://docs.opencv.org/3.0-beta/_images/math/0f2558a6357e54ae9a3cd1799dd33ffc088bf25d.png) is a weighted sum (cross-correlation with a Gaussian window) of the ![\texttt{blockSize} \times \texttt{blockSize}](https://docs.opencv.org/3.0-beta/_images/math/91b988f5a3acb7025e903a2b1bc6b7558e5970dd.png) neighborhood of ![(x, y)](https://docs.opencv.org/3.0-beta/_images/math/dee21a914bf9088bc0dfbd38a96c1f859c412ec7.png) minus `C` . The default sigma (standard deviation) is used for the specified `blockSize` . See [`getGaussianKernel()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html#Mat getGaussianKernel(int ksize, double sigma, int ktype)) .

一个实例如下：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2) #换行符号 \
images = [img,th1,th2,th3]
plt.figure()
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
plt.show()
```

![9](E:\machine_learning\opencv\9.png)

可以看到上述窗口大小使用的为11，当窗口越小的时候，得到的图像越细。想想一下，如果把窗口设置足够大以后（不能超过图像大小），那么得到的结果可能就和第二幅图像的相同了。

###  三）Otsu’s二值化

我们前面说到，**`cv2.threshold`**函数是有两个返回值的，前面一直用的第二个返回值，也就是阈值处理后的图像，那么第一个返回值（得到图像的阈值）将会在这里用到。 
前面对于阈值的处理上，我们选择的阈值都是127，那么实际情况下，怎么去选择这个127呢？有的图像可能阈值不是127得到的效果更好。那么这里我们需要算法自己去寻找到一个阈值，而**`Otsu’s`**就可以自己找到一个认为最好的阈值。并且**`Otsu’s`**非常适合于图像**`灰度直方图具有双峰`**的情况，他会在**双峰之间找到一个值作为阈值**，对于非双峰图像，可能并不是很好用。那么经过**`Otsu’s`**得到的那个阈值就是函数**`cv2.threshold`**的第一个参数了。因为**`Otsu’s`**方法会产生一个阈值，那么函数**`cv2.threshold`**的的第二个参数（设置阈值）就是0了，并且在cv2.threshold的方法参数中还得加上语句**`cv2.THRESH_OTSU`**。那么什么是**`双峰图像（只能是灰度图像才有`**），就是图像的灰度统计图中可以明显看出只有两个波峰，比如下面一个图的灰度直方图就可以是双峰图： 

![这里写图片描述](http://img.blog.csdn.net/20150709090157285)



好了现在对这个图进行**`Otsu’s`**阈值处理就非常的好，通过函数**`cv2.threshold`**会自动找到一个介于两波峰之间的阈值。一个实例如下：

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('finger.jpg',0) #直接读为灰度图像
#简单滤波
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Otsu 滤波
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print ret2
plt.figure()
plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.hist(img.ravel(),256)#.ravel方法将矩阵转化为一维
plt.subplot(223),plt.imshow(th1,'gray')
plt.subplot(224),plt.imshow(th2,'gray')1234567891011121314
```

![这里写图片描述](http://img.blog.csdn.net/20150709090234647) 
print ret2 得到的结果为122。可以看出似乎两个结果并没有很明显差别（素材也不太好弄~_~!），主要是两个阈值（127与122）太相近了，如果这两个隔得很远那么会很明显的

## opencv使用笔记（五）（图像的平滑与滤波）

对于图形的**`平滑`**与**`滤波`**，但从滤波角度来讲，一般主要的目的都是为了实现对**`图像噪声的消除`**，**`增强图像`**的效果。 
首先介绍**二维卷积运算，图像的滤波可以看成是滤波模板与原始图像对应部分的的卷积运算**。关于卷积运算，找到几篇相关的博客：

**图像处理：基础(模板、卷积运算)** 
**图像处理-模板、卷积的整理**

对于2D图像可以进行**`低通或者高通滤波操作`**，**`低通滤波（LPF）`**有利于**去噪**，**模糊图像**，**`高通滤波（HPF）`**有利于找到**图像边界**。

### （一）统一的2D滤波器cv2.filter2D

Opencv提供的一个通用的2D滤波函数为**`cv2.filter2D()`**，滤波函数的使用需要一个**核模板**，对图像的滤波操作过程为：**将和模板放在图像的一个像素A上，求与之对应的图像上的每个像素点的和**，核不同，得到的结果不同，而滤波的使用核心也是对于这个核模板的使用，需要注意的是，**该滤波函数是单通道运算的，也就是说对于彩色图像的滤波，需要将`彩色图像的各个通道提取出来`，对各个通道分别滤波才行。** 
这里说一个与matlab相似的情况，matlab中也有一个类似的滤波函数**`imfilter,`**对于滤波函数的应用其实不只在于滤波，对于许多图像的整体处理上，其实都可以用滤波函数来组合实现，得到更快的效果，相关的介绍间下面这个博客：

**[图像滤波函数imfilter函数的应用及其扩展]()**

 **filter2D**

Convolves an image with the kernel.

**` cv2.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) → dst`**

Parameters:  

- **src** – input image.  
- **dst** – output image of the same size and the same number of channels as `src`.  
- **ddepth** –desired depth of the destination image; if it is negative, it will be the same as `src.depth()`; the following combinations of `src.depth()` and `ddepth` are supported:

> > `src.depth() = CV_8U, ddepth= -1/CV_16S/CV_32F/CV_64F`

> > `src.depth()= CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F`

> > `src.depth() = CV_32F, ddepth = -1/CV_32F/CV_64F`

> > `src.depth() = CV_64F, ddepth= -1/CV_64F`

when **`ddepth=-1`**, t**he output image will have the same depth as the source**. 

- **kernel** – convolution kernel (or rather a correlation kernel), a single-channel floating point matrix; if you want to apply different kernels to different channels, **split the image into separate color planes using** [`split()`](https://docs.opencv.org/3.0-beta/modules/core/doc/operations_on_arrays.html#void split(const Mat& src, Mat* mvbegin)) and process them individually. 
- **anchor** – anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; **`default value (-1,-1)`** means that the anchor is at the **`kernel center`**.
- **delta** – optional value added to the filtered pixels before storing them in `dst`.
- **borderType** – pixel extrapolation method (see `borderInterpolate` for details). 

The function applies an arbitrary linear filter to an image. In-place operation is supported. When the aperture is partially outside the image, the function interpolates outlier pixel values according to the specified border mode.

The function does actually compute correlation, not the convolution:

![\texttt{dst} (x,y) =  \sum _{ \stackrel{0\leq x' < \texttt{kernel.cols},}{0\leq y' < \texttt{kernel.rows}} }  \texttt{kernel} (x',y')* \texttt{src} (x+x'- \texttt{anchor.x} ,y+y'- \texttt{anchor.y} )](https://docs.opencv.org/3.0-beta/_images/math/930d8a4a72259ace7a4966d4bc1b653eec1b7ce8.png)

That is, the kernel is not mirrored around the anchor point. If you need a real convolution, flip the kernel using[`flip()`](https://docs.opencv.org/3.0-beta/modules/core/doc/operations_on_arrays.html#void flip(InputArray src, OutputArray dst, int flipCode)) and set the new anchor to `(kernel.cols - anchor.x - 1, kernel.rows - anchor.y - 1)` .

The function uses the DFT-based algorithm in case of sufficiently large kernels (~``11 x 11`` or larger) and the direct algorithm for small kernels.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
img1 = np.float32(img) #转化数值类型
kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img1,-1,kernel)
#cv2.filter2D(src,dst,kernel,auchor=(-1,-1))函数：
#输出图像与输入图像大小相同
#中间的数为-1，输出数值格式的相同plt.figure()
plt.subplot(1,2,1),plt.imshow(img1,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(dst,'gray')1234567891011121314
```

![这里写图片描述](http://img.blog.csdn.net/20150710112550116) 
下面介绍的几种滤波部分可能是将函数cv2.filter2D()具体化，重新规定一个名字而已，贴一个好的博客参考：

**[图像平滑处理（归一化块滤波、高斯滤波、中值滤波、双边滤波）]()**

## （二）均值滤波

上述生成的**`5\*5核模板`**其实就是一个**均值滤波**。而opencv有一个专门的平均滤波模板供使用–**`归一化卷积模板`**，所有的滤波模板都是使**卷积框覆盖区域所有像素点与模板相乘后得到的值作为中心像素的值**。Opencv中均值模板可以用**`cv2.blur`**和**`cv2.boxFilter,`**比如一个3*3的模板其实就可以如下表示： 
$$
M=\frac{1}{9}\begin{bmatrix}
1 & 1&1 \\
1 & 1&1\\
1 & 1&1
\end{bmatrix}\quad
$$
模板大小是$m*n$是可以设置的。如果你不想要前面的1/9,可以使用非归一化的模板**`cv2.boxFilter`**。一个实例如下：

```python
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('flower.jpg',0) #直接读为灰度图像
blur = cv2.blur(img,(3,5))#模板大小3*5
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray')123456
```

![这里写图片描述](http://img.blog.csdn.net/20150710112711192)

**`blur`**

Blurs an image using the normalized box filter.

**`cv2.blur(src, ksize[, dst[, anchor[, borderType]]]) → dst`**

Parameters:  

- **src** – input image; it can have any number of channels, which are processed independently, but the depth should be `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or `CV_64F`.
- **dst** – output image of the same size and type as `src`.
- **ksize** – blurring kernel size.
- **anchor** – anchor point; default value `Point(-1,-1)` means that the anchor is at the kernel center.
- **borderType** – border mode used to extrapolate pixels outside of the image.  

The function smoothes an image using the kernel:

![\texttt{K} =  \frac{1}{\texttt{ksize.width*ksize.height}} \begin{bmatrix} 1 & 1 & 1 &  \cdots & 1 & 1  \\ 1 & 1 & 1 &  \cdots & 1 & 1  \\ \hdotsfor{6} \\ 1 & 1 & 1 &  \cdots & 1 & 1  \\ \end{bmatrix}](https://docs.opencv.org/3.0-beta/_images/math/0a3a3decb904a04778cbe67506aa86d2dba618d6.png)

**`boxFilter`**

Blurs an image using the box filter.

**` cv2.``boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) → dst`**

Parameters:

* **src** – input image.
* **dst** – output image of the same size and type as `src`.
* **ddepth** – the output image depth (-1 to use `src.depth()`).
* **ksize** – blurring kernel size.
* **anchor** – anchor point; default value `Point(-1,-1)` means that the anchor is at the kernel center.
* **normalize** – flag, specifying whether the kernel is normalized by its area or not.
* **borderType** – border mode used to extrapolate pixels outside of the image. 

The function smoothes an image using the kernel:

![\texttt{K} =  \alpha \begin{bmatrix} 1 & 1 & 1 &  \cdots & 1 & 1  \\ 1 & 1 & 1 &  \cdots & 1 & 1  \\ \hdotsfor{6} \\ 1 & 1 & 1 &  \cdots & 1 & 1 \end{bmatrix}](https://docs.opencv.org/3.0-beta/_images/math/39f9e9decf02ff5891fe62d9892ff1bee82f2904.png)

where

![\alpha = \fork{\frac{1}{\texttt{ksize.width*ksize.height}}}{when \texttt{normalize=true}}{1}{otherwise}](https://docs.opencv.org/3.0-beta/_images/math/3f79f034b1b1b131f02a860eb808df10daa25525.png)

**`Unnormalized box filter`** is useful for computing various integral characteristics over each pixel neighborhood, such as covariance matrices of image derivatives (used in dense optical flow algorithms, and so on). If you need to compute pixel sums over variable-size windows, use [`integral()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/miscellaneous_transformations.html#void integral(InputArray src, OutputArray sum, int sdepth)) .

## （三）高斯模糊模板

现在把卷积模板中的值换一下，不是全1了，换成一组符合高斯分布的数值放在模板里面，比如这时中间的数值最大，往两边走越来越小，构造一个小的高斯包。实现的函数为cv2.GaussianBlur()。对于高斯模板，我们需要**`制定的是高斯核的高和宽（奇数）`**，沿x与y方向的标准差(如果只给x，y=x，如果都给0，那么函数会自己计算)。高斯核可以有效的出去图像的高斯噪声。当然也可以自己构造高斯核，相关函数：**`cv2.GaussianKernel()`**.

**`GaussianBlur`**

**` cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst`**

Parameters:

* **src** – input image; the image can have any number of channels, which are processed independently, but the depth should be `CV_8U`, `CV_16U`, `CV_16S`, `CV_32F` or `CV_64F`.

* **dst** – output image of the same size and type as `src`.

* **ksize** – Gaussian kernel size. `ksize.width` and `ksize.height` can differ but they both must be **`positive`** and **`odd`**. Or, they **can be zero’s and then they are computed from** `sigma*` .

* **sigmaX** – Gaussian kernel standard deviation in X direction.

* **sigmaY** – Gaussian kernel standard deviation in Y direction; 

  > **if `sigmaY` is zero, it is set to be equal to `sigmaX`**, 
  >
  > if both sigmas are zeros, they are computed from `ksize.width` and`ksize.height` , respectively (see [`getGaussianKernel()`](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html?highlight=filter2d#Mat getGaussianKernel(int ksize, double sigma, int ktype)) for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of `ksize`, `sigmaX`, and `sigmaY`

* **borderType** – pixel extrapolation method (see `borderInterpolate` for details). 

The function convolves the source image with the specified Gaussian kernel. In-place filtering is supported.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray') 123456789101112
```

![这里写图片描述](http://img.blog.csdn.net/20150710112807185)

## （四）中值滤波模板

**`中值滤波模板`**就是用**卷积框中像素的中值代替中心值**，达到去噪声的目的。这个模板一般用于**去除椒盐噪声**。前面的滤波器都是用计算得到的一个新值来取代中心像素的值，而中值滤波是用中心像素周围（也可以使他本身）的值来取代他，**卷积核的大小也是个奇数**。

 **`medianBlur`**

Blurs an image using the median filter.

 `cv2.medianBlur(src, ksize[, dst]) → dst`

Parameters: 

* **src** – input 1-, 3-, or 4-channel image; when `ksize` is 3 or 5, the image depth should be `CV_8U`, `CV_16U`, or `CV_32F`, for larger aperture sizes, it can only be `CV_8U`.
* **dst** – destination array of the same size and type as `src`.
* **ksize** – aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ... 

The function smoothes an image using the median filter with the ![\texttt{ksize} \times \texttt{ksize}](https://docs.opencv.org/3.0-beta/_images/math/9c389d9c70bc7f05f5956fcdd9548afb8453d497.png) aperture. Each channel of a multi-channel image is processed independently.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg',0) #直接读为灰度图像
for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

blur = cv2.medianBlur(img,5)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray') 12345678910111213
```

![这里写图片描述](http://img.blog.csdn.net/20150710112851876) 
可以看到中值滤波对于这些白点噪声的去除是非常的好的。

## （五）双边滤波

双边滤波函数为**`cv2.bilateralFilter()`**。该滤波器可以在**保证边界清晰的情况下有效的去掉噪声**。它的构造比较复杂，即考虑了**图像的空间关系**，也**考虑图像的灰度关系**。双边滤波同时使用了**空间高斯权重和灰度相似性高斯权重**，确保了边界不会被模糊掉。有一个介绍专门介绍双边滤波的博客：

**[双边滤波器的原理及实现](http://blog.csdn.net/abcjennifer/article/details/7616663)**

cv2.bilateralFilter(img,d,’p1’,’p2’)函数有四个参数需要，d是领域的直径，后面两个参数是空间高斯函数标准差和灰度值相似性高斯函数标准差。一个实例如下：

 **bilateralFilter**

> Applies the bilateral filter to an image.

**`cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst`**

**Parameters:**

- **src** – Source 8-bit or floating-point, 1-channel or 3-channel image.
- **dst** – Destination image of the same size and type as `src` .
- **d** – Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from `sigmaSpace` .
- **sigmaColor** – Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see `sigmaSpace` ) will be mixed together, resulting in larger areas of semi-equal color.空间高斯函数标准差
- **sigmaSpace** – Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see `sigmaColor`). When `d>0` , it specifies the neighborhood size regardless of `sigmaSpace` . Otherwise, `d` is proportional to `sigmaSpace` .灰度值相似性标准差

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('flower.jpg',0) #直接读为灰度图像
for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

#9---滤波领域直径
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray')1234567891011121314
```



![这里写图片描述](http://img.blog.csdn.net/20150710113031529)

