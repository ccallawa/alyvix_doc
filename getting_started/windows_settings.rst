:author: Charles Callaway
:date: 03-01-2020
:modified: 23-01-2020
:tags: getting, started, beginner, windows, settings
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_settings:

********************************************
Opening Windows Settings from the Start Menu
********************************************

The real value of Alyvix lies in chaining together sequences of detections and actions.  So let's
extend the :ref:`previous example <getting_started_example_start>` to also recognize when the
Start Menu has opened, and click on Windows Settings within it.

We'll need to create a second test case with its own screenshot.  However, we can't detect
anything within the opened Start Menu, because it closes by itself whenever we launch a program
like Alyvix Designer.  So how can we get around this problem?

The answer is to use the :ref:`delay parameter <test_case_building_designer>` when starting
Alyvix Designer.  This will insert a delay of the requested number of seconds before the screen
is captured.  To do this:

.. rst-class:: bignums

#. Add the ``-d`` delay parameter (in seconds) as shown.  Remember to give the new test case a
   different object name (it needs to have the same file name, however):

   .. code-block:: doscon
      :class: medium-code-block

      C:\Alyvix\testcases> alyvix_designer -f start-test -o settings -d 5

#. Once you see the line "Counting down" in the console, you'll have 5 seconds to open the Start
   Menu and then wait for Alyvix Designer to capture the screen.

#. Next, use Designer to select a region around the *Settings* icon on the left side of the Start
   Menu.  This time, *right click* on the icon to autocontour
   :rawhtml:`<a href="../glossary.html#glossary-autocontour"><i class="fa fa-tiny fa-question-circle"></i></a>`.
   it, and then press :kbd:`Escape`.  You should now see:

   .. image:: images/ad_comptree_autocontour.png
      :alt: Setting up the Windows Settings button in Alyvix Designer
      :target: ../_images/ad_comptree_autocontour.png

#. Assign a *left click* action as before by selecting our new Settings icon region in the
   component tree, and then changing the action from ``None`` to ``Click``.

#. Save and exit by clicking on the :bbutton:`OK` button.

   .. _getting_started_example_settings_robot:

#. Now we can run the two objects by joining their names of our two test cases together as follows:

   .. code-block:: doscon
      :class: medium-code-block

      C:\Alyvix\testcases> alyvix_robot -f start-test -o "start settings"

   This will chain the end of one test case to the beginning of the next.

#. When you run Alyvix Robot, you'll see the Start Menu open, and then a few seconds later a
   click on the Settings icon, at which point the Windows Settings app will open.

#. Finally, look at the command prompt again.  You will see that Robot has reported the combined
   run time of the two test cases in the command prompt.
