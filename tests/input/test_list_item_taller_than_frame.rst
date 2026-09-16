.. A list item whose body is taller than the frame, by less than the
.. padding and spacing that wrap() charges and the scan in split() does
.. not.  The scan then never reaches the available height, no break point
.. is found, and the item is carried to a fresh page where it measures the
.. same -- until the build gives up.  The test is successful if a PDF is
.. created.

Splitting a list item that does not fit
=======================================

- This item holds more examples than will fit in a frame, so it has to be
  broken across pages.

  Example 1::

     line 1 of example 1
     line 2 of example 1
     line 3 of example 1
     line 4 of example 1
     line 5 of example 1

  Example 2::

     line 1 of example 2
     line 2 of example 2
     line 3 of example 2
     line 4 of example 2
     line 5 of example 2

  Example 3::

     line 1 of example 3
     line 2 of example 3
     line 3 of example 3
     line 4 of example 3
     line 5 of example 3

  Example 4::

     line 1 of example 4
     line 2 of example 4
     line 3 of example 4
     line 4 of example 4
     line 5 of example 4

  Example 5::

     line 1 of example 5
     line 2 of example 5
     line 3 of example 5
     line 4 of example 5
     line 5 of example 5

  Example 6::

     line 1 of example 6
     line 2 of example 6
     line 3 of example 6
     line 4 of example 6
     line 5 of example 6

  Example 7::

     line 1 of example 7
     line 2 of example 7
     line 3 of example 7
     line 4 of example 7
     line 5 of example 7

  Example 8::

     line 1 of example 8
     line 2 of example 8
     line 3 of example 8
     line 4 of example 8
     line 5 of example 8

  Example 9::

     line 1 of example 9
     line 2 of example 9
     line 3 of example 9
     line 4 of example 9
     line 5 of example 9

  Example 10::

     line 1 of example 10
     line 2 of example 10
     line 3 of example 10
     line 4 of example 10
     line 5 of example 10

  Example 11::

     line 1 of example 11
     line 2 of example 11
     line 3 of example 11
     line 4 of example 11
     line 5 of example 11

  Example 12::

     line 1 of example 12
     line 2 of example 12
     line 3 of example 12
     line 4 of example 12
     line 5 of example 12
     line 6 of example 12
     line 7 of example 12

- A second item, so that the first one is not the last thing here.

