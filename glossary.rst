:author: Charles Callaway
:date: 04-12-2019
:modified: 04-02-2019
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

   * CC:  Terminology:  scripting node, scripting element, antecedent? consequent?

.. _glossary_autocontour:

:Autocontour:  *Autocontour*
   is an Alyvix feature that automatically detects the boundaries of an onscreen object and
   creates a selection around it.  It can greatly speed up your interactions with Alyvix Designer,
   as it's much quicker to *right-click* on an icon than to draw a box around it.  You can press
   the :kbd:`Space` key when in capture mode to see candidate automatic selections (press
   :kbd:`Space` a second time to return to capture mode).

.. _glossary_component:

:Component:  A *component* is a visual element on the screen capture that has a specific type
   (image, rect, or text) and is either the *principle component* of a group or a *subcomponent*.
   Components are arranged in the component tree.

   .. :ref:`Concept <concepts_test_case_components>` (Designer)

.. _glossary_component_tree:

:Component Tree:  The *component tree* details the
   :ref:`hierarchy of components <alyvix_designer_component_tree_structure>`
   in a given test case object in Designer.

   .. :ref:`Concept <concepts_test_case_components>`

.. _glossary_group:

:Group:  A *group* in a test case object consists of a main component and up to 4 subcomponents
   that during execution must all match against the current screen in order for their actions
   to be carried out.

   .. :ref:`Group <alyvix_designer_component_components>`
   .. :ref:`Concept <concepts_test_case_components>`

.. _glossary_region_of_interest:

:Region of Interest:  A *region of interest* (RoI) is the area around a subselection in which
   that subselection must appear during execution for a match to be valid.  It is especially
   useful when the selection is at the edge of a resizeable region such as a window.

   .. :ref:`Concept <concepts_screen_capture_roi>`

.. _glossary_root:

:Root element:  The *root element* of a test case object holds the captured screen which serves
   as the image source for creating components.  All elements in the component tree are
   dependent on the root element.

   .. :ref:`Concept <concepts_test_case_components>`

.. _glossary_section:

:Section:  A *section* is a :ref:`user-defined subscript <alyvix_editor_interface_sections>` that
   can be called by one or more of any of the *main*, *fail* or *exit* scripts.  Sections are
   helpful whenever there are repetitive sequences of actions to carry out.

.. _glossary_selection:

:Selection:  A *selection* is a rectangular area within a screen capture that serves as the
   principal anchor for an entire group.  Unlike a *subselection*, a *selection* has no Region of
   Interest -- it can match anywhere on the screen.

.. _glossary_subselection:

:Subselection:  A *subselection* is a rectangular area within a screen capture that has an
   associated Region of Interest.  During execution, the RoI is positioned relative to the location
   of the detected *selection*, and the *subselection* must match an area within that RoI.

   .. :ref:`Concept <concepts_screen_capture_sel>`

.. _glossary_test_case:

:Test Case:  A *test case* is the sum total of the screen capture, all of the test case objects
   (containing the component tree and its components), and any mappings and scripts using those
   objects.  It is saved in a file with an :file:`.alyvix` extension, and can be loaded by Alyvix
   Editor and Selector.

   .. :ref:`Concept <concepts_test_case_top>`

.. _glossary_test_case_object:

:Test Case Object:  A *test case object* is a named object within a test case, consisting of a
   screen capture and all the components within the component tree based on that screen capture.
   A single test case can contain multiple test case objects, and all test case objects can be
   used for creating scripts within their test case.

   .. :ref:`Concept <concepts_test_case_objects>`

.. _glossary_test_case_script:

:Test Case Script:  A *test case script* is a sequence of instructions describing, during the
   execution phase, how to :ref:`compare test case objects <alyvix_editor_scripting_panel_top>`
   against the application being run.

   .. :ref:`Concept <concepts_test_case_object_name>`




.. .. toctree::
      :maxdepth: 2
      :name: toc_designer
      :hidden:

..   basic_concepts/screen_capture.rst
     basic_concepts/test_case.rst
