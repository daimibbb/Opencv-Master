# lines

```python
matplotlib.lines
```

This module contains all the 2D line class which can draw with a variety of line styles, markers and colors.

### Classes

| **`Line2D`**(xdata, ydata[, linewidth, linestyle, ...]) | A line - the line can have both a solid linestyle connecting all the vertices, and a marker at each vertex. |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| **`VertexSelector`**(line)                              | Manage the callbacks to maintain a list of selected vertices for **`matplotlib.lines.Line2D`**. |

### Functions

| **`segment_hits`**(cx, cy, x, y, radius) | Determine if any line segments are within radius of a point. |
| ---------------------------------------- | ------------------------------------------------------------ |
|                                          |                                                              |

---

# ==Line2D==

```python
class matplotlib.lines.Line2D(xdata, ydata, linewidth=None, linestyle=None, color=None, marker=None, markersize=None, markeredgewidth=None, markeredgecolor=None, markerfacecolor=None, markerfacecoloralt='none', fillstyle=None, antialiased=None, dash_capstyle=None, solid_capstyle=None, dash_joinstyle=None, solid_joinstyle=None, pickradius=5, drawstyle=None, markevery=None, **kwargs)
```

Bases: **`matplotlib.artist.Artist`**

A line - the line can have both a solid linestyle connecting all the vertices, and a marker at each vertex. Additionally, the drawing of the solid line is influenced by the drawstyle, e.g., one can create "stepped" lines in various styles.

Create a **`Line2D`** instance with *x* and *y* data in sequences *xdata*, *ydata*.

The kwargs are **`Line2D`** properties:

