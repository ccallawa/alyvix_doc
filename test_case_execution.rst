:author: Charles Callaway
:date: 5-12-2019
:modified: 03-01-2020
:tags: robot
:lang: en-US
:translation: false
:status: draft


.. _test_case_execution_top:

Description of Alyvix Robot

.. todo::

   Everything still to do in Alyvix Robot

###################
Test Case Execution
###################


.. _alyvix_robot_cli_options:
.. topic:: Launching Alyvix Robot

   Alyvix Robot can be run as follows if the Alyvix file path (e.g.,
   :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\core\\`)
   is included in your :guilabel:`Path` environment variable:

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_robot.py

For instance, if you have the file :file:`my_test.alyvix` saved with the object name ``open``,
you can call:

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_robot.py --filename my_test -o open

The following options are available:

+---------------+----------+----------------------------------------------+
| Option        | Shortcut | Description                                  |
+---------------+----------+----------------------------------------------+
| --args        | -a       | Arguments to pass                            |
+---------------+----------+----------------------------------------------+
| --filename    | -f       | Supply the file name with no extension       |
+---------------+----------+----------------------------------------------+
| --help        | -h       | Display command help                         |
+---------------+----------+----------------------------------------------+
| --object      | -o       | Supply the Object name                       |
+---------------+----------+----------------------------------------------+



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



.. Hidden section on Measurement (uncomment when ready)

   ============
   Measurements
   ============

   * How measurement is done (get from v2.7 doc?)
   * How Alyvix is integrated with monitoring/ITOA (NetEye is one example of monitoring)
