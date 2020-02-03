:author: Charles Callaway
:date: 06-12-2019
:modified: 03-02-2020
:tags: designer, gui, overview
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_designer_interface_overview:

****************************
Designer: Interface Overview
****************************

The Alyvix Designer interface consists of two elements:

* A screen capture image for creating and sizing **selections** and **regions of interest**
* A panel for indicating how those visual elements should be interpreted and interacted with

Although Designer is intended to be used in conjunction with Alyvix Editor, you can also run it
as a standalone component from the command line as follows (you can find information about its
:ref:`command arguments here <test_case_building_designer_launch>`):

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> alyvix_designer

When Designer starts, it captures the current screen, turning it white for a few seconds to
indicate the capture process is underway.  Once that's done, it displays the screen capture at
full screen resolution with purple crosshairs that track the mouse, and the reminder
:nobutton:`PRESS ESC TO OPEN DIALOG` overlaid at the top left as shown here:

.. image:: images/ad_main_screen_edit_message_h150.png
   :class: image-boxshadow
   :alt: The initial Alyvix Designer selection cursor

.. tip::  Having a second monitor will enable you to mark selections and regions of interest with
   Alyvix on one screen, while the second screen can still be used for other applications.

Each screen capture is part of a **test case object**, which can recognize and interact with up
to three groups of visual elements.  The color of the crosshairs indicates whether you are working
with the first (purple/red), second (green), or third (blue) group.

.. _alyvix_designer_interface_descriptions:

Pressing :kbd:`Escape` will bring up the Designer interface as in the following screenshot, where
no groups have yet been defined.  The principle interface elements are:

.. image:: images/ad_main_screen_initial_numbered.png
   :height: 500
   :alt: The empty Alyvix Designer interface
   :target: ../_images/ad_main_screen_initial_numbered.png

.. rst-class:: bignums

#. The **Object name** (title) of the test case object, which together with the filename is used to
   uniquely identify this test case in Alyvix Selector and Editor
#. **Test case** :ref:`options <alyvix_designer_options_test_case>`, which affect all screen
   capture elements
#. The **Screen capture** :ref:`Component Tree <alyvix_designer_component_tree_top>` that lists all
   defined regions of interest on the screen that can be interacted with along with their type
   (image, region or text)
#. **Component** :ref:`options <alyvix_designer_options_components>`, which depend on the type
   you assign to the recognized object
#. **Interface controls** that allow you to either
   :ref:`continue editing regions, or exit Designer <alyvix_designer_interface_controls>`.

When Designer is started without any arguments as above, it assigns the default name
:guilabel:`VisualObject1` to the test case object, along with the default
:ref:`options <alyvix_designer_options_test_case>`
:guilabel:`Appear`, :guilabel:`Timeout [sec]: 10`, and :guilabel:`Break: Yes`.

Whenever there are no visual elements selected from the screen capture, the component tree is
empty with only a single root element marked :greyblock:`S` and the thumbnail of the full
screen capture.



.. _alyvix_designer_region_bounding:

=================================================
Selections, Subselections and Regions of Interest
=================================================

To add a new visual component to the tree, you must be in capture mode.  If instead Designer or
Editor is visible, press :wbutton:`EDIT` in the bottom right hand of the panel to return to the
screen capture interface with the crosshairs.

Selections and subselections are made with the mouse in one of two ways:

* Hold the left mouse button down to create a selection or subselection (drawing a rectangle around
  the desired area), and then release when done.
* Right click on a visual element to **autocontour** it, using Alyvix's visual recognizer to
  automatically determine the relevant selection or subselection.  Candidate elements can be shown
  by pressing :kbd:`Space`, and then pressing it a second time to return to the standard screen
  capture.

For instance, you can manually select the Windows Start button using the left mouse button as
shown in the middle image here:

.. image:: images/ad_screen_capture_combined.png
   :alt: Before and after creating a selection in the screen capture.
   :target: ../_images/ad_screen_capture_combined.png

After making a **selection**, you can then begin to make up to 4 **subselections** within a single
group whose position will always be relative to the main selection.  For instance in the example
image above, a subselection has been made containing the Windows Cortana search box.

Unlike the main selection, a subselection consists of two boxes rather than one.  You can
resize the two boxes independently, although the smaller box, which is the subselection itself,
will always remain contained within the larger one, known as the **Region of Interest**.  The
smaller box represents what Alyvix should look for, while the region of interest represents the
space in which it should search for that subselection.

.. tip::

   Making the Region of Interest wider or taller can be very helpful for GUI elements that "float",
   such as when a window or panel is resized.

In order for a group to be considered **matched**, ALL selections and subselections (within their
region of interest) must match the screen at the same time.

The following shortcuts are available:

.. table::
   :widths: 30 20 50

   +---------------------------+--------------+----------------------------------------------------+
   | **Shortcut**              | **Focus on** | **Resulting Action**                               |
   +---------------------------+--------------+----------------------------------------------------+
   | :kbd:`Right Click`        | ROI Edges    | Push the selected RoI's edge all the way to the    |
   |                           |              | border of the screen.                              |
   +---------------------------+--------------+----------------------------------------------------+
   | :kbd:`Ctrl + Left Click`  | Subselection | Reset all RoI edges of the subselection to their   |
   |                           |              | defaults.                                          |
   +---------------------------+--------------+----------------------------------------------------+
   | :kbd:`Ctrl + Right Click` | Component    | Remove an entire component (subselection and ROI). |
   |                           |              | Remove a selection if it has no children.          |
   +---------------------------+--------------+----------------------------------------------------+
   | :kbd:`Ctrl + Z`           | Component    | Undo the most recently added component             |
   +---------------------------+--------------+----------------------------------------------------+
   | :kbd:`Ctrl + Y`           | Component    | Re-add the component just removed                  |
   +---------------------------+--------------+----------------------------------------------------+


.. _alyvix_designer_interface_return_from_sc_mode:

==================================
Returning from Screen Capture Mode
==================================

When in screen capture mode, pressing the :kbd:`Escape` key will return you to either the Alyvix
Editor or Designer interface.  After making new selections and subselections, they will appear as
components within the :ref:`Component Tree <alyvix_designer_component_tree_top>` as shown here
(the type of the component has been :ref:`changed <alyvix_designer_component_tree_types>`
from :guilabel:`Image` to :guilabel:`Text`):

.. image:: images/ad_main_screen_new_component2.png
   :class: image-boxshadow
   :alt: Adding a first component in the Alyvix Designer interface

The main selection (the Windows Start button) is automatically set as the group element, while
the second selection (the Cortana search box) is set as a component within that group.



.. _alyvix_designer_interface_controls:

==================
Interface Controls
==================

Below the component tree at the bottom of the Designer panel are three actions:

* :bbutton:`OK` --- Save the current test case and exit.  If you did not supply a file name when you
  started Designer, it will use the value for :guilabel:`Object name` as the file name.
* :nobutton:`CANCEL` --- Exit Designer without saving the test case.
* :wbutton:`EDIT` --- Return to the screen capture interface.
