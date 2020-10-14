:author: Charles Callaway
:date: 06-12-2019
:modified: 22-05-2020
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

The Alyvix installer is launched from the command prompt that, like the Python installer, must be
**started in Adminstrator mode**.  Only this single step is required:

.. rst-class:: bignums

#. Run the following command to download and install the latest Alyvix master release along
   with all of its dependencies:

   .. code-block:: doscon
      :class: short-code-block

      C:\> pip install alyvix

We recommend you place your Alyvix test cases in a separate data directory.

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

      C:\...\MyFolder> pip install alyvix-3.1.2-cp37-cp37m-win_amd64.whl --no-index --find-links .

#. Check that the installation was successful by starting Alyvix Editor:

   .. code-block:: doscon
      :class: tiny-code-block

      C:\> alyvix_editor

   If the :ref:`Editor window <alyvix_editor_interface_top>` appears, the installation was
   successful.

|



.. _install_uninstall:

==============================
Uninstalling Alyvix and Python
==============================

To uninstall Alyvix, regardless of whether you also want to uninstall Python, run the following
command in a Command Prompt or Power Shell **with Administrator privileges**:

.. code-block:: doscon

   C:\> pip uninstall alyvix

Pip will list the packages to be removed, and then ask for confirmation.

If you only use Python to run Alyvix, you can now also remove Python itself.  Go to
**Start Menu > Windows Settings > Apps**, scroll down, and remove both |python-remove-name| and
:file:`Python Launcher`.  The process may take up to 5 minutes.


Once completed, you can also manually remove the :file:`C:\\Python37\\` directory (or whichever
directory you specified during installation) and either archive or delete your test case
directory.

The Python installer does not remove environment variables, so if desired you can manually
remove them at **System Properties > Environment Variables > System Variables > Path**.

|



.. _install_troubleshooting:

============================
Installation Troubleshooting
============================

Below are some potential installation problems and their solutions.

|accordion-entry|
|right-icon-white| "Python" command does nothing or launches Microsoft Store on Windows 10
|accordion-middle|
This error occurs when during :ref:`installation steps #2 and #4 <install_release_python_install>`
you did not check the boxes to add Python to the path and environment variables.  Typing the
:command:`python` command in the command prompt under this condition will launch Microsoft Store
in an attempt to install it from there.

To correct this situation you will need to either (1) uninstall and then reinstall Python, or
(2) manually add the appropriate paths in the **System Properties > Environment Variables** panel.
|accordion-end|

|accordion-entry|
|right-icon-white| "ImportError: DLL load failed" --- Failure to Import Tesseract OCR
|accordion-middle|
This error is caused by a missing dependency of the Tesseract OCR module, which requires that the
file :file:`vcomp140.dll` be present in Windows during installation by *pip*:

.. code-block:: doscon
   :class: nocopy

   File "C:\Python37\lib\site-packages\alyvix\core\tesserocr\__init__.py", line 1, in <module> from ._tesserocr import *
   ImportError: DLL load failed: The specified module could not be found.

You can fix this problem by installing the **Microsoft Visual C++ Redistributable per Visual Studio**,
which contains the required file.  It's available at
:iconlink:`ext|https://aka.ms/vs/16/release/vc_redist.x64.exe|https://aka.ms/vs/16/release/vc_redist.x64.exe`.
|accordion-end|

|
