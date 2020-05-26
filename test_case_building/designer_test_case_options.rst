:author: Charles Callaway
:date: 05-12-2019
:modified: 22-05-2020
:tags: designer
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_designer_options_test_case_object:

========================
Test Case Object Options
========================

At the top of the Alyvix Designer panel are the options relating to the test case object as
a whole:

.. image:: images/ad_testcase_options_sized.png
   :class: image-boxshadow
   :alt: The test case options.

The **Object name** is the reference name of a particular :glossdef:`test case object`
:rawhtml:`<a href="../glossary.html#glossary-test-case-object"><i class="fa fa-tiny fa-question-circle"></i></a>`
within a given test case.  A test case typically contains multiple test case objects which are
used when building :ref:`scripts <alyvix_editor_scripting_panel_top>`
:rawhtml:`<a href="../glossary.html#glossary-test-case-script"><i class="fa fa-tiny fa-question-circle"></i></a>`,
and thus it needs a unique, descriptive name to easily distinguish it from other test case objects.

There are also three **test case parameters** that affect how the :glossdef:`selections`
:rawhtml:`<a href="../glossary.html#glossary-selection"><i class="fa fa-tiny fa-question-circle"></i></a>`
and subselections in the :ref:`component tree <alyvix_designer_component_tree_top>` are detected,
regardless of their type, and what happens if they fail to be detected:

#. **Detection condition:**  One of the following conditions will be checked at a default
   interval of every ``0.5`` seconds:

    * **Appear:**  Alyvix will continuously try to detect if the test case object as a whole
      (i.e., all of its groups and components) appear simultaneously on screen when that was
      previously not the case
    * **AppearDisappear:**  Similarly, Alyvix will check whether all the groups and components
      in the test case object appear, and then also disappear within the timeout limit
    * **Disappear:**  If the groups and components of a test case object were initially present,
      Alyvix will detect when they are no longer visible

      .. image:: images/appeardisappear_h120.png
         :class: image-boxshadow
         :alt: Visual appearance and disappearance timeline.

#. **Timeout:**  All the components will be regularly checked with the chosen detection condition
   until this number of seconds has elapsed.
#. **Break:**  If this option is checked, then timing out without the selected detection condition
   having matched will cause the test case object to fail.  If the option is not checked, the
   failure will simply be reported.
