:author: Charles Callaway
:date: 4-12-2019
:modified: 13-12-2019
:tags: install, configure, python
:lang: en-US
:translation: false
:status: draft

.. role:: warn
   :class: redbold


.. _install_upgrade_install:

******************************
Installation and Configuration
******************************

This section will show you how to install and configure Alyvix, including its dependencies.



.. _getting_started_python_install:

===================
Python Installation
===================

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

#. Download and install *pip*, the `Python packaging tool <https://pypi.org/project/pip/>`_.  For
   special cases such as installing behind a proxy, see the
   `pip installation page <https://pip.pypa.io/en/stable/installing/>`_.

   * Open a command prompt **as administrator**
   * For earlier versions of Windows, `download pip <https://bootstrap.pypa.io/get-pip.py>`_ with
     your browser.  If you are running one of the latest versions of Windows 10, you can use
     *curl* directly:

     .. code-block:: doscon
        :class: medium-code-block

        C:\Python37> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

   * Then install the downloaded file, for example:

     .. code-block:: doscon
        :class: short-code-block

        C:\Python37> python.exe get-pip.py

     Note that installing *pip* also installs *setuptools* and *wheel*
   * Before using *pip*, upgrade it to the latest version:

     .. code-block:: doscon
        :class: short-code-block

        C:\Python37> python.exe -m pip install -U pip

#. Use *pip* to install the following additional required packages:

   .. code-block:: doscon

      C:\Python37> pip install alabaster Flask gevent opencv-python Pillow tesserocr

   You can find more information about these packages at the following links:

   .. hlist::
      :columns: 3

      * `alabaster <https://pypi.org/project/alabaster/>`_
      * `Flask <https://pypi.org/project/Flask/>`_
      * `gevent <https://pypi.org/project/gevent/>`_
      * `opencv-python <https://pypi.org/project/opencv-python/>`_
      * `Pillow <https://pypi.org/project/Pillow/>`_
      * `tesserocr <https://pypi.org/project/tesserocr/>`_


.. todo::

   * Double check the full install instructions by installing on a blank Windows machine
   * Can we install a Sphinx extension to add a "Copy to Clipboard" button to each code block?
     Like `copybutton <https://sphinx-copybutton.readthedocs.io/en/latest/>`_ ?  Another option is to
     `add our own to the template <https://www.dannyguo.com/blog/how-to-add-copy-to-clipboard-buttons-to-code-blocks-in-hugo/>`_
     `Also see the RTD instructions <https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html>`_



.. _getting_started_third_party_install:

====================
Third Party Software
====================

For character recognition, Alyvix uses Tesseract OCR, which you can
`download here <https://github.com/simonflueckiger/tesserocr-windows_build/releases>`_.
Ensure that the version you select is 64-bit and compatible with the version of Python
you installed in the step above.

.. todo::

   * Is this section necessary?  It's a *.whl* file, so is it already installed when *tesserocr*
     is installed above?  Not sure because the *tesserocr* package says it's a wrapper.



.. _getting_started_alyvix_install:

===================
Alyvix Installation
===================

Alyvix itself is also installed via *pip*:

.. code-block:: doscon

   C:\Python37> pip install alyvix3

This will place the Alyvix executables in the directory :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\`.
You should maintain a separate directory where you will place your Alyvix testcases.
By adding the Alyvix executables to your path, you can use them while remaining in the directory
where you store your testcases.

.. todo::

   * Put Alyvix \*.exe files on an executable path?
   * Where to put the .alyvix files?
   * Will there eventually be an interface that's not via the command line?
   * Deployment check (could we have a simpler version of the v2.7.5 "Deployment check"?)
   * Perhaps run a version test in a shell like for alyvix_designer.py
   * Perhaps a NetEye-style "health check" service for everything at once?  Similar to Alyvix 2's
     "Deployment check", but scripted?
   * An Alyvix test/robot to test click on an Alyvix interface?
   * Does v3.0.0 still have the red warnings mentioned in the v2.7 installation instructions?
   * Is "Install background service" still relevant in v3?



.. _getting_started_alyvix_configure:

====================
Alyvix Configuration
====================

.. todo::

   * Does Alyvix actually need any configuration beyond paths/variables?
   * Do we need to add :file:`C:\\Python37\\Lib\\site-packages\\alyvix\\ide\\*` or any similar
     :file:`site-packages\\alyvix` directories to the path?
   * Are the offline installation instructions from Alyvix 2.* still relevant?
   * Once all installation instructions are written, test it (on multiple OS versions)
