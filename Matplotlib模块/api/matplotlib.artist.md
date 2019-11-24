# matplotlib.artist

![Inheritance diagram of matplotlib.axes._axes.Axes, matplotlib.axes._base._AxesBase, matplotlib.axis.Axis, matplotlib.axis.Tick, matplotlib.axis.XAxis, matplotlib.axis.XTick, matplotlib.axis.YAxis, matplotlib.axis.YTick, matplotlib.collections.AsteriskPolygonCollection, matplotlib.collections.BrokenBarHCollection, matplotlib.collections.CircleCollection, matplotlib.collections.Collection, matplotlib.collections.EllipseCollection, matplotlib.collections.EventCollection, matplotlib.collections.LineCollection, matplotlib.collections.PatchCollection, matplotlib.collections.PathCollection, matplotlib.collections.PolyCollection, matplotlib.collections.QuadMesh, matplotlib.collections.RegularPolyCollection, matplotlib.collections.StarPolygonCollection, matplotlib.collections.TriMesh, matplotlib.collections._CollectionWithSizes, matplotlib.contour.ClabelText, matplotlib.figure.Figure, matplotlib.image.AxesImage, matplotlib.image.BboxImage, matplotlib.image.FigureImage, matplotlib.image.NonUniformImage, matplotlib.image.PcolorImage, matplotlib.image._ImageBase, matplotlib.legend.Legend, matplotlib.lines.Line2D, matplotlib.offsetbox.AnchoredOffsetbox, matplotlib.offsetbox.AnchoredText, matplotlib.offsetbox.AnnotationBbox, matplotlib.offsetbox.AuxTransformBox, matplotlib.offsetbox.DrawingArea, matplotlib.offsetbox.HPacker, matplotlib.offsetbox.OffsetBox, matplotlib.offsetbox.OffsetImage, matplotlib.offsetbox.PackerBase, matplotlib.offsetbox.PaddedBox, matplotlib.offsetbox.TextArea, matplotlib.offsetbox.VPacker, matplotlib.patches.Arc, matplotlib.patches.Arrow, matplotlib.patches.Circle, matplotlib.patches.CirclePolygon, matplotlib.patches.ConnectionPatch, matplotlib.patches.Ellipse, matplotlib.patches.FancyArrow, matplotlib.patches.FancyArrowPatch, matplotlib.patches.FancyBboxPatch, matplotlib.patches.Patch, matplotlib.patches.PathPatch, matplotlib.patches.Polygon, matplotlib.patches.Rectangle, matplotlib.patches.RegularPolygon, matplotlib.patches.Shadow, matplotlib.patches.Wedge, matplotlib.patches.YAArrow, matplotlib.projections.geo.AitoffAxes, matplotlib.projections.geo.GeoAxes, matplotlib.projections.geo.HammerAxes, matplotlib.projections.geo.LambertAxes, matplotlib.projections.geo.MollweideAxes, matplotlib.projections.polar.PolarAxes, matplotlib.quiver.Barbs, matplotlib.quiver.Quiver, matplotlib.quiver.QuiverKey, matplotlib.spines.Spine, matplotlib.table.Cell, matplotlib.table.CustomCell, matplotlib.table.Table, matplotlib.text.Annotation, matplotlib.text.Text, matplotlib.text.TextWithDash](https://matplotlib.org/_images/inheritance-65ce2e47a854f0550975f5a2d9a9335356c2af71.png)

---

## ==Artist class==

```
class matplotlib.artist.Artist
```

> Abstract base class for someone who renders into a FigureCanvas.

### Interactive

| [`Artist.add_callback`](#Artist.add_callback)             | Adds a callback function that will be called whenever one of the **`Artist`**'s properties changes. |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| [`Artist.format_cursor_data`](#Artist.format_cursor_data) | Return *cursor data* string formatted.                       |
| [`Artist.get_contains`](#Artist.get_contains)             | Return the _contains test used by the artist, or *None* for default. |
| [`Artist.get_cursor_data`](#Artist.get_cursor_data)       | Get the cursor data for a given event.                       |
| [`Artist.get_picker`](#Artist.get_picker)                 | Return the picker object used by this artist.                |
| [`Artist.mouseover`](#Artist.mouseover)                   |                                                              |
| [`Artist.pchanged`](#Artist.pchanged)                     | Fire an event when property changed, calling all of the registered callbacks. |
| [`Artist.pick`](#Artist.pick)                             | Process pick event                                           |
| [`Artist.pickable`](#Artist.pickable)                     | Return *True* if **`Artist`** is pickable.                   |
| [`Artist.remove_callback`](#Artist.remove_callback)       | Remove a callback based on its *id*.                         |
| [`Artist.set_contains`](#Artist.set_contains)             | Replace the contains test used by this artist.               |
| [`Artist.set_picker`](#Artist.set_picker)                 | Set the epsilon for picking used by this artist              |
| [`Artist.contains`](#Artist.contains)                     | Test whether the artist contains the mouse event.            |

### Margins and Autoscaling

| [`Artist.sticky_edges`](#Artist.sticky_edges) | `x` and `y` sticky edge lists. |
| --------------------------------------------- | ------------------------------ |
|                                               |                                |

### Clipping

| [`Artist.get_clip_box`](#Artist.get_clip_box)   | Return artist clipbox                                        |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [`Artist.get_clip_on`](#Artist.get_clip_on)     | Return whether artist uses clipping                          |
| [`Artist.get_clip_path`](#Artist.get_clip_path) | Return artist clip path                                      |
| [`Artist.set_clip_box`](#Artist.set_clip_box)   | Set the artist's clip [`Bbox`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Bbox). |
| [`Artist.set_clip_on`](#Artist.set_clip_on)     | Set whether artist uses clipping.                            |
| [`Artist.set_clip_path`](#Artist.set_clip_path) | Set the artist's clip path, which may be:                    |

### Bulk Properties

| [`Artist.update`](#Artist.update)           | Update this artist's properties from the dictionary *prop*.  |
| ------------------------------------------- | ------------------------------------------------------------ |
| [`Artist.update_from`](#Artist.update_from) | Copy properties from *other* to *self*.                      |
| [`Artist.properties`](#Artist.properties)   | return a dictionary mapping property name -> value for all Artist props |
| [`Artist.set`](#Artist.set)                 | A property batch setter.                                     |

### Drawing

| [`Artist.draw`](#Artist.draw)                                | Derived classes drawing method                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Artist.get_animated`](#Artist.get_animated)                | Return the artist's animated state                           |
| [`Artist.set_animated`](#Artist.set_animated)                | Set the artist's animation state.                            |
| [`Artist.get_agg_filter`](#Artist.get_agg_filter)            | Return filter function to be used for agg filter.            |
| [`Artist.get_alpha`](#Artist.get_alpha)                      | Return the alpha value used for blending - not supported on all backends |
| [`Artist.get_snap`](#Artist.get_snap)                        | Returns the snap setting which may be:                       |
| [`Artist.get_visible`](#Artist.get_visible)                  | Return the artist's visiblity                                |
| [`Artist.get_zorder`](#Artist.get_zorder)                    | Return the artist's zorder.                                  |
| [`Artist.set_agg_filter`](#Artist.set_agg_filter)            | Set the agg filter.                                          |
| [`Artist.set_alpha`](#Artist.set_alpha)                      | Set the alpha value used for blending - not supported on all backends. |
| [`Artist.set_sketch_params`](#Artist.set_sketch_params)      | Sets the sketch parameters.                                  |
| [`Artist.set_snap`](#Artist.set_snap)                        | Sets the snap setting which may be:                          |
| [`Artist.get_rasterized`](#Artist.get_rasterized)            | Return whether the artist is to be rasterized.               |
| [`Artist.get_sketch_params`](#Artist.get_sketch_params)      | Returns the sketch parameters for the artist.                |
| [`Artist.set_path_effects`](#Artist.set_path_effects)        | Set the path effects.                                        |
| [`Artist.set_rasterized`](#Artist.set_rasterized)            | Force rasterized (bitmap) drawing in vector backend output.  |
| [`Artist.zorder`](#Artist.zorder)                            |                                                              |
| [`Artist.set_visible`](#Artist.set_visible)                  | Set the artist's visibility.                                 |
| [`Artist.set_zorder`](#Artist.set_zorder)                    | Set the zorder for the artist.                               |
| [`Artist.get_window_extent`](#Artist.get_window_extent)      | Get the axes bounding box in display space.                  |
| [`Artist.get_path_effects`](#Artist.get_path_effects)        |                                                              |
| [`Artist.get_transformed_clip_path_and_affine`](#Artist.get_transformed_clip_path_and_affine) | Return the clip path with the non-affine part of its transformation applied, and the remaining affine part of its transformation. |

### Figure and Axes

| [`Artist.remove`](#Artist.remove)          | Remove the artist from the figure if possible.            |
| ------------------------------------------ | --------------------------------------------------------- |
| [`Artist.axes`](#Artist.axes)              | The **`Axes`** instance the artist resides in, or *None*. |
| [`Artist.set_figure`](#Artist.set_figure)  | Set the **`Figure`** instance the artist belongs to.      |
| [`Artist.get_figure`](#Artist.get_figuree) | Return the **`Figure`** instance the artist belongs to.   |

### Children

| [`Artist.get_children`](#Artist.get_children) | Return a list of the child `Artist`s this :class:`Artist` contains. |
| --------------------------------------------- | ------------------------------------------------------------ |
| [`Artist.findobj`](#Artist.findobj)           | Find artist objects.                                         |

### Transform

| [`Artist.set_transform`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform) | Set the artist transform.                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`Artist.get_transform`](#Artist.get_transform)              | Return the **`Transform`** instance used by this artist.     |
| [`Artist.is_transform_set`](#Artist.is_transform_sett)       | Returns *True* if  **`Artist`** has a transform explicitly set. |

### Units

| [`Artist.convert_xunits`](#Artist.convert_xunits) | For artists in an axes, if the xaxis has units support, convert *x* using xaxis unit type |
| ------------------------------------------------- | ------------------------------------------------------------ |
| [`Artist.convert_yunits`](#Artist.convert_yunits) | For artists in an axes, if the yaxis has units support, convert *y* using yaxis unit type |
| [`Artist.have_units`](#Artist.have_units)         | Return *True* if units are set on the *x* or *y* axes        |

### Metadata

| [`Artist.get_gid`](#Artist.get_gid)     | Returns the group id.                             |
| --------------------------------------- | ------------------------------------------------- |
| [`Artist.get_label`](#Artist.get_label) | Get the label used for this artist in the legend. |
| [`Artist.set_gid`](#Artist.set_gid)     | Sets the (group) id for the artist.               |
| [`Artist.set_label`](#Artist.set_label) | Set the label to *s* for auto legend.             |
| [`Artist.get_url`](#Artist.get_url)     | Returns the url.                                  |
| [`Artist.set_url`](#Artist.set_url)     | Sets the url for the artist.                      |
| [`Artist.aname`](#Artist.aname)         |                                                   |

### Stale

| [`Artist.stale`](#Artist.stale) | If the artist is 'stale' and needs to be re-drawn for the output to match the internal state of the artist. |
| ------------------------------- | ------------------------------------------------------------ |
|                                 |                                                              |

## ==Functions==

| [`allow_rasterization`](#allow_rasterization) | Decorator for Artist.draw method.                            |
| --------------------------------------------- | ------------------------------------------------------------ |
| [`get`](#get)                                 | Return the value of object's property.                       |
| [`getp`](#getp)                               | Return the value of object's property.                       |
| [`setp`](#setp)                               | Set a property on an artist object.                          |
| [`kwdoc`](#kwdoc)                             | Inspect an **`Artist`** class and return information about its settable properties and their current values. |
| [`ArtistInspector`](#ArtistInspector)         | A helper class to inspect an **`Artist`** and return information about its settable properties and their current values. |

---

# 函数详解

# Artist.add_callback

```
matplotlib.artist.Artist.add_callback
```

**`Artist.add_callback(func)`**

​	Adds a callback function that will be called whenever one of the **`Artist`**'s properties changes.

​	Returns an **`id`** that is useful for removing the callback with **`remove_callback()`** later.

---

# Artist.format_cursor_data

```
matplotlib.artist.Artist.format_cursor_data
```

**`Artist.format_cursor_data(data)`**

​	Return *cursor data* string formatted. (返回格式化的数据字符串)

---

# Artist.get_contains

```
matplotlib.artist.Artist.get_contains
```

**`Artist.get_contains()`**

​	Return the _contains test used by the artist, or *None* for default.

---

# Artist.get_cursor_data

```
matplotlib.artist.Artist.get_cursor_data
```

**`Artist.get_cursor_data(event)`**

​	Get the cursor data for a given event.

------

# Artist.get_picker

```
matplotlib.artist.Artist.get_cursor_data
```

**`Artist.get_picker()`**

​	Return the picker object used by this artist.

---

# Artist.mouseover

```
matplotlib.artist.Artist.mouseover
```

**`Artist.mouseover()`**

---

# Artist.pchanged

```
matplotlib.artist.Artist.pchanged
```

**`Artist.pchanged()`**

​	Fire an event when property changed, calling all of the registered callbacks. (在属性更改时触发事件，调用所有已注册回调)

---

# Artist.pick

```
matplotlib.artist.Artist.pick
```

**`Artist.pick(mouseevent)`**

​	Process pick event

​	each child artist will fire a pick event if *mouseevent* is over the artist and the artist has picker set

---

# Artist.pickable

```
matplotlib.artist.Artist.pickable
```

**`Artist.pickable()`**

​	Return **True** if **`Artist`** is pickable.

----

# Artist.remove_callback

```
matplotlib.artist.Artist.remove_callback
```

**`Artist.remove_callback()`**

​	Remove a callback based on its *id*.

---

# Artist.set_contains

```
matplotlib.artist.Artist.set_contains
```

**`Artist.set_contains(picker)`**

​	Replace the contains test used by this artist. The new picker should be a callable function which determines whether the artist is hit by the mouse event:

```
hit, props = picker(artist, mouseevent)
```

​	If the mouse event is over the artist, return *hit* = *True* and *props* is a dictionary of properties you want returned with the contains test.

**Parameters:**

- **`picker `** : callable

---

# Artist.set_picker

```
matplotlib.artist.Artist.set_picker
```

**`Artist.set_picker(picker)`**

​	Set the epsilon for picking used by this artist

*picker* can be one of the following:

> - *None*: picking is disabled for this artist (default)
>
> - A boolean: if *True* then picking will be enabled and the artist will fire a pick event if the mouse event is over the artist
>
> - A float: if picker is a number it is interpreted as an epsilon tolerance in points and the artist will fire off an event if it's data is within epsilon of the mouse event. For some artists like lines and patch collections, the artist may provide additional data to the pick event that is generated, e.g., the indices of the data within epsilon of the pick event
>
> - A function: if picker is callable, it is a user supplied function which determines whether the artist is hit by the mouse event:
>
>   ```
>   hit, props = picker(artist, mouseevent)
>   ```
>
>   to determine the hit test. if the mouse event is over the artist, return *hit=True* and props is a dictionary of properties you want added to the PickEvent attributes.

**Parameters:**

- **`picker `** : None or bool or float or callable

---

# Artist.contains

```
matplotlib.artist.Artist.contains
```

**`Artist.contains(mouseevent)`**

​	Test whether the artist contains the mouse event.

​	Returns the truth value and a dictionary of artist specific details of selection, such as which points are contained in the pick radius. See individual artists for details.

---

# Artist.sticky_edges

```
matplotlib.artist.Artist.sticky_edges
```

**`Artist.sticky_edges`**

​	`x` and `y` sticky edge lists.

​	When performing autoscaling, if a data limit coincides with a value in the corresponding sticky_edges list, then no margin will be added--the view limit "sticks" to the edge. A typical usecase is histograms, where one usually expects no margin on the bottom edge (0) of the histogram.

This attribute cannot be assigned to; however, the `x` and `y` lists can be modified in place as needed.

**Examples**

```
>>> artist.sticky_edges.x[:] = (xmin, xmax)
>>> artist.sticky_edges.y[:] = (ymin, ymax)
```

---

# Artist.get_clip_box

```
matplotlib.artist.Artist.get_clip_box
```

**`Artist.get_clip_box()`**

​	Return artist clipbox

---

# Artist.get_clip_on

```
matplotlib.artist.Artist.get_clip_on
```

**`Artist.get_clip_on()`**

​	Return whether artist uses clipping

---

# Artist.get_clip_path

```
matplotlib.artist.Artist.get_clip_path
```

**`Artist.get_clip_path()`**

​	Return artist clip path

---

# Artist.set_clip_box

```
matplotlib.artist.Artist.set_clip_box
```

**`Artist.set_clip_box(clipbox)`**

​	Set the artist's clip **`Bbox`**.

**Parameters:**

- **`clipbox `** : **`Bbox`**.

---

# Artist.set_clip_on

```
matplotlib.artist.Artist.set_clip_on
```

**`Artist.set_clip_on(b)`**

​	Set whether artist uses clipping.

​	When False artists will be visible out side of the axes which can lead to unexpected results.

**Parameters:**

- **`b`** : bool.

---

# Artist.set_clip_path

```
matplotlib.artist.Artist.set_clip_path
```

**`Artist.set_clip_path(path, transform=None)`**

	Set the artist's clip path, which may be:

- a **`Patch`** (or subclass) instance; or
- a **`Path`** instance, in which case a **`Transform`** instance, which will be applied to the path before using it for clipping, must be provided; or
- None, to remove a previously set clipping path

For efficiency, if the path happens to be an axis-aligned rectangle, this method will set the clipping box to the corresponding rectangle and set the clipping path to None.

ACCEPTS: [**`(Path, Transform)`** | **`Patch`** | **`None`**]

---

# Artist.update

```
matplotlib.artist.Artist.update
```

**`Artist.update(props)`**

​	Update this artist's properties from the dictionary *prop*.

---

# Artist.update_from

```
matplotlib.artist.Artist.update_from
```

**`Artist.update_from(other)`**

​	Copy properties from *other* to *self*.

---

# Artist.properties

```
matplotlib.artist.Artist.properties
```

**`Artist.properties()`**

​	return a dictionary mapping property name -> value for all Artist props

---

# Artist.set

```
matplotlib.artist.Artist.set
```

**`Artist.set(*\*kwargs)`**

​	A property batch setter. Pass *kwargs* to set properties.

------

# Artist.draw

```
matplotlib.artist.Artist.draw
```

**`Artist.draw(renderer, *args, *\*kwargs)`**

​	Derived classes drawing method

---

# Artist.get_animated

```
matplotlib.artist.Artist.get_animated
```

**`Artist.get_animated()`**

​	Return the artist's animated state

---

# Artist.set_animated

```
matplotlib.artist.Artist.set_animated
```

**`Artist.set_animated(b)`**

​	Set the artist's animation state.

**Parameters:**

- **`b`** : bool.

---

# Artist.get_agg_filter

```
matplotlib.artist.Artist.get_agg_filter
```

**`Artist.get_agg_filter()`**

​	Return filter function to be used for agg filter.

----

# Artist.get_alpha

```
matplotlib.artist.Artist.get_alpha
```

**`Artist.get_alpha()`**

​	Return the alpha value used for blending - not supported on all backends

---

# Artist.get_snap

```
matplotlib.artist.Artist.get_snap
```

**`Artist.get_snap()`**

​	Returns the snap setting which may be:

> - True: snap vertices to the nearest pixel center
> - False: leave vertices as-is
> - None: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

---

# Artist.get_visible

```
matplotlib.artist.Artist.get_visible
```

**`Artist.get_visible()`**

​	Return the artist's visiblity

---

# Artist.get_zorder

```
matplotlib.artist.Artist.get_zorder
```

**`Artist.get_zorder()`**

​	Return the artist's zorder.

---

# Artist.set_agg_filter

```
matplotlib.artist.Artist.set_agg_filter
```

**`Artist.set_agg_filter(filter_func)`**

​	Set the agg filter.

**Parameters:**

- **`filter_func `** : callable

  A filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array.

---

# Artist.set_alpha

```
matplotlib.artist.Artist.set_alpha
```

**`Artist.set_alpha(alpha)`**

​	Set the alpha value used for blending - not supported on all backends.

**Parameters:**

- **`alpha `** : float

---

# Artist.set_sketch_params

```
matplotlib.artist.Artist.set_sketch_params
```

**`Artist.set_sketch_params(scale=None, length=None, randomness=None)`**

​	Set the alpha value used for blending - not supported on all backends.

**Parameters:**

- **`scale`** : float, optional
  The amplitude of the wiggle perpendicular to the source line, in pixels. If scale is None, or not provided, no sketch filter will be provided.
- **`length`** : float, optional
  The length of the wiggle along the line, in pixels (default 128.0)
- **`randomness`** : float, optional
  The scale factor by which the length is shrunken or expanded (default 16.0)

---

# Artist.set_snap

```
matplotlib.artist.Artist.set_snap
```

**`Artist.set_snap(snap)`**

​	Sets the snap setting which may be:

> - True: snap vertices to the nearest pixel center
> - False: leave vertices as-is
> - None: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center

Only supported by the Agg and MacOSX backends.

**Parameters:**

- **`snap`** : bool or None

---

# Artist.get_rasterized

```
matplotlib.artist.Artist.get_rasterized
```

**`Artist.get_rasterized()`**

​	Return whether the artist is to be rasterized.

---

# Artist.get_sketch_params

```
matplotlib.artist.Artist.get_sketch_params
```

**`Artist.get_sketch_params()`**

​	Returns the sketch parameters for the artist.

**Returns:**

- **`sketch_params`** : tuple or *None*

A 3-tuple with the following elements:

> - `scale`: The amplitude of the wiggle perpendicular to the source line.
> - `length`: The length of the wiggle along the line.
> - `randomness`: The scale factor by which the length is shrunken or expanded.

May return *None* if no sketch parameters were set.

---

# Artist.set_path_effects

```
matplotlib.artist.Artist.set_path_effects
```

**`Artist.set_path_effects(path_effects)`**

​	Set the path effects.

**Parameters:**

- **`path_effects`** : **`AbstractPathEffect`**

---

# Artist.set_rasterized

```
matplotlib.artist.Artist.set_rasterized
```

**`Artist.set_rasterized(rasterized)`**

​	Force rasterized (bitmap) drawing in vector backend output.

​	Defaults to None, which implies the backend's default behavior.

**Parameters:**

- **`rasterized`** : bool or None

---

# Artist.zorder

```
matplotlib.artist.Artist.zorder
```

**`Artist.zorder=0`**

---

# Artist.set_visible

```
matplotlib.artist.Artist.set_visible
```

**`Artist.set_visible(b)`**

​	Set the artist's visibility.

**Parameters:**

- **`b`** : bool 

---

# Artist.set_zorder

```
matplotlib.artist.Artist.set_zorder
```

**`Artist.set_zorder(level)`**

​	Set the zorder for the artist. Artists with lower zorder values are drawn first.

**Parameters:**

- **`level`** : float

---

# Artist.get_window_extent

```
matplotlib.artist.Artist.get_window_extent
```

**`Artist.get_window_extent(renderer)`**

Get the axes bounding box in display space. Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Be careful when using this function, the results will not update if the artist window extent of the artist changes. The extent can change due to any changes in the transform stack, such as changing the axes limits, the figure size, or the canvas used (as is done when saving a figure). This can lead to unexpected behavior where interactive figures will look fine on the screen, but will save incorrectly.

---

# Artist.get_path_effects

```
matplotlib.artist.Artist.get_path_effects
```

**`Artist.get_path_effects()`**

---

# Artist.get_transformed_clip_path_and_affine

```
matplotlib.artist.Artist.get_transformed_clip_path_and_affine
```

**`Artist.get_transformed_clip_path_and_affine()`**

​	Return the clip path with the non-affine part of its transformation applied, and the remaining affine part of its transformation.

---

# Artist.remove

```
matplotlib.artist.Artist.remove
```

**`Artist.remove()`**

​	Remove the artist from the figure if possible. The effect will not be visible until the figure is redrawn, e.g., with **`matplotlib.axes.Axes.draw_idle()`**. Call **`matplotlib.axes.Axes.relim()`** to update the axes limits if desired.

Note: **`relim()`** will not see collections even if the collection was added to axes with **`autolim = True`**.

Note: there is no support for removing the artist's legend entry.	

---

# Artist.axes

```
matplotlib.artist.Artist.axes
```

**`Artist.axes`**

​	The **`Axes`** instance the artist resides in, or *None*.

---

# Artist.set_figure

```
matplotlib.artist.Artist.set_figure
```

**`Artist.set_figure(fig)`**

​	Set the **`Figure`** instance the artist belongs to.

**Parameters:**

- **`fig`** : **`Figure`**

---

# Artist.get_figure

```
matplotlib.artist.Artist.get_figure
```

**`Artist.get_figure()`**

​	Return the **`Figure`** instance the artist belongs to.

---

# Artist.get_children

```
matplotlib.artist.Artist.get_children
```

**`Artist.get_children()`**

​	Return a list of the child `Artist`s this :class:`Artist` contains.

---

# Artist.findobj

```
matplotlib.artist.Artist.findobj
```

**`Artist.findobj(match=None, include_self=True)`**

	Find artist objects.

Recursively find all **`Artist`** instances contained in self.

*match* can be

> - None: return all objects contained in artist.
> - function with signature `boolean = match(artist)` used to filter matches
> - class instance: e.g., Line2D. Only return artists of class type.

If **`include_self`** is True (default), include self in the list to be checked for a match.

---

# Artist.set_transform

```
matplotlib.artist.Artist.set_transform
```

**`Artist.set_transform(t)`**

​	Set the artist transform.

**Parameters:**

- **`t`** : **` Transform`**

---

# Artist.get_transform

```
matplotlib.artist.Artist.get_transform
```

**`Artist.get_transform()`**

​	Return the **`Transform`** instance used by this artist.

---

# Artist.is_transform_set

```
matplotlib.artist.Artist.is_transform_set
```

**`Artist.is_transform_set()`**

​	Returns True if **`Artist`** has a transform explicitly set.

---

# Artist.convert_xunits

```
matplotlib.artist.Artist.convert_xunits
```

**`Artist.convert_xunits(x)`**

​	For artists in an axes, if the xaxis has units support, convert *x* using xaxis unit type

---

# Artist.convert_yunits

```
matplotlib.artist.Artist.convert_yunits
```

**`Artist.convert_yunits(y)`**

​	For artists in an axes, if the yaxis has units support, convert *y* using yaxis unit type

---

# Artist.have_units

```
matplotlib.artist.Artist.have_units
```

**`Artist.have_units()`**

​	Return *True* if units are set on the *x* or *y* axes

---

# Artist.get_gid

```
matplotlib.artist.Artist.get_gid
```

**`Artist.get_gid()`**

​	Returns the group id.

---

# Artist.get_label

```
matplotlib.artist.Artist.get_label
```

**`Artist.get_label()`**

​	Get the label used for this artist in the legend.

---

# Artist.set_gid

```
matplotlib.artist.Artist.set_gid
```

**`Artist.set_gid(gid)`**

Sets the (group) id for the artist.

**Parameters:**

- **`gid`** : str

---

# Artist.set_label

```
matplotlib.artist.Artist.set_label
```

**`Artist.set_label(s)`**

Set the label to *s* for auto legend.

**Parameters:**

- **`s`** : object
  s will be converted to a string by calling str.

---

# Artist.get_url

```
matplotlib.artist.Artist.get_url
```

**`Artist.get_url()`**

Returns the url.

---

# Artist.set_url

```
matplotlib.artist.Artist.set_url
```

**`Artist.set_url(url)`**

Sets the url for the artist.

**Parameters:**

- **`url`** : str

---

# Artist.aname

```
matplotlib.artist.Artist.aname
```

**`Artist.aname = 'Artist'`**

---

# Artist.stale

```
matplotlib.artist.Artist.stale
```

**`Artist.stale`**

If the artist is 'stale' and needs to be re-drawn for the output to match the internal state of the artist.

---

# allow_rasterization

```
matplotlib.artist.allow_rasterization
```

**`allow_rasterization(draw)`**

Decorator for Artist.draw method. Provides routines that run before and after the draw call. The before and after functions are useful for changing artist-dependent renderer attributes or making other setup function calls, such as starting and flushing a mixed-mode renderer.

---

# get

```
matplotlib.artist.get
```

**`matplotlib.artist.get(obj, property=None)`**

Return the value of object's property. *property* is an optional string for the property you want to return

Example usage:

```
getp(obj)  # get all the object properties
getp(obj, 'linestyle')  # get the linestyle property
```

obj is a Artist instance, e.g., Line2D or an instance of a Axes or matplotlib.text.Text. If the property is 'somename', this function returns

​	**`obj.get_somename()`**
**`getp() `** can be used to query all the gettable properties with **`getp(obj)`**. Many properties have aliases for shorter typing, e.g. 'lw' is an alias for 'linewidth'. In the output, aliases and full property names will be listed as:

​	**`property or alias = value`**
e.g.:

​	**`linewidth or lw = 2`**

---

# getp

```
matplotlib.artist.getp
```

**`matplotlib.artist.getp(obj, property=None)`**

Return the value of object's property. *property* is an optional string for the property you want to return

Example usage:

```
getp(obj)  # get all the object properties
getp(obj, 'linestyle')  # get the linestyle property
```

obj is a Artist instance, e.g., Line2D or an instance of a Axes or matplotlib.text.Text. If the property is 'somename', this function returns

​	**`obj.get_somename()`**
**`getp() `** can be used to query all the gettable properties with **`getp(obj)`**. Many properties have aliases for shorter typing, e.g. 'lw' is an alias for 'linewidth'. In the output, aliases and full property names will be listed as:

​	**`property or alias = value`**
e.g.:

​	**`linewidth or lw = 2`**

---

# setp

```
matplotlib.artist.setp
```

**`matplotlib.artist.setp(obj, *args, *\*kwargs)`**

Set a property on an artist object.

matplotlib supports the use of **`setp()`** ("set property") and **`getp()`** to set and get object properties, as well as to do introspection on the object. For example, to set the linestyle of a line to be dashed, you can do:

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

If you want to know the valid types of arguments, you can provide the name of the property you want to set without a value:

```python
plt.setp(line, 'linestyle')
# inestyle: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
```

If you want to see all the properties that can be set, and their possible values, you can do:

```python
plt.setp(line)
# long output listing omitted
```

you may specify another output file to setp if sys.stdout is not acceptable for some reason using the file keyword-only argument:

```python
>>> with fopen('output.log') as f:
>>>     setp(line, file=f)
```

**`setp()`** operates on a single instance or a iterable of instances. If you are in query mode introspecting the possible values, only the first instance in the sequence is used. When actually setting values, all the instances will be set. e.g., suppose you have a list of two lines, the following will make both lines thicker and red:

```python
import numpy as np

x = np.arange(0, 1.0, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = np.sin(4*np.pi*x)
lines = plt.plot(x, y1, x, y2)
plt.setp(lines, linewidth=2, color='r')
```

**`setp()`** works with the MATLAB style string/value pairs or with python kwargs. For example, the following are equivalent:

```python
plt.setp(lines, 'linewidth', 2, 'color', 'r')  # MATLAB style
plt.setp(lines, linewidth=2, color='r')        # python style
```

----

# kwdoc

```
matplotlib.artist.kwdoc
```

**`matplotlib.artist.kwdoc(artist)`**

​	Inspect an **`Artist`** class and return information about its settable properties and their current values.

​	It use the class **`ArtistInspector`**.

**Parameters:**	

- **`artist `** : **`Artist`** or an iterable of **`Artist`**s

**Returns:**

- **`string`**

  Returns a string with a list or rst table with the settable properties of the artist. The formating depends on the value of **`rcParams["docstring.hardcopy"]`**. False result in a list that is intended for easy reading as a docstring and True result in a rst table intended for rendering the documentation with sphinx.

----

# ArtistInspector

```
matplotlib.artist.ArtistInspector
```

**`class matplotlib.artist.ArtistInspector(o)`**

A helper class to inspect an Artist and return information about its settable properties and their current values.

Initialize the artist inspector with an Artist or an iterable of Artists. If an iterable is used, we assume it is a homogeneous sequence (all Artists are of the same type) and it is your responsibility to make sure this is so.

​	**`_init__(o)`**

​	Initialize the artist inspector with an Artist or an iterable of Artists. If an iterable is used, we assume it is a homogeneous sequence (all Artists are of the same type) and it is your responsibility to make sure this is so.

Methods

| [`__init__`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.__init__)(o) | Initialize the artist inspector with an [`Artist`](https://matplotlib.org/api/artist_api.html#matplotlib.artist.Artist) or an iterable of [`Artist`](https://matplotlib.org/api/artist_api.html#matplotlib.artist.Artist)s. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`aliased_name`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.aliased_name)(s) | return 'PROPNAME or alias' if *s* has an alias, else return PROPNAME. |
| [`aliased_name_rest`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.aliased_name_rest)(s, target) | return 'PROPNAME or alias' if *s* has an alias, else return PROPNAME formatted for ReST |
| [`get_aliases`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_aliases)() | Get a dict mapping property fullnames to sets of aliases for each alias in the [`ArtistInspector`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector). |
| [`get_setters`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_setters)() | Get the attribute strings with setters for object.           |
| [`get_valid_values`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_valid_values)(attr) | Get the legal arguments for the setter associated with *attr*. |
| [`is_alias`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.is_alias)(o) | Return *True* if method object *o* is an alias for another function. |
| [`pprint_getters`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_getters)() | Return the getters and actual values as list of strings.     |
| [`pprint_setters`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_setters)([prop, leadingspace]) | If *prop* is *None*, return a list of strings of all settable properties and their valid values. |
| [`pprint_setters_rest`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.pprint_setters_rest)([prop, leadingspace]) | If *prop* is *None*, return a list of strings of all settable properties and their valid values. |
| [`properties`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.properties)() | return a dictionary mapping property name -> value           |

- `aliased_name`(*s*)

  return 'PROPNAME or alias' if *s* has an alias, else return PROPNAME.e.g., for the line markerfacecolor property, which has an alias, return 'markerfacecolor or mfc' and for the transform property, which does not, return 'transform'

- `aliased_name_rest`(*s*, *target*)

  return 'PROPNAME or alias' if *s* has an alias, else return PROPNAME formatted for ReSTe.g., for the line markerfacecolor property, which has an alias, return 'markerfacecolor or mfc' and for the transform property, which does not, return 'transform'

- `get_aliases`()

  Get a dict mapping property fullnames to sets of aliases for each alias in the [`ArtistInspector`](https://matplotlib.org/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector).e.g., for lines:`{'markerfacecolor': {'mfc'},  'linewidth'      : {'lw'}, } `

- `get_setters`()

  Get the attribute strings with setters for object. e.g., for a line, return `['markerfacecolor', 'linewidth', ....]`.

- `get_valid_values`(*attr*)

  Get the legal arguments for the setter associated with *attr*.This is done by querying the docstring of the function *set_attr* for a line that begins with "ACCEPTS" or ".. ACCEPTS":e.g., for a line linestyle, return "[ `'-'` | `'--'` | `'-.'` | `':'` | `'steps'` | `'None'` ]"

- `is_alias`(*o*)

  Return *True* if method object *o* is an alias for another function.

- `pprint_getters`()

  Return the getters and actual values as list of strings.

- `pprint_setters`(*prop=None*, *leadingspace=2*)

  If *prop* is *None*, return a list of strings of all settable properties and their valid values.If *prop* is not *None*, it is a valid property name and that property will be returned as a string of property : valid values.

- `pprint_setters_rest`(*prop=None*, *leadingspace=4*)

  If *prop* is *None*, return a list of strings of all settable properties and their valid values. Format the output for ReSTIf *prop* is not *None*, it is a valid property name and that property will be returned as a string of property : valid values.

- `properties`()

  return a dictionary mapping property name -> value