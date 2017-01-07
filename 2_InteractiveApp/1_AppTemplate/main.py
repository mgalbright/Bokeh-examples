"""Generate an interactive web app using Bokeh.

   The graph is generated and embedded into the template html file
     /templates/index.html
"""

from bokeh.layouts import row, column, widgetbox   #For laying out the web-page
from bokeh.models import Select, Slider            #Interactive Widgets
from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure
import pandas as pd
import numpy as np

from get_data import get_data

#------------------------------------------------------------------------------
#Some default settings:

#Graph size
GRAPH_WIDTH = 600
GRAPH_HEIGHT = 400

#Default plot
PHASE = 0
AMPLITUDE = 2.0
FCN = np.sin
XLABEL = "time (s)"
YLABEL = "voltage (V)"

PAGE_TITLE = "Plot Demo"
#------------------------------------------------------------------------------

#Important:
#  Load data to be graphed into global variable source.  Note that source is of
#  type ColumnDataSource, the Bokeh data type (similar to a Pandas dataframe).
#  If you skip this step, the graph may respond slowly to changes.
#
#  First, load default data for default graph--the user can change that later
#  by interacting with the page through the widgets.
source = get_data(PHASE, AMPLITUDE, FCN)


def make_plot(**kwargs):
  """Make the Bokeh plot to be displayed."""

  p = figure(plot_height=GRAPH_HEIGHT, plot_width=GRAPH_WIDTH, \
    tools='pan,box_zoom,reset', **kwargs)
  p.xaxis.axis_label = XLABEL
  p.yaxis.axis_label = YLABEL

  #Important: note that we specify source as the data source, and specify
  #column names 'x', 'y' from source to be graphed.
  p.line(x='x', y='y', source=source)
  return p


def update(attr, old, new):
  """Update source variable holding data that the graph displays.

     Important note: callback functions like update() which are called by
     .on_change() events must take arguments (attr, old, new).
  """

  #Grab function_widget's value from the web app's user interface.
  if function_widget.value == 'sin':
    fcn = np.sin
  else:
    fcn = np.cos

  phase = phase_widget.value
  amplitude = amp_widget.value

  #reload data using the user preferences from the webapp's user interface
  src = get_data(phase, amplitude, fcn)

  source.data = src.data  #load data into source.data: graph will update

#------------------------------------------------------------------------------
#Layout the webapp page to be generated:

#First create interactive widgets:

function_widget = Select(title='Function', value='sin', options=['sin', 'cos'])
#Important: widget .on_change events call update() to update the page
function_widget.on_change('value', update)

phase_widget = Slider(start=0, end=2*np.pi, value=PHASE, step=np.pi/5, \
  title="Phase")
phase_widget.on_change('value', update)

amp_widget = Slider(start=0, end=2, value=AMPLITUDE, step=0.2, \
  title="Amplitude")
amp_widget.on_change('value', update)

#Create a widget-box: a group of widgets stacked vertically.
sliders_box = widgetbox([phase_widget, amp_widget], width=300)

#Next layout the page:
# Use column(a, b) to lay out items a over b in a column.
# Use row(c,d) to lay items c, d in a row
layout = column(row(function_widget, sliders_box), make_plot())

curdoc().add_root(layout)
curdoc().title = PAGE_TITLE  #webpage title
