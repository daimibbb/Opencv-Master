# markers

**`matplotlib.markers`**
This module contains functions to handle markers. Used by both the marker functionality of plot and scatter.

All possible markers are defined here:

| marker                         | symbol                                         | description                                                  |
| ------------------------------ | ---------------------------------------------- | ------------------------------------------------------------ |
| `"."`                          | ![m00](https://matplotlib.org/_images/m00.png) | point                                                        |
| `","`                          | ![m01](https://matplotlib.org/_images/m01.png) | pixel                                                        |
| `"o"`                          | ![m02](https://matplotlib.org/_images/m02.png) | circle                                                       |
| `"v"`                          | ![m03](https://matplotlib.org/_images/m03.png) | triangle_down                                                |
| `"^"`                          | ![m04](https://matplotlib.org/_images/m04.png) | triangle_up                                                  |
| `"<"`                          | ![m05](https://matplotlib.org/_images/m05.png) | triangle_left                                                |
| `">"`                          | ![m06](https://matplotlib.org/_images/m06.png) | triangle_right                                               |
| `"1"`                          | ![m07](https://matplotlib.org/_images/m07.png) | tri_down                                                     |
| `"2"`                          | ![m08](https://matplotlib.org/_images/m08.png) | tri_up                                                       |
| `"3"`                          | ![m09](https://matplotlib.org/_images/m09.png) | tri_left                                                     |
| `"4"`                          | ![m10](https://matplotlib.org/_images/m10.png) | tri_right                                                    |
| `"8"`                          | ![m11](https://matplotlib.org/_images/m11.png) | octagon                                                      |
| `"s"`                          | ![m12](https://matplotlib.org/_images/m12.png) | square                                                       |
| `"p"`                          | ![m13](https://matplotlib.org/_images/m13.png) | pentagon                                                     |
| `"P"`                          | ![m23](https://matplotlib.org/_images/m23.png) | plus (filled)                                                |
| `"*"`                          | ![m14](https://matplotlib.org/_images/m14.png) | star                                                         |
| `"h"`                          | ![m15](https://matplotlib.org/_images/m15.png) | hexagon1                                                     |
| `"H"`                          | ![m16](https://matplotlib.org/_images/m16.png) | hexagon2                                                     |
| `"+"`                          | ![m17](https://matplotlib.org/_images/m17.png) | plus                                                         |
| `"x"`                          | ![m18](https://matplotlib.org/_images/m18.png) | x                                                            |
| `"X"`                          | ![m24](https://matplotlib.org/_images/m24.png) | x (filled)                                                   |
| `"D"`                          | ![m19](https://matplotlib.org/_images/m19.png) | diamond                                                      |
| `"d"`                          | ![m20](https://matplotlib.org/_images/m20.png) | thin_diamond                                                 |
| `"|"`                          | ![m21](https://matplotlib.org/_images/m21.png) | vline                                                        |
| `"_"`                          | ![m22](https://matplotlib.org/_images/m22.png) | hline                                                        |
| `0` (`TICKLEFT`)               | ![m25](https://matplotlib.org/_images/m25.png) | tickleft                                                     |
| `1` (`TICKRIGHT`)              | ![m26](https://matplotlib.org/_images/m26.png) | tickright                                                    |
| `2` (`TICKUP`)                 | ![m27](https://matplotlib.org/_images/m27.png) | tickup                                                       |
| `3` (`TICKDOWN`)               | ![m28](https://matplotlib.org/_images/m28.png) | tickdown                                                     |
| `4` (`CARETLEFT`)              | ![m29](https://matplotlib.org/_images/m29.png) | caretleft                                                    |
| `5` (`CARETRIGHT`)             | ![m30](https://matplotlib.org/_images/m30.png) | caretright                                                   |
| `6` (`CARETUP`)                | ![m31](https://matplotlib.org/_images/m31.png) | caretup                                                      |
| `7` (`CARETDOWN`)              | ![m32](https://matplotlib.org/_images/m32.png) | caretdown                                                    |
| `8` (`CARETLEFTBASE`)          | ![m33](https://matplotlib.org/_images/m33.png) | caretleft (centered at base)                                 |
| `9` (`CARETRIGHTBASE`)         | ![m34](https://matplotlib.org/_images/m34.png) | caretright (centered at base)                                |
| `10` (`CARETUPBASE`)           | ![m35](https://matplotlib.org/_images/m35.png) | caretup (centered at base)                                   |
| `11` (`CARETDOWNBASE`)         | ![m36](https://matplotlib.org/_images/m36.png) | caretdown (centered at base)                                 |
| `"None"`, `" "` or `""`        |                                                | nothing                                                      |
| `'$...$'`                      | ![m37](https://matplotlib.org/_images/m37.png) | Render the string using mathtext. E.g `"$f$"`for marker showing the letter `f`. |
| `verts`                        |                                                | A list of (x, y) pairs used for Path vertices. The center of the marker is located at (0,0) and the size is normalized, such that the created path is encapsulated inside the unit cell. |
| **`path`**                     |                                                | A **`Path`** instance.                                       |
| **`(numsides, style, angle)`** |                                                | The marker can also be a tuple `(numsides,style, angle)`, which will create a custom, regular symbol.`numsides`:the number of sides`style`:the style of the regular symbol:0: a regular polygon1: a star-like symbol2: an asterisk3: a circle (`numsides` and `angle` is ignored); deprecated.`angle`:the angle of rotation of the symbol |

For backward compatibility, the form `(verts, 0)` is also accepted, but it is deprecated and equivalent to just `verts` for giving a raw set of vertices that define the shape.

`None` is the default which means 'nothing', however this table is referred to from other docs for the valid inputs from marker inputs and in those cases `None` still means 'default'.

Note that special symbols can be defined via the [STIX math font](https://matplotlib.org/tutorials/text/mathtext.html), e.g. `"$♫$"`. For an overview over the STIX font symbols refer to the [STIX font table](http://www.stixfonts.org/allGlyphs.html). Also see the [STIX Fonts Demo](https://matplotlib.org/gallery/text_labels_and_annotations/stix_fonts_demo.html).

Integer numbers from `0` to `11` create lines and triangles. Those are equally accessible via capitalized variables, like `CARETDOWNBASE`. Hence the following are equivalent:

```
plt.plot([1,2,3], marker=11)
plt.plot([1,2,3], marker=matplotlib.markers.CARETDOWNBASE)
```

Examples showing the use of markers:

- Marker Reference
- Marker filling-styles
- Marker Path







---

```python
NAME
    matplotlib.markers

DESCRIPTION
    This module contains functions to handle markers.  Used by both the
    marker functionality of `~matplotlib.axes.Axes.plot` and
    `~matplotlib.axes.Axes.scatter`.
    
    All possible markers are defined here:
    
    ============================== ===============================================
    marker                         description
    ============================== ===============================================
    `"."`                          point
    `","`                          pixel
    `"o"`                          circle
    `"v"`                          triangle_down
    `"^"`                          triangle_up
    `"<"`                          triangle_left
    `">"`                          triangle_right
    `"1"`                          tri_down
    `"2"`                          tri_up
    `"3"`                          tri_left
    `"4"`                          tri_right
    `"8"`                          octagon
    `"s"`                          square
    `"p"`                          pentagon
    `"P"`                          plus (filled)
    `"*"`                          star
    `"h"`                          hexagon1
    `"H"`                          hexagon2
    `"+"`                          plus
    `"x"`                          x
    `"X"`                          x (filled)
    `"D"`                          diamond
    `"d"`                          thin_diamond
    `"|"`                          vline
    `"_"`                          hline
    TICKLEFT                       tickleft
    TICKRIGHT                      tickright
    TICKUP                         tickup
    TICKDOWN                       tickdown
    CARETLEFT                      caretleft (centered at tip)
    CARETRIGHT                     caretright (centered at tip)
    CARETUP                        caretup (centered at tip)
    CARETDOWN                      caretdown (centered at tip)
    CARETLEFTBASE                  caretleft (centered at base)
    CARETRIGHTBASE                 caretright (centered at base)
    CARETUPBASE                    caretup (centered at base)
    `"None"`, `" "` or `""`        nothing
    ``'$...$'``                    render the string using mathtext.
    `verts`                        a list of (x, y) pairs used for Path vertices.
                                   The center of the marker is located at (0,0) and
                                   the size is normalized.
    path                           a `~matplotlib.path.Path` instance.
    (`numsides`, `style`, `angle`) The marker can also be a tuple (`numsides`,
                                   `style`, `angle`), which will create a custom,
                                   regular symbol.
    
                                   `numsides`:
                                       the number of sides
    
                                   `style`:
                                       the style of the regular symbol:
    
                                       0
                                         a regular polygon
                                       1
                                         a star-like symbol
                                       2
                                         an asterisk
                                       3
                                         a circle (`numsides` and `angle` is
                                         ignored)
    
                                   `angle`:
                                       the angle of rotation of the symbol
    ============================== ===============================================
    
    For backward compatibility, the form (`verts`, 0) is also accepted,
    but it is equivalent to just `verts` for giving a raw set of vertices
    that define the shape.
    
    `None` is the default which means 'nothing', however this table is
    referred to from other docs for the valid inputs from marker inputs and in
    those cases `None` still means 'default'.

CLASSES
    builtins.object
        MarkerStyle
    
    class MarkerStyle(builtins.object)
     |  MarkerStyle(marker=None, fillstyle=None)
     |  
     |  Methods defined here:
     |  
     |  __bool__(self)
     |  
     |  __getstate__(self)
     |  
     |  __init__(self, marker=None, fillstyle=None)
     |      MarkerStyle
     |      
     |      Attributes
     |      ----------
     |      markers : list of known marks
     |      
     |      fillstyles : list of known fillstyles
     |      
     |      filled_markers : list of known filled markers.
     |      
     |      Parameters
     |      ----------
     |      marker : string or array_like, optional, default: None
     |          See the descriptions of possible markers in the module docstring.
     |      
     |      fillstyle : string, optional, default: 'full'
     |          'full', 'left", 'right', 'bottom', 'top', 'none'
     |  
     |  __setstate__(self, statedict)
     |  
     |  get_alt_path(self)
     |  
     |  get_alt_transform(self)
     |  
     |  get_capstyle(self)
     |  
     |  get_fillstyle(self)
     |  
     |  get_joinstyle(self)
     |  
     |  get_marker(self)
     |  
     |  get_path(self)
     |  
     |  get_snap_threshold(self)
     |  
     |  get_transform(self)
     |  
     |  is_filled(self)
     |  
     |  set_fillstyle(self, fillstyle)
     |      Sets fillstyle
     |      
     |      Parameters
     |      ----------
     |      fillstyle : string amongst known fillstyles
     |  
     |  set_marker(self, marker)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H...
     |  
     |  fillstyles = ('full', 'left', 'right', 'bottom', 'top', 'none')
     |  
     |  markers = {'.': 'point', ',': 'pixel', 'o': 'circle', 'v': 'triangle_d...

DATA
    CARETDOWN = 7
    CARETDOWNBASE = 11
    CARETLEFT = 4
    CARETLEFTBASE = 8
    CARETRIGHT = 5
    CARETRIGHTBASE = 9
    CARETUP = 6
    CARETUPBASE = 10
    TICKDOWN = 3
    TICKLEFT = 0
    TICKRIGHT = 1
    TICKUP = 2
    absolute_import = _Feature((2, 5, 0, 'alpha', 1), (3, 0, 0, 'alpha', 0...
    division = _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192...
    print_function = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0)...
    rcParams = RcParams({'_internal.classic_mode': False,
         ...nor.widt...
    unicode_literals = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', ...
```

