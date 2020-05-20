Tutorial
###########

PyG2 is very logical and commnds are simple when it comes to graphic generations.

* Installation::

    pip install pyG2

* Open Jupyter Notebook

* Import modules::

    from PyG2 import pyG2
    import pandas

* In this example we use ``mtcars`` dataset from https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv Download CSV file, save it in the same folder as the notebook and change the header of the first column to **name**

* Prepare a Panda DataFrame::

    df = pd.read_csv('mtcars.csv')
    df.head(1)

Columns are 'name', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am',
       'gear' and 'carb'.



Data preperation
-----------------

Data should be processed by panda dataframe if any transformation presents.

Chart Layout Configuration
----------------------------

We have to construct a graph object::

    chart = Chart(height, width, autoFit, limitInPlot, padding, pixelRatio, renderer, visible)

All parameters are optional. 

    height: int (ppt)  (default 500)

    width: int (ppt)   (default 400)

    autoFit: 'true' / 'false' (default 'true')      **'true' (str) not True (bool)**

    limitInPlot: 'true' / 'false' (default 'false') 

    padding: int/ [int,int,int,int]

    pixelRatio: int    (pixelRatio for canvas rendering)

    render: 'canvas'/'svg'

    visible: 'true'/'false'


* Display changes::

    chart.render()


**All other codes comes between Chart object construction and rendering steps.**

Variable Maps
-------------------

One dimension map: e.g. ``name``
Two dimensional variable map: e.g ``name*cyl``


Main Topics
-------------

.. toctree::
    :maxdepth: 3


    tutor/scales
    tutor/axis
    tutor/geom_aes
    tutor/coordinates
    tutor/legends
    tutor/annotations

