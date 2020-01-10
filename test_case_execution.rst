:author: Charles Callaway
:date: 05-12-2019
:modified: 10-01-2020
:tags: robot
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_execution_top:

###################
Test Case Execution
###################

Alyvix test cases you have built with Alyvix Designer can be run using Alyvix Robot.
In a production environment, you will typically create a set of test cases once, and then
repeatedly run those test cases.  An example could be monitoring the usability of web pages
on a remote server, where the responsiveness must be measured every minute.

There are two principal modes for interacting with Alyvix Robot:

* Manually call Robot with the Command Prompt, principally used intermittently for testing
* Automatically call Robot, for instance via scripting, at regular intervals

In both cases, the main idea is to execute one test case object at a time, typically
:ref:`combining them in series <getting_started_example_settings_exec>`, treating them as
reusable building blocks.

When executed manually, the test case object names are passed with the *object* (``-o``) option.
In this case, the *verbosity* (``-v``) parameter can provide additional information that can
help you should you need to debug your test cases.

When scripting automatically, the :ref:`test case protocol object <test_case_protocol_top>`
(``.alyvix`` file) can similarly have multiple case names in the ``script`` field in order to
call multiple test cases in sequence.


.. _alyvix_robot_cli_options:
.. topic:: Launching Alyvix Robot

   Alyvix Robot can be run with the following command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> python alyvix_robot.py

For instance, if you used Alyvix Designer to create a file :file:`my_test.alyvix` containing a
test case with the object name "open", you can call:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> python alyvix_robot.py --filename my_test -o open

The following options are available:

+---------------+----------+----------------------------------------------+
| Option        | Shortcut | Description                                  |
+---------------+----------+----------------------------------------------+
| \-\\-args     | -a       | Arguments to pass                            |
+---------------+----------+----------------------------------------------+
| \-\\-filename | -f       | Supply the file name with no extension       |
+---------------+----------+----------------------------------------------+
| \-\\-help     | -h       | Display command help                         |
+---------------+----------+----------------------------------------------+
| \-\\-object   | -o       | Supply the Object name                       |
+---------------+----------+----------------------------------------------+
| *<none>*      | -v       | Verbosity:  0=low, 2=high                    |
+---------------+----------+----------------------------------------------+


.. todo::

   * CC:  Add info here about multiple object names as described in the Windows Settings
     tutorial in Getting Started, then link here from there.



.. _alyvix_robot_cli_result:
.. topic:: What Alyvix Robot Returns

   Alyvix Robot will give you output like this if successful.

.. code-block:: md

   C:\Alyvix\testcases> python alyvix_robot.py --filename start -o open
   2019/12/12 18:24:20.405: start starts
   2019/12/12 18:24:21.949: open DETECTED in 0.0s (+/-0.060)
   2019/12/12 18:24:21.950: start ends OK, it takes 1.544s.

If it fails instead, the output will look like this:

.. code-block:: md

   C:\Alyvix\testcases> python alyvix_robot.py --filename start-test -o settings
   2019/12/12 18:37:41.448: start-test starts
   2019/12/12 18:37:51.762: settings FAILED after 10s
   2019/12/12 18:37:51.763: start-test ends FAILED because of settings, it takes 10.315s.

If you have enabled the :ref:`break flag <alyvix_designer_options_test_case>` in Alyvix Designer
for a given test case, then if that test case fails, no more test cases will be executed.  If it
is not set, then the test case will instead be skipped after its timeout has expired.



.. Hidden section on Measurement (wait on this for now, uncomment when ready)

   .. _test_case_execution_measurements:

   ============
   Measurements
   ============

   * How measurement is done (get from v2.7 doc?)
   * How Alyvix is integrated with monitoring/ITOA (NetEye is one example of monitoring)
   * Conceptual:  what gets measured and how (appear + disappear)
   * See keynote slides with frame grabber / transaction performance slide
