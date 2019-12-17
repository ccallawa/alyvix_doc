:author: Charles Callaway
:date: 4-12-2019
:modified: 17-12-2019
:tags: getting, started
:lang: en-US
:translation: false
:status: draft


.. _getting_started_test:

******************************
Testing that Alyvix is Working
******************************

As a first step, let's check that everything is installed properly.  Run the following command
in the console:

.. code-block:: doscon

   C:> cd C:\Users\<username>\Desktop\Alyvix\Testcases\> alyvix_designer --version

.. todo::

   * If it doesn't return the value 3.x.y, there should be a link to a troubleshooting section

Now let's check that the interface is working.  Pass some dummy arguments for the ``-f`` (file)
and ``-o`` (object).

.. code-block:: doscon

   C:> cd C:\Users\<username>\Desktop\Alyvix\Testcases\> alyvix_designer -f test -o test

.. sidebar:: Fig. 1:  Testing that Alyvix Designer is working

   .. image:: ../test_case_building/images/ad_main_screen_initial.png
      :alt: Testing that Alyvix Designer is working
      :target: ../../test_case_building/images/ad_main_screen_initial.png
      :name: label_test_designer_interface

You should see the screen go blank for a few seconds, before it reappears along with a pair of
guide lines that follow the cursor.  In the top left corner you will see the instructions
:guilabel:`PRESS ESC TO OPEN DIALOG`.  Press :kbd:`ESC`, and the Alyvix Designer interface
will appear.

If you see the Alyvix Designer interface as shown in Figure 1 to the right, then everything is
working properly.

For now, press :guilabel:`CANCEL` at the bottom of the interface.  Since
we canceled the session, no files  will be saved in our working directory.

For more in-depth information on the Alyvix Designer interface, you can refer to the
:ref:`Designer documentation <alyvix_designer_interface_overview>`.

For now, let's try something a bit more complicated.

|
|
|



.. _getting_started_test_cli:

=============================================
A Complete Example:  The Windows Start Button
=============================================

Now let's try a test that will accomplish something simple that will show you the potential of
Alyvix.

First, launch Alyvix Designer with a dummy file name and object name.  For this example, the
names are not important.

.. code-block:: doscon

   C:> cd C:\Users\<username>\Desktop\Alyvix\Testcases\> alyvix_designer -f start-test -o start

.. sidebar:: Fig. 2:  Selecting the Windows Start button

   .. image:: images/gs_screen_capture_start_button.png
      :alt: Selecting the Windows Start button
      :target: ../../getting_started/images/gs_screen_capture_start_button.png
      :name: label_select_start_button

This time when you launch Alyvix Designer, use the guide lines to select the Windows Start
button by drawing a purple rectangle around it as shown in Figure 2.

Then press the :kbd:`ESC` key.  You should see the rectangle you selected as the second node in
the :ref:`Component Tree <alyvix_designer_component_tree>`, below the node with the capital letter
:guilabel:`S` that represents the entire screenshot.



.. sidebar:: Fig. 3:  The Windows Start button in the Designer interface

   .. image:: images/gs_start_button_interface.png
      :alt: The Windows Start button in the Designer interface
      :target: ../../getting_started/images/gs_start_button_interface.png
      :name: label_edit_start_button





.. _getting_started_first_test:

=======================
First Test:  App Launch
=======================

- Add example where Designer/Robot launch an app on Windows 10
- Lots of minimal, focused screenshots



- Link to the how tos
