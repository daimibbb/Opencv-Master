---
typora-root-url: E:\opencv\图片库
---

# OpenCV-Python教程（6、Sobel算子）

- 本文不介详细的理论知识，读者可从其他资料中获取相应的背景知识。笔者推荐清华大学出版社的《图像处理与计算机视觉算法及应用(第2版) 》。

## Sobel算子

### 原型

**`Sobel`**算子依然是一种过滤器，只是其是带有方向的。在OpenCV-Python中，使用Sobel的算子的函数原型如下：

**`dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])`**  

前四个是必须的参数：

- 第一个参数是需要处理的图像；

- 第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；

  output image depth; the following combinations of `src.depth()` and `ddepth` are supported:

  - `src.depth()` = `CV_8U`, `ddepth` = -1/`CV_16S`/`CV_32F`/`CV_64F`

  - `src.depth()` = `CV_16U`/`CV_16S`, `ddepth` = -1/`CV_32F`/`CV_64F`

  - `src.depth()` = `CV_32F`, `ddepth` = -1/`CV_32F`/`CV_64F`

  - `src.depth()` = `CV_64F`, `ddepth` = -1/`CV_64F`

    when `ddepth=-1`, the destination image will have the same depth as the source; in the case of 8-bit input images it will result in truncated derivatives.

- **`dx`**和**`dy`**表示的是求导的阶数，**`0`**表示这个方向上没有求导，一般为**`0、1、2`**。

其后是可选的参数：

- dst不用解释了；

- **`ksize`**是Sobel算子的大小，必须为**`1、3、5、7`**。

- **`scale`**是缩放导数的比例常数，默认情况下没有伸缩系数；

- **`delta`**是一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；

