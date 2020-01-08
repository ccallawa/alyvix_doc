:author: Charles Callaway
:date: 07-01-2020
:modified: 07-01-2020
:tags: editor overview
:lang: en-US
:translation: false
:status: draft


.. _alyvix_editor_interface_top:

*************************
Editor Interface Overview
*************************

Alyvix Editor ... (description) ...

You can start Alyvix Editor by itself from the command prompt:

.. code-block:: doscon

   C:\Alyvix\testcases> python alyvix_editor.py -f <file-name>

You will then see the Editor interface as shown here, which includes Selector and Designer:

.. figure:: images/ae_full_interface_numbered.png
   :align: center
   :alt: Alyvix Editor with Designer and Selector.
   :figwidth: 95%
   :target: ../../test_case_building/images/ae_full_interface_numbered.png

   Fig. 1:  Alyvix Editor with Designer and Selector.


.. rst-class:: bignums

#. Editor, consisting of the :ref:`Management panel <alyvix_editor_interface_management>` and
   the :ref:`Script panel <alyvix_editor_interface_script>`
#. :ref:`Designer <alyvix_designer_interface_overview>`.
#. :ref:`Selector <alyvix_selector_top>`.


.. todo::

   * FM:  Renaming in Selector doesn't automatically rename in Editor Script window.  It changes color
     as if it thinks it were from "SECTIONS", but it's not in that section.  Bug or intentional?
   * FM:  Deleting a section in Editor pops up a JavaScript Q with bad English:
     "Are you sure {you want} to delete section: [object Object]?"  Similarly for the "REMOVE"
     option which asks "Are you sure {you want} to delete steps?"  What's the procedure for informing
     the team about English errors in labels, buttons, and other GUI elements?
   * Although the Editor window consists of Designer and Selector, it seems some of their interface
     elements are visible when they are run alone, but disappear when run together with Editor.
     Is there a reasoning that can be explained simply to users?


The principle interface elements exclusive to the Editor (apart from Selector and Designer) are:

.. figure:: images/ae_main_screen_numbered.png
   :align: center
   :alt: The Alyvix Editor interface.
   :figwidth: 90%
   :target: ../../test_case_building/images/ae_main_screen_numbered.png

   Fig. 2:  The Alyvix Editor components.


.. rst-class:: bignums

#. The  :ref:`menu strip <alyvix_editor_interface_menu>`
#. The main :ref:`script management panel <alyvix_editor_interface_management>`
#. The user-defined Sections list (subroutines) to be added to scripts
#. The user-defined Maps section (for loop over keys in a map) to be added to scripts
#. Panel tab controls: scripting panel & monitor (don't need a full section)
#. The :ref:`scripting panel <alyvix_editor_interface_script>`
#. The script properties (don't need a full section)
#. Panel resizing controls (don't need a full section)



.. _alyvix_editor_interface_menu:

==============
The Menu Strip
==============



* .. rst-class:: fa fasmall fa-play-circle

     Run

* New
* Open
* Save
* Save As
* Exit




.. _alyvix_editor_interface_management:

=======================
Script Management Panel
=======================

Medium-level description here, full details on
:ref:`another page <alyvix_editor_script_mgmt_top>`

* Main
* Fail
* Exit

Other parts:

* Sections
* Maps



.. _alyvix_editor_interface_script:

===================
The Scripting Panel
===================

Medium-level description here, full details on
:ref:`another page <alyvix_editor_scripting_panel_top>`

* Script node types

   * Run + Object
   * If True + Object
   * If False + Object
   * For + Map

* Drag and drop from Selector
