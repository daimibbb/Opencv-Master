# matplotlib.pyplot

**`matplotlib.pyplot`** is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
```

#Functions

| [`acorr`](#pyplot.acorr)(x, *[, data])                       | Plot the autocorrelation of *x*.                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`angle_spectrum`](#pyplot.angle_spectrum)(x[, Fs, Fc, window, pad_to, ...]) | Plot the angle spectrum.                                     |
| [`annotate`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate)(s, xy, *args, **kwargs) | Annotate the point *xy* with text *s*.                       |
| [`arrow`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.arrow.html#matplotlib.pyplot.arrow)(x, y, dx, dy, **kwargs) | Add an arrow to the axes.                                    |
| [`autoscale`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.autoscale.html#matplotlib.pyplot.autoscale)([enable, axis, tight]) | Autoscale the axis view to the data (toggle).                |
| [`autumn`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.autumn.html#matplotlib.pyplot.autumn)() | Set the colormap to "autumn".                                |
| [`axes`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes)([arg]) | Add an axes to the current figure and make it the current axes. |
| [`axhline`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline)([y, xmin, xmax]) | Add a horizontal line across the axis.                       |
| [`axhspan`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axhspan.html#matplotlib.pyplot.axhspan)(ymin, ymax[, xmin, xmax]) | Add a horizontal span (rectangle) across the axis.           |
| [`axis`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis)(*v, **kwargs) | Convenience method to get or set some axis properties.       |
| [`axvline`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline)([x, ymin, ymax]) | Add a vertical line across the axes.                         |
| [`axvspan`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.axvspan.html#matplotlib.pyplot.axvspan)(xmin, xmax[, ymin, ymax]) | Add a vertical span (rectangle) across the axes.             |
| [`bar`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar)(x, height[, width, bottom, align, data]) | Make a bar plot.                                             |
| [`barbs`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barbs.html#matplotlib.pyplot.barbs)(*args[, data]) | Plot a 2-D field of barbs.                                   |
| [`barh`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh)(y, width[, height, left, align]) | Make a horizontal bar plot.                                  |
| [`bone`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bone.html#matplotlib.pyplot.bone)() | Set the colormap to "bone".                                  |
| [`box`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.box.html#matplotlib.pyplot.box)([on]) | Turn the axes box on or off on the current axes.             |
| [`boxplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot)(x[, notch, sym, vert, whis, ...]) | Make a box and whisker plot.                                 |
| [`broken_barh`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.broken_barh.html#matplotlib.pyplot.broken_barh)(xranges, yrange, *[, data]) | Plot a horizontal sequence of rectangles.                    |
| [`cla`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla)() | Clear the current axes.                                      |
| [`clabel`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel)(CS, *args, **kwargs) | Label a contour plot.                                        |
| [`clf`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf)() | Clear the current figure.                                    |
| [`clim`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.clim.html#matplotlib.pyplot.clim)([vmin, vmax]) | Set the color limits of the current image.                   |
| [`close`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close)([fig]) | Close a figure window.                                       |
| [`cohere`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cohere.html#matplotlib.pyplot.cohere)(x, y[, NFFT, Fs, Fc, detrend, ...]) | Plot the coherence between *x* and *y*.                      |
| [`colorbar`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar)([mappable, cax, ax]) | Add a colorbar to a plot.                                    |
| [`connect`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.connect.html#matplotlib.pyplot.connect)(s, func) | Connect event with string *s* to *func*.                     |
| [`contour`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour)(*args[, data]) | Plot contours.                                               |
| [`contourf`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf)(*args[, data]) | Plot contours.                                               |
| [`cool`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.cool.html#matplotlib.pyplot.cool)() | Set the colormap to "cool".                                  |
| [`copper`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.copper.html#matplotlib.pyplot.copper)() | Set the colormap to "copper".                                |
| [`csd`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.csd.html#matplotlib.pyplot.csd)(x, y[, NFFT, Fs, Fc, detrend, window, ...]) | Plot the cross-spectral density.                             |
| [`delaxes`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.delaxes.html#matplotlib.pyplot.delaxes)([ax]) | Remove the `Axes` *ax* (defaulting to the current axes) from its figure. |
| [`disconnect`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.disconnect.html#matplotlib.pyplot.disconnect)(cid) | Disconnect callback id cid                                   |
| [`draw`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw)() | Redraw the current figure.                                   |
| [`errorbar`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar)(x, y[, yerr, xerr, fmt, ecolor, ...]) | Plot y versus x as lines and/or markers with attached errorbars. |
| [`eventplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.eventplot.html#matplotlib.pyplot.eventplot)(positions[, orientation, ...]) | Plot identical parallel lines at the given positions.        |
| [`figimage`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figimage.html#matplotlib.pyplot.figimage)(*args, **kwargs) | Add a non-resampled image to the figure.                     |
| [`figlegend`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend)(*args, **kwargs) | Place a legend in the figure.                                |
| [`fignum_exists`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fignum_exists.html#matplotlib.pyplot.fignum_exists)(num) | Return whether the figure with the given id exists.          |
| [`figtext`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figtext.html#matplotlib.pyplot.figtext)(x, y, s, *args, **kwargs) | Add text to figure.                                          |
| [`figure`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure)([num, figsize, dpi, facecolor, ...]) | Create a new figure.                                         |
| [`fill`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill)(*args[, data]) | Plot filled polygons.                                        |
| [`fill_between`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between)(x, y1[, y2, where, ...]) | Fill the area between two horizontal curves.                 |
| [`fill_betweenx`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_betweenx.html#matplotlib.pyplot.fill_betweenx)(y, x1[, x2, where, step, ...]) | Fill the area between two vertical curves.                   |
| [`findobj`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.findobj.html#matplotlib.pyplot.findobj)([o, match, include_self]) | Find artist objects.                                         |
| [`flag`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.flag.html#matplotlib.pyplot.flag)() | Set the colormap to "flag".                                  |
| [`gca`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca)(**kwargs) | Get the current [`Axes`](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes) instance on the current figure matching the given keyword args, or create one. |
| [`gcf`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf)() | Get a reference to the current figure.                       |
| [`gci`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gci.html#matplotlib.pyplot.gci)() | Get the current colorable artist.                            |
| [`get_current_fig_manager`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html#matplotlib.pyplot.get_current_fig_manager)() | Return the figure manager of the active figure.              |
| [`get_figlabels`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.get_figlabels.html#matplotlib.pyplot.get_figlabels)() | Return a list of existing figure labels.                     |
| [`get_fignums`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums)() | Return a list of existing figure numbers.                    |
| [`get_plot_commands`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.get_plot_commands.html#matplotlib.pyplot.get_plot_commands)() | Get a sorted list of all of the plotting commands.           |
| [`ginput`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput)(*args, **kwargs) | Blocking call to interact with a figure.                     |
| [`gray`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gray.html#matplotlib.pyplot.gray)() | Set the colormap to "gray".                                  |
| [`grid`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid)([b, which, axis]) | Configure the grid lines.                                    |
| [`hexbin`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin)(x, y[, C, gridsize, bins, xscale, ...]) | Make a hexagonal binning plot.                               |
| [`hist`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist)(x[, bins, range, density, weights, ...]) | Plot a histogram.                                            |
| [`hist2d`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist2d.html#matplotlib.pyplot.hist2d)(x, y[, bins, range, normed, weights, ...]) | Make a 2D histogram plot.                                    |
| [`hlines`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib.pyplot.hlines)(y, xmin, xmax[, colors, linestyles, ...]) | Plot horizontal lines at each *y* from *xmin* to *xmax*.     |
| [`hot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hot.html#matplotlib.pyplot.hot)() | Set the colormap to "hot".                                   |
| [`hsv`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hsv.html#matplotlib.pyplot.hsv)() | Set the colormap to "hsv".                                   |
| [`imread`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread)(fname[, format]) | Read an image from a file into an array.                     |
| [`imsave`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave)(fname, arr, **kwargs) | Save an array as in image file.                              |
| [`imshow`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow)(X[, cmap, norm, aspect, ...]) | Display an image, i.e.                                       |
| [`inferno`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.inferno.html#matplotlib.pyplot.inferno)() | Set the colormap to "inferno".                               |
| [`install_repl_displayhook`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html#matplotlib.pyplot.install_repl_displayhook)() | Install a repl display hook so that any stale figure are automatically redrawn when control is returned to the repl. |
| [`ioff`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ioff.html#matplotlib.pyplot.ioff)() | Turn the interactive mode off.                               |
| [`ion`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion)() | Turn the interactive mode on.                                |
| [`isinteractive`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive)() | Return the status of interactive mode.                       |
| [`jet`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.jet.html#matplotlib.pyplot.jet)() | Set the colormap to "jet".                                   |
| [`legend`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend)(*args, **kwargs) | Place a legend on the axes.                                  |
| [`locator_params`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.locator_params.html#matplotlib.pyplot.locator_params)([axis, tight]) | Control behavior of tick locators.                           |
| [`loglog`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog)(*args, **kwargs) | Make a plot with log scaling on both the x and y axis.       |
| [`magma`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.magma.html#matplotlib.pyplot.magma)() | Set the colormap to "magma".                                 |
| [`magnitude_spectrum`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html#matplotlib.pyplot.magnitude_spectrum)(x[, Fs, Fc, window, ...]) | Plot the magnitude spectrum.                                 |
| [`margins`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib.pyplot.margins)(*margins[, x, y, tight]) | Set or retrieve autoscaling margins.                         |
| [`matshow`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow)(A[, fignum]) | Display an array as a matrix in a new figure window.         |
| [`minorticks_off`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.minorticks_off.html#matplotlib.pyplot.minorticks_off)() | Remove minor ticks from the axes.                            |
| [`minorticks_on`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.minorticks_on.html#matplotlib.pyplot.minorticks_on)() | Display minor ticks on the axes.                             |
| [`nipy_spectral`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.nipy_spectral.html#matplotlib.pyplot.nipy_spectral)() | Set the colormap to "nipy_spectral".                         |
| [`pause`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause)(interval) | Pause for *interval* seconds.                                |
| [`pcolor`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor)(*args[, alpha, norm, cmap, vmin, ...]) | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`pcolormesh`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh)(*args[, alpha, norm, cmap, vmin, ...]) | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`phase_spectrum`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.phase_spectrum.html#matplotlib.pyplot.phase_spectrum)(x[, Fs, Fc, window, pad_to, ...]) | Plot the phase spectrum.                                     |
| [`pie`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie)(x[, explode, labels, colors, autopct, ...]) | Plot a pie chart.                                            |
| [`pink`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pink.html#matplotlib.pyplot.pink)() | Set the colormap to "pink".                                  |
| [`plasma`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plasma.html#matplotlib.pyplot.plasma)() | Set the colormap to "plasma".                                |
| [`plot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)(*args[, scalex, scaley, data]) | Plot y versus x as lines and/or markers.                     |
| [`plot_date`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot_date.html#matplotlib.pyplot.plot_date)(x, y[, fmt, tz, xdate, ydate, data]) | Plot data that contains dates.                               |
| [`plotfile`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plotfile.html#matplotlib.pyplot.plotfile)(fname[, cols, plotfuncs, comments, ...]) | Plot the data in a file.                                     |
| [`polar`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib.pyplot.polar)(*args, **kwargs) | Make a polar plot.                                           |
| [`prism`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.prism.html#matplotlib.pyplot.prism)() | Set the colormap to "prism".                                 |
| [`psd`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd)(x[, NFFT, Fs, Fc, detrend, window, ...]) | Plot the power spectral density.                             |
| [`quiver`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver)(*args[, data]) | Plot a 2-D field of arrows.                                  |
| [`quiverkey`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiverkey.html#matplotlib.pyplot.quiverkey)(Q, X, Y, U, label, **kw) | Add a key to a quiver plot.                                  |
| [`rc`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc)(group, **kwargs) | Set the current rc params.                                   |
| [`rc_context`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib.pyplot.rc_context)([rc, fname]) | Return a context manager for managing rc settings.           |
| [`rcdefaults`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rcdefaults.html#matplotlib.pyplot.rcdefaults)() | Restore the rc params from Matplotlib's internal default style. |
| [`rgrids`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids)(*args, **kwargs) | Get or set the radial gridlines on the current polar plot.   |
| [`savefig`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig)(*args, **kwargs) | Save the current figure.                                     |
| [`sca`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.sca.html#matplotlib.pyplot.sca)(ax) | Set the current Axes instance to *ax*.                       |
| [`scatter`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)(x, y[, s, c, marker, cmap, norm, ...]) | A scatter plot of *y* vs *x* with varying marker size and/or color. |
| [`sci`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.sci.html#matplotlib.pyplot.sci)(im) | Set the current image.                                       |
| [`semilogx`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx)(*args, **kwargs) | Make a plot with log scaling on the x axis.                  |
| [`semilogy`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy)(*args, **kwargs) | Make a plot with log scaling on the y axis.                  |
| [`set_cmap`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.set_cmap.html#matplotlib.pyplot.set_cmap)(cmap) | Set the default colormap.                                    |
| [`setp`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp)(obj, *args, **kwargs) | Set a property on an artist object.                          |
| [`show`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show)(*args, **kw) | Display a figure.                                            |
| [`specgram`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram)(x[, NFFT, Fs, Fc, detrend, window, ...]) | Plot a spectrogram.                                          |
| [`spring`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.spring.html#matplotlib.pyplot.spring)() | Set the colormap to "spring".                                |
| [`spy`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy)(Z[, precision, marker, markersize, ...]) | Plot the sparsity pattern of a 2D array.                     |
| [`stackplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib.pyplot.stackplot)(x, *args[, data]) | Draw a stacked area plot.                                    |
| [`stem`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem)(*args[, linefmt, markerfmt, basefmt, ...]) | Create a stem plot.                                          |
| [`step`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step)(x, y, *args[, where, data]) | Make a step plot.                                            |
| [`streamplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot)(x, y, u, v[, density, linewidth, ...]) | Draw streamlines of a vector flow.                           |
| [`subplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot)(*args, **kwargs) | Add a subplot to the current figure.                         |
| [`subplot2grid`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid)(shape, loc[, rowspan, colspan, fig]) | Create an axis at specific location inside a regular grid.   |
| [`subplot_tool`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplot_tool.html#matplotlib.pyplot.subplot_tool)([targetfig]) | Launch a subplot tool window for a figure.                   |
| [`subplots`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots)([nrows, ncols, sharex, sharey, ...]) | Create a figure and a set of subplots.                       |
| [`subplots_adjust`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust)([left, bottom, right, top, ...]) | Tune the subplot layout.                                     |
| [`summer`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.summer.html#matplotlib.pyplot.summer)() | Set the colormap to "summer".                                |
| [`suptitle`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle)(t, **kwargs) | Add a centered title to the figure.                          |
| [`switch_backend`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib.pyplot.switch_backend)(newbackend) | Close all open figures and set the Matplotlib backend.       |
| [`table`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table)(**kwargs) | Add a table to the current axes.                             |
| [`text`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text)(x, y, s[, fontdict, withdash]) | Add text to the axes.                                        |
| [`thetagrids`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids)(*args, **kwargs) | Get or set the theta gridlines on the current polar plot.    |
| [`tick_params`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params)([axis]) | Change the appearance of ticks, tick labels, and gridlines.  |
| [`ticklabel_format`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ticklabel_format.html#matplotlib.pyplot.ticklabel_format)(*[, axis, style, ...]) | Change the [`ScalarFormatter`](https://matplotlib.org/api/ticker_api.html#matplotlib.ticker.ScalarFormatter) used by default for linear axes. |
| [`tight_layout`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout)([pad, h_pad, w_pad, rect]) | Automatically adjust subplot parameters to give specified padding. |
| [`title`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title)(label[, fontdict, loc, pad]) | Set a title for the axes.                                    |
| [`tricontour`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour)(*args, **kwargs) | Draw contours on an unstructured triangular grid.            |
| [`tricontourf`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf)(*args, **kwargs) | Draw contours on an unstructured triangular grid.            |
| [`tripcolor`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.tripcolor.html#matplotlib.pyplot.tripcolor)(*args, **kwargs) | Create a pseudocolor plot of an unstructured triangular grid. |
| [`triplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot)(*args, **kwargs) | Draw a unstructured triangular grid as lines and/or markers. |
| [`twinx`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.twinx.html#matplotlib.pyplot.twinx)([ax]) | Make a second axes that shares the *x*-axis.                 |
| [`twiny`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.twiny.html#matplotlib.pyplot.twiny)([ax]) | Make a second axes that shares the *y*-axis.                 |
| [`uninstall_repl_displayhook`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.uninstall_repl_displayhook.html#matplotlib.pyplot.uninstall_repl_displayhook)() | Uninstall the matplotlib display hook.                       |
| [`violinplot`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot)(dataset[, positions, vert, ...]) | Make a violin plot.                                          |
| [`viridis`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.viridis.html#matplotlib.pyplot.viridis)() | Set the colormap to "viridis".                               |
| [`vlines`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines)(x, ymin, ymax[, colors, linestyles, ...]) | Plot vertical lines.                                         |
| [`waitforbuttonpress`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress)(*args, **kwargs) | Blocking call to interact with the figure.                   |
| [`winter`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.winter.html#matplotlib.pyplot.winter)() | Set the colormap to "winter".                                |
| [`xcorr`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xcorr.html#matplotlib.pyplot.xcorr)(x, y[, normed, detrend, usevlines, ...]) | Plot the cross correlation between *x* and *y*.              |
| [`xkcd`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd)([scale, length, randomness]) | Turn on [xkcd](https://xkcd.com/) sketch-style drawing mode.This will only have effect on things drawn after this function is called.. |
| [`xlabel`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel)(xlabel[, fontdict, labelpad]) | Set the label for the x-axis.                                |
| [`xlim`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim)(*args, **kwargs) | Get or set the x limits of the current axes.                 |
| [`xscale`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xscale.html#matplotlib.pyplot.xscale)(value, **kwargs) | Set the x-axis scale.                                        |
| [`xticks`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks)([ticks, labels]) | Get or set the current tick locations and labels of the x-axis. |
| [`ylabel`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel)(ylabel[, fontdict, labelpad]) | Set the label for the y-axis.                                |
| [`ylim`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim)(*args, **kwargs) | Get or set the y-limits of the current axes.                 |
| [`yscale`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale)(value, **kwargs) | Set the y-axis scale.                                        |
| [`yticks`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks)([ticks, labels]) | Get or set the current tick locations and labels of the y-axis. |

---

# 函数详解

# pyplot.acorr

```python
matplotlib.pyplot.acorr(x, *, data=None, **kwargs)
```

Plot the autocorrelation of *x*.

**Parameters:**

- **`x`** : **sequence of scalar**
- **`detrend`** : **callable**, optional, default: **`mlab.detrend_none`**
  ​		    *x* is detrended by the *detrend* callable. Default is no normalization.

- **`normed`** : **bool**, optional, default: **`True`**
   		   ​    If True, input vectors are normalised to unit length.

- **`usevlines`** : **bool**, optional, default: **`True`**
     		 ​	   If True, **`Axes.vlines`** is used to plot the vertical lines from the origin to the acorr. Otherwise, **`Axes.plot`** is used.

- **`maxlags`** : **int**, optional, default: **`10`**
  ​			Number of lags to show. If None, will return all 2 * len(x) - 1 lags

**Returns:**

- **`lags`** : array (length 2*maxlags+1)
  ​	    lag vector.

- **`c`** : array (length 2*maxlags+1)
  ​     auto correlation vector.

- **`line`** : LineCollection or Line2D
  ​         Artist added to the axes of the correlation.

​		LineCollection if usevlines is True Line2D if usevlines is False

- **`b`** : Line2D or None
  ​	Horizontal line at 0 if usevlines is True None usevlines is False

**Notes**

The cross correlation is performed with **`numpy.correlate()`** with mode = 2.

**Other Parameters:**

- **`linestyle`** : **~matplotlib.lines.Line2D prop**, optional, default: **`None`**
  ​    Only used if **`usevlines`** is ``False``.

- **`marker`** : **string**, optional, default: 'o'

---

如果**`normed = True`**,通过零滞后自相关规范数据，x 通过非趋势可调用（默认没有归一化）的方式除趋势

数据绘制形如 **`plot(lags, c, \**kwargs)`**

返回值是元组**`(lags, c, line)`**，其中：

- lags 是一个长度为**`2×maxlags + 1`** 的滞后（lags）向量
- C 是**`2×maxlags + 1`** 的自相关向量
- line 是一个**`line2d`** 实例，通过plot()返回

默认**`linestyle`** 是**None**，默认的**`marker`** 是**'o'**，交叉相关性是通过**`numpy.correlate()`**函数、**`mode = 2`** 实现的。

若**`usevlines`** 是**True**, **`vlines()`**将被调用（而不调用plot()函数），用来绘制从起点到acorr 的垂线。否则，**`plot()`**由Line2D properties 属性参数（kwargs）决定。

**`maxlags`** 是正整数，决定**`lags`** 的显示数目。默认值**None** 将返回**`（2×len（x）- 1）`**个lags，返回值是一个元组**`(lags, c, linecol, b)`**，其中：

- **`linecol`** 是**linecollection**
- **`b`** 是x-axis

---

# pyplot.angle_spectrum

```python
matplotlib.pyplot.angle_spectrum(x, Fs=None, Fc=None, window=None, pad_to=None, sides=None, *, data=None, **kwargs)
```

Plot the angle spectrum.

Compute the angle spectrum (wrapped phase spectrum) of *x*. Data is padded to a length of *pad_to* and the windowing function *window* is applied to the signal.

**Parameters：**

- **`x`** : 1-D array or sequence
  Array or sequence containing the data.

- **`Fs`** : scalar
  The sampling frequency (samples per time unit). It is used to calculate the Fourier frequencies, freqs, in cycles per time unit. The default value is 2.

- **`window`** : callable or ndarray
  A function or a vector of length NFFT. To create window vectors see **`window_hanning()`**, **`window_none()`**, **`numpy.blackman()`**, **`numpy.hamming()`**, **`numpy.bartlett()`**, **`scipy.signal()`**, **`scipy.signal.get_window()`**, etc. The default is **`window_hanning()`**. If a function is passed as the argument, it must take a data segment as an argument and return the windowed version of the segment.

- **`sides`** : {'default', '**onesided**', '**twosided**'}
  Specifies which sides of the spectrum to return. Default gives the default behavior, which returns one-sided for real data and both for complex data. **`'onesided'`** forces the return of a one-sided spectrum, while **`'twosided'`** forces two-sided.

- **`pad_to`** : **int**
  The number of points to which the data segment is padded when performing the FFT. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the n parameter in the call to fft(). The default is None, which sets pad_to equal to the length of the input signal (i.e. no padding).

- **Fc** : int

  The center frequency of *x* (defaults to 0), which offsets the x extents of the plot to reflect the frequency range used when a signal is acquired and then filtered and downsampled to baseband.

**Returns:**

- **`spectrum`** : 1-D array
  The values for the angle spectrum in radians (real valued).
- **`freqs`** : 1-D array
  The frequencies corresponding to the elements in spectrum.
- line : a **`Line2D`** instance
  The line created by this function.

---

## pyplot.annotate

```python
matplotlib.pyplot.annotate(s, xy, *args, **kwargs)
```

Annotate the point *xy* with text *s*.

In the simplest form, the text is placed at *xy*.

Optionally, the text can be displayed in another position *xytext*. An arrow pointing from the text to the annotated point *xy*can then be added by defining *arrowprops*.

**`Parameters:`**

**`s`** : str
​	  The text of the annotation.

**`xy`** : (float, float)
​		The point (x,y) to annotate.

**`xytext`** : (float, float), optional
​		The position (x,y) to place the text at. If None, defaults to xy.

**`xycoords`** : str, Artist, Transform, callable or tuple, optional
​	The coordinate system that xy is given in. The following types of values are supported:

​	One of the following strings:

| Value             | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| 'figure points'   | Points from the lower left of the figure                     |
| 'figure pixels'   | Pixels from the lower left of the figure                     |
| 'figure fraction' | Fraction of figure from lower left                           |
| axes points'      | Points from lower left corner of axes                        |
| axes pixels'      | Pixels from lower left corner of axes                        |
| axes fraction'    | Fraction of axes from lower left                             |
| 'data'            | Use the coordinate system of the object being annotated (default) |
| 'polar'           | theta,r) if not native 'data' coordinates                    |

**`arrowprops`** : dict, optional
​	The properties used to draw a FancyArrowPatch arrow between the positions xy and xytext.

​	If arrowprops does not contain the key 'arrowstyle' the allowed keys are:

| Key        | Description                                       |
| ---------- | ------------------------------------------------- |
| width      | The width of the arrow in points                  |
| headwidth  | The width of the base of the arrow head in points |
| headlength | The length of the arrow head in points            |
| shrink     | Fraction of total length to shrink from both ends |

If *arrowprops* contains the key 'arrowstyle' the above keys are forbidden. The allowed values of `'arrowstyle'` are:

| Name       | Attrs                                         |
| ---------- | --------------------------------------------- |
| `'-'`      | None                                          |
| `'->'`     | head_length=0.4,head_width=0.2                |
| `'-['`     | widthB=1.0,lengthB=0.2,angleB=None            |
| `'|-|'`    | widthA=1.0,widthB=1.0                         |
| `'-|>'`    | head_length=0.4,head_width=0.2                |
| `'<-'`     | head_length=0.4,head_width=0.2                |
| `'<->'`    | head_length=0.4,head_width=0.2                |
| `'<|-'`    | head_length=0.4,head_width=0.2                |
| `'<|-|>'`  | head_length=0.4,head_width=0.2                |
| `'fancy'`  | head_length=0.4,head_width=0.4,tail_width=0.4 |
| `'simple'` | head_length=0.5,head_width=0.5,tail_width=0.2 |
| `'wedge'`  | tail_width=0.3,shrink_factor=0.5              |

Valid keys for [`FancyArrowPatch`](https://matplotlib.org/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch) are:

| Key             | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| arrowstyle      | the arrow style                                              |
| connectionstyle | the connection style                                         |
| relpos          | default is (0.5, 0.5)                                        |
| patchA          | default is bounding box of the text                          |
| patchB          | default is None                                              |
| shrinkA         | default is 2 points                                          |
| shrinkB         | default is 2 points                                          |
| mutation_scale  | default is text size (in points)                             |
| mutation_aspect | default is 1.                                                |
| ?               | any key for [`matplotlib.patches.PathPatch`](https://matplotlib.org/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch) |

Defaults to None, i.e. no arrow is drawn.

**`annotation_clip`** : bool or None, optional

Whether to draw the annotation when the annotation point *xy* is outside the axes area.

- If *True*, the annotation will only be drawn when *xy* is within the axes.
- If *False*, the annotation will always be drawn.
- If *None*, the annotation will only be drawn when *xy* is within the axes and *xycoords* is 'data'.

Defaults to *None*.

---

## pyplot.arrow

```py
matplotlib.pyplot.arrow(x, y, dx, dy, **kwargs)[source]
```

Add an arrow to the axes.

This draws an arrow from `(x, y)` to `(x+dx, y+dy)`.

**Parameters:**

**x, y** : float

​	The x/y-coordinate of the arrow base.

**dx, dy** : float

​	The length of the arrow along x/y-direction.

**arrow** : FancyArrow
The created FancyArrow object.

**Constructor arguments**

- *width*: float (default: 0.001)

  width of full arrow tail

- *length_includes_head*: bool (default: False)

  True if head is to be counted in calculating the length.

- *head_width*: float or None (default: 3*width)

  total width of the full arrow head

- *head_length*: float or None (default: 1.5 * head_width)

  length of arrow head

- *shape*: ['full', 'left', 'right'] (default: 'full')

  draw the left-half, right-half, or full arrow

- *overhang*: float (default: 0)

  fraction that the arrow is swept back (0 overhang means triangular shape). Can be negative or greater than one.

- *head_starts_at_zero*: bool (default: False)

  if True, the head starts being drawn at coordinate 0 instead of ending at coordinate 0.

**other valid kwargs (inherited from :class:`Patch`) are:**

| Property                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`agg_filter`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter) | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array |
| [`alpha`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_alpha) | float or None                                                |
| [`animated`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated) | bool                                                         |
| [`antialiased`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_antialiased) | unknown                                                      |
| [`capstyle`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_capstyle) | {'butt', 'round', 'projecting'}                              |
| [`clip_box`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box) | [`Bbox`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Bbox) |
| [`clip_on`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on) | bool                                                         |
| [`clip_path`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path) | [([`Path`](https://matplotlib.org/api/path_api.html#matplotlib.path.Path), [`Transform`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Transform)) | [`Patch`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch) \| None] |
| [`color`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color) | color                                                        |
| [`contains`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_contains.html#matplotlib.artist.Artist.set_contains) | callable                                                     |
| [`edgecolor`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_edgecolor) | color or None or 'auto'                                      |
| [`facecolor`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor) | color or None                                                |
| [`figure`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure) | [`Figure`](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure) |
| [`fill`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_fill) | bool                                                         |
| [`gid`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid) | str                                                          |
| [`hatch`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch) | {'/', '\', '\|', '-', '+', 'x', 'o', 'O', '.', '*'}          |
| `in_layout`                                                  | bool                                                         |
| [`joinstyle`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_joinstyle) | {'miter', 'round', 'bevel'}                                  |
| [`label`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label) | object                                                       |
| [`linestyle`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linestyle) | {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}        |
| [`linewidth`](https://matplotlib.org/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth) | float or None for default                                    |
| [`path_effects`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects) | [`AbstractPathEffect`](https://matplotlib.org/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect) |
| [`picker`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker) | None or bool or float or callable                            |
| [`rasterized`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized) | bool or None                                                 |
| [`sketch_params`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params) | (scale: float, length: float, randomness: float)             |
| [`snap`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap) | bool or None                                                 |
| [`transform`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform) | [`Transform`](https://matplotlib.org/api/transformations.html#matplotlib.transforms.Transform) |
| [`url`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url) | str                                                          |
| [`visible`](https://matplotlib.org/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible) | bool                                                         |

