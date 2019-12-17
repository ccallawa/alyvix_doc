:author: Charles Callaway
:date: 5-12-2019
:modified: 17-12-2019
:tags: designer
:lang: en-US
:translation: false
:status: draft


.. _test_case_building_top:

##################
Test Case Building
##################

Alyvix Designer lets you select patterns on a copy of the screen, whether they're images,
rectangles, or text.  You can then define triggers for actions when those patterns are recognized
later in a simulated interaction with an application.

Designer will then save the set of patterns as a single :ref:`test case <glossary_test_case>`, which
you can then use as building blocks to compose more complicated objects and scripts, and to
measure the performance of executed test cases with :ref:`Alyvix Robot <test_case_execution_top>`.

The following documentation presents information on Alyvix Designer:

* The :ref:`Interface Overview <alyvix_designer_interface_overview>` page provides a high-level overview
  and describes the general layout of the interface.

* To learn more about interacting with specific visual elements and what they can do, see the
  :ref:`Component Tree <alyvix_designer_component_tree>` page.

* You can find more detailed information about the available options for test cases and components
  on the :ref:`Interface Options <alyvix_designer_options>` page.

* The :ref:`Test Case Protocol <test_case_protocol_top>` page provides technical details on how
  Alyvix object files are organized and what they contain.



.. _alyvix_designer_cli_options:
.. topic:: Launching Alyvix Designer

   Alyvix Designer can be run as follows if the Alyvix file path (e.g.,
   :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\`)
   is included in your :guilabel:`Path` environment variable:

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_designer.py

The following options are available:

+---------------+----------+----------------------------------------------+
| Option        | Shortcut | Description                                  |
+---------------+----------+----------------------------------------------+
| --delay       | -d       | ``unknown``                                  |
+---------------+----------+----------------------------------------------+
| --filename    | -f       | Supply the file name with no extension       |
+---------------+----------+----------------------------------------------+
| --help        | -h       | Display command help                         |
+---------------+----------+----------------------------------------------+
| --object      | -o       | Supply the Object name                       |
+---------------+----------+----------------------------------------------+
| --verbose     | -v       | Set the verbosity level for debugging output |
+---------------+----------+----------------------------------------------+
| --window      | -w       | ``unknown``                                  |
+---------------+----------+----------------------------------------------+




.. todo::

   * Should we call the capture lines "guide lines", "crosshair", something else?
   * Link to the simple how-to for Designer when ready
   * Fill in unknown details in the CLI options section




.. toctree::
   :maxdepth: 2
   :name: toc_designer
   :hidden:

   test_case_building/designer_interface_overview.rst
   test_case_building/designer_options.rst
   test_case_building/designer_component_tree.rst
