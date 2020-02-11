:author: Charles Callaway
:date: 07-01-2020
:modified: 11-02-2020
:tags: editor, script, management
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_editor_script_mgmt_top:

****************************
Editor: Scripting Management
****************************

The script management panel organizes and provides quick access to the scripts and subscripts
necessary for creating complex behaviors.  The script management panel is divided
into three parts:

.. image:: images/ae_script_management_panel_h230.png
   :class: image-boxshadow
   :alt: The script management panel.

* Top-level scripts that serve as the main entry points for execution with Alyvix Robot (MAIN,
  FAIL, and EXIT)
* Sections, which are user-defined subroutines that can be used inside other scripts
* Maps, which are definable iterations over multiple elements from Designer, and which can also be
  used inside other scripts

From this panel you can:

* Click on a script's name to show its contents in the
  :ref:`scripting panel <alyvix_editor_scripting_panel_top>`
* **Add** a new Section or Map element (see below) with the :nobutton:`ADD` action
* **Delete** an existing section or map element with the :gbutton:`REMOVE` action
* Use the |bar-icon| icon to drag a section or map element and drop it in the currently opened
  script in the scripting panel



.. _alyvix_editor_interface_top_level_scripts:

=================
Top level Scripts
=================

The following scripts are predefined and are executed by Alyvix Robot at the appropriate time:

.. rst-class:: bignums-xl

#. **Main:**  The principal script that is executed when Alyvix Robot is invoked via the
   |runblue| button
#. **Fail:**  A script that is executed if one of the test case objects in the Main script having
   the :guilabel:`Break` flag *unset* times out
#. **Exit:**  A separate script that is executed if one of the test case objects in the Main
   script having the :guilabel:`Break` flag *set* times out, allowing you for instance to kill a
   process like Chrome automatically



.. _alyvix_editor_interface_sections:

========
Sections
========

Sections are sub-scripts (subroutines) that can be called one or more times by name from other
scripts or subscripts.  This can greatly help improve the readability of scripts, especially when
they become very long.

When you insert or replace a test case object with a section in the scripting panel, the color
will become dark green to indicate it is a section.

.. note::

   You cannot use a section as the condition in an |if-true| or |if-false| expression,
   although you can use it as the argument of a conditional or a |for| expression.

.. tip::

   You may find it useful to explicitly mark sections and maps using their names, to avoid
   potentially confusing them with test case object names, e.g.:  ``logout_section`` or
   ``download_map``.



.. _alyvix_editor_interface_maps:

=================
The Map Interface
=================

*Maps* let you insert a series of values into text fields, for instance to enter a user name in
one field and a password in another.

You can add a new map by clicking on the :nobutton:`ADD` button next to **MAPS** in the script
management panel.  You should then change the name of the map to something that helps you easily
remember its purpose.

The first step after creating a map is to define the set of keys and values that can be
inserted.  The map interface is shown here, with the available actions listed below:

.. image:: images/ae_basic_map_example.png
   :class: image-boxshadow
   :alt: The Map interface.

.. todo::

   * CC:  Be sure to link to :ref:`Strings <alyvix_designer_options_strings_functions>` when ready
   * CC:  **FOR** MapMMM **RUN** *TestCaseObject* --- from 1 to #NumRows in MapMMM
   * CC:  Rows are automatically sorted alphabetically by first column
   * CC:  Scrape must match the text in the first column (column #0)
   * CC:  Link to or describe the {1} {2} {bla} {bla.extract} and {bla.text} features
   * CC:  Link to the Designer options section for Text
   * CC+FM:  Waiting for mapping to be fixed
   * FM:  No undo if you delete a row or column?
   * FM:  Can't delete an internal column?

* :wbutton:`ADD ROW` --- Add a new row to the bottom of the table
* :nobutton:`ADD COLUMN` --- Add a new column to the right of the table
* |times-icon| --- Delete a row or the rightmost column


.. todo::

   * FM:  Assume the loop is over a single row, from leftmost to rightmost
   * FM:  What is for-loop behavior when there is more than 1 row?  What is it used for, table data?
   * FM:  How are the values used?  Inserted as parameters to a script?  What are the inseration
     and ordering mechanisms?
   * CC+FM:  How do you make the connection between *map* in Designer and the map section in
     Editor?  **A:  Try it out, but there is a bug ATM that keeps it from populating.**
   * CC:  Eventually link to the page that describes how looping is done (if it's not too large,
     then just put the explanation here)
