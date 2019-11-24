# matplotlib.pyplot.savefig

```python
savefig(fname, *, frameon=None, transparent=None, **kwargs)
```

Save the current figure.

Call signature:

```python
savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
```

The output formats available depend on the backend being used.

**Parameters:**

- **`fname`** : **str** or file-like object

**A string containing a path to a filename**, or a Python file-like object, or possibly some backend-dependent object such as **`PdfPages`**.

- [x] If format is **None** and **`fname`** is a **string**, the **output format is deduced from the extension of the filename**. 

- [x] If the **`fname`** has no extension, **`rcParams["savefig.format"]`** is used. (**png** by default)

- [x] If **`fname`** is not a string, remember to specify format to ensure that the correct **backend** is used.

**Other Parameters:**

- **`dpi`** : [ **None** | **scalar > 0** | **'figure'** ]

**The resolution in dots per inch.** If **None**, defaults to **`rcParams["savefig.dpi"]`**. If **'figure'**, uses the figure's dpi value. (**72.0** by default)

- **`quality`** : [ **None** | **1 <= scalar <= 100** ]

**The image quality**, on a scale from 1 (worst) to 95(best). **Applicable only if format is jpg or jpeg**, ignored otherwise. If **None**, defaults to **`rcParams["savefig.jpeg_quality"]`** (**95** by default). **Values above 95 should be avoided**; **100 completely disables the JPEG quantization stage.**

- **`facecolor`** : **color spec** or **None**,

**The facecolor of the figure;** if **None**, defaults to **`rcParams["savefig.facecolor"]`**.

- **`edgecolor`** : **color spec** or **None**,

**The edgecolor of the figure**; if **None**, defaults to **`rcParams["savefig.edgecolor"]`**

- **`orientation`** : {'**landscape**', '**portrait**'}

**Currently only supported by the postscript backend.**

- **`papertype`** : **str**

**One of 'letter', 'legal', 'executive', 'ledger', 'a0' through 'a10', 'b0' through 'b10'.** 

Only supported for postscript output.

- **`format`** : **str**

**One of the file extensions supported by the active backend.** 

Most backends support **`png`**, **`pdf`**, **`ps`**, **`eps`** and **`svg`**.

- **`transparent`** : **bool**

**If True, the axes patches will all be transparent;** the figure patch will also be transparent unless facecolor and/or edgecolor are specified via kwargs. 

This is useful, for example, for displaying a plot on top of a colored background on a web page. The transparency of these patches will be restored to their original values upon exit of this function.

- **`frameon`** : **bool**

- [x] If **True**, the figure patch will be colored,

- [x]  if False, the figure background will be transparent. 

- [x] If not provided, the **`rcParam ["savefig.frameon"]`**' will be used.

- **`bbox_inches`** : **str** or **`Bbox`**

**`Bbox`** in inches. Only the given portion of the figure is saved. If '**tight**', try to figure out the tight bbox of the figure. If **None**, use **`rcParam["savefig.bbox"]`**.

- **`pad_inches`**: **scalar**

Amount of padding around the figure when **`bbox_inches`** is '**tight**'. If None, use **`rcParam["savefig.pad_inches"]`**

- **`bbox_extra_artists`** : list of **`Artist`**, optional

A list of extra artists that will be considered when the tight **`bbox`** is calculated.

- **`metadata`** : **dict**

**Key/value pairs to store in the image metadata.** 

The supported keys and defaults depend on the image format and backend:

- [x] 'png' with **Agg** backend: See the parameter metadata of **`print_png`**.
- [x] 'pdf' with **pdf** backend: See the parameter metadata of **`PdfPages`**.
- [x] 'eps' and 'ps' with PS backend: Only 'Creator' is supported.

---



# rcParams.savefig

```python
'savefig.bbox': None,
'savefig.directory': '~',
'savefig.dpi': 'figure',
'savefig.edgecolor': 'w',
'savefig.facecolor': 'w',
'savefig.format': 'png',
'savefig.frameon': True,
'savefig.jpeg_quality': 95,
'savefig.orientation': 'portrait',
'savefig.pad_inches': 0.1,
'savefig.transparent': False,
```

