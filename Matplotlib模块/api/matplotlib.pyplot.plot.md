# matplotlib.pyplot.plot

```python
matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
```

Plot *y* versus *x* as lines and/or markers.

Call signatures:

```python
plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```

The coordinates of the points or line nodes are given by *x*, *y*.

The optional parameter *fmt* is a convenient way for defining basic formatting like color, marker and linestyle. It's a shortcut string notation described in the *Notes*section below.

```python
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
```

You can use [`Line2D`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) properties as keyword arguments for more control on the appearance. Line properties and *fmt* can be mixed. The following two calls yield identical results:

```python
plot(x, y, 'go--', linewidth=2, markersize=12)
plot(x, y, color='green', marker='o', linestyle='dashed',
     linewidth=2, markersize=12)
```

When conflicting with *fmt*, keyword arguments take precedence.

**Plotting labelled data**

There's a convenient way for plotting objects with labelled data (i.e. data that can be accessed by index `obj['y']`). Instead of giving the data in *x* and *y*, you can provide the object in the *data* parameter and just give the labels for *x* and *y*:

```python
plot('xlabel', 'ylabel', data=obj)
```

> All indexable objects are supported. This could e.g. be a `dict`, a `pandas.DataFame`or a structured numpy array.

**Plotting multiple sets of data**

There are various ways to plot multiple sets of data.

- The most straight forward way is just to call `plot `multiple times. Example:

  ```python
  plot(x1, y1, 'bo')
  lot(x2, y2, 'go')
  ```

- Alternatively, if your data is already a 2d array, you can pass it directly to *x*, *y*. A separate data set will be drawn for every column.

  Example: an array `a` where the first column represents the *x* values and the other columns are the *y* columns:

  ```python
  plot(a[0], a[1:])
  ```

- The third way is to specify multiple sets of *[x]*, *y*, *[fmt]* groups:

  ```python
  plot(x1, y1, 'g^', x2, y2, 'g-')
  ```

  In this case, any additional keyword argument applies to all datasets. Also this syntax cannot be combined with the *data* parameter.

By default, each line is assigned a different style specified by a 'style cycle'. The *fmt*and line property parameters are only necessary if you want explicit deviations from these defaults. Alternatively, you can also change the style cycle using the '`axes.prop_cycle`' rcParam.

###  Returns: 

- lines : A list of `Line2D `objects representing the plotted data.

###  Other Parameters: 

- ***\*kwargs** : `Line2D `properties, optional

*kwargs* are used to specify properties like a line label (for auto legends), linewidth, antialiasing, marker face color. Example:

```python
>>> plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
>>> plot([1,2,3], [1,4,9], 'rs',  label='line 2')
```

If you make multiple lines with one plot command, the kwargs apply to all those lines.

