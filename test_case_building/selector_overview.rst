:author: Charles Callaway
:date: 30-12-2019
:modified: 30-12-2019
:tags: selector overview
:lang: en-US
:translation: false
:status: draft


.. todo::

   * Describe object import
   * Describe multiple files


.. _alyvix_selector_top:

***************************
Selector Interface Overview
***************************

Alyvix Selector allows you to visualize and change some of the basic test case parameters,
organize individual test cases, and copy test case objects from one file to another.
The interface is centered around a list display of each test case in a given file.

You can start Alyvix Selector by itself from the command prompt:

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_selector.py -f <file-name>

You will then see the Selector interface as shown here:

.. figure:: images/as_main_screen_numbered.png
   :align: center
   :alt: The Alyvix Selector interface.
   :figwidth: 100%
   :target: ../../test_case_building/images/as_main_screen_numbered.png

   Fig. 1:  The Alyvix Selector interface.

The principle interface elements are:


.. rst-class:: bignums

#. The **file tabs** show the opened :ref:`Alyvix test case files <alyvix_selector_interface_tabs>`.
   By switching between tabs, you can see the test case objects contained separately in each
   :ref:`file <test_case_protocol_top>`.
#. The **list headers** :ref:`categorize the properties <alyvix_selector_interface_headers>` of each
   object, allowing you to find the details of a particular test case object at a glance.
#. The **test case object list** :ref:`shows the principal properties <alyvix_selector_interface_list>`
   (excluding the component tree) of each test case object, with one line for each object.
#. The **global list options** let you quickly select or deselect all test cases in the list.
#. The **filtering and search** fields let you select all test case objects with a given resolution,
   or that contain a given text string in either the ``Name`` or ``Date modified`` fields.
#. The **test case object options** for items in the list allow you to
   :ref:`edit <alyvix_selector_interface_object_options>` that test case object.
#. The :guilabel:`OK` and :guilabel:`Cancel` buttons will exit Alyvix Selector, either saving or
   discarding any changes, respectively.


.. todo::

   * What can you do with the "+" tabs in (1)?
   * What is a transaction group?
   * Delay is not shown in the list, nor when a test case is selected.  Why is it in (6)
     instead of in (3)?
   * What happens if you accidentally open the same file twice (two tabs)?
   * Can't use *-f "file1 file2"* with Selector?  Can't kill the first working case?
     Running alyvix_selector.py with no arguments creates a tab.
   * How to select a line in the list without selecting one of its elements
   * Using "COPY" in (4), what is copied and how do you paste it?  How is it different
     than the "DUPLICATE" button in (6)?  Why is "DELAY" an action like "EDIT" in (6)?
   * Search seems to work only for the *Name* and *Date modified* fields
   * Warning and Critical need to be described here.
   * Unlike Designer, you can right-click in Selector and it brings up a Chrome window.
     Is Chrome required to run Alyvix?



.. _alyvix_selector_interface_tabs:

==================
Selector File Tabs
==================

- "+" sign to add a tab
- "x" symbol to remove a tab
- cannot remove the first tab



.. _alyvix_selector_interface_headers:

================
Selector Headers
================

- Can sort based on the first three columns (name, Tgroup, Date)
- Some are described in :ref:`Designer <alyvix_designer_options_test_case>`
  (Name, timeout, break)

* **Name:**
* **Transaction group:**
* **Date modified:**
* **Timeout:**
* **Break:**
* **Measure:**
* **Warning:**
* **Critical:**
* **Resolution:**
* The **Screen** element serves as a double check that you have the correct test case, which is
  especially helpful when you have a large number of objects in a single file.



.. _alyvix_selector_interface_list:

==============
Test Case List
==============

- Selected row(s) are shown with the light blue background
- Some fields can be changed (Name, Tgroup, Timeout, Break, Measure, Warning, Critical).
  The others are fixed.


.. _alyvix_selector_interface_object_options:

==============
Object Options
==============

- General description
- Any changes made by the following actions will not be written out to the test case file until
  the :guilabel:`OK` button is pressed, causing Selector to save and exit (or Designer, in the
  case of the **EDIT** button.

* The :guilabel:`DELAY**` control allows you to add or change the countdown delay in seconds
  between when a test case is invoked, and when it begins visually searching the screen.
* The :guilabel:`**EDIT**` button calls Alyvix Designer with the currently selected test case
  file and object.
* :guilabel:`**DUPLICATE**` will create a new test case object(s) whose name is the same name as
  the object(s) in the current row(s), but with the string "_copy" appended.
* **REMOVE** Will delete the currently selected test case object.

.. todo::

   * Is the ``EDIT`` button designed to be used within Editor?  Will it work if I run it
     from the command line?
   * Is the delay not saved to the .json file?  When I added ``-d 3`` to the command line
     calling Designer, it counted down at the time, but I can't find it in the .json and
     Selector says it's ``0``.  When I try to change the delay to ``3`` in Selector and
     press ``OK``, it sometimes exits with an error and sometimes counts down immediately
     and then calls Designer with an empty test case.
