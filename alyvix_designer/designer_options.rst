:author: Charles Callaway
:date: 5-12-2019
:modified: 11-12-2019
:tags: designer
:lang: en-US
:translation: false
:status: draft



.. _alyvix_designer_options:

****************************
Testcase and Element Options
****************************

Parameters and settings for Alyvix Designer are separated into those that affect an entire
testcase, and those that affect a specific element type for a group or component.

All options shown in this panel are used during the execution of a testcase, not when creating it.



.. _alyvix_designer_options_testcase:

================
Testcase Options
================

At the top of the Alyvix Designer panel (see Figure 1) are the options for the testcase as a whole.

.. figure:: images/ad_testcase_options_sized.png
   :alt: The testcase options.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_testcase_options_sized.png

   Fig. 1:  The testcase options.

The **Object name** is the reference name (not the file name) of the testcase object allowing the
testcase to be used in testcase scripts.

There are also three **testcase parameters** that affect how the
:ref:`screen capture elements <alyvix_designer_element_tree_types>` in its element tree
are detected, regardless of their type, and what happens if they fail to be detected.

* **Detection condition:**  One of the following conditions will be checked at a default
  interval of every ``0.5`` seconds

   * **Appear:**  Alyvix will continuously try to detect any of the main group elements (*image*
     or *rect*) on screen if it was not already there when the testcase started
   * **AppearDisappear:**  Alyvix will see whether any of the main group elements appears,
     and then disappears
   * **Disappear:**  If any of the main group elements was present when the testcase started,
     Alyvix will detect when one is no longer visible

* **Timeout:**  The chosen detection condition will be continuously checked until this number
  of seconds is reached
* **Break:**  If this option is ticked, then a timeout will cause the testcase to fail, and
  if it is part of a series of testcases, then the entire series will fail.  If not ticked,
  it will report failure but let the series of testcases continue.

.. todo::

   * Check if the pieces of text above from the 2.7.5 doc are still valid.



.. _alyvix_designer_options_elements:

===============
Element Options
===============

Below the element tree you can find the options that affect a specific instance of an element type
used in an Alyvix testcase.  Whenever you select a row in the element tree, these options will be
updated to reflect the currently assigned options to that row's element.




.. _alyvix_designer_options_elements_root:

--------------------
Root Element Options
--------------------

The *root* element corresponds to the execution phase that will be invoked when Alyvix Robot starts,
before any detection algorithms are run.  This allows you to start or close a particular
application before Alyvix begins looking for any graphical elements.

.. todo::

   * What happens if ``Run`` is set with no path?  Does that correspond to leaving the screen as is?
   * If a testcase is intended to run in series, how do you indicate it should use the current screen?
   * What happens if the arguments aren't right?  Is it a runtime error?
   * Are the arguments fixed, or can you include variables?

.. figure:: images/ad_root_options_sized.png
   :alt: Options for the root element.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_root_options_sized.png

   Fig. 2:  Options for the *root* element.

The **Call** option shown in Figure 2 allows you to select an application either to start or
terminate when the testcase begins.

* The **Run** option lets you start a new application before beginning the testcase.  For instance,
  you could start a browser session with the URL as an argument.  The two parameters it takes are:

   * **Path:**  Either write the full path for an executable file in your environment, or use
     the :guilabel:`SELECT` button to bring up a file selection dialog.
   * **Arguments:**  Here you can enter zero or more arguments to pass to the application when
     it starts up.

* The **Kill** option allows you instead to select a currently running process to terminate.
  It provides a dropdown named **Process**, populated with all running processes, and a filtering
  field that allows you to make a quick selection with just a few keystrokes.



.. _alyvix_designer_options_elements_image:

------------------
Image Type Options
------------------

.. rst-class:: fa fa-image

   The *image* element corresponds to a
   :ref:`matchable image region <alyvix_designer_element_tree_types>`
   on the captured screen, such as an icon.  As shown in Figure 3, it has the following
   visual recognition parameters:

* **Match:**  Only recognize an image that is exactly the same as the one selected during screen capture.
* **Color:**  Match a region that has the same color as the area selected in the screen capture.
* **Shape:**  Match the same shape as a detailed object in the screen capture region.

