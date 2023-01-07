nmaxmin
========

A Python package for finding the maximum and minimum values in a list.

Installation
------------

To install nmaxmin, run the following command:

.. code-block:: bash

    pip install nmaxmin

Usage
-----

To use the nmaxmin package, import it and call the ``maxn()`` and ``minn()`` functions:

.. code-block:: python

    import nmaxmin

    my_list = [1, 2, 3, 4]
    max_val = nmaxmin.maxn(my_list)
    min_val = nmaxmin.minn(my_list)
    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")

Output:

.. code-block:: python

    Maximum value: 4
    Minimum value: 1


