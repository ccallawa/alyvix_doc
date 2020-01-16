:author: Charles Callaway
:date: 06-12-2019
:modified: 15-01-2020
:tags: designer, gui, overview
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _alyvix_designer_interface_overview:

****************************
Designer: Interface Overview
****************************

The interface for Alyvix Designer consists of two elements:

* A screen capture image to use for selecting and resizing Regions of Interest
* An editor panel for indicating how those regions should be interpreted and interacted with

To illustrate how it works, run Designer with no arguments from the command line as follows
(you can find information about its
:ref:`command arguments here <test_case_building_designer_launch>`):

.. code-block:: doscon
   :class: short-code-block

   C:\Alyvix\testcases> python alyvix_designer.py

The screen will turn white for a few seconds.  When it returns, you will see a copy of the screen
with the phrase :nobutton:`PRESS ESC TO OPEN DIALOG` at the top left, while purple/red crosshairs
will track the mouse as shown here:

.. image:: images/ad_main_screen_edit_message.png
   :class: image-with-boxshadow
   :height: 150
   :alt: The initial Alyvix Designer selection cursor
   :target: ../_images/ad_main_screen_edit_message.png

.. tip::  Having a second monitor will enable you to mark regions of interest with Alyvix on one
   screen, while the second screen can still be used for other applications.

In Alyvix Designer, the color of the crosshairs indicates whether you are working with the first
(purple/red), second (green), or third (blue) object group.

.. _alyvix_designer_interface_descriptions:

If you press :kbd:`Escape`, you will see the default Designer interface as in the following
screenshot.  The principle interface elements are:

.. image:: images/ad_main_screen_initial_numbered.png
   :height: 500
   :alt: The empty Alyvix Designer interface
   :target: ../_images/ad_main_screen_initial_numbered.png

.. rst-class:: bignums

#. The **Object name** (title) of the test case object, which together with the filename is used to
   uniquely identify this test case in Alyvix Selector and Editor
#. **Test case** :ref:`options <alyvix_designer_options_test_case>`, which affect all screen
   capture elements
#. The **Screen capture** :ref:`Component Tree <alyvix_designer_component_tree>` that lists all
   defined regions of interest on the screen that can be interacted with along with their type
   (image, region or text)
#. **Component** :ref:`options <alyvix_designer_options_components>`, which depend on the type
   of the recognized object
#. **Interface controls** that allow you to either
   :ref:`continue editing regions, or exit Designer <alyvix_designer_interface_controls>`.

Since we started Designer above without any arguments, it assigned the default name
:guilabel:`VisualObject1` to the object, along with the default options :guilabel:`Appear`,
:guilabel:`Timeout(s): 10`, and :guilabel:`Break: Yes`.

Also, since we have yet to select any screen capture elements, the component tree has only a single
root element marked :greyblock:`S` along with a thumbnail of the screen capture.



.. _alyvix_designer_region_bounding:
.. topic:: Regions of Interest and Bounding Boxes

   To add a visual component to the tree, press :wbutton:`EDIT` in the bottom right hand of the
   Designer panel.  This will return us to the screen capture interface with the crosshairs.

Using the mouse, move to the bottom left of the screen and select the area around the Windows
Start button.  It should now be similar to the middle image here:

.. image:: images/ad_screen_capture_combined.png
   :alt: Before and after selecting a rectangle in the screen capture.
   :target: ../_images/ad_screen_capture_combined.png

Next, select a new area in the search box to the right of the Start button, staying in the first
(purple/red) group.  This time you will see two red boxes rather than one.  You can resize them
independently, although the smaller box will always remain contained with the larger one.

Place the smaller box over the word "Search", and size the larger box so that it almost fills up
the search box as on the right side of the screenshot above.  The smaller box represents what
Alyvix should look for, while the larger box represents the space in which it should search.
Making the larger box wider or taller can be very helpful for GUI elements that "float", such as
when a browser window is resized.

Note that there is an important distinction between the two types of selections we made:  the first
selection only has one bounding box, which represents the Region of Interest.  It is used as
the anchor of a group of one to four additional interaction areas.

Now, press the :kbd:`Escape` key to bring up the Designer interface again.  You should see
the new components you just selected in the :ref:`Component Tree <alyvix_designer_component_tree>`
interface shown here (the type of the component has been manually changed to :guilabel:`Text`
from :guilabel:`Image`):

.. image:: images/ad_main_screen_new_component2.png
   :class: image-with-boxshadow
   :alt: Adding a first component in the Alyvix Designer interface
   :target: ../_images/ad_main_screen_new_component2.png

Our first region selection automatically created this group, while our second selection created
a component within that group.



.. _alyvix_designer_interface_controls:
.. topic:: Interface Controls

   Below the component tree at the bottom of the Designer panel are three actions:

* :bbutton:`OK` --- Save the current test case and exit.  If you did not supply a file name when you
  started Designer, it will use the value for :guilabel:`Object name` as the file name.
* :nobutton:`CANCEL` --- Exit Designer without saving the test case.
* :wbutton:`EDIT` --- Return to the screen capture interface.

For now, press the :nobutton:`CANCEL` button to exit without creating an object.



.. _alyvix_designer_interface_reading:
.. topic:: Further Information

   To learn more about interacting with the visual elements and what they can do, see the
   :ref:`Component Tree <alyvix_designer_component_tree>` page.

You can find more information about the available options for test cases and components on the
:ref:`Interface Options <alyvix_designer_options>` page.

The :ref:`Test Case Data Format <test_case_data_format_top>` page provides technical details on how
Alyvix Designer files are organized and what they contain.

Finally, the :ref:`Getting Started example <getting_started_example_start>` for Designer provides
step-by-step instructions on using Designer as part of a simple workflow.