.. figure:: images/ad_type_submenu_image_sized.png
   :alt: Options for the image type.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_image_sized.png

   Fig. 3:  Options for the *image* type.


.. todo::

   * For the color match, does it have to be exact?  Can it match a gradient?  The same size?
   * For the shape match, is it done by openCV?  Are default parameters used?



.. _alyvix_designer_options_elements_rect:

----------------------
Rectangle Type Options
----------------------

.. rst-class:: fa fa-retweet

   The *rect* element corresponds to a
   :ref:`matchable rectangular region <alyvix_designer_element_tree_types>`
   on the captured screen, such as a button, text box, panel or window.  As shown in Figure 4,
   it has the following visual recognition parameters:

* **Button:**  Match a region with button-style edges and text in the middle.
* **Box:**  Recognize a text field or box.
* **Window:**  Locate a panel or a window.

.. figure:: images/ad_type_submenu_rect_sized.png
   :alt: Options for the rect type.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_rect_sized.png

   Fig. 4:  Options for the *rect* type.


.. todo::

   * It's not clear what's the difference between Button, Box and Window
   * Why are there two bounding boxes?  Do they have different meanings for the different types?



.. _alyvix_designer_options_elements_text:

-----------------
Text Type Options
-----------------

.. rst-class:: fa fa-font

   The *text* element corresponds to a
   :ref:`matchable rectangular region <alyvix_designer_element_tree_types>`
   on the captured screen, such as a label, title or input text.  As shown in Figure 5, it has the
   following visual recognition parameters, which vary depending on the type selected.  For both
   types, the :guilabel:`Scrap` field is the text that was automatically recognized in the screen
   capture region.

**Detect**

* **Mode:**  Determines how the text is interpreted, using these 3 methods:

   * **Regex**  The recognized text is considered matched only if it satisfies the regular
     expression in the :guilabel:`Regex` field.
   * **Number**  The recognized text is considered matched only if it results in a number that
     satisfy the condition selected in the :guilabel:`Logic` field (e.g., "more than zero")
   * **Date**  The recognized text is considered matched only if it results in day and time that
     satisfies the time interval selected in the :guilabel:`Logic` field  (e.g., "last hour",
     "last day", etc.)

* **Scrap:**  This field contains the text detected by OCR in the selected capture region

.. figure:: images/ad_type_submenu_text_detect_sized.png
   :alt: Options for the detect text type.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_text_detect_sized.png

   Fig. 5:  Options for the *detect* text type.


**Map**

.. figure:: images/ad_type_submenu_text_map_sized.png
   :alt: Options for the map text type.
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_text_map_sized.png

   Fig. 6:  Options for the *map* text type.


.. todo::

   * The dropdown for ``Logic`` only has "more than zero" as an option. ("greater than zero")
   * The dropdown for ``Map`` currently has "None" as the only option.



.. _alyvix_designer_options_elements_common:

--------------
Common Options
--------------

For all group and component object types, once a region has been detected, you can optionally
create an action to occur immediately.

.. figure:: images/ad_action_string_sized.png
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_action_string_sized.png

   Fig. 7:  ad_action_string_sized.png.

* **Action** (all mouse actions)

   * **None (default):**  Don't perform any action
   * **Move:**  (SET POINT) moves the cursor
   * **Click**  (SET POINT, Button [Mouse Left|Right], Units w/delay)
   * **Scroll**  (SET POINT, Direction [Up|Down|Left|Right], Units w/delay/ms)
   * **Hold**  (SET POINT)
   * **Release**  (SET POINT, Direction [None|Up|Down|Left|Right])

* **String:**  An optional string to enter into a text box like a login/password field
  after the mouse action




.. todo::

   * Timeout(s) implies more than one?  How?
   * The Timeout value can be set as a command line parameter, but not "Appear" and "Break"?
   * Need a clear explanation of `break`
   * Is the detection interval still set at 0.5 seconds as described in the 2.7.5 doc?  Is
     it still configurable?
   * Instantiate the ``execution`` references to Alyvix Robot
