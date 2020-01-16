:author: Charles Callaway
:date: 08-01-2020
:modified: 14-01-2020
:tags: editor, gui
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt

.. role:: rawhtml(raw)
   :format: html


.. _getting_started_editor_top:

*********************************
Scripting a Test Case with Editor
*********************************

This task will introduce you to the scripting mechanism in Alyvix Editor.  It will allow you to
create much more complex behaviors than we saw when calling Alyvix Robot in
:ref:`our prior task <getting_started_example_settings_robot>`.

.. rst-class:: bignums

#. Launch Alyvix Editor with the file name from our previous example:

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_editor -f start-test

#. The Editor interface will appear along with both Designer and Selector, showing the two
   objects in our test case, :guilabel:`settings` and :guilabel:`start`:

   .. image:: images/ae_getting_started_example_main.png
      :alt: The initial screen in Alyvix Selector
      :target: ../_images/ae_getting_started_example_main.png

#. Now *drag and drop* the :guilabel:`start` object (here it's on the second row) by clicking on
   the :rawhtml:`<i class="fa fasmall fablack fa-bars"></i>` icon at the left and dragging it to
   the large middle panel.  Its scripting element will appear:

   .. image:: images/ae_getting_started_example_drag01.png
      :alt: Selecting a row in Alyvix Selector
      :target: ../_images/ae_getting_started_example_drag02.png

#. Next, repeat this procedure for the *settings* object, dragging it to the panel underneath
   the :guilabel:`start` scripting element:

   .. image:: images/ae_getting_started_example_drag02.png
      :alt: Duplicating a row in Alyvix Selector
      :target: ../_images/ae_getting_started_example_drag02.png

#. Finally, click on the |runblue| button at the top left, which will call Alyvix Robot with
   the script we just created.

#. Since this simple script is the same as when we called Alyvix Robot using the command prompt,
   it has the same effect:  opening the Start menu and then opening the Settings app.  Also as
   before, the timing data is reported in the command prompt.
