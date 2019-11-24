# matplotlib.pyplot.legend

```python
matplotlib.pyplot.legend(*args, **kwargs)
```

Place a legend on the axes.

Call signatures:

```python
legend()
legend(labels)
legend(handles, labels)
```

The call signatures correspond to three different ways how to use this method.

**1. Automatic detection of elements to be shown in the legend**

The elements to be added to the legend are automatically determined, when you do not pass in any extra arguments.

In this case, the labels are taken from the artist. You can specify them either at artist creation or by calling the **`set_label()`** method on the artist:

```python
line, = ax.plot([1, 2, 3], label='Inline label')
ax.legend()
```

or:

```
line.set_label('Label via method')
line, = ax.plot([1, 2, 3])
ax.legend()
```

Specific lines can be excluded from the automatic legend element selection by defining a label starting with an underscore. This is default for all artists, so calling **`Axes.legend`** without any arguments and without setting the labels manually will result in no legend being drawn.

---

**2. Labeling existing plot elements**

To make a legend for lines which already exist on the axes (via plot for instance), simply call this function with an iterable of strings, one for each legend item. For example:

```
ax.plot([1, 2, 3])
ax.legend(['A simple line'])
```

Note: This way of using is **discouraged**, because the relation between plot elements and labels is only implicit by their order and can **easily be mixed up**.

---

**3. Explicitly defining the elements in the legend**

For full control of which artists have a legend entry, it is possible to pass an iterable of legend artists followed by an iterable of legend labels respectively:

```
legend((line1, line2, line3), ('label1', 'label2', 'label3'))
```

---

**Parameters:**	

- **`handles`** : sequence of **`Artist`**, optional

A list of **`Artists`** (**lines**, **patches**) to be added to the legend. Use this together with labels, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

The length of handles and labels should be the **same** in this case. If they are not, they are **truncated** to the smaller length.

- **`labels`** : sequence of strings, optional

A list of labels to show next to the **`artists`**. Use this together with **`handles`**, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

**Returns:**

- **`class`** : **`matplotlib.legend.Legend`** **instance**

```python
plt.plot([1, 2, 3])
plt.legend(["demo"])
# Out[58]: <matplotlib.legend.Legend at 0x2dcce9d1c50>
```



**Other Parameters:**

- **`loc`** : **int** or **string** or **pair of floats**, default: **`rcParams["legend.loc"]`**

The location of the legend. Possible codes are:

| Location String | Location Code |
| --------------- | ------------- |
| 'best'          | 0             |
| 'upper right'   | 1             |
| 'upper left'    | 2             |
| 'lower left'    | 3             |
| 'lower right'   | 4             |
| 'right'         | 5             |
| 'center left'   | 6             |
| 'center right'  | 7             |
| 'lower center'  | 8             |
| 'upper center'  | 9             |
| 'center'        | 10            |

Alternatively can be a **`2-tuple`** giving **`( x, y)`** of the **lower-left corner of the legend in axes coordinates** (in which case **`bbox_to_anchor`** will be ignored).

The 'best' option can be quite slow for plots with large amounts of data. Your plotting speed may benefit from providing a specific location.

对于具有大量数据的绘图，“最佳”选项可能很慢。提供一个特定的位置可以提高绘图速度。

- **`bbox_to_anchor`** : **`BboxBase`**, **2-tuple**, or **4-tuple of floats**

Box that is used to position the legend in conjunction with **`loc. Defaults`** to **`axes.bbox`** (if called as a method to **`Axes.legend`**) or **`figure.bbox`** (if **`Figure.legend`**). **This argument allows arbitrary placement of the legend**.

Bbox coordinates are interpreted in the coordinate system given by **`bbox_to_anchor`**, with the default transform Axes or Figure coordinates, depending on which legend is called.

If a **`4-tuple`** or **`BboxBase`** is given, then it specifies the **`bbox (x, y, width, height)`** that the legend is placed in. To put the legend in the best location in the bottom right quadrant of the axes (or figure):

```python
loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5)
```

A 2-tuple **`(x, y)`** places the corner of the legend **specified by** **`loc`** **at x, y**. For example, to put the legend's upper right-hand corner in the center of the axes (or figure) the following keywords can be used:

```python
loc='upper right', bbox_to_anchor=(0.5, 0.5)
```

- **`ncol`** : integer

The number of columns that the legend has. Default is 1.

- **`prop`** : **None** or **`matplotlib.font_manager.FontProperties`** or **dict**

**The font properties of the legend.** If **None** (default), the current **`matplotlib.rcParams`** will be used.

- **`fontsize`** : **int** or **float** or {'**xx-small**', '**x-small**', '**small**', '**medium**', '**large**', '**x-large**', '**xx-large**'}

**Controls the font size of the legend.** If the value is numeric the size will be the absolute font size in points. String values are relative to the current default font size. This argument is only used if prop is not specified.

- **`numpoints`** : **None** or **int**

**The number of marker points in the legend** when creating a legend entry for a Line2D (line). Default is None, which will take the value from **`rcParams["legend.numpoints"]`**.

- **`scatterpoints`** : **None** or **int**

