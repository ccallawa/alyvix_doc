:author: Charles Callaway
:date: 06-12-2019
:modified: 18-02-2020
:tags: robot, execution, test cases
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _test_case_execution_top:

###################
Test Case Execution
###################

Alyvix test cases you have built with Alyvix Editor can be run using Alyvix Robot.  Robot will
also execute any individual test case objects you have created with Alyvix Designer along with
Alyvix objects you have set up with Alyvix Selector.

In a production environment, the typical use case is to create a set of test cases once, and then
repeatedly run those test cases at regular intervals.  Examples include monitoring the usability
of proprietary clients, streamed applications, and web pages on a remote server.  A test case
may measure responsiveness every 5 minutes, for instance, and send timing and other data to
a monitoring system in the output format it expects.

Before you can use Alyvix in a production environment, however, you will first need to iteratively
develop and improve your test cases.  Here human readable output is more important, and accordingly
there is no output format option within Alyvix Editor.

There are two principal modes for interacting with Alyvix Robot to ensure test cases work
properly during the development phase:

* Calling Robot from the Command Prompt, passing it the name of a test case object, using the
  default **-\\-mode** option
* Calling Robot from :ref:`within Alyvix Editor <alyvix_editor_run_script>` via the |runblue|
  button to run the main script

In either case, one test case is executed at a time.



.. _alyvix_robot_cli_options:


**********************************************
Launching Alyvix Robot from the Command Prompt
**********************************************

When Robot executes a test case via the command prompt, it first checks to see if one or more test
case object names were passed via the **-o** parameter.  If so, Robot will execute those test case
objects in sequence.  Otherwise, if the **-o** parameter is not specified and the :file:`.alyvix`
file test case :ref:`contains a script previously defined by Editor <test_case_data_format_description>`
in its ``script`` field, then Robot will run that script.

Adding the *verbosity* (**-v**) parameter will provide additional information that can help you
should you need to debug your test cases (see the section
:ref:`CLI Output Format <alyvix_robot_result_cli>` below).

Alyvix Robot can be run with the following command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot

If you used Alyvix Editor to create a file named :file:`start-test.alyvix` containing a a test
case object named ``start``, you can run it with this command:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot -f start-test -o start

.. _alyvix_robot_cli_launch:

Robot also allows you to execute multiple test case objects in sequence by putting them in order
in quotation marks after the **-\\-object** parameter, as long as all those objects exist in the
test case:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot -f start-test -o "start settings"

The following options are available:

+---------------+-------+----------+-----------------------------------------------------------+
| Option        | Alias | Argument | Description                                               |
+---------------+-------+----------+-----------------------------------------------------------+
| -\\-args      | -a    | *<strs>* | Supply one or more strings to use in the                  |
|               |       |          | :ref:`String <alyvix_designer_options_strings>`           |
|               |       |          | field of a test case object in Designer                   |
+---------------+-------+----------+-----------------------------------------------------------+
| -\\-filename  | -f    | *<name>* | Supply the file name with or without extension            |
+---------------+-------+----------+-----------------------------------------------------------+
| -\\-object    | -o    | *<name>* | Supply the Object name(s)                                 |
+---------------+-------+----------+-----------------------------------------------------------+
| -\\-mode      | -m    | *<name>* | ``alyvix`` --- CLI output format for humans               |
|               |       |          | (default)                                                 |
|               |       |          |                                                           |
|               |       |          | ``nagios`` --- Nagios output                              |
|               |       |          | :ref:`(see below) <alyvix_robot_result_nagios>`           |
+---------------+-------+----------+-----------------------------------------------------------+
| -\\-verbose   | -v    | *<n>*    | Set the verbosity level for debugging output              |
|               |       |          | ranging from **0** (min) to **2** (max)                   |
|               |       |          |                                                           |
|               |       |          | **0**:  Records start/stop timestamps, state and time     |
|               |       |          | measures for each object (with measure option enabled)    |
|               |       |          |                                                           |
|               |       |          | **1**:  Also logs Alyvix actions                          |
|               |       |          |                                                           |
|               |       |          | **2**:  Also creates annotated screenshots as             |
|               |       |          | separate .png files in the same directory                 |
+---------------+-------+----------+-----------------------------------------------------------+



.. _alyvix_robot_result:

*************************
What Alyvix Robot Returns
*************************

Alyvix uses the following industry-standard return values for monitoring systems:

+-------+--------------+-------------------------------------------------------------------------------+
| Value | Label        | Meaning                                                                       |
+-------+--------------+-------------------------------------------------------------------------------+
| 0     | ``OK``       | The service responded and the results were within expectations                |
+-------+--------------+-------------------------------------------------------------------------------+
| 1     | ``WARNING``  | Action should be taken to prevent a likely near-term problem from becoming    |
|       |              | more serious                                                                  |
+-------+--------------+-------------------------------------------------------------------------------+
| 2     | ``CRITICAL`` | A significant incident has already occurred and should be handled immediately |
+-------+--------------+-------------------------------------------------------------------------------+

