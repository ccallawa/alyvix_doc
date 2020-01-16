:author: Charles Callaway
:date: 03-01-2020
:modified: 14-01-2020
:tags: getting, started, beginner, windows, start
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_start:

******************************
Opening the Windows Start Menu
******************************

This short task will accomplish something simple, yet will show you the potential of
using Alyvix.

.. rst-class:: bignums

#. Launch Alyvix Designer with a dummy file name and object name (for the purposes of this
   example, the names used are not important):

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_designer -f start-test -o start

#. Use the mouse to select the Windows Start button by *left-clicking* and *dragging* to create
   a rectangular region (a :ref:`Region of Interest <glossary_region_of_interest>`) so that it
   looks like the image here:

   .. image:: images/gs_screen_capture_start_button.png
      :width: 55%
      :alt: Selecting the Windows Start button.
      :target: ../../getting_started/images/gs_screen_capture_start_button.png

#. With our region still selected, press the :kbd:`Escape` key.  The Designer interface will
   appear with our region containing the Start button as shown:

   .. image:: images/gs_start_selected.png
      :alt: The Windows Start button in Alyvix Designer
      :target: ../../getting_started/images/gs_start_selected.png

#. Towards the bottom of the panel under the label :guilabel:`Action` there is a dropdown option
   with the value ``None``.  Change that value from ``None`` to ``Click``.  A small red dot will
   appear in the center of the selected region, indicating that is where Alyvix Robot will click
   when it recognizes the Start button image onscreen.

   .. image:: images/gs_start_click_action.png
      :alt: The click point on the Windows Start button
      :target: ../../getting_started/images/gs_click_action.png

#. Save the test case by clicking the :bbutton:`OK` button at the bottom left.  Since we started
   Designer with the option ``-f start-test``, :ref:`the resulting file <test_case_data_format_top>`
   will be called :file:`start-test.alyvix`.

#. Now call Alyvix Robot with the same parameters (file name and object name) as for Designer
   in Step #1 above:

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_robot -f start-test -o start

   You should see the mouse move over to the Start button and click, causing the Start Menu to open.

If you saw the Start Menu appear after running Robot, then you've successfully built and run
your very first Alyvix test case!
