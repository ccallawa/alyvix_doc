:author: Charles Callaway
:date: 04-12-2019
:modified: 10-01-2020
:tags: getting, started, beginner, test
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_test:

******************************
Testing that Alyvix is Working
******************************

.. rst-class:: bignums

#. Start a Windows Command Prompt, change to a working directory, and run the following command:

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_designer

#. You should see the screen go blank for a few seconds as Alyvix makes a copy of the screen.  If
   this doesn't happen, go back and check that :ref:`Python and Alyvix were properly installed
   <install_release_top>`.

#. After the screen capture has completed, red crosshairs will appear that track the mouse.

   .. image:: ../test_case_building/images/ad_crosshairs.png
      :width: 40%
      :alt: Check that the Alyvix Designer crosshairs are visible.
      :target: ../_images/ad_crosshairs.png

   |

#. Now press :kbd:`Escape`.  If the Alyvix Designer interface appears as shown here, then
   everything is working properly:

   .. image:: ../test_case_building/images/ad_main_screen_initial.png
      :alt: Testing that Alyvix Designer is working.
      :target: ../_images/ad_main_screen_initial.png

#. Finally, press :nobutton:`CANCEL` at the bottom of the interface to exit.  When you cancel
   a session, no files are saved.

As a next step, you can:

* Continue on to the next section to try a more complete example with Alyvix to see how it works
* Look at :ref:`more complex tutorials <tutorials_top>` for common use cases
* Read more detailed, technical information on :ref:`building test cases <test_case_building_top>`
* Read about the ideas behind Alyvix, and :ref:`find explanations <glossary_top>`
  that will help you understand why Alyvix is structured the way it is
