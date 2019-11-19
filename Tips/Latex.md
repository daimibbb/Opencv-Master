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