- **`borderType`**是判断图像边界的模式。这个参数默认值为`cv2.BORDER_DEFAULT`。

  ​

  In all cases except one, the ![\texttt{ksize} \times\texttt{ksize}](https://docs.opencv.org/3.0-beta/_images/math/67ac8e01d254361095b28f8ac83e332f208d1e31.png) separable kernel is used to calculate the derivative. When ![\texttt{ksize = 1}](https://docs.opencv.org/3.0-beta/_images/math/4daed318cc0381d143ca27f60277e6d1ea50e432.png) , the ![3 \times 1](https://docs.opencv.org/3.0-beta/_images/math/100762acf79bb70bf5737e3a41067c09cb55b050.png) or ![1 \times 3](https://docs.opencv.org/3.0-beta/_images/math/0901cf2fbd419b32993984f209910f744424b80d.png) kernel is used (that is, no Gaussian smoothing is done). `ksize = 1` can only be used for the first or the second x- or y- derivatives.

  There is also the special value `ksize = CV_SCHARR` (-1) that corresponds to the ![3\times3](https://docs.opencv.org/3.0-beta/_images/math/913c4034db44a98d07b02c893a2c7dede83be898.png) Scharr filter that may give more accurate results than the ![3\times3](https://docs.opencv.org/3.0-beta/_images/math/913c4034db44a98d07b02c893a2c7dede83be898.png) Sobel. The Scharr aperture is

  ![\vecthreethree{-3}{0}{3}{-10}{0}{10}{-3}{0}{3}](https://docs.opencv.org/3.0-beta/_images/math/3ab98ff1a5283f63057e5f3ff52c25e49ef01318.png)

  for the x-derivative, or transposed for the y-derivative.

  The function calculates an image derivative by convolving the image with the appropriate kernel:

  ![\texttt{dst} =  \frac{\partial^{xorder+yorder} \texttt{src}}{\partial x^{xorder} \partial y^{yorder}}](https://docs.opencv.org/3.0-beta/_images/math/f6b50963327c57345aabf72f164a3faf10d255a4.png)

  The Sobel operators combine Gaussian smoothing and differentiation, so the result is more or less resistant to the noise. Most often, the function is called with ( `xorder` = 1, `yorder` = 0, `ksize` = 3) or ( `xorder` = 0, `yorder` = 1, `ksize` = 3) to calculate the first x- or y- image derivative. The first case corresponds to a kernel of:

  ![\vecthreethree{-1}{0}{1}{-2}{0}{2}{-1}{0}{1}](https://docs.opencv.org/3.0-beta/_images/math/f2531c53069c2dabcab2bcb391518bd65dc535eb.png)

  The second case corresponds to a kernel of:

  ![\vecthreethree{-1}{-2}{-1}{0}{0}{0}{1}{2}{1}](https://docs.opencv.org/3.0-beta/_images/math/03e50d0ac972c69085ccbff5cadd0b53f791fce8.png)

### 使用

在OpenCV-Python中，Sobel函数的使用如下：

```python
import cv2  
import numpy as np    
  
img = cv2.imread("D:/lion.jpg", 0)  
  
x = cv2.Sobel(img,cv2.CV_16S,1,0)  
y = cv2.Sobel(img,cv2.CV_16S,0,1)  
  
absX = cv2.convertScaleAbs(x)   # 转回uint8  
absY = cv2.convertScaleAbs(y)  
  
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)  
  
cv2.imshow("absX", absX)  
cv2.imshow("absY", absY)  
  
cv2.imshow("Result", dst)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()   
```



### 解释

在Sobel函数的第二个参数这里使用了**`cv2.CV_16S`**。因为OpenCV文档中对Sobel算子的介绍中有这么一句：`“in the case of 8-bit input images it will result in truncated derivatives”`。即Sobel函数求完导数后会有**负值**，还有会**大于255的值**。**而原图像是uint8，即8位无符号数，所以Sobel建立的图像位数不够，会有截断**。因此要使用**16位有符号的数据类型**，即**cv2.CV_16S**。

 **convertScaleAbs**

> **Scales, calculates absolute values, and converts the result to 8-bit.**

在经过处理后，别忘了用**`convertScaleAbs()`**函数将其转回原来的uint8形式。否则将无法显示图像，而只是一副灰色的窗口。**`convertScaleAbs()`**的原型为：

**`dst = cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])`**  

**`Parameters:`**

- **src** – input array.
- **dst** – output array.
- **alpha** – optional scale factor.
- **beta** – optional delta added to the scaled values.

由于Sobel算子是在两个方向计算的，最后还需要用**`cv2.addWeighted(...)`**函数将其组合起来。其函数原型为：

**`dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])`**  

 **addWeighted**

**Calculates the weighted sum of two arrays.**

**Parameters:**

- **src1** – first input array.
- **alpha** – weight of the first array elements.
- **src2** – second input array of the same size and channel number as `src1`.
- **beta** – weight of the second array elements.
- **dst** – output array that has the same size and number of channels as the input arrays.
- **gamma** – scalar added to each sum.
- **dtype** – optional depth of the output array; when both input arrays have the same depth, `dtype`can be set to `-1`, which will be equivalent to `src1.depth()`.

The function `addWeighted` calculates the weighted sum of two arrays as follows:

![\texttt{dst} (I)= \texttt{saturate} ( \texttt{src1} (I)* \texttt{alpha} +  \texttt{src2} (I)* \texttt{beta} +  \texttt{gamma} )](https://docs.opencv.org/3.0-beta/_images/math/d9e87b75f6c0526dfca3f8c483fbda1ad7251046.png)

where `I` is a multi-dimensional index of array elements. In case of multi-channel arrays, each channel is processed independently.

The function can be replaced with a matrix expression:

```python
dst = src1*alpha + src2*beta + gamma;
```

> **Note:**  Saturation is not applied when the output array has the depth `CV_32S`. You may even get result of an incorrect sign in the case of overflow.

### 结果

原图像为：

![img](http://img.blog.csdn.net/20130627154241703?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3VubnkyMDM4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

结果为：

![img](http://img.blog.csdn.net/20130627154403390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3VubnkyMDM4/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

## 参考资料：

1、《Opencv2 Computer Vision Application Programming Cookbook》

2、《OpenCV References Manule》