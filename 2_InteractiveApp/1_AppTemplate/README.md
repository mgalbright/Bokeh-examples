# Basic interactive Bokeh webapp

This is a simple template for a webapp in Bokeh.  It is meant to be
easily modified to build your own custom apps.

`get_data.py` contains the function `get_data()` where 
data to be plotted is prepared.  You will need to add your data loading
code here.

`main.py` is the main python script where the interactive webapp is 
built using Bokeh.  This is where you can customize the Bokeh 
app by adding buttons, sliders, text boxes, etc.  You can also
add event handlers to make the app interactive.

Inside *templates* is `index.html`: the Bokeh webapp is embedded
into this file inside double brackets {{}}.  You can customize this
file to customize your webpage.