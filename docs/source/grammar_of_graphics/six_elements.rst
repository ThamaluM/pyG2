Six Specification statements
==============================

1. Data
2. Transformations
3. Scale
4. Coordinate
5. Element
6. Guide

Data
-------

In pyG2, data should be specified as a list of dictionaries or as a pandas.DataFrame object.

Transformations
------------------

Data transformations should be done beforehand you provide them to the Chart object. You can use pandas.DataFrame to obtain
these transformations.

Scales
--------

``Chart.scale(variable, **config)`` is used to specify the scale and scale transformations. 

Coordinate
------------

``Chart.coordinate(variable, **config)`` is used to specify the coordinate system and coordinate transformations.
 Default is Cartesian coordinates.


Element
----------

In pyG2 chart elements are named geometry. They are the main components of the graphic: line in line chart, bar in bar chart etc.

Guides
--------

In G2, guides are legends, tooltips and annotations. They are the auxillary components of a chart that helps the user to understand the chart
easily.


