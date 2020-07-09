:author: Charles Callaway
:date: 05-12-2019
:modified: 16-06-2020
:tags: test cases, data format
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_data_format_top:

*********************
Test Case Data Format
*********************

Alyvix :iconlink:`gloss|test cases|glossary.html#glossary-test-case` are stored as JSON files,
which are then used by all Alyvix applications.  Alyvix files represent the unique mechanism for
interchange between Alyvix modules, and each file is self-contained, without any external
dependencies.



.. _test_case_data_format_file:

===============
Test Case Files
===============

Each time you exit :ref:`Designer <alyvix_designer_interface_overview>` or
:ref:`Selector <alyvix_selector_interface_top>` by pressing the :bbutton:`OK` button, or save
an object in :ref:`Editor <alyvix_editor_interface_top>`, the JSON object representing the test
case is saved in the current directory under the file name:

:file:`<filename>.alyvix`

where ``filename`` is the value of the ``-f`` parameter passed when starting Editor or Designer.

If you then call Alyvix Robot :ref:`via the command line <alyvix_robot_result_cli>` with that
file as a parameter, when it finishes it will create a new file based on the original test case,
but with the resulting measures included.  The file name will have the timestamp at the moment
of execution appended:

:file:`<filename>_<full-timestamp>.alyvix`

For example:

:file:`logintest_20191220_145228_UTC+0100.alyvix`

.. note::

   This file is not produced when a test case is executed in Editor via |runblue|, only when
   executed directly from Alyvix Robot.



.. _test_case_data_format_json:

