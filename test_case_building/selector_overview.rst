:author: Charles Callaway
:date: 30-12-2019
:modified: 15-01-2020
:tags: selector, gui, overview
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt

.. role:: rawhtml(raw)
   :format: html


.. _alyvix_selector_top:

****************************
Selector: Interface Overview
****************************

Alyvix Selector allows you to organize individual test cases, copy test case objects from one
file to another, and visualize and change basic test case parameters.  Unlike Designer, you can
quickly compare multiple test case objects with each other, even if they reside in separate files.

When used with Alyvix Editor rather than as a standalone application, it allows you to quickly
select test case objects to create scripted interactions.

The Selector interface is centered around a list-based display of each test case, with a separate
tab for each :file:`.alyvix` file.  The *primary* tab (the first one opened that has the blue
background) is the only file whose objects can be changed.  All other *secondary* tabs are used
for the purpose of viewing and filtering their test cases, and potentially importing them into the
primary tab.  The values of test case objects in secondary tabs cannot be changed.

You can start Alyvix Selector by itself from the command prompt (you can find information about its
:ref:`command arguments here <test_case_building_selector_launch>`):

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> python alyvix_selector.py -f <file-name>

You will then see the Selector interface as shown here:

.. image:: images/as_main_screen_numbered.png
   :alt: The Alyvix Selector interface.
   :target: ../../test_case_building/images/as_main_screen_numbered.png

The principle interface elements are:


.. rst-class:: bignums

#. The **file tabs** show the primary tab and any additional opened :file:`.alvyix`
   :ref:`test case files <test_case_data_format_top>`.  Switching between tabs shows the existing
   test case objects that each file contains.  New files can be loaded by clicking on the
   :nobutton:`+` button.  Similarly, the :nobutton:`x` button next to a non-primary tab will
   remove that tab (note that you cannot remove the primary tab).
#. The **list headers** :ref:`categorize the properties <alyvix_selector_interface_headers>` of each
   object, allowing you to sort on some fields and find the details of a particular test case
   object at a glance.
#. The **test case object list** :ref:`shows the principal properties <alyvix_selector_interface_list>`
   (excluding the component tree) of each test case object, with one line for each object.
#. The **list actions** let you quickly select or deselect all test cases in the list.
#. The **filtering and search** fields let you select all test case objects with a given resolution,
   or that contain a given text string in either the :guilabel:`Name` or :guilabel:`Date modified`
   fields.  The Search field uses a non-regex substring search, and the :nobutton:`x` action
   clears the field.
#. The **test case object actions** act on the
   :ref:`currently selected test case objects <alyvix_selector_interface_object_actions>`
   in the list.
#. The :bbutton:`OK` and :nobutton:`CANCEL` buttons will exit Alyvix Selector, either saving or
   discarding any changes, respectively.


.. todo::

   In the Selector interface main section:

   * FM: What happens if you accidentally open the same file twice (primary+secondary or
     secondary+secondary tabs)?  **A: Not a problem, by design**
   * FM:  Using "COPY" in (4), what is copied and how do you paste it?  How is it different
     than the "DUPLICATE" button in (6)? **A: copy only copies the name**
   * FM:  Search seems to work only for the *Name* and *Date modified* fields, is that expected?
     **A:  Yes**
   * FM:  Unlike Designer, you can right-click in Selector and Editor and it brings up a Chrome menu.
     Is Chrome required to run Alyvix?
     **A:  No, known issue, don't mention**




.. _alyvix_selector_interface_headers:

=====================
Selector List Headers
=====================

The test case object list headers describe the contents of their respective columns.
The list can be sorted on the first three columns by clicking on the header name, with the
:rawhtml:`<i class="fa fasmall fa-sort-up" style="vertical-align:bottom;"></i>` and
:rawhtml:`<i class="fa fasmall fa-sort-down" style="vertical-align:top;"></i>`
icons indicating whether the sort is ascending or descending.

The list headers have the following characteristics:

