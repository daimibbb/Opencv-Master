# matplotlib.legend_handler

This module defines default legend handlers.

**`Legend`** handlers are expected to be a callable object with a following signature.

```
legend_handler(legend, orig_handle, fontsize, handlebox)
```

Where **`legend`** is the legend itself, **`orig_handle`** is the original plot, **`fontsize`** is the fontsize in pixels, and **`handlebox`** is a **`OffsetBox`** instance. Within the call, you should create relevant artists (using relevant properties from the **`legend`** and/or **`orig_handle`**) and add them into the **`handlebox`**. The artists needs to be scaled according to the fontsize (note that the size is in pixel, i.e., this is dpi-scaled value).

This module includes definition of **several legend handler classes** derived from the base class (**`HandlerBase`**) with the following method:

```python
def legend_artist(self, legend, orig_handle, fontsize, handlebox)
```

---

## HandlerBase

```python
class matplotlib.legend_handler.HandlerBase(xpad=0.0, ypad=0.0, update_func=None)
```

A Base class for default legend handlers.

The derived classes are meant to override *create_artists* method, which has a following signature.:

```python
def create_artists(self, legend, orig_handle,
                   xdescent, ydescent, width, height, fontsize,
                   trans):
```

The overridden method needs to create artists of the given transform that fits in the given dimension (xdescent, ydescent, width, height) that are scaled by fontsize if necessary.

### method

#### adjust_drawing_area

```python
adjust_drawing_area(legend, orig_handle, xdescent, ydescent, width, height, fontsize)
```

#### create_artists

```python
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

#### legend_artist

```python
legend_artist(legend, orig_handle, fontsize, handlebox)
```

Return the artist that this **`HandlerBase`** generates for the given original artist/handle.

**Parameters:**

- **`legend`** : matplotlib.legend.Legend instance

The legend for which these legend artists are being created.

- **`orig_handle`** : matplotlib.artist.Artist or similar

The object for which these legend artists are being created.

- **`fontsize`** : float or int

The fontsize in pixels. The artists being created should be scaled according to the given fontsize.

- **`handlebox`** : **`matplotlib.offsetbox.OffsetBox`** instance

The box which has been created to hold this legend entry's artists. Artists created in the legend_artist method must be added to this handlebox inside this method.

#### update_prop

```
update_prop(legend_handle, orig_handle, legend)
```

---

## HandlerCircleCollection

```python
class matplotlib.legend_handler.HandlerCircleCollection(yoffsets=None, sizes=None, **kw)
```

Handler for **`CircleCollections`**.

### method

#### create_collection

```
create_collection(orig_handle, sizes, offsets, transOffset)
```

----

## HandlerErrorbar

```python
class matplotlib.legend_handler.HandlerErrorbar(xerr_size=0.5, yerr_size=None, marker_pad=0.3, numpoints=None, **kw)
```

Handler for Errorbars.

### method

#### create_artists

```python
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

#### get_err_size

```
get_err_size(legend, xdescent, ydescent, width, height, fontsize)
```

---

## HandlerLine2D

```python
class matplotlib.legend_handler.HandlerLine2D(marker_pad=0.3, numpoints=None, **kw)
```

Handler for **`Line2D`** instances.

**Parameters:**

- **`marker_pad`** : float

Padding between points in legend entry.

- **`numpoints`** : int

Number of points to show in legend entry.

Notes

Any other keyword arguments are given to **`HandlerNpoints`**.

### method

#### create_artists

```python
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

----

#### HandlerLineCollection

```python
class matplotlib.legend_handler.HandlerLineCollection(marker_pad=0.3, numpoints=None, **kw)
```

Handler for **`LineCollection`** instances.

**Parameters:**

- **`marker_pad`** : float

Padding between points in legend entry.

- **`numpoints`** : int

Number of points to show in legend entry.

Notes

Any other keyword arguments are given to **`HandlerNpoints`**.

### method

#### create_artists

```python
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

#### get_numpoints

```
get_numpoints(legend)
```

------

## HandlerNpoints

```python
class matplotlib.legend_handler.HandlerNpoints(marker_pad=0.3, numpoints=None, **kw)[source]
```

