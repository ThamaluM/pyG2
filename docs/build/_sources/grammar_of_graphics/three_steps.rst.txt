Three Steps of Grammar of Graphics
===================================

Charting graphic generation is a systematic process. There are three steps in graphic generation.

Specification
---------------
Describe how the graph should be created. We have to specify six elements of the chart.

Implementation
---------------
Construct related objects and communication between them. You do not have to worry about this. This is what chart library
does. When your code runs set of objects are constructed and the graphic or the chart is created through the communication
of these objects.

Rendering
-----------
Show graphics to the user. 

PyG2 supports two rendering methods

1. **Canvas rendering**: Graphic is rendered as in a raster format.
2. **SVG rendering**: Graphic is rendered in a vector format.

Raster format stores a picture as a matrix of pixels (like painting) while vector formats stores details on 
mathematical formulaes that generate the parts of the picture (like drawing the picture).

Vector formats are scalable without blurring. However when the number of elements in the graphic is very higher it will
take more time to render the image. You can read more about it in the internet.

* To specify canvas rendering (default)::

    chart = G2.Chart(renderer='canvas')

* To specify svg rendering::

    chart = G2.Chart(renderer='svg')






