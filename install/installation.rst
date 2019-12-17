:author: Charles Callaway
:date: 4-12-2019
:modified: 17-12-2019
:tags: install, python, pip
:lang: en-US
:translation: false
:status: draft

.. role:: warn
   :class: redbold


.. _install_release_install:

************
Installation
************

This section will show you how to install Alyvix, including its dependencies.



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

#. Install Python by right-clicking on the executable and selecting **"Run as Administrator".**
   The preferred location is :file:`C:\\Python37\\`.  Be sure that Python is added to your path
   (i.e., the path containing the Python executable is in your *environment variables* under
   ``Path``).  The path is correct if the following command returns a version rather than an error:

   .. code-block:: doscon
      :class: short-code-block

      C:\> python --version
      Python 3.7.5




.. _install_release_alyvix_install:

===================
Alyvix Installation
===================

Alyvix itself is also installed *pip*, the official Python package manager:

.. code-block:: doscon

   C:\Python37> pip install alyvix3

This will place the Alyvix executables in the directory :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\`.
You should maintain a separate directory where you will place your Alyvix test cases, for instance
:file:`C:\\Users\\<username>\\Desktop\\Alyvix\\Testcases\\`.  By adding the Alyvix executables to
your path, you can use them while remaining in your test case directory.


.. todo::

   * Recommend to users where they should put their .alyvix files?
   * How to put Alyvix \*.py files on an executable path? (e.g.
     :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\*`) so they don't have to be in the
     same directory as the .alyvix files?
   * Once all installation instructions are written, test it (on multiple OS versions, completely
     fresh install)
