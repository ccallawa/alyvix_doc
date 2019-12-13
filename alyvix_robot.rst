:author: Charles Callaway
:date: 5-12-2019
:modified: 13-12-2019
:tags: robot
:lang: en-US
:translation: false
:status: draft


.. _alyvix_robot_top:

Description of Alyvix Robot

.. todo::

   Everything still to do in Alyvix Robot

************
Alyvix Robot
************


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

   Alyvix Robot will give you output like this.

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_robot.py --filename my_test -o open
   2019/12/12 18:24:20.405: start starts
   2019/12/12 18:24:21.949: open DETECTED in 0.0s (+/-0.060)
   2019/12/12 18:24:21.950: start ends OK, it takes 1.544s.



.. toctree::
   :maxdepth: 2
   :name: toc_test
   :hidden:

   alyvix_robot/robot_start.rst
   alyvix_robot/robot_medium.rst
   alyvix_robot/robot_advanced.rst
