:author: Charles Callaway
:date: 09-11-2021
:modified: 02-02-2022
:tags: release notes
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt



.. _release_notes_v3_2_0:

=====================
Version 3.2.0 - 3.2.3
=====================

Alyvix is an open source APM software tool for visual monitoring. If your machine matches the
system requirements for Alyvix, you can :ref:`install or upgrade it <getting_started_top>`.

:ref:`Python 3.9.7 64-bit official distribution <install_release_python_install>` is the recommended
Python version to power Alyvix 3.2.x.

|


.. _install_release_v3_2_3:

.. rubric:: Version 3.2.3

**Release date:**  February 2nd, 2022

**Improvements**

* :iconlink:`pivotal|Pivotal Tracker Issue #178573058|178573058` |mdash|
  Add new map rows with new sequential keys

**Bug Fixes**

* :iconlink:`pivotal|Pivotal Tracker Issue #178586988|178586988` |mdash|
  Rename objects (after adding, duplicating or importing them) without breaking others
* :iconlink:`pivotal|Pivotal Tracker Issue #180840734|180840734` |mdash|
  Fix a crash in Editor when returning from a test case run
* :iconlink:`pivotal|Pivotal Tracker Issue #178573058|178573058` |mdash|
  Retain maps without saving the entire test case just to do that
* :iconlink:`pivotal|Pivotal Tracker Issue #178626207|178626207` |mdash|
  Retain (dis)appear settings without saving the entire test case just to do that
* :iconlink:`pivotal|Pivotal Tracker Issue #178629938|178629938` |mdash|
  Don't allow sections and maps to be nameless

|


.. _install_release_v3_2_0:

.. rubric:: Version 3.2.0

**Release date:**  November 9th, 2021

**Improvements**

* :iconlink:`pivotal|Pivotal Tracker Issue #178625613|178625613` |mdash|
  Alyvix and its dependencies are now aligned with Python version 3.9.7

**Bug Fixes**

* :iconlink:`pivotal|Pivotal Tracker Issue #178470580|178470580` |mdash|
  One or more **warning** transactions are no longer enough by themselves to cause Alyvix to
  report a test case failure

|