Using the **-\\-mode** option, you can specify the format for the information returned (defaults
to CLI output mode).



.. _alyvix_robot_result_cli:

=================
CLI Output Format
=================

When run from the command prompt like this:

.. code-block:: doscon
   :class: medium-code-block

   C:\Alyvix\testcases> alyvix_robot -f start-test

Alyvix Robot will both *(a)* display a short log describing basic events and timing data, and
*(b)* create a new file based on the original test case, but with more detailed time measures
added.  A timestamp corresponding to the moment of execution will be appended to the file name:

:file:`<filename>_<full-timestamp>.alyvix`

For example:

:file:`start-test_20191220_145228_UTC+0100.alyvix`


When run from the command prompt with the default **-m alyvix** parameter, Alyvix Robot will
return human-readable output like the following when successful:

.. code-block:: md

   2019/12/12 18:24:20.405: start starts
   2019/12/12 18:24:21.949: open DETECTED in 0.0s (+/-0.060)
   2019/12/12 18:24:21.950: start ends OK, taking 1.544s.

If it fails instead, the output will appear like this:

.. code-block:: md

   2019/12/12 18:37:41.448: start-test starts
   2019/12/12 18:37:51.762: settings FAILED after 10s
   2019/12/12 18:37:51.763: start-test ends FAILED because of settings, taking 10.315s.

If you have enabled the :ref:`break flag <alyvix_designer_options_test_case>` in Alyvix Selector
for a given test case object, then if that test case object fails, no further test case objects
will be executed.  If it is not set, then the test case object will instead be skipped after
its timeout has expired.

When run from the Windows command prompt, you can access the return value as follows:

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> %errorlevel%
   0



.. _alyvix_robot_result_nagios:

====================
Nagios Output Format
====================

When Alyvix Robot is run from the command prompt, the **-\\-mode nagios** command option
will generate performance data in |nagios-format-link|.  The main status result for the
monitoring check will be one of the following values:

+-----------------------------+----------------------------------------------------------------+
| **test_case_output_status** | **Description**                                                |
+-----------------------------+----------------------------------------------------------------+
| ``OK``                      | When the test case exits with ``OK``                           |
+-----------------------------+----------------------------------------------------------------+
| ``WARNING``                 | When the test case exits with ``OK``, but the performance of   |
|                             | at least 1 object is greater than its warning threshold and    |
|                             | still lower than its critical threshold                        |
+-----------------------------+----------------------------------------------------------------+
| ``CRITICAL``                | When the test case exits with ``OK``, but the performance of   |
|                             | at least 1 object is greater than its critical threshold and   |
|                             | still lower than its threshold threshold                       |
+-----------------------------+----------------------------------------------------------------+
| ``CRITICAL``                | Whenever the test case exits with ``FAILED``                   |
+-----------------------------+----------------------------------------------------------------+

The time measurements for Nagios are specified as follows (note that *object_timeout_s* for
*SKIPPED* must be converted to milliseconds):

+-----------------------------+-----------------------------+-----------------------------------------+
| **Test Case Object Status** | **Format**                  | **JSON Path**                           |
+-----------------------------+-----------------------------+-----------------------------------------+
| ``DETECTED``                | <object_performance_ms>ms   | *object_name>measure>exit>true*         |
+-----------------------------+-----------------------------+-----------------------------------------+
| ``SKIPPED``                 | <object_timeout_s>ms        | *object_name>measure>exit>false*        |
+-----------------------------+-----------------------------+-----------------------------------------+
| ``FAILED``                  | ms |tab| :hint:`(no value)` | *object_name>measure>exit>fail*         |
+-----------------------------+-----------------------------+-----------------------------------------+
| ``NOT EXECUTED``            | ms |tab| :hint:`(no value)` | *object_name>measure>exit>not_executed* |
+-----------------------------+-----------------------------+-----------------------------------------+

**First nagios output line:**

.. code-block:: html

   <test_case_output_status>: <test_case_output_message> | duration=<test_case_duration_s>s;;; <object_01_name>=<object_01_performance_ms>ms;<object_01_warning_s>s;<object_01_critical_s>s;; <object_02_name>=<object_02_performance_ms>ms;<object_02_warning_s>s;<object_02_critical_s>s;;

**Second nagios output line:**

.. code-block:: html

   FAILED transactions (from first to last): <failed_object_01_name>; <failed_object_02_name>

**Third nagios output line:**

.. code-block:: html

   NOT EXECUTED transactions: <not_executed_object_01_name>; <not_executed_object_02_name>




.. Hidden section on Measurement (wait on this for now, uncomment when ready)

   .. _test_case_execution_measurements:

   ************
   Measurements
   ************

   * How measurement is done (get from v2.7 doc?)
   * How Alyvix is integrated with monitoring/ITOA (NetEye is one example of monitoring)
   * Conceptual:  what gets measured and how (appear + disappear)
   * See keynote slides with frame grabber / transaction performance slide
