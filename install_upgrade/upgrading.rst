:author: Charles Callaway
:date: 4-12-2019
:modified: 13-12-2019
:tags: how-to
:lang: en-US
:translation: false
:status: draft


.. _install_upgrade_upgrade:

****************
Upgrading Alyvix
****************

Upgrading Alyvix will ensure that you have the latest features, bugfixes, and security patches.
Follow the Alyvix website or twitter feed to find out when a new upgrade is available.  The
versions assigned to each Alyvix upgrade follows the
`Semantic Versioning 2.0 <https://semver.org/>` initiative.

Upgrading is easy, there are only two steps:

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

      C:\\> pip install --upgrade alyvix

And the upgrade process is now complete.


.. todo::

   * How do we communicate when upgrades are available?  Is there a regular schedule?
   * Can something go wrong during the upgrade?  How is it fixed, in general?  Can a "health check"
     like Alyvix 2's "Deployment check" be run automatically after the update has finished?
   * Do we need to mention any extra info like repositories, URLs, websites, etc.?



.. _install_upgrade_release_notes:

=============
Release Notes
=============

The release notes for each version list all new features, bug fixes, and security patches
contained in that release.



.. _install_upgrade_v3_0_0:

-------------
Version 3.0.0
-------------

Version 3.0.0 is the first released version of Alyvix 3.
