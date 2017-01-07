# Simple Bokeh graph

Basic example of building an interactive line graph in Bokeh.  
To make the graph, open a terminal inside this folder and run
```bash
python graph.py
```
This will create an html file (graph.html) containing the interactive graph.

If instead you want to make interactive graphs from a Jupyter notebook,
in `graph.py` comment out the line
```python
output_file("graph.html")
```
and uncomment
```python
output_notebook()
```
