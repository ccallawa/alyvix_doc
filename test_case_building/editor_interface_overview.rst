:author: Charles Callaway
:date: 07-01-2020
:modified: 31-01-2020
:tags: editor, gui, overview
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_editor_interface_top:

**************************
Editor: Interface Overview
**************************

Alyvix Editor lets you create and execute complex scripts that can interact with applications.
Each script consists of multiple test case objects, organized as sequential, conditional and loop
commands, along with :ref:`Sections <alyvix_editor_interface_sections>`
and :ref:`Maps <alyvix_editor_interface_maps>`.

The Editor interface includes Alyvix Selector and Designer as collapsible panels, which let
you easily inspect and choose test case objects to include when building a script.

To :ref:`run Alyvix Editor from the command prompt <test_case_building_editor_launch>`,
use the following command:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_editor -f <alyvix-file>

This loads the Editor interface, which has the following elements:

.. image:: images/ae_full_interface_numbered.png
   :class: image-boxshadow
   :alt: Alyvix Editor with Designer and Selector.
   :target: ../_static/targets/ae_full_interface.png

.. rst-class:: bignums

#. The Editor panel, consisting of the
   :ref:`Script Management panel <alyvix_editor_script_mgmt_top>` (left)
   and the :ref:`Scripting panel <alyvix_editor_scripting_panel_top>` (right)
#. The :ref:`Selector <alyvix_selector_interface_top>` pane, where test case objects can be
   dragged from, and then dropped into the scripting panel
#. The :ref:`Designer <alyvix_designer_interface_overview>` pane, which shows the details of
   the currently selected test case object



.. topic:: Editor-Specific Features

   The principle interface elements specific to Alyvix Editor are:

.. image:: images/ae_main_screen_numbered.png
   :class: image-boxshadow
   :alt: The Alyvix Editor interface.
   :width: 80%
   :target: ../_static/targets/ae_main_screen.png

.. rst-class:: bignums

#. The :ref:`test case menu <alyvix_editor_interface_menu>`, described below, containing actions
   for Alyvix Editor and the current test case
#. The main :ref:`scripting management panel <alyvix_editor_script_mgmt_top>`, used to select
   the principal scripts to be edited
#. The :ref:`Sections <alyvix_editor_interface_sections>` list, containing  user-defined
   scripts that can be used as subroutines within any of the principal scripts
#. The :ref:`Maps <alyvix_editor_interface_maps>` list, containing user-defined maps where a
   script can be called multiple times, once for each key in the map that is then passed as an
   argument to the named script
#. The scripting mode selector, containing the :guilabel:`Script` tab to display the currently
   selected script or map, the :guilabel:`Monitor` tab to show the screen capture of Selector's
   current test case object and the :guilabel:`Console` tab to show the output of Alyvix Robot
   after executing the test case script
#. The :ref:`scripting panel <alyvix_editor_scripting_panel_top>`, which contains the individual
   scripting elements, placed there using Selector
#. The script properties and actions, where you can enable, disable or remove individual script
   elements that have been dropped into the scripting panel
#. Panel resizing controls allowing you to resize, minimize, or restore the three peripheral
   panels



.. _alyvix_editor_interface_menu:

==================
The Test Case Menu
==================

The following actions are available from Alyvix Editor's menu:

* |runblue| --- Execute the current script displayed in the scripting panel
* **New** --- Throw away the current test case, replacing it with an empty one.
* **Open** --- Replace the current test case with a new one chosen from the file dialog.
* **Save** --- Save the current test case with its existing filename, overwriting the previous version.
* **Save As** --- Create a copy of the current test case under a new file name.
* **Exit** --- Close Alyvix Editor.
