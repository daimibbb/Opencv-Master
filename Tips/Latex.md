# Latex输入矩阵的几种方式

直接用`matrix、pmatrix、bmatrix、Bmatrix、vmatrix`或者`Vmatrix`环境:

```latex
$$
\begin{gathered}
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}
\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\quad
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}
\quad
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
\end{gathered}
$$
```

 效果： 
$$
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}
\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\quad
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}
\quad
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
$$
第二种方法是使用`array`环境来输入矩阵，示例如下：

```latex
\left( \begin{matrix}
	a11&		a12&		a13\\
	a21&		a22&		a23\\
\end{matrix} \right) 
```

$$
\left( \begin{matrix}
	a11&		a12&		a13\\
	a21&		a22&		a23\\
\end{matrix} \right)               %右括号
$$

## 公式对齐

```latex
\begin{equation}
\begin{split}
x&=a+b+c\\
&=d+e\\
&=f+g
\end{split}
\end{equation}
```

$$
\begin{equation}
\begin{split}
x&=a+b+c\\
&=d+e\\
&=f+g
\end{split}
\end{equation}
$$

```latex
\begin{aligned}
	\nabla \times \vec{H}^m&=\epsilon \frac{\partial \vec{E}^m}{\partial t}\\
	\nabla \times \vec{E}^m&=-\vec{J}^m-\mu \frac{\partial \vec{H}^m}{\partial t}\\
	\epsilon \nabla \cdot \vec{E}^m&=0\\
	\mu \nabla \cdot \vec{H}^m&=\rho ^m\\
\end{aligned}
```



## 大括号

```latex
\left\{\right.\begin{aligned}
	\nabla \times \vec{H}^e&=\vec{J}+\epsilon \frac{\partial \vec{E}^e}{\partial t}\\
	\nabla \times \vec{E}^e&=-\mu \frac{\partial \vec{H}^e}{\partial t}\\
	\epsilon \nabla \cdot \vec{E}^e&=\rho\\
	\mu \nabla \cdot \vec{H}^e&=0\\
\end{aligned}
```

```latex
\left.  
\begin{aligned}
	H_{\varphi}^{e}&=j\frac{Il\sin \theta}{2\lambda r}e^{-jkr}\\
	E_{\theta}^{e}&=j\frac{Il\sin \theta}{2\lambda r}\sqrt{\frac{\mu _0}{\epsilon _0}}e^{-jkr}\\
\end{aligned}
\right\}
\left\{  
\begin{aligned}
	H_{\varphi}^{e}&=j\frac{Il\sin \theta}{2\lambda r}e^{-jkr}\\
	E_{\theta}^{e}&=j\frac{Il\sin \theta}{2\lambda r}\sqrt{\frac{\mu _0}{\epsilon _0}}e^{-jkr}\\
\end{aligned}\right.
```

$$
\left.  
\begin{aligned}
	H_{\varphi}^{e}&=j\frac{Il\sin \theta}{2\lambda r}e^{-jkr}\\
	E_{\theta}^{e}&=j\frac{Il\sin \theta}{2\lambda r}\sqrt{\frac{\mu _0}{\epsilon _0}}e^{-jkr}\\
\end{aligned}
\right\}
\left\{  
\begin{aligned}
	H_{\varphi}^{e}&=j\frac{Il\sin \theta}{2\lambda r}e^{-jkr}\\
	E_{\theta}^{e}&=j\frac{Il\sin \theta}{2\lambda r}\sqrt{\frac{\mu _0}{\epsilon _0}}e^{-jkr}\\
\end{aligned}\right.
$$