Here is a list of available Line2D properties:

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`agg_filter`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter) | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array |
| [`alpha`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha) | float                                                        |
| [`animated`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated) | bool                                                         |
| [`antialiased`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_antialiased) or aa | bool                                                         |
| [`clip_box`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box) | [`Bbox`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Bbox) |
| [`clip_on`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on) | bool                                                         |
| [`clip_path`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path) | [([`Path`](https://matplotlib.org/api/path_api.html#matplotlib.path.Path), [`Transform`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Transform)) | [`Patch`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch) \| None] |
| [`color`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color) or c | color                                                        |
| [`contains`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_contains.html#matplotlib.artist.Artist.set_contains) | callable                                                     |
| [`dash_capstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle) | {'butt', 'round', 'projecting'}                              |
| [`dash_joinstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle) | {'miter', 'round', 'bevel'}                                  |
| [`dashes`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes) | sequence of floats (on/off ink in points) or (None, None)    |
| [`drawstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_drawstyle) or ds | {'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}, default: 'default' |
| [`figure`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure) | [`Figure`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) |
| [`fillstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_fillstyle) | {'full', 'left', 'right', 'bottom', 'top', 'none'}           |
| [`gid`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid) | str                                                          |
| [`in_layout`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout) | bool                                                         |
| [`label`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label) | object                                                       |
| [`linestyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle) or ls | {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}        |
| [`linewidth`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth) or lw | float                                                        |
| [`marker`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker) | marker style                                                 |
| [`markeredgecolor`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgecolor) or mec | color                                                        |
| [`markeredgewidth`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markeredgewidth) or mew | float                                                        |
| [`markerfacecolor`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecolor) or mfc | color                                                        |
| [`markerfacecoloralt`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markerfacecoloralt) or mfcalt | color                                                        |
| [`markersize`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markersize) or ms | float                                                        |
| [`markevery`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery) | None or int or (int, int) or slice or List[int] or float or (float, float) |
| [`path_effects`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects) | [`AbstractPathEffect`](https://matplotlib.org/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect) |
| [`picker`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_picker) | float or callable[[Artist, Event], Tuple[bool, dict]]        |
| [`pickradius`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_pickradius) | float                                                        |
| [`rasterized`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized) | bool or None                                                 |
| [`sketch_params`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params) | (scale: float, length: float, randomness: float)             |
| [`snap`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap) | bool or None                                                 |
| [`solid_capstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_capstyle) | {'butt', 'round', 'projecting'}                              |
| [`solid_joinstyle`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_solid_joinstyle) | {'miter', 'round', 'bevel'}                                  |
| [`transform`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_transform) | [`matplotlib.transforms.Transform`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Transform) |
| [`url`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url) | str                                                          |
| [`visible`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible) | bool                                                         |
| [`xdata`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata) | 1D array                                                     |
| [`ydata`](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata) | 1D array                                                     |
| [`zorder`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder) | float                                                        |

###  Format Strings

 format string consists of a part for color, marker and line:

```python
fmt = '[marker][line][color]'
```

Each of them is optional. If not provided, the value from the style cycle is used. Exception: If `line` is given, but no `marker`, the data will be a line without markers.

Other combinations such as `[color][marker][line]` are also supported, but note that their parsing may be ambiguous.

#### Markers

| character | description           |
| --------- | --------------------- |
| `'.'`     | point marker          |
| `','`     | pixel marker          |
| `'o'`     | circle marker         |
| `'v'`     | triangle_down marker  |
| `'^'`     | triangle_up marker    |
| `'<'`     | triangle_left marker  |
| `'>'`     | triangle_right marker |
| `'1'`     | tri_down marker       |
| `'2'`     | tri_up marker         |
| `'3'`     | tri_left marker       |
| `'4'`     | tri_right marker      |
| `'s'`     | square marker         |
| `'p'`     | pentagon marker       |
| `'*'`     | star marker           |
| `'h'`     | hexagon1 marker       |
| `'H'`     | hexagon2 marker       |
| `'+'`     | plus marker           |
| `'x'`     | x marker              |
| `'D'`     | diamond marker        |
| `'d'`     | thin_diamond marker   |
| `'|'`     | vline marker          |
| `'_'`     | hline marker          |

#### Line Styles

| character | description         |
| --------- | ------------------- |
| `'-'`     | solid line style    |
| `'--'`    | dashed line style   |
| `'-.'`    | dash-dot line style |
| `':'`     | dotted line style   |

Example format strings:

```python
'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line
```

#### Colors

The supported color abbreviations are the single letter codes

| character | color   |
| --------- | ------- |
| `'b'`     | blue    |
| `'g'`     | green   |
| `'r'`     | red     |
| `'c'`     | cyan    |
| `'m'`     | magenta |
| `'y'`     | yellow  |
| `'k'`     | black   |
| `'w'`     | white   |

and the `'CN'` colors that index into the default property cycle.

If the color is the only part of the format string, you can additionally use any [`matplotlib.colors`](https://matplotlib.org/api/colors_api.html#module-matplotlib.colors) spec, e.g. full names (`'green'`) or hex strings (`'#008000'`).