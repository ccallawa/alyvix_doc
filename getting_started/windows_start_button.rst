:author: Charles Callaway
:date: 03-01-2020
:modified: 29-01-2020
:tags: getting, started, beginner, windows, start, editor
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_start:

****************************************
Example:  Opening the Windows Start Menu
****************************************

This short task will accomplish something simple, yet will show you the potential of
using Alyvix.

.. rst-class:: bignums

#. Launch Alyvix Editor, giving it a file name to use (the exact name is not important,
   but we will reuse them in subsequent examples):

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_editor -f start-test

   The Editor screen will appear:

   .. image:: images/ae_empty_panel.png
      :class: image-with-border
      :alt: The Windows Start button in Alyvix Designer
      :target: ../_images/ae_empty_panel.png

#. Click on the :wbutton:`DELAY [SEC]  0  ADD` button at the bottom to create a screen capture.

#. Next, use the mouse to create a **selection**
   :rawhtml:`<a href="../glossary.html#glossary-selection"><i class="fa fa-tiny fa-question-circle"></i></a>`
   around the Windows Start button by *left-clicking* and *dragging* so that it looks similar to
   this screenshot (if you don't get it quite right the first time, just resize any of the edges
   using the left mouse button):

   .. image:: images/gs_screen_capture_start_button.png
      :class: image-with-border
      :alt: Selecting the Windows Start button.

#. With our region still selected, press the :kbd:`Escape` key.  The Editor interface will return
   with the region containing the Start button as shown in the panel at the right:

   .. image:: images/ae_basic_designer_panel.png
      :class: image-with-border
      :alt: The Windows Start button in Alyvix Editor's Designer panel

#. At the bottom of that panel under the label :guilabel:`Action` there is a dropdown option
   with the value ``None``.  Change that value from ``None`` to ``Click`` and keep its default
   values.  A mouse icon to the right of the button image will confirm this with a red highlight.

   .. image:: images/ae_designer_panel_selection.png
      :class: image-with-border
      :alt: The click point added to the Windows Start button in the Designer panel

#. Save this new test case by clicking the :nobutton:`SAVE AS` button at the top.  Since we started
   Editor with the option ``-f start-test``, :ref:`the resulting file <test_case_data_format_top>`
   will be called :file:`start-test.alyvix`.

#. In the Selector panel at the bottom left, change the name of our **test case object**
   :rawhtml:`<a href="../glossary.html#glossary-test-case-object"><i class="fa fa-tiny fa-question-circle"></i></a>`
   from the default name :guilabel:`VisualObject1` to a new one like :guilabel:`PressStartButton`:

   .. image:: images/as_rename_object.png
      :class: image-with-border
      :alt: The start button test case in Alyvix Selector

#. Using the |bar-icon| icon, drag the new test case object and drop it into the Scripting panel
   marked :bbutton:`Script: MAIN`.

   .. image:: images/ae_basic_script_element.png
      :class: image-with-border
      :alt: The start button script element in Alyvix Editor

#. Now call Alyvix Robot by pressing the |runblue| button at the top left.  You should see the
   mouse move over to the Windows Start button and click, causing the Start Menu to open.  Finally,
   exit Alyvix Editor using the :nobutton:`EXIT` button at the top.

If you saw the Start Menu appear, then you've successfully built and run your very first Alyvix
test case!

The following page will continue this example to create a more complex script.
