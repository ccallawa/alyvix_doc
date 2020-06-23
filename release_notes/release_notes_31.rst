:author: Charles Callaway
:date: 08-06-2020
:modified: 23-06-2020
:tags: release notes
:lang: en-US
:translation: false
:status: updating

.. include:: ../sphinx-roles.txt



.. _release_notes_v3_1_0:

=======================
Version 3.1.0 - Current
=======================

Alyvix is an open source APM software tool for visual monitoring. If your machine matches the
system requirements for Alyvix, you can :ref:`install or upgrade it <getting_started_top>`.

**Python 3.7.6 64-bit official distribution** is the recommended Python version to power
Alyvix 3.1.x.



.. _install_release_v3_0_2:

.. topic:: Version 3.1.0

   **Release date:**  June 26th, 2020

**New Features**

* When running a test case, whether via Alyvix Robot or Alyvix Editor, the CLI output
  :ref:`now reports measurements <alyvix_robot_result_cli>`
  for every loop iteration, or else for the last execution of a test case object.  The format of
  the :ref:`Measure and Series <test_case_data_format_measure>` data structures supporting this
  have been udpated with more detailed information.
* It is now
  :ref:`faster and easier to debug <alyvix_editor_interface_debug>`
  both individual test case objects and partial scripts with the addition of dedicated
  interface controls.
* We've introduced a new interface control which will
  :ref:`grab a new screen capture <alyvix_selector_interface_grab_resolution>`
  (either to replace an existing one or use in conjunction with Duplicate) or add an additional
  screen capture at a different resolution than those already contained in the test case object.

**Improvements**

* |rn31-impr-a-link| |mdash| **Restructured CLI and Map Arguments:**

  Better organization for default, CLI and Map arguments, including a default value for
  String insertions when there are more loop iterations than supplied values.

* |rn31-impr-b-link| |mdash| **Better Interface Controls:**

  Easier to use interface controls for script management, including:

  * Added hover confirmation via a blue bar in the scripting panel
  * Multi-selection over scripting nodes
  * New Drag, Insert and Run controls employed by the new debugging capabilities

* |rn31-impr-c-link| |mdash| **Improved User Experience:**

  Improved the user experience throughout the UI, such as:

  * Confirm/cancel dialog boxes
  * Annotations of failed objects in the Console tab
  * Better drag-and-drop support for scripting
  * Checks employed on scripts when renaming and deleting the underlying test case objects
  * Renamed objects in Selector are no longer sorted out of focus

**Bug Fixes**

* *Bugfix #1:*  Description
* *Bugfix #2:*  Description
* *Bugfix #3:*  Description
