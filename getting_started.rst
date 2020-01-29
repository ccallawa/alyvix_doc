:author: Charles Callaway
:date: 04-12-2019
:modified: 15-01-2020
:tags: getting, started, beginner
:lang: en-US
:translation: false
:status: draft

.. include:: sphinx-roles.txt


.. _getting_started_top:

###############
Getting Started
###############

Before continuing, make sure you've already :ref:`installed Alyvix <install_release_top>`.

For the examples in this section, you'll need to run the Windows Command Prompt
(**Start > Windows System > Command Prompt**) and switch to the directory where you want to
keep your test cases, e.g.:

.. code-block:: doscon
   :class: short-code-block

   C:\> cd C:\Alyvix\testcases

Each subsequent example builds on the previous example, so it is important to try them in order.

Walking through the steps of the examples below will give you a pretty good idea of
how the Alyvix interface works.

.. rst-class:: bignums-xxl

#. Open the Windows :ref:`Start Menu <getting_started_example_start>` with Alyvix Editor

   * Build a simple test case that looks for and clicks on the Windows Start button
   * Run the test case, so that Alyvix actually opens the Window Start Menu

#. Open the :ref:`Start Menu, then the Settings app <getting_started_example_settings>` as two
   separate test cases

   * Build two separate test cases, where the second depends on the results of the first
   * Join them together to create a combined action
   * Execute the test cases, checking that they work together

#. Use Selector to :ref:`quickly replicate test cases <getting_started_selector_top>`

   * Use Selector to load one of your existing test cases
   * Replicating the test cases
   * Use Robot to see the results

#. Use Editor to :ref:`script a simple test case <getting_started_editor_top>`

   * Start Editor with the prior test case
   * Use Selector to drag & drop some test case objects
   * Create a script on those objects in Editor
   * Run the resulting scripted test case


.. todo::

   * CC: Add links from the subpages to the basic_concepts page when ready


.. toctree::
   :maxdepth: 2
   :name: toc_test
   :hidden:

   getting_started/windows_start_button.rst
   getting_started/windows_settings.rst
   getting_started/using_selector.rst
   getting_started/using_editor.rst
