:author: Charles Callaway
:date: 05-12-2019
:modified: 05-02-2020
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

In a production environment, the typical use case is to create a set of test cases once, and then
repeatedly run those test cases at regular intervals.  An example could be monitoring the usability
of web pages on a remote server, where responsiveness must be measured every 5 minutes.

Before you can use Alyvix in a production environment, however, you will first need to iteratively
develop and improve your test cases.  Alyvix Robot can help you here, too.  There are two
principal modes for interacting with Alyvix Robot to ensure test cases work properly:

* Calling Robot from the Command Prompt, passing it the name of a test case object
* Calling Robot from within Alyvix Editor via the |runblue| button to run the main script

In either case, one test case is executed at a time.



.. _alyvix_robot_cli_options:


**********************************************
Launching Alyvix Robot from the Command Prompt
**********************************************

When Robot executes a test case via the command prompt, it first checks to see if one or more test
case object names were passed via the ``-o`` parameter.  If so, Robot will execute those test case
objects in sequence.  Otherwise, if the ``-o`` parameter is not specified and the :file:`.alyvix`
file test case :ref:`contains a script previously defined by Editor <test_case_data_format_description>` in its ``script``
field, then Robot will run that script.

Adding the *verbosity* (``-v``) parameter will provide additional information that can help you
should you need to debug your test cases.

Alyvix Robot can be run with the following command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot

If you used Alyvix Editor to create a file :file:`start-test.alyvix` containing a a test case
object named ``start``, you can run it with this command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot -f start-test -o start

Robot allows you to execute multiple test case objects in sequence by putting all of them in order
after the ``--object`` parameter, as long as all those objects exist in the test case:

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
| \-\\-mode     | -m       | ``alyvix`` --- CLI output format for humans  |
|               |          |                                              |
|               |          | ``nagios`` ---  |nagios-pivotal-link|        |
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

Alyvix Robot can be run on the test case currently loaded in Editor by pressing the |runblue|
button at the top left.  The starting point is the :guilabel:`main` script specified in the
:ref:`scripting panel <alyvix_editor_script_mgmt_top>`.

The output is the same as when run in the command prompt, but can be found in the
:guilabel:`Console` tab at the top of the
:ref:`scripting panel <alyvix_editor_scripting_panel_top>`.

Currently the verbosity level for Alyvix Robot cannot be set within Editor.


.. todo::

   * CC: Need a screenshot, cannot reuse an old one
   * FM: Can you set verbosity for Robot within Editor?




.. _alyvix_robot_cli_result:

*************************
What Alyvix Robot Returns
*************************

Whether run from the command prompt or within Editor, Alyvix Robot will give you output like the
following if successful:

.. code-block:: md

   2019/12/12 18:24:20.405: start starts
   2019/12/12 18:24:21.949: open DETECTED in 0.0s (+/-0.060)
   2019/12/12 18:24:21.950: start ends OK, it takes 1.544s.

If it fails instead, the output will look like this:

.. code-block:: md

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
