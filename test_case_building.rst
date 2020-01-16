:author: Charles Callaway
:date: 05-12-2019
:modified: 15-01-2020
:tags: designer, test cases
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_building_top:

##################
Test Case Building
##################

When you build a test case, you're creating a visual template that can be matched in real time
in a variety of ways that you define against your future computer screens/interfaces.  There
are three main tools for building test cases:

.. rst-class:: bignums-xl

#. **Alyvix Designer:**  Define individual test cases consisting of matchable regions that can be
   used by Alyvix Robot to scan for and act on visual elements of an interface
#. **Alyvix Selector:**  Easily manipulate (inspect, copy, edit, delete) those test cases as
   objects and view, filter and sort their properties
#. **Alyvix Editor:**  Script test cases (run, conditionals, and loops) defined in Alyvix Designer
   and pulled in via Alyvix Selector

Alyvix gives you two basic approaches to building test cases:

* Build up a library of test cases with Designer and Selector
  (:ref:`launching them <test_case_building_designer_launch>` individually from the command
  prompt), and then later integrate them with Alyvix Editor.
* Use Alyvix Editor from the beginning, which unifies Designer and Selector into a single
  interface, and lets you script test cases from the start.

The :ref:`Test Case Data Format <test_case_data_format_top>` page provides technical details on how
Alyvix object files are organized and what they contain.

Finally, the :ref:`Getting Started <getting_started_top>` section includes detailed mini-tutorials
on how to use Alyvix Designer and Editor if you haven't used them before.



.. _test_case_building_launch:
.. topic:: Launching Alyvix Editor, Designer and Selector

   All three of these applications can be launched from the Windows Command Prompt or PowerShell.
   They inherit the permissions of the shell they were launched from.



.. _test_case_building_editor:

.. topic:: Alyvix Editor

   Alyvix Editor helps you create scripted connections between individual test case objects,
   allowing you to create more complicated interactions compared to using Designer alone.

The following sections of the Alyvix Guide present further information about Alyvix Editor:

* The :ref:`Interface Overview <alyvix_editor_interface_top>` page describes the layout of
  the panels and the interface controls.
* The :ref:`Scripting Panel <alyvix_editor_scripting_panel_top>` page lets you create the
  scripted interactions between existing test cases.
* The :ref:`Scripting Management <alyvix_editor_script_mgmt_top>` page lets you manipulate
  (view, copy, edit, delete) the scripts and scripting components you have created.

.. _test_case_building_editor_launch:

Alyvix Editor can be run as follows if the Alyvix file path (e.g.,
:file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\`)
is included in your :guilabel:`Path` environment variable:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> python alyvix_ide.py

The following command line options are available for Editor:

+---------------+-------+----------+----------------------------------------------+
| Option        | Alias | Argument | Description                                  |
+---------------+-------+----------+----------------------------------------------+
| \-\\-filename | -f    | *<name>* | Supply the file name with no extension       |
+---------------+-------+----------+----------------------------------------------+
| \-\\-verbose  | -v    | *<n>*    | Set the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)      |
+---------------+-------+----------+----------------------------------------------+



.. _test_case_building_designer:
.. topic:: Alyvix Designer

   Alyvix Designer lets you select patterns on a copy of the screen, whether they're images,
   rectangles, or text.  You can then define triggers for actions when those patterns are
   recognized later in a simulated interaction with an application.

Designer will save the set of patterns as a single :ref:`test case <glossary_test_case>`, which
you can then use as building blocks to compose more complicated objects and scripts using Alyvix
Editor, and to measure the performance of executed test cases with
:ref:`Alyvix Robot <test_case_execution_top>`.

The following sections of the Alyvix Guide present further information on Alyvix Designer:

* The :ref:`Interface Overview <alyvix_designer_interface_overview>` page provides a high-level
  overview and describes the general layout of the interface.
* To learn more about interacting with specific visual elements and what they can do, see the
  :ref:`Component Tree <alyvix_designer_component_tree>` page.
* You can find more detailed information about the available options for test cases and components
  on the :ref:`Interface Options <alyvix_designer_options>` page.

.. _test_case_building_designer_launch:

Alyvix Designer can be run as follows if the Alyvix file path (e.g.,
:file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\`)
is included in your :guilabel:`Path` environment variable:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> python alyvix_designer.py

The following command line options are available for Designer:

+---------------+-------+----------+----------------------------------------------+
| Option        | Alias | Argument | Description                                  |
+---------------+-------+----------+----------------------------------------------+
| \-\\-delay    | -d    | *<n>*    | Wait *n* seconds before grabbing the screen, |
|               |       |          | giving you time to move windows around       |
+---------------+-------+----------+----------------------------------------------+
| \-\\-filename | -f    | *<name>* | Supply the file name with no extension       |
+---------------+-------+----------+----------------------------------------------+
| \-\\-object   | -o    | *<name>* | Supply the Object name                       |
+---------------+-------+----------+----------------------------------------------+
| \-\\-verbose  | -v    | *<n>*    | Set the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)      |
+---------------+-------+----------+----------------------------------------------+



.. _test_case_building_selector:
.. topic:: Alyvix Selector

   Alyvix Selector is used to centralize the management of all of your test cases which may
   be distributed across multiple files.  It provides options to view, copy, edit and delete
   test cases objects.

Selector is organized as a list of test case objects, and with each Alyvix file as a tab
that allows you to quickly switch between them and filter, search and edit either within
a single file or across all opened files.

.. _test_case_building_selector_launch:

Alyvix Selector can be run as follows if the Alyvix file path (e.g.,
:file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\`)
is included in your :guilabel:`Path` environment variable:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> python alyvix_selector.py

The following command line options are available for Selector:

+---------------+-------+----------+----------------------------------------------+
| Option        | Alias | Argument | Description                                  |
+---------------+-------+----------+----------------------------------------------+
| \-\\-filename | -f    | *<name>* | Supply the file name with no extension       |
+---------------+-------+----------+----------------------------------------------+
| \-\\-verbose  | -v    | *<n>*    | Set the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)      |
+---------------+-------+----------+----------------------------------------------+




.. toctree::
   :maxdepth: 2
   :name: toc_designer
   :hidden:

   test_case_building/designer_interface_overview.rst
   test_case_building/designer_options.rst
   test_case_building/designer_component_tree.rst
   test_case_building/selector_overview.rst
   test_case_building/editor_overview.rst
   test_case_building/editor_script_mgmt.rst
   test_case_building/editor_scripting_panel.rst