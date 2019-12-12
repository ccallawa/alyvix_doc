:author: Charles Callaway
:date: 5-12-2019
:modified: 12-12-2019
:tags: designer
:lang: en-US
:translation: false
:status: draft


.. _alyvix_designer_testcase:

###################
The Testcase Object
###################

Alyvix Designer testcases are stored as JSON files.  Each time you exit Designer by pressing the
:guilabel:`OK` button, the JSON object representing the testcase will be saved in the current
directory under the file name:

:file:`<filename>.alyvix`

where ``filename`` is the value of the ``-f`` parameter passed when starting Designer.

If you then call Alyvix Robot with that file as a parameter, when it finishes it will create a new
file based on the original testcase, but with the resulting measures included.  The file name will
have the timestamp at the moment of execution appended:

:file:`<filename>_<full-timestamp>.alyvix`

For example:

:file:`logintest_20191220_145228_UTC+0100.alyvix`



.. _alyvix_designer_testcase_json:

.. topic:: Alyvix Testcase JSON Structure

   Unlike prior versions of Alyvix, this single ``.alyvix`` file contains everything needed to model
   the testcase and store the resulting measures.

The following JSON structure illustrates the high-level structure of the Testcase object:

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

   * Why is there a second (or even third) screenshot in the .json file?  Is it a dump of the
     entire screen when a component was detected?
