:author: Charles Callaway
:date: 04-12-2019
:modified: 05-02-2020
:tags: how-to
:lang: en-US
:translation: false
:status: updating

.. include:: ../sphinx-roles.txt



.. _install_release_notes_top:

=============
Release Notes
=============

Below you can find the release notes for Alyvix in reverse chronological order.



.. _install_release_v3_0_2:

-------------
Version 3.0.2
-------------

**Release date:  March 25th, 2020**

**Python 3.7.6 64-bit official distribution** is the recommended Python version to power Alyvix 3.

Alyvix is an open source APM software tool for visual monitoring. If your machine matches the
system requirements for Alyvix, you can
:ref:`install or upgrade it <getting_started_top>`.

**Bug Fixes**

* :ref:`NATS-InfluxDB output mode <alyvix_robot_result_nats_influxdb>` can now publish system
  call objects (*i.e.*, without requiring visual components to detect)
* Running single objects from test cases through Alyvix Robot now correctly saves their measures
  in :file:`.alyvix` output files
* The field name ``performance_ms``, a feature of ``measure`` in :file:`.alyvix` files, had a typo



.. _install_release_v3_0_1:

-------------
Version 3.0.1
-------------

**Release date:  March 11th, 2020**

**Python 3.7.6 64-bit official distribution** is the recommended Python version to power Alyvix 3.

Alyvix is an open source APM software tool for visual monitoring. If your machine matches the
system requirements for Alyvix, you can
:ref:`install or upgrade it <getting_started_top>`.

**New Features**

* :ref:`NATS-InfluxDB <alyvix_robot_result_nats_influxdb>`:  You can now output test case performance
  in Nagios format, and publish all measures to an InfluxDB database through a NATS channel
* :ref:`Alyvix Cipher <alyvix_robot_cipher_encryption>`:  You can encrypt a text string
  (*e.g.*, a password) with a given private key

**Improvements**

* *Editor focus handling:*  Both the **ADD** and **RUN** buttons in Alyvix Editor put the cursor
  focus on the previous window rather than Editor itself
* *Scaling factor check:*  Alyvix Editor and Robot supports any scaling factor setting
* *Text component scraper:*  :file:`.alyvix` output files now store all text scrapes from all the
  object candidates and, eventually, their related proper extracts



.. _install_release_v3_0_0:

-------------
Version 3.0.0
-------------

**Release date:  February 3rd, 2020**

**Python 3.7.6 64-bit official distribution** is the recommended Python version to power Alyvix 3.

Alyvix is an open source APM software tool for visual monitoring. If your machine matches the
system requirements for Alyvix, you can
:ref:`install or upgrade it <getting_started_top>`.

Alyvix 3 is a major product release, but it shares only the core concept with the previous
version (https://v2.alyvix.com/doc): it has been totally re-designed, re-engineered and
re-coded from scratch.

Build end-user bots and measure end-user experiences: with
:ref:`Alyvix Editor <test_case_building_top>` you can define visual transactions and script
test cases, while with :ref:`Alyvix Robot <test_case_execution_top>` you can
run these test cases to measure end-user transactions.

**New high level features:**

* Multitype objects are defined by image, rectangle and text components
* Objects are defined by up to 3 groups of 5 components each
* Objects can be defined for more than one resolution and scaling factor
* Object names, which are transaction names, are editable
* Each object is browsable through its tree view and is shown in a monitor
* Object interactions are sortable through a tree view
* Objects can be duplicated (as an entire test case) and imported
* A single object can be run from a test case
* The editor is a single instance and designed to properly build visual test cases
* Transactions, conditionals and loops can be scripted visually
* Test case output is customizable, has multiple formats and includes debugging information
* Transaction measurement accuracy can be improved by adding additional processing resources
* It is a FLOSS tool entirely written in pure Python 3
