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


.. _getting_started_selector_top:

*********************************
Duplicating Objects with Selector
*********************************

This task is mostly just to explore Alyvix Selector.  We won't add anything to our running
example, but we'll learn about how Selector works, which will be necessary for the next step
when we look at Alyvix Editor.

.. rst-class:: bignums

#. Launch Alyvix Selector with the file name from our previous example:

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_selector -f start-test

#. The Selector interface will appear, showing the two objects in our test case:

   .. image:: images/as_getting_started_example_main.png
      :alt: The initial screen in Alyvix Selector
      :target: ../_images/as_getting_started_example_main.png

#. Now select the first row by clicking on the
   :rawhtml:`<i class="fa fasmall fablack fa-bars"></i>`
   icon to the left of the object name :guilabel:`settings`:

   .. image:: images/as_getting_started_example_selected.png
      :alt: Selecting a row in Alyvix Selector
      :target: ../_images/as_getting_started_example_selected.png

#. Next click on the :wbutton:`DUPLICATE` button at the bottom right, which will copy the
   :guilabel:`settings` object and call it :guilabel:`settings_copy`:

   .. image:: images/as_getting_started_example_duplicated.png
      :alt: Duplicating a row in Alyvix Selector
      :target: ../_images/as_getting_started_example_duplicated.png

#. Let's set a filter so only our new copy is visible.  Go to the :guilabel:`Search` field
   at the bottom and type ``copy``.  Right after you type the first letter ``c``, the objects
   are already being filtered:

   .. image:: images/as_getting_started_example_filtered.png
      :alt: Duplicating a row in Alyvix Selector
      :target: ../_images/as_getting_started_example_filtered.png

#. Now remove this test case object by clicking on the :rbutton:`REMOVE` button.

#. Next, remove the Search filter by pressing the black :nobutton:`x` icon immediately to its
   right.  Our original two test cases will reappear.

#. Finally, let's exit without saving by pressing the :nobutton:`CANCEL` button.

On the next page we'll see more about Selector when we use Alyvix Editor.
