# matplotlib.legend

The legend module defines the **`Legend`** class, which is responsible for drawing legends associated with axes and/or figures.

>**Important**
>
>It is unlikely that you would ever create a Legend instance manually. Most users would normally create a legend via the **`legend()`** function. 

The **`Legend`** class can be considered as a container of **legend handles** and **legend texts**. Creation of corresponding legend handles from the plot elements in the axes or figures (e.g., lines, patches, etc.) are specified by the handler map, which **defines the mapping between the plot elements and the legend handlers** to be used (the default legend handlers are defined in the **`legend_handler`** module). Note that not all kinds of artist are supported by the legend yet by default but it is possible to extend the legend handler's capabilities to support arbitrary objects. 

----

## DraggableLegend

```python
class matplotlib.legend.DraggableLegend(legend, use_blit=False, update='loc')
```

​	Bases: **`matplotlib.offsetbox.DraggableOffsetBox`**

​	Wrapper around a **`Legend`** to support mouse dragging. (包装图例以支持鼠标拖动)

**Parameters:**

- **`legend`** : **`Legend`**

The Legend instance to wrap.

- **`use_blit`** : **bool**

Use blitting for faster image composition. For details see FuncAnimation.

- **`update`** : {'**loc**', '**bbox**'}

If "**loc**", update the loc parameter of the legend upon finalizing. 

If "**bbox**", update the **`bbox_to_anchor`** parameter.

---

## artist_picker

```
artist_picker(legend, evt)
```

---

## finalize_offset

```python
finalize_offset()
```

---

## Legend

```python
class matplotlib.legend.Legend(parent, handles, labels, loc=None, numpoints=None, markerscale=None, markerfirst=True, scatterpoints=None, scatteryoffsets=None, prop=None, fontsize=None, borderpad=None, labelspacing=None, handlelength=None, handleheight=None, handletextpad=None, borderaxespad=None, columnspacing=None, ncol=1, mode=None, fancybox=None, shadow=None, title=None, title_fontsize=None, framealpha=None, edgecolor=None, facecolor=None, bbox_to_anchor=None, bbox_transform=None, frameon=None, handler_map=None)
```

​	Bases: **`matplotlib.artist.Artist`**

​	Place a legend on the axes at location loc.

### params

**Parameters:**

- **`parent`** : **`Axes`** or **`Figure`**

The artist that contains the legend.

- **`handles`** : sequence of **`Artist`**

A list of Artists (lines, patches) to be added to the legend.

- **`labels`** : sequence of strings

A list of labels to show next to the **`artists`**. The length of handles and labels should be the same. If they are not, they are truncated to the smaller of both lengths.

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

Notes

Users can specify any arbitrary location for the legend using the **`bbox_to_anchor`** keyword argument. **`bbox_to_anchor`** can be an instance of **`BboxBase`**(or its derivatives) or a tuple of 2 or 4 floats. See **`set_bbox_to_anchor`** for more detail.

The legend location can be specified by setting *loc* with a tuple of 2 floats, which is interpreted as the lower-left corner of the legend in the normalized axes coordinate.

---

### method

#### codes

```python
codes={'best': 0,
 'upper right': 1,
 'upper left': 2,
 'lower left': 3,
 'lower right': 4,
 'right': 5,
 'center left': 6,
 'center right': 7,
 'lower center': 8,
 'upper center': 9,
 'center': 10}
```

---

#### contains

```
contains(event)
```

Test whether the artist contains the **mouse event.**

Returns the truth value and a dictionary of artist specific details of selection, such as which points are contained in the pick radius. See individual artists for details.

---

#### draggable

```
draggable(state=None, use_blit=False, update='loc')
```

Set the draggable state -- if state is

- *None* : toggle the current state
- *True* : turn draggable on
- *False* : turn draggable off

If draggable is on, you can drag the legend on the canvas with the mouse. The **`DraggableLegend`** helper instance is returned if draggable is on.

The update parameter control which parameter of the legend changes when dragged. If update is "loc", the *loc* parameter of the legend is changed. If "**bbox**", the **`bbox_to_anchor`** parameter is changed.

---

####  draw

```
draw(renderer)
```

Draw everything that belongs to the legend.

---

#### draw_frame

```
draw_frame(b)
```

Set draw frame to b.

**Parameters:**

- **`b`** : bool

---

####  get_bbox_to_anchor

