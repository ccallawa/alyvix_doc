:author: Charles Callaway
:date: 04-12-2019
:modified: 21-09-2020
:tags: concept, glossary
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _glossary_top:

########
Glossary
########

.. todo::

   * CC:  Terminology:  scripting node, scripting element, script, map, section, scripting mode

.. table::
   :class: table-body-no-borders

   +----------------------------------+--------------------------------------------------------------------------------------+
   | **Term**                         | **Description**                                                                      |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_autocontour:        | *Autocontour* is an Alyvix feature that :ref:`automatically detects the boundaries   |
   |                                  | <alyvix_designer_region_bounding>` of an onscreen object and creates a selection     |
   | :deflabel:`Autocontour`          | around it.  It can greatly speed up your interactions with Alyvix Designer, as it's  |
   |                                  | much quicker to *right-click* on an icon than to draw a box around it.  You can      |
   |                                  | press the :kbd:`Space` key when in capture mode to see candidate automatic           |
   |                                  | selections (press  :kbd:`Space` a second time to return to normal capture mode).     |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_component:          | A *component* is a                                                                   |
   |                                  | :ref:`visual element <alyvix_designer_region_bounding>` on the screen capture that   |
   | :deflabel:`Component`            | has a specific type (image, rect, or text) and is either the *principle component*   |
   |                                  | of a group or a  *subcomponent*.  A component represents the link between that       |
   |                                  | visual element and a logical element that Alyvix can                                 |
   |                                  | :ref:`logically interact with <alyvix_designer_component_tree_top>`.                 |
   |                                  | Unless moved, components are positioned in the component tree according to the       |
   |                                  | order they were created.                                                             |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_component_tree:     | The *component tree* reflects the                                                    |
   |                                  | :ref:`hierarchy of components <alyvix_designer_component_tree_structure>`            |
   | :deflabel:`Component Tree`       | in a given test case object in Designer.                                             |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_group:              | A *group* in a test case object                                                      |
   |                                  | :ref:`consists of <alyvix_designer_component_tree_structure>`                        |
   | :deflabel:`Group`                | a main component and up to 4 subcomponents that during execution must  all match     |
   |                                  | against the current screen in order for their actions to be carried out.             |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_map:                | A *map* is a user-defined table of strings, consisting of a column of                |
   |                                  | keys, and one or  more columns of values.  Maps can be used both for                 |
   | :deflabel:`Map`                  | :ref:`transforming an extracted value <alyvix_designer_options_strings_map_extract>` |
   |                                  | and for :ref:`looping over a test case object <alyvix_editor_interface_maps>`        |
   |                                  | with the keys as parameters.                                                         |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_region_of_interest: | A *region of interest* (RoI) is the                                                  |
   |                                  | :ref:`area around a subselection <alyvix_designer_region_bounding>` in which that    |
   |                                  | subselection must appear during execution for a match to be valid.  It is especially |
   | :deflabel:`Region of Interest`   | useful when the selection is at the edge of a resizeable region such as a window.    |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_root:               | The *root element* of a test case object holds the captured screen which serves as   |
   |                                  | the image source for creating components.  It is the root of the component tree, and |
   | :deflabel:`Root`                 | all groups and their subcomponents are dependent on it.                              |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_test_case_script:   | A *test case script* is a sequence of instructions (each consisting of one or more   |
   |                                  | test case objects) describing, during the execution phase:                           |
   | :deflabel:`Script`               |                                                                                      |
   |                                  | * The order to :ref:`compare test case objects <alyvix_editor_scripting_panel_top>`  |
   |                                  |   against the graphical interface of the application being run                       |
   |                                  | * The :ref:`script expression mode <alyvix_editor_scripting_node_expressions>` for   |
   |                                  |   the node (run, conditional, or loop)                                               |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_section:            | A *section* is a :ref:`user-defined subscript <alyvix_editor_interface_sections>`    |
   |                                  | that can be called by one or more of the *main*, *fail* or *exit* scripts.  Sections |
   | :deflabel:`Section`              | are helpful whenever there are repetitive sequences of actions to carry out.         |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_selection:          | A *selection* is a rectangular area within a screen capture that serves as the       |
   |                                  | principal anchor for an entire group.  Unlike a *subselection*, a *selection* has no |
   | :deflabel:`Selection`            | Region of Interest -- it can match anywhere on the screen.  For further information, |
   |                                  | see the :ref:`Designer Interface Overview <alyvix_designer_region_bounding>`.        |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_subselection:       | A *subselection* is a                                                                |
   |                                  | :ref:`rectangular area within a screen capture <alyvix_designer_region_bounding>`    |
   | :deflabel:`Subselection`         | that has an associated Region of Interest and is relative to a Selection.  During    |
   |                                  | execution, the RoI is positioned relative to the location of the detected            |
   |                                  | *selection*, and the *subselection* must match an area within that RoI.              |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_test_case:          | A *test case* is the sum total of the screen capture, all test case objects          |
   |                                  | (containing the component tree and its components), and any mappings and scripts     |
   | :deflabel:`Test Case`            | using those objects.  It is                                                          |
   |                                  | :ref:`saved in a file with an <test_case_data_format_top>` :file:`.alyvix`           |
   |                                  | extension, and can be loaded by Alyvix applications.                                 |
   +----------------------------------+--------------------------------------------------------------------------------------+
   | .. _glossary_test_case_object:   | A *test case object* is a                                                            |
   |                                  | :ref:`named object within a test case <alyvix_selector_interface_top>`, consisting   |
   | :deflabel:`Test Case Object`     | of a screen capture and all the components within the component tree based on that   |
   |                                  | screen capture.  A single test case can contain multiple test case objects, and all  |
   |                                  | test case objects can be used for creating scripts within their test case.           |
   +----------------------------------+--------------------------------------------------------------------------------------+

|
|
|
|
|
|
|



.. .. toctree::
      :maxdepth: 2
      :name: toc_designer
      :hidden:
