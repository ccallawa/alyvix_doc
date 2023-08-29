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

#. Example:  Launch a web browser and :ref:`monitor a web page <getting_started_web_browser>`

   * Launch an application by its executable path with command line parameters
   * Measure how long it takes for the application to launch
   * Kill the application so it can be launched the next time the test case runs
   * Best practices when builiding test cases

#. Example:  Log in to a web app :ref:`using credentials <getting_started_authentication>`

   * Use the credentials and a private key to create encrypted credentials
   * Launch the web app as in the previous example and click on the login button
   * Use the encrypted credentials in the login fields (Alyvix will automatically decrypt them)
   * Do a simple task and then log out

|

.. note::  You can find further examples, conceptual descriptions, and production-oriented use
           cases on the :ref:`Video Tutorials <video_tutorials_top>` page.

|
|
|

-----

|



.. toctree::
   :name: toc_getting_started

   getting_started/install.rst
   getting_started/windows_start_button.rst
   getting_started/windows_settings.rst
   getting_started/web_browser.rst
   getting_started/authentication.rst
