:author: Charles Callaway
:date: 04-12-2019
:modified: 31-01-2020
:tags: getting, started, beginner
:lang: en-US
:translation: false
:status: final

.. include:: sphinx-roles.txt


.. _getting_started_top:

###############
Getting Started
###############

Before using Alyvix, you'll first need to :ref:`take a minute to install it <install_release_top>`.

To follow along with the examples in this section on your own system, you'll need to open the
Windows Command Prompt (**Start > Windows System > Command Prompt**) and switch to the directory
where you want to keep your test cases, for example:

.. code-block:: doscon
   :class: short-code-block

   C:\> cd C:\Alyvix\testcases

Walking through the steps of the examples below will give you a pretty good idea of
how the Alyvix interface works.

.. rst-class:: bignums-xxl

#. Example:  Open the Windows :ref:`Start Menu <getting_started_example_start>` with Alyvix Editor

   * Build a simple test case that looks for and clicks on the Windows Start button
   * Run the test case, so that Alyvix actually opens the Window Start Menu

#. Example:  Open the Start Menu, then the :ref:`Settings app <getting_started_example_settings>`
   immediately afterwards

   * Build a second test case object, where the second depends on the results of the first
   * Add the new step to the workflow from the previous example
   * Execute the test cases, checking that they work together


.. note::  You can find further examples, conceptual descriptions, and production-centered use
           cases on the :ref:`Video and Tutorial <video_tutorials_top>` page.


.. toctree::
   :maxdepth: 2
   :name: toc_getting_started
   :hidden:

   getting_started/install.rst
   getting_started/windows_start_button.rst
   getting_started/windows_settings.rst
