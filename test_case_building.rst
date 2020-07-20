:author: Charles Callaway
:date: 05-12-2019
:modified: 26-05-2020
:tags: designer, test cases
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_building_top:

##################
Test Case Building
##################

When you build a :iconlink:`gloss|test case|glossary.html#glossary-test-case`, you're creating
a set of visual templates that can be matched against your app interfaces in real time, allowing
Alyvix to interact with those interfaces just like a person would.


.. todo::

   * Building TCs is the most important Alyvix task
   * Building TCs is done frequently
   * So it's worth investing time to learn it
   * TCs are made up of one or more TCOs (moving the glossary link up to here)


There are three main tools for building test cases:

.. rst-class:: bignums-xl

#. **Alyvix Designer:**  Define individual
   :iconlink:`gloss|test case objects|glossary.html#glossary-test-case-object`
   to be dynamically matched against the visual components of your app's interface, and assign
   GUI actions that are carried out when those matches are detected
#. **Alyvix Selector:**  Easily manipulate (inspect, copy, edit, delete) large numbers of test
   case objects created with Designer, as well as view, filter and sort their properties
#. **Alyvix Editor:**  Create scripts using test case objects (as sequential execution units,
   conditionals, and loops) to interact with any app according to complex behaviors you define

For most use cases, Alyvix Editor (which includes Designer and Selector) is all you'll need.
But if required, Designer and Selector can also be run as separate modules.

Once you've built a test case, you can let it interact with your chosen app either by using
:ref:`Alyvix Robot <test_case_execution_top>`, or testing it directly within Editor.

The :ref:`Test Case Data Format <test_case_data_format_top>` page provides technical details on how
Alyvix test case files are organized and what they contain, while the
:ref:`Getting Started <getting_started_top>` and :ref:`Videos and Tutorials <video_tutorials_top>`
sections include detailed mini-tutorials and topic-based videos on how to use Alyvix Editor and Robot.

All of these applications can be launched from the Windows Command Prompt or PowerShell.
Note that they inherit the permissions of the shell they were launched from.

|



.. _test_case_building_designer:

.. topic:: Alyvix Designer

   Alyvix Designer lets you select graphic :iconlink:`gloss|components|glossary.html#glossary-component`
   on a captured screen to use as test case objects, whether they're images, rectangles, or text.
   You can then define triggers and actions to apply when those templates are recognized later
   in a live interaction with an application.

Designer will save the set of templates, called the
:iconlink:`gloss|component tree|glossary.html#glossary-component-tree` as a single test case
object, which you can then use as a building block to compose more complicated behaviors with
:iconlink:`gloss|scripts|glossary.html#glossary-test-case-script` using Alyvix Editor.

.. _test_case_building_designer_launch:

The following sections of the guide present further information on Alyvix Designer:

* The :ref:`Designer Interface Overview <alyvix_designer_interface_overview>` page provides a
  high-level overview and describes the general layout of the interface
* The :ref:`Component Tree <alyvix_designer_component_tree_top>` page describes the specific
  test case object types available, including what they can do and how to interact with them
* You can find more detailed information about the available options for test case objects and
  components on the :ref:`Interface Options <alyvix_designer_options>` page

Although it is typically run together with Alyvix Editor, Designer can be run in standalone
mode as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_designer

with the following command line options:

+---------------+-------+----------+----------------------------------------------+
| Option        | Alias | Argument | Description                                  |
+---------------+-------+----------+----------------------------------------------+
| -\ -delay     | -d    | *<n>*    | Wait *n* seconds before grabbing the screen, |
|               |       |          | giving you time to move windows around       |
+---------------+-------+----------+----------------------------------------------+
| -\ -filename  | -f    | *<name>* | Supply the file name with no extension       |
+---------------+-------+----------+----------------------------------------------+
| -\ -object    | -o    | *<name>* | Supply the Object name                       |
+---------------+-------+----------+----------------------------------------------+
| -\ -verbose   | -v    | *<n>*    | Set the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)      |
+---------------+-------+----------+----------------------------------------------+

|



.. _test_case_building_selector:

.. topic:: Alyvix Selector

   Alyvix Selector is used to :ref:`centralize the management <alyvix_selector_interface_top>`
   of all of your test case objects, such as exporting them to other Alyvix files.  It also
   provides options to view, copy, edit and delete test cases objects.

.. _test_case_building_selector_launch:

Selector is organized as a set of tabbed panels representing one or more test case files, and
a list of test case objects within each tab.  This allows you to quickly switch between them and
filter, search and edit within a single file, or copy test case objects across opened test case
files.

Although it is typically run together with Alyvix Editor, Selector can be run in standalone
mode as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_selector

with the following command line options:

+---------------+-------+----------+----------------------------------------------+
| Option        | Alias | Argument | Description                                  |
+---------------+-------+----------+----------------------------------------------+
| -\ -filename  | -f    | *<name>* | Supply the file name with no extension       |
+---------------+-------+----------+----------------------------------------------+
| -\ -verbose   | -v    | *<n>*    | Set the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)      |
+---------------+-------+----------+----------------------------------------------+

|



.. _test_case_building_editor:

.. topic:: Alyvix Editor

   Alyvix Editor helps you create scripts using the individual test case objects in a single
   test case file, and allows you to create more complex interactions compared to using
   Designer alone.

.. _test_case_building_editor_launch:

The following sections of the guide present further information about Alyvix Editor:

* The :ref:`Editor Interface Overview <alyvix_editor_interface_top>` page describes the layout of
  the panels and how to use the interface controls
* The :ref:`Scripting Management <alyvix_editor_script_mgmt_top>` page shows you how to manipulate
  (view, copy, edit, delete) the scripts and scripting components you have created
* The :ref:`Scripting Panel <alyvix_editor_scripting_panel_top>` page explains how to create
  scripted interactions between existing test cases

Alyvix Editor can be run as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_editor

with the following command line options:

+---------------+-------+----------+-----------------------------------------------+
| Option        | Alias | Argument | Description                                   |
+---------------+-------+----------+-----------------------------------------------+
| -\ -filename  | -f    | *<name>* | The test case file name (with no extension)   |
+---------------+-------+----------+-----------------------------------------------+
| -\ -verbose   | -v    | *<n>*    | Sets the verbosity level for debugging output |
|               |       |          | ranging from **0** (min) to **2** (max)       |
+---------------+-------+----------+-----------------------------------------------+




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
