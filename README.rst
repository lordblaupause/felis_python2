Python II lecture notes
=======================

Supplementary material, lecture notes and exercises for the Python II
lecture at University of Freiburg.

This module will install all requirements needed for the lecture.


Installation
~~~~~~~~~~~~

Basically, all lectures are in the *.ipynb* format of version 4.
Therefore you need Jupyter to view them. The most straitforward way to install the package
is using pip from your desired target environment like:

.. code-block:: bash

  pip install felis_python2

This will install the requirements and the lecture notes to the `site-packages` folder of the target
Python environment. The module does include some auxiliary functions to use the notebooks from there.
Alternatively, it can also be downloaded from github and installed manually like:

.. code:: bash

    ~$ git clone https://github.com/mmaelicke/felis_python2.git
    ~$ cd felis_python2
    ~$ pip install -r requirements.txt
    ~$ cd lectures
    ~$ jupyter notebook


Usage
~~~~~

There are also two auxiliary functions included in the package. If installed using pip, `felis_python2` can
be imported. The `run` function will start a Jupyter notebook server at the correct location and open a browser.
The `copy` function takes a path and will copy the lecute notes notebooks to that specific path.

.. code-block:: python

  from felis_python2 import run, copy

  # to copy the notebooks to another location
  copy('my/new/location')

  # to run them from the site-packages
  run()
