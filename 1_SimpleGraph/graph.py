from bokeh.plotting import figure, show, output_file, output_notebook
import numpy as np


def get_data(phase, amplitude):
  """Return data to graph."""
  x = np.linspace(0, 2*np.pi)
  y = amplitude*np.sin(x + phase)
  return x, y


def make_plot(x, y):
  """Make bokeh line plot of x vs y"""

  # create a new plot with a title and axis labels
  p = figure(title="Simple line graph", x_axis_label='x', y_axis_label='y')

  # add a line with legend and line thickness
  p.line(x, y, legend="Temp.", line_width=2)
  return p



PHASE     = np.pi/4.0
AMPLITUDE = 2.0
(x, y) = get_data(PHASE, AMPLITUDE)


output_file("graph.html")  # Use this to output graph to static HTML file
#output_notebook()         # Use this instead in Jupyter notebook


bokeh_plot = make_plot(x, y)
show(bokeh_plot)