| Property                                    | Description                                                  |
| ------------------------------------------- | ------------------------------------------------------------ |
| [`agg_filter`](#agg_filter)                 | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array |
| [`alpha`](#alpha)                           | float                                                        |
| [`animated`](#animated)                     | bool                                                         |
| [`antialiased`](#antialiased)               | bool                                                         |
| [`clip_box`](#clip_box)                     | **`Bbox`**(`matplotlib.transforms.Bbox`)                     |
| [`clip_on`](#clip_on)                       | bool                                                         |
| [`clip_path`](#clip_path)                   | [(**`Path`**, **`Transform`**)                               |
| [`color`](#color)                           | color                                                        |
| [`contains`](#contains)                     | callable                                                     |
| [`dash_capstyle`](#dash_capstyle)           | {'butt', 'round', 'projecting'}                              |
| [`dash_joinstyle`](#dash_joinstyle)         | {'miter', 'round', 'bevel'}                                  |
| [`dashes`](#dashes)                         | sequence of floats (on/off ink in points) or (None, None)    |
| [`drawstyle`](#drawstyle)                   | {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'} |
| [`figure`](#figure)                         | **`Figure`**                                                 |
| [`fillstyle`](#fillstyle)                   | {'full', 'left', 'right', 'bottom', 'top', 'none'}           |
| [`gid`](#gid)                               | str                                                          |
| **`in_layout`**                             | bool                                                         |
| [`label`](#label)                           | object                                                       |
| [`linestyle`](#linestyle)                   | {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}        |
| [`linewidth`](#linewidth)                   | float                                                        |
| [`marker`](#marker)                         | unknown                                                      |
| [`markeredgecolor`](#markeredgecolor)       | color                                                        |
| [`markeredgewidth`](#markeredgewidth)       | float                                                        |
| [`markerfacecolor`](#markerfacecolor)       | color                                                        |
| [`markerfacecoloralt`](#markerfacecoloralt) | color                                                        |
| [`markersize`](#markersize)                 | float                                                        |
| [`markevery`](markevery)                    | unknown                                                      |
| [`path_effects`](#path_effects)             | **`AbstractPathEffect`**                                     |
| [`picker`](#picker)                         | float or callable[[Artist, Event], Tuple[bool, dict]]        |
| [`pickradius`](#pickradius)                 | float                                                        |
| [`rasterized`](#rasterized)                 | bool or None                                                 |
| [`sketch_params`](#sketch_params)           | (scale: float, length: float, randomness: float)             |
| [`snap`](#snap)                             | bool or None                                                 |
| [`solid_capstyle`](#solid_capstyle)         | {'butt', 'round', 'projecting'}                              |
| [`solid_joinstyle`](#solid_joinstyle)       | {'miter', 'round', 'bevel'}                                  |
| [`transform`](#transform)                   | matplotlib.transforms.Transform                              |
| [`url`](#url)                               | str                                                          |
| [`visible`](#visible)                       | bool                                                         |
| [`xdata`](#xdata)                           | 1D array                                                     |
| [`ydata`](#ydata)                           | 1D array                                                     |
| [`zorder`](#zorder)                         | float                                                        |

---

# ==VertexSelector==

```python
class matplotlib.lines.VertexSelector(line)
```

​	Bases: **`object`**

​	Manage the callbacks to maintain a list of selected vertices for **`matplotlib.lines.Line2D`**. Derived classes should override **`process_selected()`** to do something with the picks.

​	Here is an example which highlights the selected verts with red circles:

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class HighlightSelected(lines.VertexSelector):
    def __init__(self, line, fmt='ro', **kwargs):
        lines.VertexSelector.__init__(self, line)
        self.markers, = self.axes.plot([], [], fmt, **kwargs)

    def process_selected(self, ind, xs, ys):
        self.markers.set_data(xs, ys)
        self.canvas.draw()

fig, ax = plt.subplots()
x, y = np.random.rand(2, 30)
line, = ax.plot(x, y, 'bs-', picker=5)

selector = HighlightSelected(line)
plt.show()
```

​	Initialize the class with a **`matplotlib.lines.Line2D`** instance. The line should already be added to some **`matplotlib.axes.Axes`** instance and should have the picker property set.

- **`onpick(event)`**

When the line is picked, update the set of selected indices.

- **`process_selected(ind, xs, ys)`**

Default "do nothing" implementation of the **`process_selected()`** method.

*ind* are the indices of the selected vertices. *xs* and *ys* are the coordinates of the selected vertices.

---

# ==segment_hits==

```python
matplotlib.lines.segment_hits(cx, cy, x, y, radius)
```

Determine if any line segments are within radius of a point. Returns the list of line segments that are within that radius.

----

# 函数详解

# agg_filter

```python
matplotlib.artist.Artist.set_agg_filter
```

**`Artist.set_agg_filter(filter_func)`**

Set the **agg_filter**.

**Parameters：**

- **`filter_func`** : callable
  A filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array.

----

# alpha

```python
matplotlib.artist.Artist.set_alpha
```

**`Artist.set_alpha(alpha)`**

Set the alpha value used for blending - not supported on all backends.

**Parameters：**

- **`alpha`** : float

---

# animated

```python
matplotlib.artist.Artist.set_animated
```

**`Artist.set_animated(b)`**

Set the artist's animation state.

**Parameters：**

- **`b`** : bool

---

# antialiased

```python
matplotlib.lines.Line2D.set_antialiased
```

**`set_antialiased(b)`**

Set whether to use antialiased rendering.(设置是否使用抗锯齿渲染)

**Parameters：**

- **`b`** : bool

---

# clip_box

```python
matplotlib.artist.Artist.set_clip_box
```

**`Artist.set_clip_box(clipbox)`**

Set the artist's clip **`Bbox`**.

**Parameters：**

- **`clipbox`** : **`Bbox`**

---

# clip_on

```python
matplotlib.artist.Artist.set_clip_on
```

**`Artist.set_clip_on(b)`**

Set whether artist uses clipping.

When False artists will be visible out side of the axes which can lead to unexpected results.

**Parameters：**

- **`b`** : bool

---

# clip_path

```python
matplotlib.artist.Artist.set_clip_path
```

**`Artist.set_clip_path(path, transform=None)`**

Set the artist's clip path, which may be:

- a **`Patch`** (or subclass) instance; or
- a **`Path`** instance, in which case a **`Transform`** instance, which will be applied to the path before using it for clipping, must be provided; or
- **`None`**, to remove a previously set clipping path.

For efficiency, if the path happens to be an axis-aligned rectangle, this method will set the clipping box to the corresponding rectangle and set the clipping path to **`None`**.

ACCEPTS: **`[(Path, Transform) | Patch | None]`**

---

# color

```python
matplotlib.lines.Line2D.set_color
```

**`set_color(color)`**

Set the color of the line

**Parameters：**

- **`color`** : color

---

# contains

```python
matplotlib.artist.Artist.set_contains
```

**`Artist.set_contains(picker)`**

Replace the contains test used by this artist. The new picker should be a **callable function** which determines whether the artist is hit by the mouse event:

```
hit, props = picker(artist, mouseevent)
```

If the mouse event is over the artist, return *hit* = *True* and *props* is a dictionary of properties you want returned with the contains test.

**Parameters：**

- **`picker `** : callable

---

# dash_capstyle

```python
matplotlib.lines.Line2D.set_dash_capstyle
```

**`set_dash_capstyle(s)`**

Set the cap style for dashed linestyles.

**Parameters：**

- **`s`** : {'butt', 'round', 'projecting'}

---

# dash_joinstyle

```python
matplotlib.lines.Line2D.set_dash_joinstyle
```

**`set_dash_joinstyle(s)`**

Set the join style for dashed linestyles.

**Parameters：**

- **`s`** : {'miter', 'round', 'bevel'}

---

# dashes

```python
matplotlib.lines.Line2D.set_dashes
```

**`set_dashes(seq)`**

Set the dash sequence, sequence of dashes with on off ink in points. 

If **seq** is empty or if **`seq = (None, None)`**, the linestyle will be set to **solid**.

**Parameters：**

- **`seq`** : sequence of floats (on/off ink in points) or (None, None)

---

# drawstyle

```python
matplotlib.lines.Line2D.set_drawstyle
```

**`set_drawstyle(drawstyle)`**

Set the drawstyle of the plot

**`default`** connects the points with lines. The steps variants produce step-plots. 'steps' is equivalent to 'steps-pre' and is maintained for backward-compatibility.

**Parameters：**

- **`drawstyle`** :{'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}

---

# figure

```python
matplotlib.artist.Artist.set_figure
```

**`Artist.set_figure(fig)`**

Set the **`Figure`** instance the artist belongs to.

**Parameters：**

- **`fig `** : **`Figure`**

---

# fillstyle

```python
matplotlib.lines.Line2D.set_fillstyle
```

**`set_fillstyle(fs)`**

Set the marker fill style; **`full`** means fill the whole marker. **`none`** means no filling; other options are for half-filled markers.

**Parameters：**

- **`fs `** : {'full', 'left', 'right', 'bottom', 'top', 'none'}

----

# gid

```python
matplotlib.artist.Artist.set_gid
```

**`Artist.set_gid(gid)`**

Sets the (group) id for the artist.

**Parameters：**

- **`gid `** :str

---

# label

```:film_strip:
matplotlib.artist.Artist.set_label
```

**`Artist.set_label(s)`**

Set the label to *s* for auto legend.

**Parameters：**

- **`s`** : object
  s will be converted to a string by calling str.

---

# linestyle

```:film_strip:
matplotlib.lines.Line2D.set_linestyle
```

**`set_linestyle(ls)`**

Set the linestyle of the line (also accepts drawstyles, e.g., `'steps--'`)

| linestyle             | description      |
| --------------------- | ---------------- |
| `'-'` or `'solid'`    | solid line       |
| `'--'` or `'dashed'`  | dashed line      |
| `'-.'` or `'dashdot'` | dash-dotted line |
| `':'` or `'dotted'`   | dotted line      |
| `'None'`              | draw nothing     |
| `' '`                 | draw nothing     |
| `''`                  | draw nothing     |

'steps' is equivalent to 'steps-pre' and is maintained for backward-compatibility.

Alternatively a dash tuple of the following form can be provided:

```
(offset, onoffseq),
```

where `onoffseq` is an even length tuple of on and off ink in points.

**Parameters：**

- **`ls`** : {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

  The line style.

---

# linewidth

```:signal_strength:
matplotlib.lines.Line2D.set_linewidth
```

**`set_linewidth(w)`**

Set the line width in points

**Parameters：**

- **`w`** : float

---

# marker

```:straight_ruler:
matplotlib.lines.Line2D.set_marker
```

**`set_marker(marker)`**

Set the line marker.

**Parameters：**

- **`marker`** : marker style
  See **`markers`** for full description of possible arguments.

---

# markeredgecolor

```:strawberry:
matplotlib.lines.Line2D.set_markeredgecolor
```

**`set_markeredgecolor(ec)`**

Set the marker edge color.

**Parameters：**

- **`ec `** : color

---

# markeredgewidth

```:film_strip:
matplotlib.lines.Line2D.set_markeredgewidth
```

**`set_markeredgewidth(ew)`**

Set the marker edge width in points.

**Parameters：**

- **`ew `** : float

---

# markerfacecolor

```:signal_strength:
matplotlib.lines.Line2D.set_markerfacecolor
```

**`set_markerfacecolor(fc)`**

Set the marker face color.

**Parameters：**

- **`fc `** : color

---

# markerfacecoloralt

```:straight_ruler:
matplotlib.lines.Line2D.set_markerfacecoloralt
```

**`set_markerfacecoloralt(fc)`**

Set the **alternate** marker face color.

**Parameters：**

- **`fc `** : color

---

# markersize

```:strawberry:
matplotlib.lines.Line2D.set_markersize
```

**`set_markersize(sz)`**

Set the marker size in points.

**Parameters：**

- **`sz `** : float

---

# markevery

```:film_strip:
matplotlib.lines.Line2D.set_markevery
```

**`set_markevery(every)`**

Set the markevery property to subsample the plot when using markers.

e.g., if every=5, every 5-th marker will be plotted.

**Parameters:**	

- **`every`**: None or int or (int, int) or slice or List[int] or float or (float, float)
  Which markers to plot.

  ​	**`every=None`**, every point will be plotted.
  ​	**`every=N`**, every N-th marker will be plotted starting with marker 0.
  ​	**`every=(start, N)`**, every N-th marker, starting at point start, will be plotted.
  ​	**`every=slice(start, end, N)`**, every N-th marker, starting at point start, up to but not including point end, will be plotted.
  ​	**`every=[i, j, m, n]`**, only markers at points i, j, m, and n will be plotted.
  ​	**`every=0.1`**, (i.e. a float) then markers will be spaced at approximately equal distances along the line; the distance along 	the line between markers is determined by multiplying the display-coordinate distance of the axes bounding-box diagonal by the value of every.
  ​	**`every=(0.5, 0.1)`** (i.e. a length-2 tuple of float), the same functionality as every=0.1 is exhibited but the first marker will be 0.5 multiplied by the display-cordinate-diagonal-distance along the line.

Notes

Setting the markevery property will only show markers at actual data points. When using float arguments to set the markevery property on irregularly spaced data, the markers will likely not appear evenly spaced because the actual data points do not coincide with the theoretical spacing between markers.

When using a start offset to specify the first marker, the offset will be from the first data point which may be different from the first the visible data point if the plot is zoomed in.

If zooming in on a plot when using float arguments then the actual data points that have markers will change because the distance between markers is always determined from the display-coordinates axes-bounding-box-diagonal regardless of the actual axes data limits.

----

# path_effects

```:signal_strength:
matplotlib.artist.Artist.set_path_effects
```

**`Artist.set_path_effects(path_effects)`**

Set the path effects.

**Parameters:**	

- **`path_effects `**: **`AbstractPathEffect`**

---

# picker

```python
matplotlib.lines.Line2D.set_picker
```

**`set_picker(p)`**

Sets the event picker details for the line.

**Parameters:**	

- **`p `**: **`float`** or **`callable[[Artist, Event]`**, Tuple[bool, dict]]
  If a float, it is used as the pick radius in points.

---

# pickradius

```python
matplotlib.lines.Line2D.set_pickradius
```

**`set_pickradius(d)`**

Set the pick radius used for containment tests.

**Parameters:**	

- **`d `**:  float

  Pick radius, in points.

----

# rasterized

```python
matplotlib.artist.Artist.set_rasterized
```

**`Artist.set_rasterized(rasterized)`**

Force rasterized (bitmap) drawing in vector backend output.(栅格化)

Defaults to None, which implies the backend's default behavior.

**Parameters:**	

- **`rasterized`** : bool or None

---

# sketch_params

```
matplotlib.artist.Artist.set_sketch_params
```

**`Artist.set_sketch_params(scale=None, length=None, randomness=None)`**

Sets the sketch parameters.

**Parameters:	**

- **`scale`** : float, optional
  The amplitude of the wiggle perpendicular to the source line, in pixels. If scale is None, or not provided, no sketch filter will be provided.

- **`length`** : float, optional
  The length of the wiggle along the line, in pixels (default 128.0)

- **`randomness`** : float, optional
  The scale factor by which the length is shrunken or expanded (default 16.0)

---

# snap

```
matplotlib.artist.Artist.set_snap
```

**`Artist.set_snap(snap)`**

Sets the snap setting which may be:

> - True: snap vertices to the nearest pixel center
> - False: leave vertices as-is
> - None: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

**Parameters:	**

- **`snap `** : bool or None

---

# solid_capstyle

```:signal_strength:
matplotlib.lines.Line2D.set_solid_capstyle
```

**`set_solid_capstyle(s)`**

Set the cap style for solid linestyles.

**Parameters:	**

- **`s `** : {'butt', 'round', 'projecting'}

---

# set_solid_joinstyle

```:signal_strength:
matplotlib.lines.Line2D.set_solid_joinstyle
```

**`set_solid_joinstyle(s)`**

Set the join style for solid linestyles.

**Parameters:	**

- **`s `** :{'miter', 'round', 'bevel'}

---

# set_transform

```:signal_strength:
matplotlib.lines.Line2D.set_transform
```

**`set_transform(t)`**

set the Transformation instance used by this artist

**Parameters:	**

- **`t `** : **`Transform`**

---

# url

```:signal_strength:
matplotlib.artist.Artist.set_url
```

**`Artist.set_url(url)`**

Sets the url for the artist.

**Parameters:	**

- **`url`** : str

---

# visible

```
matplotlib.artist.Artist.set_visible
```

**`Artist.set_visible(b)`**

Set the artist's visibility.

**Parameters:	**

- **`b`** : bool

---

# set_xdata

```:signal_strength:
matplotlib.lines.Line2D.set_xdata
```

**`set_xdata(t)`**

Set the data array for x.

**Parameters:	**

- **`x `** : 1D array

---

# set_ydata

```:signal_strength:
matplotlib.lines.Line2D.set_ydata
```

**`set_ydata(t)`**

Set the data array for y.

**Parameters:	**

- **`y `** : 1D array

---

# set_zorder

```:signal_strength:
matplotlib.artist.Artist.set_zorder
```

**`Artist.set_zorder(level)`**

Set the zorder for the artist. Artists with lower zorder values are drawn first.

**Parameters:	**

- **`level `** : float



---

# Details

See [`set_linestyle()`](#linestyle) for a description of the line styles, [`set_marker()`](#marker) for a description of the markers, and [`set_drawstyle()`](#drawstyle) for a description of the draw styles.

## axes

**`axes`**

the Axes instance the artist resides in, or None.

---

## contains

**`contains(mouseevent)`**

Test whether the mouse event occurred on the line. The pick radius determines the precision of the location test (usually within five points of the value). Use **`get_pickradius()`** or **`set_pickradius()`** to view or modify it.

Returns True if any values are within the radius along with {'ind': pointlist}, where pointlist is the set of points within the radius.

TODO: sort returned indices by distance

---

## draw

**`draw(renderer)`**

draw the Line with `renderer` unless visibility is False

----

## drawStyleKeys 

```:strawberry:
drawStyleKeys = ['default', 'steps-mid', 'steps-pre', 'steps-post', 'steps']
```

---

## drawStyles 

```
drawStyles = {'default': '_draw_lines', 'steps': '_draw_steps_pre', 'steps-mid': '_draw_steps_mid', 'steps-post': '_draw_steps_post', 'steps-pre': '_draw_steps_pre'}
```

---

## fillStyles 

```
fillStyles = ('full', 'left', 'right', 'bottom', 'top', 'none')
```

---

## filled_markers 

```
filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
```

----

## get_aa

```
get_aa(*args, **kwargs)
```

alias for **`get_antialiased`**

---

## get_antialiased

**`get_antialiased()`**

---

## get_c

```
get_c(*args, **kwargs)
```

alias for **`get_color`**

---

## get_color

**`get_color()`**

---

## get_dash_capstyle

**`get_dash_capstyle()`**

Get the cap style for dashed linestyles

---

## get_dash_joinstyle

**`get_dash_joinstyle()`**

Get the join style for dashed linestyles

---

## get_data

**`get_data(orig=True)`**

Return the xdata, ydata.

If *orig* is *True*, return the original data.

---

## get_drawstyle

**`get_drawstyle()`**

---

## get_fillstyle

**`get_fillstyle()`**

return the marker fillstyle

---

## get_linestyle

**`get_linestyle()`**

---

## get_linewidth

**`get_linewidth()`**

---

## get_ls

```
get_ls(*args, **kwargs)
```

alias for **`get_linestyle`**

---

## get_lw

```
get_lw(*args, **kwargs)
```

alias for **`get_linewidth`**

---

## get_marker

**`get_marker()`**

---

## get_markeredgecolor

**`get_markeredgecolor()`**

---

## get_markeredgewidth

**`get_markeredgewidth()`**

---

## get_markerfacecolor

**`get_markerfacecolor()`**

---

## get_markerfacecoloralt

**`get_markerfacecoloralt()`**

---

## get_markersize

**`get_markersize()`**

---

## get_markevery

**`get_markevery()`**

return the markevery setting

---

## get_mec

```
get_mec(*args, **kwargs)
```

alias for **`get_markeredgecolor`**

---

## get_mew

```
get_mew(*args, **kwargs)
```

alias for **`get_markeredgewidth`**

---

## get_mfc

```
get_mfc(*args, **kwargs)
```

alias for **`get_markerfacecolor`**

---

## get_mfcalt

```
get_mfcalt(*args, **kwargs)
```

alias for **`get_markerfacecoloralt`**

---

## get_ms

```
get_ms(*args, **kwargs)
```

alias for **`get_markersize`**

---

## get_path

**`get_path()`**

Return the **`Path`** object associated with this line.

---

## get_pickradius

**`get_pickradius()`**

return the pick radius used for containment tests

---

## get_solid_capstyle

**`get_solid_capstyle()`**

Get the cap style for solid linestyles

---

## get_solid_joinstyle

**`get_solid_joinstyle()`**

Get the join style for solid linestyles

---

## get_window_extent

**`get_window_extent(renderer)`**

Get the axes bounding box in display space. Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Be careful when using this function, the results will not update if the artist window extent of the artist changes. The extent can change due to any changes in the transform stack, such as changing the axes limits, the figure size, or the canvas used (as is done when saving a figure). This can lead to unexpected behavior where interactive figures will look fine on the screen, but will save incorrectly.

---

## get_xdata

**`get_xdata(rig=True)`**

Return the xdata.

If *orig* is *True*, return the original data, else the processed data.

---

## get_xydata

**`get_xydata()`**

Return the *xy* data as a Nx2 numpy array.

---

## get_ydata

**`get_ydata(rig=True)`**

Return the xdata.

If *orig* is *True*, return the original data, else the processed data.

---

## is_dashed

**`is_dashed()`**

return True if line is dashstyle

---

## lineStyles

```
lineStyles = {'': '_draw_nothing', ' ': '_draw_nothing', '-': '_draw_solid', '--': '_draw_dashed', '-.': '_draw_dash_dot', ':': '_draw_dotted', 'None': '_draw_nothing'}
```

----

## markers 

```
markers = {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_down', '^': 'triangle_up', '<': 'triangle_left', '>': 'triangle_right', '1': 'tri_down', '2': 'tri_up', '3': 'tri_left', '4': 'tri_right', '8': 'octagon', 's': 'square', 'p': 'pentagon', '*': 'star', 'h': 'hexagon1', 'H': 'hexagon2', '+': 'plus', 'x': 'x', 'D': 'diamond', 'd': 'thin_diamond', '|': 'vline', '_': 'hline', 'P': 'plus_filled', 'X': 'x_filled', 0: 'tickleft', 1: 'tickright', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase', 10: 'caretupbase', 11: 'caretdownbase', 'None': 'nothing', None: 'nothing', ' ': 'nothing', '': 'nothing'}
```

---

## recache

**`recache(always=False)`**

---

## recache_always

**`recache_always()`**

---

## set_data

**`set_data(*args)`**

Set the x and y data

ACCEPTS: 2D array (rows are x, y) or two 1D arrays

---









