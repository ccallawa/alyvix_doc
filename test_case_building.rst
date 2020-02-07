:author: Charles Callaway
:date: 05-12-2019
:modified: 29-01-2020
:tags: designer, test cases
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_building_top:

##################
Test Case Building
##################

When you build a test case, you're creating a set of visual templates that can be matched against
and interact with your app interfaces in real time, just like a person would.  There are three main
tools for building test cases:

.. rst-class:: bignums-xl

#. **Alyvix Designer:**  Define individual *test case objects* to be dynamically matched with
   visual components of your app's interface, and assign interactive actions that are carried
   out when they are detected
#. **Alyvix Selector:**  Easily manipulate (inspect, copy, edit, delete) test case objects created
   with Designer, as well as view, filter and sort their properties
#. **Alyvix Editor:**  Create scripts using test case objects (execution, conditionals, and loops)
   to interact with any app according to complex behaviors you can define

For most use cases, Alyvix Editor (which includes Designer and Selector) is all that you will
need.  Both Designer and Selector can also be run as separate modules.

Once you have built a test case, you can let it interact with your chosen app by using
:ref:`Alyvix Robot <test_case_execution_top>`.

The :ref:`Test Case Data Format <test_case_data_format_top>` page provides technical details on how
Alyvix test case files are organized and what they contain, while the
:ref:`Getting Started <getting_started_top>`
section includes detailed mini-tutorials on how to use Alyvix Editor.



.. _test_case_building_launch:
.. topic:: Launching Alyvix Editor, Designer and Selector

   All three of these applications can be launched from the Windows Command Prompt or PowerShell.
   They inherit the permissions of the shell they were launched from.



.. _test_case_building_editor:

.. topic:: Alyvix Editor

   Alyvix Editor helps you create scripted connections between the individual test case objects
   in a single test file, and allows you to create more complex interactions compared to using
   Designer alone.

.. _test_case_building_editor_launch:

The following sections of the Alyvix Guide present further information about Alyvix Editor:

* The :ref:`Editor Interface Overview <alyvix_editor_interface_top>` page describes the layout of
  the panels and how to use the interface controls
* The :ref:`Scripting Panel <alyvix_editor_scripting_panel_top>` page explains how to create
  scripted interactions between existing test cases
* The :ref:`Scripting Management <alyvix_editor_script_mgmt_top>` page shows you how to manipulate
  (view, copy, edit, delete) the scripts and scripting components you have created

Alyvix Editor can be run as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_editor

with the following command line options:

+---------------+-------+----------+-----------------------------------------------+
| Option        | Alias | Argument | Description                                   |
+---------------+-------+----------+-----------------------------------------------+
| \-\\-filename | -f    | *<name>* | The test case file name (with no extension)   |
+---------------+-------+----------+-----------------------------------------------+
| \-\\-verbose  | -v    | *<n>*    | Sets the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)       |
+---------------+-------+----------+-----------------------------------------------+



.. _test_case_building_designer:
.. topic:: Alyvix Designer

   Alyvix Designer is used to select graphic components on a screen capture to use as test case
   objects, whether they're images, rectangles, or text.  You can then define triggers and actions
   to apply when those patterns are recognized later in a simulated interaction with an application.

Designer will save the set of patterns as a single **test case object**
:rawhtml:`<a href="glossary.html#glossary-test-case-object"><i class="fa fa-tiny fa-question-circle"></i></a>`,
which you can then use as a building block to compose more complicated objects and scripts using
Alyvix Editor.

.. _test_case_building_designer_launch:

The following sections of the Alyvix Guide present further information on Alyvix Designer:

* The :ref:`Designer Interface Overview <alyvix_designer_interface_overview>` page provides a
  high-level overview and describes the general layout of the interface
* The :ref:`Component Tree <alyvix_designer_component_tree_top>` page describes the specific
  test case object types available, including what they can do and how to interact with them
* You can find more detailed information about the available options for test case objects and
  components on the :ref:`Interface Options <alyvix_designer_options>` page

Alyvix Designer can be run as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_designer

with the following command line options:

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

   Alyvix Selector is used to centralize the management of all of your test case objects, which may
   be exported across multiple test case files.  It provides options to view, copy, edit and
   delete those test cases objects.

.. _test_case_building_selector_launch:

Selector is organized as a set of tabbed panels representing one or more test case files, and
a list of test case objects within each tab.  This allows you to quickly switch between them and
filter, search and edit within a single file, or copy test case objects across opened test case
files.

Alyvix Selector can be run as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_selector

with the following command line options:

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

   test_case_building/editor_interface_overview.rst
   test_case_building/editor_script_mgmt.rst
   test_case_building/editor_scripting_panel.rst
   test_case_building/designer_interface_overview.rst
   test_case_building/designer_options.rst
   test_case_building/designer_component_tree.rst
   test_case_building/selector_interface_overview.rst
