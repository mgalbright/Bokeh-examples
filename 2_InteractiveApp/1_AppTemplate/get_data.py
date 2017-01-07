"""Add your code here to retrieve data and return for plotting:"""

from bokeh.models import ColumnDataSource
import pandas as pd
import numpy as np


def get_data(phase, amplitude, fcn):
  """Add your code here to generate and return data to be plotted.

  For best results, it's easiest to import data into a Pandas dataframe and
  then convert the dataframe into a Bokeh ColumnDataSource.

  In this example, get_data() generates x and y values for a trig function.
  It takes as input the phase, amplitude, and trig function to use.
  """

  x_data = np.linspace(0, 4*np.pi, 50)
  y_data = amplitude*fcn(x_data + phase)

  #pack data into a Pandas dataframe.  Here, 'x' and 'y' are column names.
  df = pd.DataFrame({'x' : x_data, 'y' : y_data})

  #Convert pandas dataframe to ColumnDataSource (Bokeh's native data format)
  return ColumnDataSource(data=df)
  