```
get_bbox_to_anchor()
```

Return the **`bbox`** that the legend will be anchored to.

---

####  get_children

```
get_children()
```

Return a list of child artists.

```python
import matplotlib.legend
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
a = plt.legend(['demo'])
matplotlib.legend.Legend.get_children(a)  
# Out[64]: [<matplotlib.offsetbox.VPacker at 0x2dccd3ec588>,
# <matplotlib.patches.FancyBboxPatch at 0x2dccc7e1668>]
```

---

#### get_default_handler_map

```
classmethod get_default_handler_map()
```

A class method that returns the default handler map.

---

#### get_draggable

```
get_draggable()
```

Return True if the legend is draggable, False otherwise.

---

####  get_frame

```
get_frame()
```

Return the **`Rectangle`** instances used to frame the legend.

```python
import matplotlib.legend
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
a = plt.legend(['demo'])
matplotlib.legend.Legend.get_frame(a)
# Out[65]: <matplotlib.patches.FancyBboxPatch at 0x2dccd373390>
```

---

#### get_frame_on

```
get_frame_on()
```

Get whether the legend box patch is drawn.

---

#### get_legend_handler

```
static get_legend_handler(legend_handler_map, orig_handle)
```

Return a legend handler from *legend_handler_map* that corresponds to *orig_handler*.

*legend_handler_map* should be a dictionary object (that is returned by the get_legend_handler_map method).

It first checks if the *orig_handle* itself is a key in the *legend_hanler_map* and return the associated value. Otherwise, it checks for each of the classes in its method-resolution-order. If no matching key is found, it returns `None`.

---

#### get_legend_handler_map

```
get_legend_handler_map()
```

Return the handler map.

---

#### get_lines

```
get_lines()
```

Return a list of **`Line2D`** **instances** in the legend.

```python
import matplotlib.legend
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
a = plt.legend(['demo'])
matplotlib.legend.Legend.get_lines(a)  
# Out[]: [<matplotlib.lines.Line2D at 0x2dccd7d98d0>]
```

---

#### get_patches

```
get_patches()
```

Return a list of **`Patch`** **instances** in the legend.

---

get_texts

```
get_texts()
```

Return a list of **`Text`** instances in the legend.

---

#### get_tightbbox

```
get_tightbbox(renderer)
```

Like **`Legend.get_window_extent`**, but uses the box for the legend.

**Parameters:**

- **`renderer`** : **`RendererBase`** instance
  renderer that will be used to draw the figures (i.e. fig.canvas.get_renderer())

**Returns:**

- **`.BboxBase`** : containing the bounding box in figure pixel co-ordinates.

---

#### get_title

```
get_title()
```

Return the **`Text`** instance for the legend title.

---

#### get_window_extent

```
get_window_extent(renderer=None)
```

Return extent of the legend.

---

#### set_bbox_to_anchor

```
Set the bbox that the legend will be anchored to.
```

bbox can be

- A **`BboxBase`** instance
- A tuple of (left, bottom, width, height) in the given transform (normalized axes coordinate if None)
- A tuple of (left, bottom) where the width and height will be assumed to be zero.

---

#### set_default_handler_map

```
classmethod set_default_handler_map(handler_map)
```

A class method to set the default handler map.

---

#### set_draggable

```
set_draggable(state, use_blit=False, update='loc')
```

Enable or disable mouse dragging support of the legend.

**Parameters:**

- **`state`** : **bool**

Whether mouse dragging is enabled.

- **`use_blit`** : bool, optional

Use blitting for faster image composition. For details see **`FuncAnimation`**.

- **`update`** : {'**loc**', '**bbox**'}, optional

The legend parameter to be changed when dragged:

- [x] '**loc**': update the loc parameter of the legend
- [x] '**bbox**': update the bbox_to_anchor parameter of the legend

**Returns：**

If *state* is ``True`` this returns the `~.DraggableLegend` helper
instance. Otherwise this returns ``None``.

---

#### set_frame_on

```
set_frame_on()
```

Set whether the legend box patch is drawn.

**Parameters:**

- **`b`** : **bool**

---

#### set_title

```
set_title(title, prop=None)
```

Set the legend title. Fontproperties can be optionally set with *prop*parameter.

---

#### update_default_handler_map

```
classmethod update_default_handler_map(handler_map)
```

A class method to update the default handler map.

---

#### zorder

```
zorder=5
```

---



