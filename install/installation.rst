:author: Charles Callaway
:date: 04-12-2019
:modified: 09-01-2020
:tags: install, python, pip
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _install_release_install:

************
Installation
************

This section will show you how to install Python and Alyvix.



.. _install_release_python_install:

===================
Python Installation
===================

Install Python as follows:

.. rst-class:: bignums

#. Download the `latest version of Python 3.7 for Windows <https://www.python.org/downloads/>`_.
   For instance, `Python 3.7.5 <https://www.python.org/downloads/release/python-375/>`_ was released
   in October, 2019.  Choose an installer for Windows x86-64 (zip, full or web-based).  Alyvix is
   :warn:`not` compatible with 32-bit versions of Python.

#. Install Python by right-clicking on the executable and selecting **"Run as administrator".**
   The preferred location is :file:`C:\\Python37\\`.  Be sure that Python is added to your path
   (i.e., the path containing the Python executable is in your *Environment variables* under
   ``Path``).  The path is correct if the following command returns a version rather than an
   error message:

   .. code-block:: doscon
      :class: short-code-block

      C:\> python --version
      Python 3.7.5




.. _install_release_alyvix_install:

===================
Alyvix Installation
===================

Alyvix itself is installed via *pip*, the official Python package manager:

.. code-block:: doscon

   C:\Python37> pip install alyvix3

This will place the Alyvix executables in the directory :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\`.
You should place your Alyvix test cases in a separate data directory.
