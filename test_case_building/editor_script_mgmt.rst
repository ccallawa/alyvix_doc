:author: Charles Callaway
:date: 07-01-2020
:modified: 31-01-2020
:tags: editor, script, management
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_editor_script_mgmt_top:

****************************
Editor: Scripting Management
****************************

The script management panel organizes and provides quick access to the scripts and scripting
components needed to create complex scripted behaviors.  The script management panel is divided
into three parts:

.. image:: images/ae_script_management_panel_h230.png
   :class: image-boxshadow
   :alt: The script management panel.

* Top-level scripts that serve as the main entry points for execution with Alyvix Robot
* Sections, which are user-defined subroutines that can be used in top-level scripts
* Maps, which are definable iterations over multiple elements from Designer, and that can
  be used in both top-level scripts and sections

From this panel you can:

* Click on a script's name to show its contents in the
  :ref:`scripting panel <alyvix_editor_scripting_panel_top>`
* **Add** a new section or map element with the :nobutton:`ADD` action
* **Delete** an existing section or map element with the :gbutton:`REMOVE` action
* Use the |bar-icon| icon to drag a section or map element and drop it in the opened script
  in the scripting panel



.. _alyvix_editor_interface_top_level_scripts:

=================
Top level Scripts
=================

The following scripts are predefined and are executed by Alyvix Robot at the appropriate time:

.. rst-class:: bignums-xl

#. **Main:**  The principal script that is executed when Alyvix Robot is invoked via the
   |runblue| button
#. **Fail:**  A script that is executed if one of the test case objects in the Main script with
   the :guilabel:`Break` flag *unset* times out, for instance a logout script
#. **Exit:**  A separate script that is executed if one of the test case objects in the Main
   script with the :guilabel:`Break` flag *set* times out


.. todo::

   * CC+FM:  It would be helpful to have good examples explaining fail & exit
   * FM:  Are the above reserved keywords?  I.e., you can't define a section or map named
     "main", "fail" or "exit"?  **A: No, they're in a different section in .alyvix.**
   * FM:  Are section and map names subject to the same restrictions of Python identifiers
     as test case object names are?
   * FM:  Editing names in the script management panel is very hard -- it keeps refreshing and
     losing focus frequently (seems to happen whenever the panel is refreshed)
   * FM: Is Undo/Redo (Ctrl-Z/Y) planned for the scripting management panel?



.. _alyvix_editor_interface_sections:

======================
Sections (Subroutines)
======================

Sections are sub-scripts that can be called from top-level scripts, allowing you to improve
their readability when a large number of steps is involved.

When you insert or replace a test case object with a section in the scripting panel, the color
of its box will change from light green to dark green to indicate it is a section.

.. note::

   You cannot use a section to replace the condition in an |if-true| or |if-false| expression,
   although you can use it as the argument of a conditional or a |for| expression.

.. todo::

   * FM:  Can sections call other sections, or can only the top-level scripts call sections?
   * CC:  Can we use |if-true| etc. when they are not introduced up to this point in the page?

.. tip::

   You may find it useful to explicitly mark sections and maps within their names to avoid
   potentially confusing them with test case object names, e.g.:  ``logout_section`` or
   ``download_map``.



.. _alyvix_editor_interface_maps:

=================
The Map Interface
=================

.. todo::

   * CC+FM:  Waiting for mapping to be fixed

* :wbutton:`ADD ROW`
* :nobutton:`ADD COLUMN`
* |times-icon|

.. image:: images/ae_basic_map_example.png
   :class: image-boxshadow
   :alt: The Map interface.

* Cannot remove the ``value1`` column
* Can only be used in the FOR element, dragging it over an existing element will change its type

.. todo::

   * FM:  Assume the loop is over a single row, from leftmost to rightmost
   * FM:  What is for-loop behavior when there is more than 1 row?  What is it used for, table data?
   * FM:  How are the values used?  Inserted as parameters to a script?  What are the inseration
     and ordering mechanisms?
   * FM:  Can remove any row at any time, but only the rightmost column?
   * CC+FM:  How do you make the connection between *map* in Designer and the map section in
     Editor?  **A:  Try it out, but there is a bug ATM that keeps it from populating.**
   * CC:  Eventually link to the page that describes how looping is done (if it's not too large,
     then just put the explanation here)
