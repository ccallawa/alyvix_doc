:author: Charles Callaway
:date: 04-12-2019
:modified: 09-01-2020
:tags: getting, started, beginner, test
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_test:

******************************
Testing that Alyvix is Working
******************************

As a first step, let's check that everything is installed properly.  Start a Windows Command Prompt
(**Start > Windows System > Command Prompt**) and run the following command:

.. code-block:: doscon

   C:\> cd C:\Users\[username]\Desktop\Alyvix\Testcases\>
   C:\Users\[username]\Desktop\Alyvix\Testcases\> alyvix_designer --version

If the version check doesn't return a value like "3.X.Y", then either Alyvix is not properly
installed, there is an error in your path configuration, or your system does not meet the
requirements.  Please go back and check that
:ref:`everything was properly installed <install_release_top>`.

As a further check, let's make sure that the Alyvix Designer interface is working:

.. code-block:: doscon

   C:\> cd C:\Users\[username]\Desktop\Alyvix\Testcases\> alyvix_designer

.. sidebar:: Fig. 1:  Testing that Alyvix Designer is working

   .. image:: ../test_case_building/images/ad_main_screen_initial.png
      :alt: Testing that Alyvix Designer is working
      :target: ../../test_case_building/images/ad_main_screen_initial.png
      :name: label_test_designer_interface

You should see the screen go blank for a few seconds, before it reappears along with the
crosshairs that follow the mouse.  In the top left corner you will see the instructions
:guilabel:`PRESS ESC TO OPEN DIALOG`.  Press :kbd:`ESC`, and the Alyvix Designer interface
will appear.

If you see the Alyvix Designer interface as shown in Figure 1 to the right, then everything is
working properly.

For now, press :guilabel:`CANCEL` at the bottom of the interface.  When you cancel a session,
no files are saved.

Go on to the next section if you want to try a complete example with Alyvix to see how it works.
Otherwise, you can :ref:`look at more complex tutorials <tutorials_top>`, or start reading right
away to get more in-depth information on :ref:`how to build test cases <test_case_building_top>`
with Alyvix Designer and Alyvix Selector.
