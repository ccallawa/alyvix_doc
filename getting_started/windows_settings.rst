:author: Charles Callaway
:date: 03-01-2020
:modified: 28-01-2020
:tags: getting, started, beginner, windows, settings
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_settings:

********************************************
Opening Windows Settings from the Start Menu
********************************************

The :ref:`previous example <getting_started_example_start>` had you create an Alyvix test case
consisting of a single test case object
:rawhtml:`<a href="../glossary.html#glossary-test-case-object"><i class="fa fa-tiny fa-question-circle"></i></a>`.
Most of the time though, you'll need to chain together multiple test case objects.  So let's
extend that example to also open Windows Settings.  We'll start by delaying the screen capture
to give us time to set things up first.

.. rst-class:: bignums

#. Add the ``-d`` parameter to set a delay in seconds as shown, and give the new test case a
   different object name (it needs to have the same file name, however):

   .. code-block:: doscon
      :class: medium-code-block

      C:\Alyvix\testcases> alyvix_designer -f start-test -o settings -d 5

#. Once you see the line "Counting down" in the console, you will have 5 seconds to open the
   Windows Start Menu before Alyvix Designer captures the screen.

#. Use Designer to select a region around the *Settings* icon on the left side of the Start
   Menu.  This time, *right click* on the icon to **autocontour**
   :rawhtml:`<a href="../glossary.html#glossary-autocontour"><i class="fa fa-tiny fa-question-circle"></i></a>`
   it, and then press :kbd:`Escape`.  You should now see the selection in the Designer panel:

   .. image:: images/ad_comptree_autocontour.png
      :alt: Setting up the Windows Settings button in Alyvix Designer
      :target: ../_images/ad_comptree_autocontour.png

#. Assign a *left click* action as in the previous example by clicking on our new Settings icon
   in the component tree
   :rawhtml:`<a href="../glossary.html#glossary-component-tree"><i class="fa fa-tiny fa-question-circle"></i></a>`
   and then changing the value of the :guilabel:`Action` dropdown from ``None`` to ``Click``.

#. Save and exit by clicking on the :bbutton:`OK` button.

   .. _getting_started_example_settings_robot:

#. Now run the two test case objects :ref:`in sequence <alyvix_robot_cli_options>` by
   joining their names together after the ``-o`` parameter as follows:

   .. code-block:: doscon
      :class: medium-code-block

      C:\Alyvix\testcases> alyvix_robot -f start-test -o "start settings"

   This tells Robot to start the ``settings`` test case object as soon as it finishes ``start``.

#. When you run Alyvix Robot, you'll see the Start Menu open, and then a few seconds later a
   click on the Settings icon, at which point the Windows Settings app will open.

#. Finally, take a look at the output in the command prompt, where Robot now reports the
   combined run time of the two test cases.
