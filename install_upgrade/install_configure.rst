:author: Charles Callaway
:date: 4-12-2019
:modified: 6-12-2019
:tags: install, configure, python
:lang: en-US
:translation: false
:status: draft


.. _install_upgrade_install:

##############################
Installation and Configuration
##############################

- Generic information
- Download links (sidebar?)



.. _getting_started_python_install:

===================
Python Installation
===================

- Download and install Python (3.7.2) for Windows

   - python-3.7.2-amd64.exe (or .msi ?)
   - Install as administrator
   - Preferred location:  :file:C:/Python37
   - Make sure Python is added to the path
   - Screenshot(s), small

- Download and install *pip* (version?)

   - get-pip.py ?
   - Install as administrator

- Install other packages with *pip*

   - Can this be done with an installation batch file?

.. todo::

   Integrate the .. rst-class:: bignums and bignums-xxl classes from typo3 into the RTD theme



.. _getting_started_third_party_install:

====================
Third Party Software
====================

- Download and install Tesseract OCR (version?)



.. _getting_started_alyvix_install:

===================
Alyvix Installation
===================

- Install Alyvix with *pip*
- Put Alyvix \*.exe files on an executable path?
- Where to put the .alyvix files?
- Will there eventually be an interface that's not via the command line?
- Deployment check

   - Could we have a simpler version of the v2.7.5 "Deployment check"?
   - Perhaps run a version test in a shell
   - A NetEye-style "health check" service, or does it have to be checked manually?
   - An Alyvix test/robot to test click on an Alyvix interface?

- What's recommended, Command Prompt or Powershell?
- Does v3.0.0 still have the red warnings mentioned in the v2.7 installation instructions?
- Is "Install background service" still relevant in v3?



.. _getting_started_alyvix_configure:

====================
Alyvix Configuration
====================

- Are the offline installation instructions still relevant?


.. todo::

   Does Alyvix actually need any configuration beyond paths/variables?


.. todo::

   Once all installation instructions are written, test it (on multiple OS versions)
