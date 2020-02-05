:author: Charles Callaway
:date: 05-12-2019
:modified: 05-02-2020
:tags: test cases, data format
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt

.. role:: rawhtml(raw)
   :format: html


.. _test_case_data_format_top:

*********************
Test Case Data Format
*********************

Alyvix test cases are stored as JSON files, which are then used by all Alyvix applications.
Alyvix files represent the unique mechanism for interchange between Alyvix modules, and each
file is self-contained, without any external dependencies.



.. _test_case_data_format_file:

===============
Test Case Files
===============

Each time you exit Designer or Selector by
pressing the :bbutton:`OK` button, or save an object in Editor, the JSON object representing the
test case is saved in the current directory under the file name:

:file:`<filename>.alyvix`

where ``filename`` is the value of the ``-f`` parameter passed when starting Editor or Designer.

If you then call Alyvix Robot with that file as a parameter, when it finishes it will create a new
file based on the original test case, but with the resulting measures included.  The file name will
have the timestamp at the moment of execution appended:

:file:`<filename>_<full-timestamp>.alyvix`

For example:

:file:`logintest_20191220_145228_UTC+0100.alyvix`



.. _test_case_data_format_json:

========================
Test Case JSON Structure
========================

.. topic:: Alyvix Test Case Object JSON Structure

   A single ``.alyvix`` file stores the entire test case and holds all measures resulting from
   a single execution run.

The following example JSON structure illustrates the high-level structure of the test case object:

.. code-block:: json
   :linenos:

   {
      "maps": { },
      "objects": {
         "<test-case-object-name>": {
            "call": { },
            "components": {
               "<resolution>": {
                  "groups": [
                     { "main": { },
                       "subs": [ ] },
                     { "main": { },
                       "subs": [ ] },
                     { "main": { },
                       "subs": [ ] }
                  ],
                  "screen": "<base64>"
               }
            },
            "date_modified": "<timestamp>",
            "detection": {
               "break": true,
               "timeout_s": 10,
               "type": "appear" },
            "measure": {
               "output": true,
               "thresholds": {} }
         }
      },
      "script": {
         "case": [
            "<test-case-object-name>",
            { "disable": "<test-case-object-name>" },
            { "flow": "<test-case-object-name>",
              "if-true": "<test-case-object-name>" },
            { "flow": "<test-case-object-name>",
              "if-false": "<test-case-object-name>" } ],
         "sections": {
            "<section-name>": [
               "<test-case-object-name"
            ],
            "exit": [],
            "fail": [] }
      }
   }


.. _test_case_data_format_description:

The individual sections of the JSON structure are explained below.

