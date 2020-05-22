Geometry and Aesthetic
########################

Geometry
==============

Geometries are the main components of the chart. Geometries maps the variables into graphic space.

G2 supports:

point, line, area, interval, polygon, edge, schema geometry types.

point
-------
::

    chart.point().position('x*y')

This code generates points at the places specified by position aesthetic as (x,y).

Supported shapes are (default is ``hollow-circle``),

'circle', 'square', 'bowtie', 'diamond', 'hexagon', 'triangle', 'triangle-down', 'hollow-circle', 'hollow-square',
'hollow-bowtie', 'hollow-diamond', 'hollow-hexagon', 'hollow-triangle', 'hollow-triangle-down', 'cross',
'tick', 'plus', 'hyphen', 'line'


line
--------
::

    chart.line().position('x*y')


This code generates a line chart that is drawn connecting all points specified by position aesthetic. If shape or color
aesthetics are used then there will be several lines related to each aesthetic.

Supported shapes are

 'line',' dot', 'dash',' smooth', 'hv',' vh', 'hvh',' vhv'

('hv',' vh', 'hvh',' vhv' are used for ladder diagrams) 


area
-----------------
::

    chart.area().position('x*y')

This code generates area chart. Here under the field ``y`` there may be a single value or a list of two values

If ``y`` is a single value then the area is the area under the line drawn by connecting (x,y) points.
If ``y`` is a list then the area is between two y values is the area.



Shape and line aeasthetics generates seperate area for each set.
Supported shapes are

 'area', 'smooth', 'line', 'smooth-line'

**N.B:**

**If we use lists in lines and points then there will be several lines and points for each record.**

interval
-------------

::

    chart.interval().position('x,y')

If ``y`` is a single value then the interval is the interval between y value and 0.
If ``y`` is a list then the interval is between two y values is the interval.
If ``x`` is a single value the is of a default fixed width bar at (x,y)
If ``x`` is a list then the interval is a bar spreaded between first and second value of the list.

 
Supported shapes are 

'rect', 'hollow-rect', 'line', 'tick', 'funnel', 'pyramid'

'funnel' is for funnel chart.
'pyramid' is for pyramid chart.

polygon
-------------

::

    chart.polygon().position('x,y')

``x`` and ``y`` are lists such that corresponding values of two lists gives coordinates of the vertices.
(Vertices are connected as they are ordered in two lists.)

Shape and size aesthetics are not related to polygons.

schema
---------
::

    chart.schema().position('x,y')

If the map is one dimensional then list must be supplied.

When the map is two dimensional,

``x`` is categorical variable and ``y`` is an array of values.

Supported shapes:

'box'



Aesthetics
=============

position
-----------

:: 

    chart.<geometry>().position('x*y')

This part is completed under the previous section.

shape
-----------

:: 

    chart.<geometry>().position('x*y').shape('z')

If we put a specific shape to ``z`` that given under geometries the geometry will take that shape. If we give a variable
name to ``z`` the shape will change with the value of that variable. 

As below we can specify list of shapes we want to use as an optional argument

:: 

    chart.<geometry>().position('x*y').shape('z',values)



color
----------

::

    chart.<geometry>().position('x,y').color('z')

or

::

    chart.<geometry>().position('x,y').color('z',values)

::

    chart.<geometry>().position('x,y').color(color)


Here ``values`` are list of colors to be used and  ``color`` is a color if one color is used for complete geometry.


size
----------

::

    chart.<geometry>().position('x,y').size('z')

Label
=======

::

    chart.<geometry>().position('x,y').label('z')

Collision Handelling
=======================

Sometimes several parts of the graphs collides, that is to say locate in the overlapping positions.
We can fix this by ``adjust()``

There are several ``adjust`` types. ``stack`` to make colliding parts in a stack. ``dodge`` to present them
horizontally packed. ``jitter`` in point maps to show them as a cluster.

The collisions of labels can be handled using ``overlap`` and ``fixed-overlap``.
