:author: Charles Callaway
:date: 05-12-2019
:modified: 14-02-2020
:tags: designer
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_designer_options_test_case:

=================
Test Case Options
=================

At the top of the Alyvix Designer panel are the options that pertain to the test case as a whole:

.. image:: images/ad_testcase_options_sized.png
   :class: image-boxshadow
   :alt: The test case options.

The **Object name** is the reference name of a particular **test case object**
:rawhtml:`<a href="../glossary.html#glossary-test-case-object"><i class="fa fa-tiny fa-question-circle"></i></a>`
within a given test case.  Each test case typically contains multiple test case objects which are
used when building :ref:`scripts <alyvix_editor_scripting_panel_top>`, and thus need unique,
descriptive names to easily distinguish them from other test case objects.

There are also three **test case parameters** that affect how the
:ref:`selections and subselections <alyvix_designer_component_tree_types>` in the component tree
are detected, regardless of their type, and what happens if they fail to be detected.

#. **Detection condition:**  One of the following conditions will be checked at a default
   interval of every ``0.5`` seconds:

    * **Appear:**  Alyvix will continuously try to detect any of the main group components (*image*
      or *rect*) on screen if it was not already there when the test case started
    * **AppearDisappear:**  Alyvix will see whether any of the main group components appears,
      and then disappears within the timeout limit
    * **Disappear:**  If any of the main group components was present when the test case started,
      Alyvix will detect when one is no longer visible

      .. image:: images/appeardisappear_h120.png
         :class: image-boxshadow
         :alt: Visual appearance and disappearance timeline.

#. **Timeout:**  The chosen detection condition will be continuously checked until this number
   of seconds has elapsed.
#. **Break:**  If this option is checked, then a timeout will cause the test case to fail, and
   if it is part of a series of test cases, then the entire series will fail.  If not checked,
   it will report the failure but continue with the next test cases in the series.
