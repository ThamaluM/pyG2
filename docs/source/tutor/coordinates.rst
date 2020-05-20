Coordinates
=============

We can specify coordinates as below::

    chart.coordinate('type')

There are four types.

#. ``rect``/ ``cartesian``    (x,y)::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('rect')
    chart.render()

Output:

.. image:: rect_coord.png

#. ``polar``                  (r,theta)::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('polar')
    chart.render()

Output:

    .. image:: polar_coord.png

#. ``theta``                  (theta,r)::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('theta')
    chart.render()

.. image:: theta_coord.png

#. ``helix`` ::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('helix')
    chart.render()

Output:

.. image:: helix_coord.png



There are coordinate transformation functions.

#. transpose ::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('rect').transpose()
    chart.render()

Output:

.. image:: coord_transpose.png

#. reflect ::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('rect').reflect('y')
    chart.render()

Output:

.. image:: coord_reflect.png

#. rotate::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('rect').rotate(0.1)
    chart.render()

Output:

.. image:: coord_rotate.png

#. scale::

    chart = G2.Chart(height=500, width=1000)
    chart.data(df)
    chart.interval().position('name*mpg')
    chart.coordinate('rect').scale(0.5,0.1)
    chart.render()

.. image:: coord_scale.png