========================
Test Case JSON Structure
========================

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
               "group": "<transaction-group-name>",
               "output": true,
               "series": { },
               "thresholds": { } }
         }
      },
      "script": {
         "case": [
            "<test-case-object-name>",
            { "disable": "<test-case-object-name>" },
            { "flow": "<test-case-object-name>",
              "if-true": "<test-case-object-name>" },
            { "flow": "<test-case-object-name>",
              "if-false": "<test-case-object-name>" },
            { "flow": "<test-case-object-name>",
              "for": "<test-case-map-name>" }
         ],
         "sections": {
            "<section-name>": [
               "<test-case-object-name>"
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

      { "maps": {
           "map-name":  { } },
        "objects": {
           "<test-case-object-name>":  { } },
        "script": {
           "case":  [ ],
           "sections":  { } }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :iconlink:`gloss|maps|glossary.html#glossary-map`
      **---**  An ordered set of values that a script can loop over, for
      instance to insert a sequence of values in multiple text fields
   #. :bolditalic:`objects`  **---**  A list of the individual test case objects created with
      Alyvix Designer.  Each :iconlink:`gloss|test case object|glossary.html#glossary-test-case-object`
      is identified uniquely in the list by its object name
   #. :iconlink:`gloss|script|glossary.html#glossary-test-case-script`  **---**  The scripts
      created for a test case, both the main script and any section (subroutine) scripts.


.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. .. rubric:: *Maps*

   Each named map under the :bolditalic:`maps` field contains a set of named keys (rows) and a
   fixed number of cell values, to represent a **m x n** matrix (columns cannot be named):

   .. code-block:: json
      :class: tiny-code-block

      { "<map-name-1>": {
           "key1": [ "key1-val1",
                     "key1-val2" ],
           "key2": [ "key2-val1",
                     "key2-val2" ] }
      }


.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. .. rubric:: *Objects*

   The value of each property contained within the :bolditalic:`objects` substructure (shown here
   as "test-case-object-name") corresponds to a test case object created in Designer.
   Those values have the following meanings:

   .. code-block:: json
      :class: tiny-code-block

      { "<test-case-object-name>": {
           "call": { },
           "components": { },
           "date_modified": "<timestamp>",
           "detection": { },
           "measure": { }
        }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`call`  **---**  The recorded options to start or kill an external application
      when a test case object is :ref:`first called <alyvix_designer_options_components_root>`
   #. :bolditalic:`components`  **---**  The representation for the
      :iconlink:`gloss|component tree|glossary.html#glossary-component-tree`
      (:ref:`detailed below <test_case_data_format_components>`)
   #. :bolditalic:`date_modified`  **---**  The time the test case object was last modified
      (:ref:`also displayed in Selector <alyvix_selector_interface_screenshot>`)
   #. :bolditalic:`detection`  **---**  The test case object's
      :ref:`detection conditions <alyvix_designer_options_test_case_object>` such as *timeout*, *break*,
      and *appear/disappear*
   #. :bolditalic:`measure`  **---**  Details of the last execution via Alyvix Editor or Robot
      (:ref:`see below <test_case_data_format_measure>`), along with the settings for transaction
      group, output, and thresholds.


.. _test_case_data_format_components:

.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. .. rubric:: *Objects* > *{object}* > *Components*

   The *components* section represents the :ref:`component tree <alyvix_designer_component_tree_top>`
   of a given test case object.  The example below shows how you can have one component tree at
   each distinct screen resolution.

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

   :bolditalic:`<resolution>`  **---**  The resolution of a screen capture as shown in
   :ref:`Alyvix Selector <alyvix_selector_interface_screenshot>`.  This value is not selected by
   the user, but is dependent on the hardware and the settings in use when the screen is
   captured.

   .. rst-class:: bignums
      :class: backmedbeige

   #. :iconlink:`gloss|groups|glossary.html#glossary-group`  **---**  A JSON array of exactly
      3 items, each of which corresponds to one of the groups in the component tree.

      .. rst-class:: bignums
         :class: backlightbeige

      #. :bolditalic:`main`  **---**  The main component in a group.

         .. rst-class:: bignums
            :class: backlightbeige

         #. :bolditalic:`detection`  **---**  Information about the match method to use when
            trying to detect the region of interest.
         #. :bolditalic:`interactions`  **---**  Details on any mouse or keyboard actions to
            initiate in the event of a positive detection.
         #. :bolditalic:`visuals`  **---**  Information about the region of interest and the
            selection box laid over the screen capture.

      #. :bolditalic:`subs`  **---**  A JSON array of exactly 4 items, each of which corresponds
         to one of the subcomponents in a group.  The structure of each element is identical to
         the structure of the main component above.

   #. :bolditalic:`screen`  **---**  The :iconlink:`ext|Base64|https://en.wikipedia.org/wiki/Base64`
      representation of the screen capture.  There is exactly one screen capture for each
      resolution in a test case object.


.. _test_case_data_format_measure:

.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. .. rubric:: *Objects* > *{object}* > *Measure*

   The *measure* structure holds some of the user-selected options
   :ref:`visible in Selector <alyvix_selector_interface_headers>` for a given test case object,
   along with the **series** array, which contains recorded data resulting from each run of the
   test case object by Alyvix Robot in the test case's script within a single session.

   When a test case is executed, its :file:`.alyvix` file is taken as the starting point, and thus
   the **series** structure for all of its test case objects are empty.  Each time a test case
   object is called by the test case script, the results and auxiliary data are added to **series**
   as a new array element.

   This example shows the structure and some default values:

   .. code-block:: json
      :class: short-code-block

      { "measure": {
          "group": "<transaction-group-name>",
          "output": "<true/false>",
          "series": [
              {
                  "accuracy_ms": "<ms-amount>",
                  "annotation": "<base64>",
                  "exit": "<true/false/fail/not_executed>",
                  "performance_ms": "<ms-amount>",
                  "records": {
                      "check": "<true/false>",
                      "extract": "<extracted-text>",
                      "image": "<base64>",
                      "text": "<scraped-text>"
                  },
                  "resolution": {
                      "height": "<pixel-amount>",
                      "width": "<pixel-amount>"
                  },
                  "scaling_factor": "<zoom-amount>",
                  "screenshot": "<base64>",
                  "timestamp": "<epoch>"
              }
          ],
          "thresholds": {
              "critical_s": 5,
              "warning_s": 3 }
      }

   .. rst-class:: bignums
      :class: backdarkbeige

   #. :bolditalic:`group`  **---**  The transaction group assigned to the test case object.

   #. :bolditalic:`output`  **---**  Whether the test case object's "Measure" checkbox is marked.

   #. :bolditalic:`series`  **---**  An array containing the results and auxiliary data for each
      run of the parent test case object.  It contains the following information:

      .. rst-class:: bignums
         :class: backmedbeige

      #. :bolditalic:`accuracy_ms`  **---**  Given the performance measurement from the same run
         (see below), this is the interval (+/-) over which that measurement is guaranteed to have
         occurred.

      #. :bolditalic:`annotation`  **---**  The :iconlink:`ext|Base64|https://en.wikipedia.org/wiki/Base64`
         representation of the screen when the test case object was being run, overlaid with
         graphic annotations to indicate those components that matched, and potentially the first
         component that did not match.

      #. :bolditalic:`exit`  **---**  The result type of the most recent run.  If the test case
         object did not match, then the type ``false`` or ``fail`` is determined by whether the
         :guilabel:`break` flag was set.

      #. :bolditalic:`performance_ms`  **---**  The number of milliseconds that elapsed from when
         the run of a test case object began until a match was confirmed, subject to the accuracy
         interval described above; otherwise ``-1``.

      #. :bolditalic:`records`  **---**  Temporary variables that are computed during the matching
         process, such as a text string extracted by a text component.

      #. :bolditalic:`resolution`  **---**  The screen resolution at which the test case object
         was executed.

      #. :bolditalic:`scaling_factor`  **---**  The Windows zoom level at the time when the test
         case object was executed.

      #. :bolditalic:`screenshot`  **---**  The :iconlink:`ext|Base64|https://en.wikipedia.org/wiki/Base64`
         representation of the screen during the test case object run.  It's similar to the main
         screen capture, but is made during the execution phase, rather than during the building
         phase.

      #. :bolditalic:`timestamp`  **---**  The time (Unix epoch) when this series element
         was run; otherwise ``-1``.

   #. :bolditalic:`thresholds`  **---**  The number of elapsed seconds after the test case object
      has been started until a ``warning`` and/or ``critical`` alert should be triggered.  If no
      values are specified, no alerts will be triggered.

   |


.. _test_case_data_format_script:

.. rst-class:: bignums
   :class: backdarkbeige nobignum

#. .. rubric:: *Script*

   The **script** parameter records the
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
             "if-false": "<test-case-object-name>" },
           { "flow": "<test-case-object-name>",
             "for": "<test-case-map-name>" }
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

   #. :bolditalic:`case`  **---**  The main script that will be
      :ref:`executed by Alyvix Robot <test_case_execution_top>`.  The script is an ordered
      list of :ref:`scripting elements <alyvix_editor_scripting_node_expressions>`, where a simple,
      enabled element is just the name of a test case object.  Other elements have the following
      meanings:

      .. rst-class:: bignums
         :class: backlightbeige

      #. :bolditalic:`disable`  **---**  Skip this test case object and continue with the next.
      #. :bolditalic:`flow`  **---**  Indicates the test case object or section that is the value
         of this key should be executed by Alyvix Robot in the context of a conditional
         (*if-true* or *if-false*) or a loop (*map*) .
      #. :bolditalic:`if-true`  **---**  Evaluates whether the detection part of a given test case
         object would match, but without executing its actions.
      #. :bolditalic:`if-false`  **---**  As above, but if the test case object would not match.
      #. :bolditalic:`for`  **---**  Indicates there should be a loop over the values in the
         specified :ref:`Map <alyvix_editor_interface_maps>`.

   #. :bolditalic:`sections`  **---**  Corresponds to the
      :ref:`named subroutine scripts <alyvix_editor_script_mgmt_top>` created in Alyvix Editor.
      Each section is a parameter where its key is the name of the section and its value is the
      same as the :bolditalic:`case` value described above.

      .. rst-class:: bignums
         :class: backlightbeige

      #. :bolditalic:`exit`  **---**  The (teardown) script to execute when a script has
         completed, regardless of whether it succeeded or failed.
      #. :bolditalic:`fail`  **---**  The (teardown) script to execute when a script has failed
         during the execution of its test case objects.
