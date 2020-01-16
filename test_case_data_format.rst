:author: Charles Callaway
:date: 05-12-2019
:modified: 15-01-2020
:tags: test cases, data format
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_data_format_top:

*********************
Test Case Data Format
*********************

Alyvix test case objects are stored as JSON files.  Each time you exit Designer by pressing the
:guilabel:`OK` button, or modify an object in Editor, the JSON object representing the test case
is saved in the current directory under the file name:

:file:`<filename>.alyvix`

where ``filename`` is the value of the ``-f`` parameter passed when starting Editor or Designer.

If you then call Alyvix Robot with that file as a parameter, when it finishes it will create a new
file based on the original test case, but with the resulting measures included.  The file name will
have the timestamp at the moment of execution appended:

:file:`<filename>_<full-timestamp>.alyvix`

For example:

:file:`logintest_20191220_145228_UTC+0100.alyvix`



.. _test_case_data_format_json:

.. topic:: Alyvix Test Case Object JSON Structure

   Unlike prior versions of Alyvix, this single ``.alyvix`` file contains everything needed to model
   the test case and store the resulting measures.

The following JSON structure illustrates the high-level structure of the test case object:

.. code-block:: json

   {
      "maps": { },
      "objects": {
         "open": {
            "call": { },
            "components": {
               "<resolution>": {
                  "groups": [
                     { "main": { } },
                     { "main": { } },
                     { "main": { } }
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
         "case": [],
         "sections": { }
      }
   }




.. todo::

   * FM:  Why is there a second (or even third) screenshot in the .json file?  Is it a dump of the
     entire screen when a component was detected?
     **A:  One SS for each test case object, always.  A regular dump as when Designer is called**

