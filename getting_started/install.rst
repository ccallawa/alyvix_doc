:author: Charles Callaway
:date: 06-12-2019
:modified: 12-02-2020
:tags: install, python, pip
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt


.. _install_release_top:

************************
Installation and Upgrade
************************

Before installing Alyvix, first check that your setup meets the system requirements.
If it does, you will then need to install Python on your Windows machine before installing
Alyvix itself.

|



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

|



.. _install_release_python_install:

=================
Installing Python
=================

Follow this procedure to install Python on your system:

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
   error message (if not, you will need to edit your ``Path`` environment variable):

   .. code-block:: doscon
      :class: short-code-block

      C:\> python --version
      Python 3.7.6

|



.. _install_release_alyvix_install:

=================
Installing Alyvix
=================

Alyvix itself is installed via *pip*, the official Python package manager.  *pip* will
automatically detect that your system is running Python 3 and will install Alyvix 3,
placing all executables in the directory
:file:`C:\\Python37\\Lib\\site-packages\\alyvix\\`.

As with the installer, this command prompt must also be **started in Adminstrator mode**.  Only
this single step is required:

.. rst-class:: bignums

#. Run the following command to download and install the latest Alyvix master release along
   with all of its dependencies:

   .. code-block:: doscon
      :class: short-code-block

      C:\> pip install alyvix

You should place your Alyvix test cases in a separate data directory.

|



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

|



.. _install_offline_install:

====================
Offline Installation
====================

In order to create an offline installation, you will need two machines:

* An internet-connected *installer* machine with a working Python 3 installation to serve as a
  source for downloading the required software packages
* A second *target* machine that will serve as the offline probe

Both machines must meet the second :ref:`system requirement <system_requirements_top>` above, and
have access to removable media in order to physically transfer the software from the *installer*
to the *target*.

The following steps will then enable you to install Alyvix on the target machine:

.. rst-class:: bignums

#. On the *installer* Windows **64-bit** machine with an existing **Python 3** installation
   (not Python 2):

   * Create a new directory with appropriate permissions
   * Download the |python-download-link| to that directory
   * Download the Alyvix application and its dependencies with this command:

     .. code-block:: doscon
        :class: short-code-block

        C:\...\MyFolder> pip download alyvix

#. Copy the entire directory onto the removable media, then copy that directory onto the target
   machine

#. Use the Python installer now on the target machine to
   :ref:`install Python following the instructions above <install_release_python_install>`

#. Open a command prompt in the directory on the target machine and install Alyvix with this
   command:

   .. code-block:: doscon
      :class: code-block

      C:\...\MyFolder> pip install alyvix-3.0.0-cp37-cp37m-win_amd64.whl --no-index --find-links .

#. Check that the installation was successful by starting Alyvix Editor:

   .. code-block:: doscon
      :class: tiny-code-block

      C:\> alyvix_editor

   If the :ref:`Editor window <alyvix_editor_interface_top>` appears, the installation was
   successful.
