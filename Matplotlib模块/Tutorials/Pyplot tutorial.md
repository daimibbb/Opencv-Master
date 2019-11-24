# Pyplot tutorial

## Intro to pyplot

`matplotlib.pyplot` is a collection of command style functions that make matplotlib work like MATLAB. Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

 Generating visualizations with pyplot is very quick: 

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

 plot $x$ versus $y$ 

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

### Formatting the style of your plot

For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot.   you concatenate a color string with a line style string. The default format string is '`b-`', which is a solid blue line. 

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```
 ![../../_images/sphx_glr_pyplot_003.png](https://matplotlib.org/_images/sphx_glr_pyplot_003.png) 

  a plotting several lines with different format styles in one command using arrays. 

```python
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

## Plotting with keyword strings

 Matplotlib allows you provide such an object with the `data` keyword argument. If provided, then you may generate plots with the strings corresponding to these variables. 

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```

 <img src="https://matplotlib.org/_images/sphx_glr_pyplot_005.png" alt="../../_images/sphx_glr_pyplot_005.png" style="zoom: 80%;" />

###  Plotting with categorical variables

 t is also possible to create a plot using categorical variables. Matplotlib allows you to pass categorical variables directly to many plotting functions. For example: 

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

 <img src="https://matplotlib.org/_images/sphx_glr_pyplot_006.png" alt="../../_images/sphx_glr_pyplot_006.png" style="zoom:80%;" /> 

## Controlling line properties

 Use keyword args: 

```python
plt.plot(x, y, linewidth=2.0)
```

 Use the setter methods of a `Line2D` instance. `plot` returns a list of `Line2D` objects; e.g., `line1, line2 = plot(x1, y1, x2, y2)`. In the code below we will suppose that we have only one line so that the list returned is of length 1. We use tuple unpacking with `line,` to get the first element of that list: 

```python
line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialiasing
```

 Use the `setp()` command. The example below uses a MATLAB-style command to set multiple properties on a list of lines. `setp` works transparently with a list of objects or a single object. You can either use python keyword arguments or MATLAB-style string/value pairs: 

```python
lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
```

Here are the available `Line2D `properties.

| Property               | Value Type                                                |
| ---------------------- | --------------------------------------------------------- |
| alpha                  | float                                                     |
| animated               | [True \| False]                                           |
| antialiased or aa      | [True \| False]                                           |
| clip_box               | a matplotlib.transform.Bbox instance                      |
| clip_on                | [True \| False]                                           |
| clip_path              | a Path instance and a Transform instance, a Patch         |
| color or c             | any matplotlib color                                      |
| contains               | the hit testing function                                  |
| dash_capstyle          | [`'butt'` | `'round'` | `'projecting'`]                   |
| dash_joinstyle         | [`'miter'` | `'round'` | `'bevel'`]                       |
| dashes                 | sequence of on/off ink in points                          |
| data                   | (np.array xdata, np.array ydata)                          |
| figure                 | a matplotlib.figure.Figure instance                       |
| label                  | any string                                                |
| linestyle or ls        | [ `'-'` | `'--'` | `'-.'` | `':'` | `'steps'` \| ...]     |
| linewidth or lw        | float value in points                                     |
| marker                 | [ `'+'` | `','` | `'.'` | `'1'` | `'2'` | `'3'` | `'4'` ] |
| markeredgecolor or mec | any matplotlib color                                      |
| markeredgewidth or mew | float value in points                                     |
| markerfacecolor or mfc | any matplotlib color                                      |
| markersize or ms       | float                                                     |
| markevery              | [ None \| integer \| (startind, stride) ]                 |
| picker                 | used in interactive line selection                        |
| pickradius             | the line pick selection radius                            |
| solid_capstyle         | [`'butt'` | `'round'` | `'projecting'`]                   |
| solid_joinstyle        | [`'miter'` | `'round'` | `'bevel'`]                       |
| transform              | a matplotlib.transforms.Transform instance                |
| visible                | [True \| False]                                           |
| xdata                  | np.array                                                  |
| ydata                  | np.array                                                  |
| zorder                 | any number                                                |

To get a list of settable line properties, call the `setp()` function with a line or lines as argument

```python
lines = plt.plot([1, 2, 3])
plt.setp(lines)
# alpha: float
# animated: bool
# antialiased: bool
```

## Working with multiple figures and axes

MATLAB, and `pyplot`, have the concept of the current `figure `and the current `axes`. All plotting commands apply to the current `axes`. The function `gca()` returns the current `axes `(a `matplotlib.axes.Axes` instance), and `gcf()` returns the current figure (`matplotlib.figure.Figure` instance). 

Normally, you don't have to worry about this, because it is all taken care of behind the scenes. Below is a script to create two subplots.

```python
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

 ![../../_images/sphx_glr_pyplot_007.png](https://matplotlib.org/_images/sphx_glr_pyplot_007.png)

这个 `figure()` 这里的命令是可选的，因为` figure(1)` 将在默认情况下创建，就像 `subplot(111)` 如果不手动指定任何轴，默认情况下将创建。这个 `subplot()` 命令指定 *numrows*, *numcols*, *plot_number* 在哪里？ *plot_number* 范围从`1`到 `numrows*numcols `。如果 `numrows*numcols<10`，`subplot`中的`,`可以省略， 所以 `subplot(211)` 相同 `subplot(2, 1, 1) `.

 可以创建任意数量的子批次和轴。如果要手动放置轴（即不在矩形网格上），请使用` axes()` 命令，允许您将位置指定为 `axes([left, bottom, width, height]) `其中所有值都是分数（`0`到`1`）坐标。

You can create multiple figures by using multiple `figure()` calls with an increasing figure number. Of course, each figure can contain as many axes and subplots as your heart desires:

You can clear the current figure with `clf()` and the current axes with `cla()`. 

If you are making lots of figures, you need to be aware of one more thing: the memory required for a figure is not completely released until the figure is explicitly closed with `close()`. 

## Working with text

The `text()` command can be used to add text in an arbitrary location, and the `xlabel()`, `ylabel()` and `title()` are used to add text in the indicated locations

```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

All of the `text()` commands return an `matplotlib.text.Text` instance. you can customize the properties by passing keyword arguments into the text functions or using `setp()`:

```python
t = plt.xlabel('my data', fontsize=14, color='red')
```

### Using mathematical expressions in text

```python
plt.title(r'$\sigma_i=15$')
```

 The `r` preceding the title string is important -- it signifies that the string is a *raw* string and not to treat backslashes as python escapes. matplotlib has a built-in TeX expression parser and layout engine, and ships its own math fonts 

### Annotating text

```python
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
```

## Logarithmic and other nonlinear axes

 Changing the scale of an axis is easy: 

```python
plt.xscale('log')
```

```python
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure()

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
```

 ![../../_images/sphx_glr_pyplot_010.png](https://matplotlib.org/_images/sphx_glr_pyplot_010.png) 