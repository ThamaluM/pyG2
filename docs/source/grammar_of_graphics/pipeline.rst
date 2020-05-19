Graphic Generation Pipeline
===================================

Leland Wilkinson identified that there is a pipelined process in graphic generation.


.. figure:: pipeline.png

    Fair use: taken from **The Grammar of Graphics** of Leland Wilkinson

Source
-------
The data source

Variable
-----------
Variable represents a property of an object.

Algebra
---------
Varset algebra: there are operations between varsets. (e.g. cross, nest, blend)

This concept is not properly adopted into G2. Therefore it is not included in pyG2 also.
map of variables is closely related to cross operation. e.g ``name*cyl``

Scales
---------

Scales are mapping values of the variables to dimensions of a coordinate system. 

Statistics
-----------

More oftenly what we want to visualize in the graphic is differs from raw data points. (Remember linear regression)
Therefore statistics is to alter positions of data points.

Geometry
----------

Geometry is to map data with unbounded dimensions into bounded graph dimensions.

Coordinate
------------

Coordinates are coordinates of the graph space.

Aesthetics
------------

Aesthetics are the observable physical properties of the graphics.

Renderer
-----------

Renderer generates the graphic 


Variable vs. Varset
=====================

To define a variable we need three things.

#. Set of objects
#. Set of values
#. Function mapping objects to values

To define a varset we need,

#. Set of values
#. Set of objects
#. Function mapping values to objects

What is the difference? In varsets value has more priority than objects. 
In a graph basically we represent values. An object may be a certain data point. Coordinates are values.
Therefore graphs are made of varsets.


Graph vs. Graphic
===================

* Graph is a mathematical representaion of a bounded multidimentional space. A graph is an abstract entity.

* Graphic is to represent a graph in observable physical properties (aesthetics) such as position, color, shape.


Explanation of Pipeline
=========================

Pipeline is the process of generating any graphic. First we have to get data from a source. Then we have to create variables 
and turn them into varsets. Then using varset algebra we create complex varsets. Thereafter you have to map variable into a 
dimension. (Dimension gives a direction or order to the values.) Then you have to alter positions of the data points to
find the points that are to be visualized in the graphic. Upto here we worked with arbitrary dimension. Then we should
specify coordinate system related to the graphic space. Then we can choose aesthetic to visualize the graph. Finally we 
render the graph through a rendering mechanism. 

We cannot by-pass these steps. This is the way we naturally generate a graphic visualization.

Wilikinson suggested to go through this pipeline and to provide functions to work on relevent steps of the pipeline instead 
of giving ad hoc functions for certain chart types.

Instead of providing list of specific usages, this architecture provides **a grammar** to generate any graphic as you wish.



