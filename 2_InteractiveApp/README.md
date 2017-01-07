# Interactive webapps in Bokeh

Reusable examples of Bokeh webapps.

The folder *1_AppTemplate* contains a reusable template for an interactive webapp made with Bokeh.
It is meant to be easily modified to build your own custom web app.  


As an example, in *2_GraphEconData* I used the template to quickly build
a web app to graph US economic data from the Federal Reserve.  

To run the example in *1_AppTemplate*, open a terminal to this folder and run
```bash
bokeh serve --show 1_AppTemplate/
```
This will launch a Bokeh server and serve the web page on your local host. The webapp 
should open in your default browser.  

(Press Ctrl + c to stop the Bokeh server.)

To run the second example, instead run
```bash
bokeh serve --show 2_GraphEconData/
```
