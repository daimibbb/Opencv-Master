# Choosing Colormaps in Matplotlib

### 获取方法

```python
a = plt.contourf(X, Y, Z, 3, cmap='Greys')
a = plt.contourf(X, Y, Z, 3, cmap=plt.cm.Greys)
a = plt.contourf(X, Y, Z, 3, cmap=plt.cm.get_cmap('Greys'))
```

### Sequential

```python
cmaps['Perceptually Uniform Sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']

cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
```

![../../_images/sphx_glr_colormaps_001.png](https://matplotlib.org/_images/sphx_glr_colormaps_001.png)

![../../_images/sphx_glr_colormaps_002.png](https://matplotlib.org/_images/sphx_glr_colormaps_002.png)

### Sequential2

```python
cmaps['Sequential (2)'] = [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']
```

![../../_images/sphx_glr_colormaps_003.png](https://matplotlib.org/_images/sphx_glr_colormaps_003.png)

### Diverging

```python
cmaps['Diverging'] = [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
```

![../../_images/sphx_glr_colormaps_004.png](https://matplotlib.org/_images/sphx_glr_colormaps_004.png)

### Cyclic

```python
cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']
```

![../../_images/sphx_glr_colormaps_005.png](https://matplotlib.org/_images/sphx_glr_colormaps_005.png)

### Qualitative

```python
cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']
```

![../../_images/sphx_glr_colormaps_006.png](https://matplotlib.org/_images/sphx_glr_colormaps_006.png)

### Miscellaneous

```python
cmaps['Miscellaneous'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
```

![../../_images/sphx_glr_colormaps_007.png](https://matplotlib.org/_images/sphx_glr_colormaps_007.png)





