:author: Charles Callaway
:date: 07-01-2020
:modified: 19-02-2020
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
necessary for creating complex behaviors.  The script management panel is divided into three parts:

.. image:: images/ae_script_management_panel_h230.png
   :class: image-boxshadow
   :alt: The script management panel.

* **Top-level scripts** that serve as the main entry points for execution with Alyvix Robot (MAIN,
  FAIL, and EXIT)
* **Sections**, which are user-defined subroutines that can be used inside other scripts
* **Maps**, which are user-defined tables of keys and values that can be used to *(a)* take a text
  string scraped from the screen and map it to another string, or *(b)* loop over a test case
  object (using the :ref:`FOR <alyvix_editor_scripting_node_expressions>` expression) for as many
  rows as there are in the table

From the script management panel you can:

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

#. **Main:**  The principal script that is invoked when launching a test case from either Alyvix
   Editor (via the |runblue| button) or Robot
#. **Fail:**  A script that is executed if one of the test case objects in the Main script having
   the :guilabel:`Break` flag *unset* times out
#. **Exit:**  A separate script that is always run once the Main script terminates, allowing you
   to restore your machine to its prior state (for instance, to shut down a browser that was
   launched as part of a test case)



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

The *Maps* feature lets you create a table of strings that you can use to *(a)*
:ref:`map a string <alyvix_designer_options_strings_map_extract>` scraped from an application
(the *key*) to extract another string (the *value*), or *(b)* loop over
a :ref:`test case object or a section <alyvix_editor_scripting_node_expressions>`, once for
each row (top to bottom) in the map.

.. note::

   Rows are automatically sorted alphabetically by the key, so if order is important, it should
   be reflected in how the keys are named.

You can add a new map by clicking on the :nobutton:`ADD` button next to **MAPS** in the script
management panel.  You should then change the name of the map from the default to something
that helps you easily remember what it's used for.

The first step after creating a map is to define the set of keys and values that can be
inserted.  The map interface is shown here, with the available actions listed below:

.. image:: images/ae_basic_map_example.png
   :class: image-boxshadow
   :alt: The Map interface.

* :wbutton:`ADD ROW` --- Add a new row to the bottom of the table
* :nobutton:`ADD COLUMN` --- Add a new column to the right of the table
* |times-icon| --- Delete a row or the rightmost column
