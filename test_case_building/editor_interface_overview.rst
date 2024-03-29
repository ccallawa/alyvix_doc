:author: Charles Callaway
:date: 07-01-2020
:modified: 21-09-2020
:tags: editor, gui, overview
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_editor_interface_top:

**************************
Editor: Interface Overview
**************************

Alyvix Editor lets you visually create, edit and run complex scripts allowing Alyvix to interact
with your applications just like a human user would.  Each
:iconlink:`gloss|script|../glossary.html#glossary-test-case-script`
consists of multiple test case objects, organized as
:ref:`sequential, conditional and loop commands <alyvix_editor_scripting_node_expressions>`,
along with :ref:`Sections <alyvix_editor_interface_sections>`
and :ref:`Maps <alyvix_editor_interface_maps>`.

The Editor interface includes the Alyvix :ref:`Selector <alyvix_selector_interface_top>`
and :ref:`Designer <alyvix_designer_interface_overview>` modules as collapsible panels,
which lets you easily inspect and choose test case objects to include when building your scripts.

To :ref:`run Alyvix Editor from the command prompt <test_case_building_editor_launch>`,
use the following command:

.. code-block:: doscon

   C:\Alyvix\testcases> alyvix_editor -f <alyvix-file-name>

This loads the Editor interface, whose layout has the following elements:

.. image:: images/ae_full_interface_numbered.png
   :class: image-boxshadow image-very-large zoomable-image
   :alt: Alyvix Editor with Designer and Selector.
   :target: ../_static/targets/ae_full_interface.png

.. rst-class:: bignums

#. The Editor panel, consisting of the
   :ref:`Script Management panel <alyvix_editor_script_mgmt_top>` (left)
   and the :ref:`Scripting panel <alyvix_editor_scripting_panel_top>` (right)
#. The :ref:`Selector <alyvix_selector_interface_top>` pane, containing
   :iconlink:`gloss|test case objects|../glossary.html#glossary-test-case-object`
   that can be added to the Scripting panel
#. The :ref:`Designer <alyvix_designer_interface_overview>` pane, which shows the details of
   the currently selected test case object



.. _alyvix_editor_interface_features:

========================
Editor-Specific Features
========================

The principle interface elements specific to Alyvix Editor are:

.. image:: images/ae_main_screen_numbered.png
   :class: image-boxshadow image-very-large zoomable-image
   :alt: The Alyvix Editor interface.
   :width: 80%
   :target: ../_static/targets/ae_main_screen.png

.. rst-class:: bignums

#. The :ref:`test case menu <alyvix_editor_interface_menu>` (described below), containing actions
   for Alyvix Editor and the current :iconlink:`gloss|test case|../glossary.html#glossary-test-case`
#. The main :ref:`Script Management panel <alyvix_editor_script_mgmt_top>`, used to select
   the principal scripts to be edited
#. The :ref:`Sections <alyvix_editor_interface_sections>` list, containing user-defined
   scripts (:iconlink:`gloss|sections|../glossary.html#glossary-section`)
   that can be used as subroutines within any of the principal scripts
#. The :ref:`Maps <alyvix_editor_interface_maps>` list, containing user-defined
   :iconlink:`gloss|maps|../glossary.html#glossary-map` (consisting of keys and one or more
   values for each key) that can be used either by a script via
   :ref:`looping <alyvix_editor_scripting_node_expressions>`, or to insert values in a
   :ref:`String <alyvix_designer_options_strings_top>` field.
#. The scripting mode selector, containing the :guilabel:`Script` tab to
   :ref:`display the currently selected script or map <alyvix_editor_scripting_panel_top>`,
   the :guilabel:`Monitor` tab to
   :ref:`show the screen capture <alyvix_editor_interface_monitor>` of Selector's current test case
   object, and the :guilabel:`Console` tab to
   :ref:`show the output along with any potential failure causes<alyvix_editor_run_script>`
   after running the test case script from within Alyvix Editor
#. The :ref:`scripting panel <alyvix_editor_scripting_panel_top>`, containing individual
   scripting nodes and the logic connecting them
#. The script properties and actions that work both for single nodes and subsets of nodes, where
   you can :ref:`enable, disable, run, or remove <alyvix_editor_scripting_node_actions>` the
   scripted elements that have been placed in the scripting panel
#. Panel resizing controls, allowing you to resize, minimize, or restore the three peripheral
   panels



.. _alyvix_editor_interface_menu:

==================
The Test Case Menu
==================

The following actions are available from Editor's menu:

* |runblue| --- Run the current script displayed in the scripting panel (see below)
* **New** --- Throw away the current test case, replacing it with an empty one
* **Open** --- Replace the current test case with a new one chosen from the file dialog
* **Save** --- Save the current test case with its existing filename, overwriting the previous version
* **Save As** --- Create a copy of the current test case under a new file name
* **Exit** --- Close Alyvix Editor



.. _alyvix_editor_interface_monitor:

===============
The Monitor Tab
===============

When you just need to quickly look at the positions of components in a test case object
without making any changes, the fastest way isn't to return to editing the test case object
in Designer.  Instead you can use the monitor tab to see the screen capture for the currently
selected test case object.

.. image:: images/ae_monitor_tab_sized.png
   :class: image-boxshadow zoomable-image
   :alt: An example Monitor tab screenshot

The monitor tab displays a read-only, full-size, instantly available copy of the screen grab
for the test case object currently opened in the Designer panel.



.. _alyvix_editor_run_script:

=========================================
Launching Alyvix Robot from Alyvix Editor
=========================================

The script of the currently loaded  test case can be run directly in Editor by pressing
the |runblue| button at the top left.  The default starting point is the :nobutton:`MAIN` script
in the :ref:`script management panel <alyvix_editor_script_mgmt_top>` (you can
:ref:`use the debugging methods <alyvix_editor_interface_debug>` available in Alyvix Editor to
change this starting point).

When run, Editor will be minimized until the scripted interaction has completed, after which
the Editor window will return, and the output will appear in the Console tab at the top of the
:ref:`scripting panel <alyvix_editor_scripting_panel_top>`:

.. image:: ../getting_started/images/ae_console_result.png
   :class: image-boxshadow image-very-large zoomable-image
   :alt: The results of running the script in Alyvix Editor

The structure of the output is the same regardless of whether the test case is started in Editor or
run in the command prompt.  The effect of the *Break* and *Measure* flags are described in detail in
the :ref:`Test Execution <alyvix_robot_result_cli>` section.

In addition, if a failure was caused by a simple sequential scripting node, then the
annotated screenshot describing the failure will be displayed below the output in the
Console tab:

.. image:: images/ae_console_tab_error.png
   :class: image-boxshadow image-very-large zoomable-image
   :alt: A matching error displayed in the console tab

The annotation indicates the position, size and group of the first component that could
not be matched during execution.  In the PowerPoint example shown above, the Paste icon
was marked as a subselection in the first group without an enlarged region of interest,
so reducing the window horizontally means the Paste icon no longer fell within that region.
The exclamation mark inside the red square representing the color of the first group
indicates where Alyvix expected to find the Paste icon.

.. note::

   Note that currently
   :ref:`arguments such as a private key and the verbosity level <alyvix_robot_cli_launch>`
   for Alyvix Robot cannot be set within Editor.
