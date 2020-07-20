:author: Charles Callaway
:date: 03-01-2020
:modified: 18-08-2020
:tags: getting, started, beginner, windows, start, editor
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt


.. _getting_started_example_start:

****************************************
Example:  Opening the Windows Start Menu
****************************************

This short task will accomplish something simple, yet will show you the potential of
using Alyvix.

Tutorials similar to this one are also available in :ref:`video format <video_tutorials_top>`.

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

#. Click on the :wbutton:`DELAY [SEC]  0  ADD` button at the bottom to trigger a screen capture.

#. Next, use the mouse to create a :iconlink:`gloss|selection|../glossary.html#glossary-selection`
   around the Windows Start button by *left-clicking* and *dragging* so that it looks similar to
   this screenshot (if you don't get it quite right the first time, just resize any of the edges
   using the left mouse button):

   .. image:: images/gs_screen_capture_start_button.png
      :class: image-with-border
      :alt: Selecting the Windows Start button.

#. With our graphic component still selected, press the :kbd:`Escape` key.  The Editor interface
   will return with the area containing the Start button as shown in the panel at the right:

   .. image:: images/ae_basic_designer_panel.png
      :class: image-with-border
      :alt: The Windows Start button in Alyvix Editor's Designer panel

#. At the bottom of that panel under the label :guilabel:`Action` there is a dropdown option
   with the value ``None``.  Change that value from ``None`` to ``Click`` and keep its default
   values.  A mouse icon to the right of the Start button will confirm this with a red highlight.

   .. image:: images/ae_designer_panel_selection.png
      :class: image-with-border
      :alt: The click point added to the Windows Start button in the Designer panel

#. Save this new test case by clicking the :nobutton:`SAVE` button at the top.  Since we started
   Editor with the option ``-f start-test``, :ref:`the resulting file <test_case_data_format_top>`
   will be called :file:`start-test.alyvix`.

#. In the Selector panel at the bottom left, change the name of our
   :iconlink:`gloss|test case object|../glossary.html#glossary-test-case-object`
   from the default name :guilabel:`VisualObject1` to a new one like :guilabel:`PressStartButton`:

   .. image:: images/as_rename_object.png
      :class: image-with-border
      :alt: The start button test case in Alyvix Selector

#. Click on the |lineadd-icon| action next to :guilabel:`PressStartButton` shown in the screenshot
   above to insert the new test case object into the Scripting panel marked :bbutton:`Script: MAIN`:

   .. image:: images/ae_basic_script_element.png
      :class: image-with-border
      :alt: The start button script element in Alyvix Editor

#. Now start Alyvix Robot by pressing the |runblue| button at the top left.  The Editor window will
   disappear and the mouse will move over to the Windows Start button and click, causing the Start
   Menu to open.  Finally, save and exit Alyvix Editor using the :nobutton:`SAVE` and
   :nobutton:`EXIT` buttons at the top.

If you saw the Start Menu appear, then you've successfully built and run your very first Alyvix
test case!

The following page will continue this example to create a more complex script.