A legend handler that shows *numpoints* points in the legend entry.

**Parameters:**

- **`marker_pad`** : float

Padding between points in legend entry.

- **`numpoints`** : int

Number of points to show in legend entry.

Notes

Any other keyword arguments are given to **`HandlerBase`**.

### method

#### get_numpoints

```
get_numpoints(legend)
```

#### get_xdata

```
get_xdata(legend, xdescent, ydescent, width, height, fontsize)
```

---

## HandlerNpointsYoffsets

```
class matplotlib.legend_handler.HandlerNpointsYoffsets(numpoints=None, yoffsets=None, **kw)
```

A legend handler that shows *numpoints* in the legend, and allows them to be individually offest in the y-direction.

**Parameters:**

- **`numpoints`** : int

Number of points to show in legend entry.

- **`yoffsets`** : array of floats

Length numpoints list of y offsets for each point in legend entry.

**Notes**

Any other keyword arguments are given to **`HandlerNpoints`**.

---

## HandlerPatch

```
class matplotlib.legend_handler.HandlerPatch(patch_func=None, **kw)
```

Handler for **`Patch`** instances.

**Parameters:**

- **`patch_func`** : callable, optional

The function that creates the legend key artist. patch_func should have the signature:

```python
def patch_func(legend=legend, orig_handle=orig_handle,
               xdescent=xdescent, ydescent=ydescent,
               width=width, height=height, fontsize=fontsize)
```

Subsequently the created artist will have its `update_prop` method called and the appropriate transform will be applied.

Notes

Any other keyword arguments are given to **`HandlerBase`**.

### method

#### create_artists

```
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

---

## HandlerPathCollection

```python
class matplotlib.legend_handler.HandlerPathCollection(yoffsets=None, sizes=None, **kw)
```

Handler for **`PathCollections`**, which are used by **`scatter`**.

### method

#### create_collection

```
create_collection(orig_handle, sizes, offsets, transOffset)
```

---

## HandlerPolyCollection

```python
class matplotlib.legend_handler.HandlerPolyCollection(xpad=0.0, ypad=0.0, update_func=None)
```

Handler for **`PolyCollection`** used in **`fill_between`** and **`stackplot`**.

### method

#### create_artists

```
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

---

## HandlerRegularPolyCollection

```python
class matplotlib.legend_handler.HandlerRegularPolyCollection(yoffsets=None, sizes=None, **kw)
```

Handler for **`RegularPolyCollections`**.

### method

#### create_artists

```
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

#### create_collection

```
create_collection(orig_handle, sizes, offsets, transOffset)
```

#### get_numpoints

```
get_numpoints(legend)
```

#### get_sizes

```
get_sizes(legend, orig_handle, xdescent, ydescent, width, height, fontsize)
```

#### update_prop

```
update_prop(legend_handle, orig_handle, legend)
```

----

## HandlerStem

```python
class matplotlib.legend_handler.HandlerStem(marker_pad=0.3, numpoints=None, bottom=None, yoffsets=None, **kw)
```

Handler for plots produced by **`stem`**.

**Parameters:**

- **`marker_pad`** : float

Padding between points in legend entry. Default is 0.3.

- **`numpoints`** : int, optional

Number of points to show in legend entry.

- **`bottom`** : float, optional

- **`yoffsets`** : array of floats, optional

Length numpoints list of y offsets for each point in legend entry.

**Notes**

Any other keyword arguments are given to **`HandlerNpointsYoffsets`**.

### method

#### create_artists

```
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

#### get_ydata

```
get_ydata(legend, xdescent, ydescent, width, height, fontsize)
```

---

## HandlerTuple

```python
class matplotlib.legend_handler.HandlerTuple(ndivide=1, pad=None, **kwargs)
```

Handler for Tuple.

Additional kwargs are passed through to **`HandlerBase`**.

**Parameters:**

- **`ndivide`** : int, optional

The number of sections to divide the legend area into. If None, use the length of the input tuple. Default is 1.

- **`pad`** : float, optional

If None, fall back to legend.borderpad as the default. In units of fraction of font size. Default is None.

### method

#### create_artists

```
create_artists(legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans)
```

