:author: Charles Callaway
:date: 06-12-2019
:modified: 07-02-2020
:tags: install, python, pip
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _install_release_top:

************
Installation
************

Before installing Alyvix, first check that your setup meets the system requirements.
If it does, you will then need to install Python on your Windows machine before installing
Alyvix itself.



.. _system_requirements_top:

===================
System Requirements
===================

.. note::

   Alyvix assumes that you have **one virtual or physical machine** exclusively dedicated to
   running Alyvix test cases.

You should check that your designated machine meets the following requirements before you install
Alyvix:

.. admonition::  Requirements
   :class: warning

   * Screen color depth:  24-bit RGB or 32-bit RGBA
   * OS: **Windows 64-bit** 10, 8, 7, Server 2012 or Server 2016 (32-bit versions of Windows
     are :warn:`not` compatible with Alyvix)



.. _install_release_python_install:

=================
Installing Python
=================

Install Python as follows:

.. rst-class:: bignums

#. Download the |python-download-link|.
   Alyvix is :warn:`not` compatible with 32-bit versions of Python.

#. Start the installation by right-clicking on the executable and selecting **"Run as administrator"**.
   Check the box "Add Python 3.7 to PATH" and then choose **"Customize installation"**.

   .. image:: images/python-install-01.png
      :width: 75%
      :alt: The first panel of the python installation process.

#. On the second panel all the option boxes should already be checked.  Click **"Next"** to
   continue.

   .. image:: images/python-install-02.png
      :width: 75%
      :alt: The second panel of the python installation process.

#. On the third panel, make sure the advanced options are set as shown below.  Then under
   **"Customize install location"**, insert the recommended location :file:`C:\\Python37\\`.
   Finally, click on **"Install"**.  At this point Python will begin installing, typically
   requiring about 5 minutes.

   .. image:: images/python-install-03.png
      :width: 75%
      :alt: The third panel of the python installation process.

#. The installation is correct if the following command returns a version number rather than an
   error message (if not, you will need to edit your *Environment variables* under ``Path``):

   .. code-block:: doscon
      :class: short-code-block

      C:\> python --version
      Python 3.7.6



.. _install_release_alyvix_install:

=================
Installing Alyvix
=================

Alyvix itself is installed via *pip*, the official Python package manager.  *pip* will
automatically detect that your system is running Python 3 and will install Alyvix 3,
placing all executables in the directory
:file:`C:\\Python37\\Lib\\site-packages\\alyvix\\`.

As above, this command prompt must also be **run in Adminstrator mode** (or simply reuse the
previous command prompt).  Only this single step is required:

.. rst-class:: bignums

#. .. raw:: html

      <br />

   .. code-block:: doscon
      :class: short-code-block

      C:\> pip install alyvix

You should place your Alyvix test cases in a separate data directory.



.. _install_upgrade:

================
Upgrading Alyvix
================

Only two steps are needed to upgrade to the latest version:

.. rst-class:: bignums

#. Close Alyvix

   * Save all of your currently open projects
   * Close all Alyvix user interfaces and applications
   * Terminate all running Alyvix processes

#. Upgrade Alyvix with *pip*

   * Start a Command Prompt **in administrator mode**
   * Run the following command to download and upgrade to the latest Alyvix master release along
     with all of its dependencies:

     .. code-block:: doscon
        :class: short-code-block

        C:\> pip install --upgrade alyvix