The number of marker points in the legend when creating a legend entry for a **`PathCollection`** (scatter plot). Default is **None**, which will take the value from **`rcParams["legend.scatterpoints"]`**.

- **`scatteryoffsets`** : **iterable** of **floats**

The **vertical offset** (relative to the font size) for the markers created for a scatter plot legend entry. 

为散点图图例条目创建的标记的垂直偏移量(相对于字体大小)

**`0.0`** is at the base the legend text, and **`1.0`** is at the top. To draw all markers at the same height, set to **`[0.5]`**. Default is **`[0.375, 0.5, 0.3125]`**.

- **`markerscale`** : **None** or **int** or **float**

The relative size of legend markers compared with the originally drawn ones. Default is **None**, which will take the value from **`rcParams["legend.markerscale"]`**.

- **`markerfirst`** : bool

If **`True`**, legend marker is placed to the **left of the legend label**. If **`False`**, legend marker is placed to the **right of the legend label**. **Default** is **`True`**.

- **`frameon`** : **None** or **bool**

**Control whether the legend should be drawn on a patch (frame)**. Default is **None**, which will take the value from **`rcParams["legend.frameon"]`**. ( 是否显示图例背景)

- **`fancybox`** : **None** or **bool**

**Control whether round edges should be enabled around** the **`FancyBboxPatch`** which makes up the legend's background. Default is **None**, which will take the value from **`rcParams["legend.fancybox"]`**.

- **`shadow`** : **None** or **bool**

**Control whether to draw a shadow behind the legend**. Default is **None**, which will take the value from **`rcParams["legend.shadow"]`**.

- **`framealpha`** : **None** or **float**

**Control the alpha transparency of the legend's background.** Default is **None**, which will take the value from **`rcParams["legend.framealpha"]`**. If **`shadow`** is activated and **`framealpha`** is **None**, **the default value is ignored.**

- **`facecolor`** : **None** or **"inherit"** or **a color spec**

**Control the legend's background color.** Default is **None**, which will take the value from **`rcParams["legend.facecolor"]`**. If **`"inherit"`**, it will take **`rcParams["axes.facecolor"]`**.

- **`edgecolor`** : **None** or "**inherit**" or **a color spec**

**Control the legend's background patch edge color.** Default is **None**, which will take the value from **`rcParams["legend.edgecolor"]`** If **`"inherit"`**, it will take **`rcParams["axes.edgecolor"]`**.

- **`mode`** : {"**expand**", **None**}

If mode is set to "expand" the legend will be horizontally expanded to fill the axes area (or **`bbox_to_anchor`** if defines the legend's size).

- **`bbox_transform`** : **None** or **`matplotlib.transforms.Transform`**

The transform for the bounding box (**`bbox_to_anchor`**). For a value of **None** (default) the **`Axes' transAxes transform`** will be used.

- **`title`** : **str** or **None**

**The legend's title.** Default is no title (**None**).

- **`title_fontsize`**: **str** or **None**

**The fontsize of the legend's title.** Default is the default fontsize.

- **`borderpad`** : **float** or **None**

**The fractional whitespace inside the legend border.** **Measured in font-size units.** Default is **None**, which will take the value from **`rcParams["legend.borderpad"]`**. （没有字区域的空白大小, **`borderpad x font-size`**）

- **`labelspacing`** : **float** or **None**

**The vertical space between the legend entries. Measured in font-size units.** Default is **None**, which will take the value from **`rcParams["legend.labelspacing"]`**.

- **`handlelength`** : **float** or **None**

**The length of the legend handles. Measured in font-size units.** Default is **None**, which will take the value from **`rcParams["legend.handlelength"]`**.

- **`handletextpad`** : **float** or **None**

The pad between the legend handle and text. Measured in font-size units. Default is **None**, which will take the value from **`rcParams["legend.handletextpad"]`**.

- **`borderaxespad`** : **float** or **None**

**The pad between the axes and legend border. Measured in font-size units.** Default is **None**, which will take the value from **`rcParams["legend.borderaxespad"]`**.

- **`columnspacing`** : **float** or **None**

The spacing between columns. Measured in font-size units. Default is **None**, which will take the value from **`rcParams["legend.columnspacing"]`**.

- **`handler_map`** : **dict** or **None**

**The custom dictionary mapping instances or types to a legend handler.** This handler_map updates the default handler map found at **`matplotlib.legend.Legend.get_legend_handler_map()`**.

---

# rcParams.legend

```python
'legend.borderaxespad': 0.5,
'legend.borderpad': 0.4,
'legend.columnspacing': 2.0,
'legend.edgecolor': '0.8',
'legend.facecolor': 'inherit',
'legend.fancybox': True,
'legend.fontsize': 'medium',
'legend.framealpha': 0.8,
'legend.frameon': True,
'legend.handleheight': 0.7,
'legend.handlelength': 2.0,
'legend.handletextpad': 0.8,
'legend.labelspacing': 0.5,
'legend.loc': 'best',
'legend.markerscale': 1.0,
'legend.numpoints': 1,
'legend.scatterpoints': 1,
'legend.shadow': False,
```





