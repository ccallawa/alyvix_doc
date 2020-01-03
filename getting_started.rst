:author: Charles Callaway
:date: 04-12-2019
:modified: 03-01-2020
:tags: getting, started, beginner
:lang: en-US
:translation: false
:status: draft


.. _getting_started_top:

###############
Getting Started
###############

Before continuing, make sure you've already :ref:`installed Alyvix <install_release_top>`.

For the examples in this section, you'll need to run the Windows Command Prompt and switch to
the directory where you want to keep your test cases, e.g.:

.. code-block:: doscon

   C:\> cd C:\Users\<username>\Desktop\Alyvix\Testcases\


Once you've walked through the steps for the examples below, you'll have a pretty good idea of
how Alyvix works:

.. rst-class:: bignums-xxl

#. :ref:`Check that Alyvix is working <getting_started_example_test>` with a minimal test

   * Show Python and Alyvix are working at the command prompt with ``--version``
   * Launch Alyvix Designer from the command prompt with no arguments and exit

#. Open the Windows :ref:`Start Menu <getting_started_example_start>` with Alyvix

   * Build a simple test case that looks for and clicks on the Windows Start button
   * Run the test case, so that Alyvix actually opens the Window Start Menu

#. Open the :ref:`Start Menu, then Settings App <getting_started_example_settings>` with two
   separate test cases

   * Build two separate test cases, where the second depends on the results of the first
   * Join them together to create a combined action
   * Execute the test cases, checking that they work together

.. #. A slightly :ref:`more difficult task <getting_started_workflow>`

   * Page with immediate test working instructions

.. Once you've mastered these Alyvix basics, why don't you try something a bit harder like
   a tutorial in our :ref:`Tutorials section <tutorials_top>`?



.. toctree::
   :maxdepth: 2
   :name: toc_test
   :hidden:

   getting_started/simple_working_test.rst
   getting_started/windows_start_button.rst
   getting_started/windows_settings.rst

.. getting_started/typical_workflow.rst
