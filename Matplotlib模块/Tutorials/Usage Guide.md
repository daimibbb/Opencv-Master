# Usage Guide

## General Concepts

```python
import matplotlib.pyplot as plt
import numpy as np
```

## Parts of a Figure

![../../_images/anatomy.png](https://matplotlib.org/_images/anatomy.png) 

### Figure

The **whole** figure. The `figure` keeps track of all the child `Axes`, a smattering of 'special' `artists` (`titles`, `figure legends`, etc), and the `canvas`. (Don't worry too much about the `canvas`, it is crucial as it is the object that actually does the drawing to get you your plot, but as the user it is more-or-less invisible to you). A figure can have any number of `Axes`, but to be useful should have at least one.

The easiest way to create a new figure is with pyplot:

```python
fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
```

 ![../../_images/sphx_glr_usage_001.png](https://matplotlib.org/_images/sphx_glr_usage_001.png)

 ![../../_images/sphx_glr_usage_002.png](https://matplotlib.org/_images/sphx_glr_usage_002.png)  

---

### Axes

This is what you think of as 'a plot', it is the region of the image with the data space. A given figure can contain many `Axes`, but a given `Axes `object can only be in one `Figure`. The Axes contains two (or three in the case of 3D) `Axis` objects (be aware of the difference between **Axes** and **Axis**) which take care of the data limits (the data limits can also be controlled via set via the `set_xlim()` and `set_ylim()` Axes methods). Each Axes has a title (set via `set_title()`), an x-label (set via `set_xlabel()`), and a y-label set via `set_ylabel()`).

The `Axes` class and its member functions are the primary entry point to working with the OO interface.

---

### Axis

These are the number-line-like objects. They take care of setting the graph limits and generating the ticks (the marks on the axis) and ticklabels (strings labeling the ticks). The location of the ticks is determined by a `Locator `object and the ticklabel strings are formatted by a `Formatter`. The combination of the correct `Locator `and Formatter gives very fine control over the tick locations and labels.

---

### Artist

Basically everything you can see on the figure is an artist (even the Figure, Axes, and Axis objects). This includes Text objects, Line2D objects, collection objects, Patch objects ... (you get the idea). When the figure is rendered, all of the artists are drawn to the **canvas**. Most Artists are tied to an Axes; such an Artist cannot be shared by multiple Axes, or moved from one to another.

---

## Types of inputs to plotting functions

 All of plotting functions expect `np.array` or `np.ma.masked_array` as input.

`pandas `data objects and `np.matrix` may or may not work as intended. It is best to convert these to `np.array` objects prior to plotting.

> use `np.array`

convert a `pandas.DataFrame`
```python
a = pd.DataFrame(np.random.rand(4, 5), columns=list('abcde'))
a_asarray = a.values
```

 convert a `np.matrix` 

```python
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)
```

---

## Matplotlib, pyplot and pylab: how are they related?

Matplotlib is the whole package and `matplotlib.pyplot` is a module in Matplotlib.

 `pyplot`  只会在当前`Axes`绘制图形

```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()
```

` pylab `is *deprecated* and its use is strongly discouraged because of namespace pollution. Use `pyplot `instead. 

---

## Coding Styles

```python
import matplotlib.pyplot as plt
import numpy as np
```

```python
x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

 *recommended function signature* 

```python
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})
```

 or if you wanted to have 2 sub-plots: 

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
```

---

## Backends

### What is a backend?

网站和邮件列表中的很多文档都指的是“ `backend `”，许多新用户对这个术语感到困惑。Matplotlib针对许多不同的用例和输出格式。有些人在python shell中交互地使用matplotlib，当他们输入命令时会弹出绘图窗口。有些人跑  Jupyter notebooks和绘制内联绘图，以便快速进行数据分析。其他人将matplotlib嵌入到图形用户界面中，比如wxpython或pygtk，以构建丰富的应用程序。有些人在批处理脚本中使用matplotlib从数值模拟中生成PostScript图像，还有一些人运行Web应用服务器来动态地提供图形。

为了支持所有这些用例，matplotlib可以针对不同的输出，这些功能中的每一个都称为 `backend `；“ `frontend`”是 is the user facing code，即 the plotting code，而“ `backend`”则在幕后完成了所有繁重的工作来生成数字。有两种 `backends`：用户界面后端（用于pygtk、wxpython、tkinter、qt4或macosx；也称为“交互后端”）和硬拷贝后端以生成图像文件（png、svg、pdf、ps；也称为“非交互后端”）。

如果脚本依赖于特定的后端，则可以使用 `use()` 功能：

```python
import matplotlib
matplotlib.use('PS')   # generate postscript output by default
```

---

## What is interactive mode?

交互模式也可以通过 `matplotlib.pyplot.ion()` 打开，并通过 `matplotlib.pyplot.ioff()` 关闭。

### 交互式示例

```python
import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
```

```python
plt.title("interactive test")
plt.xlabel("index")
```

 you will see the plot being updated after each line.

```python
ax = plt.gca()
ax.plot([3.1, 2.2])
```

### 非交互式示例

像前一个示例中那样启动一个新会话，但现在关闭交互式模式：

```python
import matplotlib.pyplot as plt

plt.ioff()
plt.plot([1.6, 2.7])
```

 Nothing happened。要使绘图显示，您需要执行以下操作：

```
plt.show()
```

现在您看到了绘图，但是您的终端命令行没有响应；该 `show()` 命令 *阻碍* 输入附加命令，直到手动终止绘图窗口。

这有什么好处——被迫使用阻塞函数？假设您需要一个将文件内容绘制到屏幕上的脚本。你想看那个情节，然后结束脚本。如果没有诸如`show()`之类的阻塞命令，脚本将刷新绘图，然后立即结束，在屏幕上什么也不留下。

此外，非交互模式会延迟所有绘图，直到调用s`how()`；这比每次脚本中的一行添加新功能时重新绘制绘图更有效。

```python
import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
```

这就形成了三个情节，一次一个。也就是说，一旦第一个图关闭，第二个图就会出现。

### Summary

- In interactive mode, `pyplot` functions automatically draw to the screen.

- When plotting interactively, if using object method calls in addition to `pyplot `functions, then call `draw()` whenever you want to refresh the plot.

- Use non-interactive mode in scripts in which you want to generate one or more figures and display them before ending or generating a new set of figures. In that case, use `show()` to display the figure(s) and to block execution until you have manually destroyed them.

## Performance

 无论是以交互模式浏览数据还是以编程方式保存大量绘图，渲染性能都可能是管道中的一个痛苦瓶颈。Matplotlib提供了两种方法，可以大大减少渲染时间，但代价是对绘图外观进行细微更改（达到可设置的公差）。可用于减少渲染时间的方法取决于正在创建的绘图类型。 

### Line segment simplification

 For plots that have line segments (e.g. typical line plots, outlines of polygons, etc.), rendering performance can be controlled by the `path.simplify` and `path.simplify_threshold`parameters 

- The `path.simplify` parameter is a boolean indicating whether or not line segments are simplified at all.
- The`path.simplify_threshold` parameter controls how much line segments are simplified; higher thresholds result in quicker rendering. 

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
```

### Marker simplification

Markers can also be simplified, albeit less robustly than line segments. Marker simplification is only available to `Line2D `objects (through the markevery property). Wherever `Line2D `construction parameters are passed through, such as `matplotlib.pyplot.plot()` and `matplotlib.axes.Axes.plot()`, the markevery parameter can be used:

```python
plt.plot(x, y, markevery=10)
```

### Splitting lines into smaller chunks

If you are using the Agg backend, then you can make use of the `agg.path.chunksize` rc parameter. This allows you to specify a *chunk* size, and any lines with greater than that many vertices will be split into multiple lines, each of which has no more than `agg.path.chunksize` many vertices. (Unless `agg.path.chunksize` is zero, in which case there is no chunking.) For some kind of data, chunking the line up into reasonable sizes can greatly decrease rendering time.

The following script will first display the data without any chunk size restriction, and then display the same data with a chunk size of 10,000. The difference can best be seen when the figures are large, try maximizing the GUI and then interacting with them: 

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1,np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()
```

### Legends

the default legend behavior for axes attempts to find the location that covers the fewest data points (`loc='best'`). This can be a very expensive computation if there are lots of data points. In this case, you may want to provide a specific location. 

### Using the *fast* style

The *fast* style can be used to automatically set simplification and chunking parameters to reasonable settings to speed up plotting large amounts of data. It can be used simply by running:

```python
import matplotlib.style as mplstyle
mplstyle.use('fast')
```

It is very light weight, so it plays nicely with other styles, just make sure the fast style is applied last so that other styles do not overwrite the settings:

```python
mplstyle.use(['dark_background', 'ggplot', 'fast'])
```