.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. The **top level** corresponds to the elements used in Alyvix Editor:

   .. code-block:: json
      :class: tiny-code-block

      { "maps": {  },
        "objects": {
           "<test-case-object-name>": { } },
        "script": {
           "case": [],
           "sections": { } }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`maps` **---**

      .. todo::

         CC:  Need to finish Editor before writing this

   #. :bolditalic:`objects` **---** A list of the individual test case objects created with
      Alyvix Designer.  Each test case object is identified uniquely in the list by its **object name**
      :rawhtml:`<a href="glossary.html#glossary-object-name"><i class="fa fa-tiny fa-question-circle"></i></a>`.
   #. :bolditalic:`script` **---** The scripts created for a test case, both the main script and
      any section (subroutine) scripts.

.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. The value of each property contained within the :bolditalic:`objects` substructure (shown here
   as "test-case-object-name") corresponds to a test case object created in Designer.
   Those values have the following meanings:

   .. code-block:: json
      :class: tiny-code-block

      { "<test-case-object-name>": {
           "call": { },
           "components": { },
           "date_modified": "<timestamp>",
           "detection": { },
           "measure": { } }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`call` **---** The recorded options to start or kill an external application
      when a test case object is :ref:`first called <alyvix_designer_options_components_root>`
   #. :bolditalic:`components` **---** The representation for the component tree (detailed below)
   #. :bolditalic:`date_modified` **---** The time the test case object was last modified,
      :ref:`displayed in Selector <alyvix_selector_interface_screenshot>`
   #. :bolditalic:`detection` **---** The test case object's
      :ref:`detection conditions <alyvix_designer_options_test_case>` such as *timeout*, *break*,
      and *appear/disappear*
   #. :bolditalic:`measure` **---**

      .. todo::

         * FM:  Need to more information on *measure*


.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. The *components* section represents the :ref:`component tree <alyvix_designer_component_tree_top>`
   of a test case object.  The example below shows how you can have one component tree at each
   distinct screen resolution.

   .. code-block:: json
      :class: tiny-code-block

      { "components": {
           "<resolution>": {
              "groups": [
                 { "main": {
                      "detection": { },
                      "interactions": { },
                      "visuals": { } },
                   "subs": [ ] },
                 { "main": { },
                   "subs": [ ] },
                 { "main": { },
                   "subs": [ ] } ],
              "screen": "<base64>" } }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`<resolution>` **---**  The resolution of a screen capture as shown in
      :ref:`Alyvix Selector <alyvix_selector_interface_screenshot>`.  This value is not selected by
      the user, but is dependent on the hardware and the settings in use when the screen is
      captured.

      .. rst-class:: bignums
         :class: backmedbeige

      #. :bolditalic:`groups` **---**  A JSON array of exactly 3 items, each of which corresponds
         to one of the groups in the component tree.

         .. rst-class:: bignums
            :class: backlightbeige

         #. :bolditalic:`main` **---** The main component in a group.

            .. rst-class:: bignums
               :class: backlightbeige

            #. :bolditalic:`detection` **---** Information about the match method to use when
               trying to detect the region of interest.
            #. :bolditalic:`interactions` **---** Details on any mouse or keyboard actions to
               initiate in the event of a positive detection.
            #. :bolditalic:`visuals` **---** Information about the region of interest and the
               selection box laid over the screen capture.

         #. :bolditalic:`subs` **---**  A JSON array of exactly 4 items, each of which corresponds
            to one of the subcomponents in a group.  The structure of each element is identical to
            the structure of the main component above.

      #. :bolditalic:`screen` **---** The |base64-link| representation of the screen capture.
         There is exactly one screen capture for each resolution in a test case object.


.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. The **script** parameter records the
   :ref:`main script and any subroutines <alyvix_editor_scripting_panel_top>`
   used to compose more complex interaction behaviors.

   .. code-block:: json
      :class: short-code-block

      { "case": [
           "<test-case-object-name>",
           { "disable": "<test-case-object-name>" },
           { "flow": "<test-case-object-name>",
             "if-true": "<test-case-object-name>" },
           { "flow": "<test-case-object-name>",
             "if-false": "<test-case-object-name>" }
        ],
        "sections": {
           "<section-name>": [
              "<test-case-object-name>",
              "<test-case-object-name>"
           ],
           "exit": [],
           "fail": [] }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`case` **---** The main script that will be
      :ref:`executed by Alyvix Robot <test_case_execution_top>`.  The script is an ordered
      list of scripting elements, where a simple, enabled element is just the name of a
      test case object.  Other elements have the following meanings:

      .. rst-class:: bignums
         :class: backlightbeige

      #. :bolditalic:`disable` **---** Skip this test case object and continue with the next.
      #. :bolditalic:`flow` **---** Indicates the test case object that is the value of this key
         should be executed by Alyvix Robot if the condition listed in the second paramater is true.
      #. :bolditalic:`if-true` **---** Evaluates whether the detection part of a given test case
         object would match, but without executing its actions.
      #. :bolditalic:`if-false` **---** As above, but if the test case object would not match.

   #. :bolditalic:`sections` **---** Corresponds to the named subroutine scripts created in
      Alyvix Editor.  Each section is a parameter where its key is the name of the section and
      its value is the same as the :bolditalic:`case` value described above.

      .. rst-class:: bignums
         :class: backlightbeige

      #. :bolditalic:`exit` **---** The (teardown) script to execute when a script has
         completed successfully.
      #. :bolditalic:`fail` **---** The (teardown) script to execute when a script has failed
         during the execution of its test case objects.



.. todo::

   * FM:  Are "exit" and "fail" official reserved words for sections?
   * FM:  Do we need to describe elements any further down into the JSON data structure than this?