* **Name:**  The object name :ref:`assigned to the test case object <alyvix_designer_interface_descriptions>`
  in Director
* **Transaction group:**
* **Date modified:**  The last date and time automatically recorded when saved in Designer
* **Timeout, Break, Measure:**  Displays the values of the corresponding
  :ref:`test case options <alyvix_designer_options_test_case>` in Designer
* **Warning, Critical:**  The threshold values set for integration with monitoring
* **Resolution:**  The horizontal and vertical pixel resolution, and the frequency (Hz) when the
  screen capture was created
* The **Screen** element serves as a visual "double check" that you have the correct test case,
  which is especially helpful when you have a large number of objects in a single file


.. todo::

   In the Selector list headers section:

   * FM+CC:  What is a transaction group (2nd column)?  We need to describe it, Warning and Critical.
     **Tgroup is a semantic human-readable note allowing you to group similar actions like Login pages, then Add Contact pages, then Pay pages**
     **Then you can sort it by those groups**
   * FM:  You can set Warning and Critical in the interface, but it disappears after a few seconds
     (perhaps related to the break/measure reset we saw in our meeting on Editor?)  Is this the
     place you are supposed to set these values, not in Designer?
     **A:  Being fixed, only need the description**



.. _alyvix_selector_interface_list:

=====================
Test Case Object List
=====================

This list shows all test case objects contained in file of the currently selected tab.

The values for most fields in the primary tab can be changed directly without opening Designer
(except for **Date modified**, **Resolution** and **Screen**).  This can be accomplished merely
by clicking on the existing value (or blank space where it should go), entering the new value,
and then clicking elsewhere in the list.  Remember that any changes will not be saved until
you have exited Selector by clicking on the :bbutton:`OK` button.

.. note::

   The values of test case objects in secondary tabs cannot be changed.

The *bars* icon :rawhtml:`<i class="fa fasmall fablack fa-bars"></i>` at the start of each row
allows you to (1) select that test case object, or (2) *drag-and-drop* the test case into the
:ref:`Editor scripting panel <alyvix_editor_interface_script>` when Selector is not being used
as a standalone application.

The :kbd:`Shift` and :kbd:`Control` keys work together with the mouse to select multiple rows
in the standard way when using Windows applications.  Selected rows are shown with a light blue
background, and can then be used with the actions described in the next section below.

.. todo::

   In the Selector test case list section:

   * FM:  You can drag an object from a secondary tab into the Editor interface.  Does that
     object then get automatically imported into the file of the primary tab?  When I did it,
     the new object didn't appear in the primary tab.  Is it also a requirement to use the
     Import button when doing this?
     **A:  Being fixed as a future feature**



.. _alyvix_selector_interface_object_actions:

========================
Test Case Object Actions
========================

The :wbutton:`DELAY [S] <n> ADD` control allows you to add a completely new test case by launching
Designer directly from the Selector interface with the specified countdown delay in seconds
just as if you had used Designer's :file:`--delay` option from the command prompt.  This
action is available regardless of whether a test case object is selected.

The :wbutton:`EDIT` button appears when only a single test case is selected.  Clicking on it
launches Alyvix Designer with the currently selected test case file and object.

Two other actions affect all test case objects currently selected:

* :wbutton:`DUPLICATE` will create a new test case object(s) from each selected row.  The new
  name(s) will be the same name(s) as the currently selected object(s), but with the string
  *_copy* appended at the end.  The new objects will appear at the bottom of the list.
* :rbutton:`REMOVE` will delete all currently selected test case objects.  A confirmation
  request dialog will appear to make sure test cases aren't accidentally deleted.

When an additional file tab is open, only the :wbutton:`IMPORT` action will appear.
Any objects selected will be copied just as for :wbutton:`DUPLICATE`, except that the new
object(s) are copied to the primary tab rather than to the currently opened tab.

Remember that any changes you make to test case objects in the primary tab are not saved unless
you exit Selector by pressing the :bbutton:`OK` button.  (No changes will be made to any objects
in any additional tabs).