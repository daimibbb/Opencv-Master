# canny算子

原创 2012年07月04日 14:19:06

###1.Canny边缘检测基本原理

​     (1)图象边缘检测必须满足两个条件：**一能有效地抑制噪声**；**二必须尽量精确确定边缘的位置**。

​     (2)**根据对信噪比与定位乘积进行测度，得到最优化逼近算子**。这就是**`Canny`**边缘检测算子。

​     (3)类似与Marr（LoG）边缘检测方法，也属于先平滑后求导数的方法。

 

### 2. Canny边缘检测算法：

​     step1:用高斯滤波器**平滑图象**；

​     step2:用一阶偏导的有限差分来计算**梯度的幅值和方向**；

​     step3:对梯度幅值进行**非极大值抑制**；

​     step4:用双阈值算法**检测和连接边缘**。

##### step1:高斯平滑函数

![img](http://my.csdn.net/uploads/201207/06/1341540868_5233.png)

（可以理解下维基百科上关于卷积函数的定义，如下图移动的红色窗口代表我们的高斯和函数，蓝色为图像灰度函数）

![img](http://upload.wikimedia.org/wikipedia/commons/6/6a/Convolution_of_box_signal_with_itself2.gif)

通过高斯函数产生k\*k的模板如3\*3

![img](http://hi.csdn.net/attachment/201109/29/0_1317299636lGV5.gif)

用这个模板对每个像素进行加权平均

#### Step2：一阶微分卷积模板

![img](http://my.csdn.net/uploads/201207/06/1341540897_4675.png)

#### step3:对梯度幅值进行非极大值抑制

​      仅仅得到全局的梯度并不足以确定边缘，因此为确定边缘，**必须保留局部梯度最大的点，而抑制非极大值**。（**`non-maxima suppression,NMS`**）

解决方法：利用梯度的方向。

![img](http://my.csdn.net/uploads/201207/06/1341540927_4163.png)

 

图1非极大值抑制

四个扇区的标号为0到3，对应3*3邻域的四种可能组合。在每一点上，邻域的中心象素M与沿着梯度线的两个象素相比。**如果M的梯度值不比沿梯度线的两个相邻象素梯度值大，则令M=0**。

即： ![img](http://my.csdn.net/uploads/201207/06/1341540955_8775.png)

####  **Step4:用双阈值算法检测和连接边缘:　　**

　　对非极大值抑制图像**作用两个阈值th1和th2**，两者关系**`th1=0.4th2`**  。我们把**梯度值小于th1的像素的灰度值设为0，得到图像1**。**然后把梯度值小于th2的像素的灰度值设为0，得到图像2**。由于**图像2的阈值较高，去除大部分噪音，但同时也损失了有用的边缘信息**。而**图像1的阈值较低，保留了较多的信息，我们可以以图像2为基础，以图像1为补充来连结图像的边缘**。

　　链接边缘的具体步骤如下：

- 对图像2进行扫描，**当遇到一个非零灰度的像素p(x,y)时，跟踪以p(x,y)为开始点的轮廓线，直到轮廓线的终点q(x,y)**。

- 考察图像1中与图像2中q(x,y)点位置对应的点s(x,y)的8邻近区域。如果在s(x,y)点的8邻近区域中有非零像素s(x,y)存在，则将其包括到图像2中，作为r(x,y)点。从r(x,y)开始，重复第一步，直到我们在图像1和图像2中都无法继续为止。

- ### 当完成对包含p(x,y)的轮廓线的连结之后，将这条轮廓线标记为已经访问。回到第一步，寻找下一条轮廓线。重复第一步、第二步、第三步，直到图像2中找不到新轮廓线为止。

  ###3.canny算法程序实现

   Canny算法程序中将上述的4个步骤再加以细分，分成以下7步：

l 生成高斯滤波系数；

l 用生成的高斯滤波系数对原图像进行平滑；

l 求滤波后图像的梯度；

l 进行非最大抑制；

l 统计图像的直方图，对阈值进行判定；

l 利用函数寻找边界起点；

l 根据第6步执行的结果，从一个像素点开始搜索，搜索以该像素点为边界起点的一条边界的一条边界的所有边界点；