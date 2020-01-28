:author: Charles Callaway
:date: 05-12-2019
:modified: 28-01-2020
:tags: robot, execution, test cases
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_execution_top:

###################
Test Case Execution
###################

Alyvix test cases you have built with Alyvix Editor or Designer can be run using Alyvix Robot.
Robot can either be run from the command line, or directly within the Alyvix Editor itself.

In a production environment, the typical use case is to create a set of test cases once, and then
repeatedly run those test cases at regular intervals.  An example could be monitoring the usability
of web pages on a remote server, where responsiveness must be measured every 2 minutes.

Before you can use Alyvix in a production environment, however, you will first need to iteratively
develop and debug your test cases.  This is where Alyvix Robot can help you.  There are two
principal modes for interacting with Alyvix Robot:

* Calling Robot from the Command Prompt
* Calling Robot from within Alyvix Editor via the |runblue| button

In both cases, one test case at a time is executed, the main script shown in Editor, or
:ref:`one or more of the test case objects in series <getting_started_example_settings>` in
the command prompt.



.. _alyvix_robot_cli_options:


**********************************************
Launching Alyvix Robot from the Command Prompt
**********************************************

When Robot executes a test case, it first checks to see if one or more test case object names were
passed via the ``-o`` parameter.  If so, Robot will execute those test case objects.  Otherwise, if
the test case in the :file:`.alyvix` file
:ref:`contains a script <test_case_data_format_description>` in its ``script`` field, then Robot
will run that script.

Adding the *verbosity* (``-v``) parameter will provide additional information that can help you
should you need to debug your test cases.

Alyvix Robot can be run with the following command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> python alyvix_robot.py

If you used Alyvix Editor to create a file :file:`start-test.alyvix` containing a a test case
object named ``start``, you should run:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> python alyvix_robot.py --filename start-test -o start

Robot allows you to execute multiple test case objects in sequence by putting all of them in order
after the ``--object`` parameter:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot -f start-test -o "start settings"

The following options are available:

+---------------+----------+----------------------------------------------+
| Option        | Shortcut | Description                                  |
+---------------+----------+----------------------------------------------+
| \-\\-filename | -f       | Supply the file name with no extension       |
+---------------+----------+----------------------------------------------+
| \-\\-object   | -o       | Supply the Object name(s)                    |
+---------------+----------+----------------------------------------------+
| *<none>*      | -v       | Verbosity:  0=low, 2=high                    |
+---------------+----------+----------------------------------------------+


.. todo::

   * CC:  Add info here about multiple object names as described in the Windows Settings
     tutorial in Getting Started, then link here from there.
   * CC:  The other commands have ``--verbose``, why not Robot?



.. _alyvix_robot_editor:

*****************************************
Launching Alyvix Robot from Alyvix Editor
*****************************************

When run manually from Alyvix Editor, the test case objects are executed as specified in the
:ref:`scripting panel <alyvix_editor_scripting_panel_top>`.


.. todo::

   * Can you set verbosity for Robot within Editor?


Alyvix Robot can be run ...



.. _alyvix_robot_cli_result:

*************************
What Alyvix Robot Returns
*************************

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

   ************
   Measurements
   ************

   * How measurement is done (get from v2.7 doc?)
   * How Alyvix is integrated with monitoring/ITOA (NetEye is one example of monitoring)
   * Conceptual:  what gets measured and how (appear + disappear)
   * See keynote slides with frame grabber / transaction performance slide
